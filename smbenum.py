import sys
import os
import re
import nmap
from smb.SMBConnection import SMBConnection
samba_user = 'guest'
samba_password = ''

def connect_to_samba(server_ip):
    connection = SMBConnection(samba_user, samba_password, 'python-smb-client', server_ip, use_ntlm_v2=True)
    try:
        connection.connect(server_ip, 445)
    except Exception as e:
        print(f'Error connecting to Samba on {server_ip}: {str(e)}')
    return connection

def disconnect_from_samba(connection):
    connection.close()

# Function to list all files in a directory on the Samba share
def list_files(connection, share_name, directory):
    file_list = []
    try:
        print(f'Listing files on share {share_name}, directory {directory}')
        directory = os.path.normpath(directory)  # Normalize the path
        items = connection.listPath(share_name, directory)
        for item in items:
            if item.isDirectory and item.filename not in ('.', '..'):
                file_list.extend(list_files(connection, share_name, os.path.join(directory, item.filename)))
            else:
                try:
                    file_list.append(os.path.join(directory, item.filename))
                except Exception as e:
                    print(f'Error adding file to the list: {str(e)}')
    except FileNotFoundError:
        print(f'Directory not found: {directory}')
    except Exception as e:
        print(f'Error listing files on share {share_name}, directory {directory}: {str(e)}')
    return file_list    

def scan_file_for_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            pattern = re.compile(r'username\s*=\s*["\'](.+?)["\']\s*\n\s*password\s*=\s*["\'](.+?)["\']', re.IGNORECASE)
            matches = re.findall(pattern, content)
            if matches:
                print(f'Potential hardcoded credentials found in file: {file_path}')
                for match in matches:
                    print(f'Username: {match[0]}, Password: {match[1]}')
    except Exception as e:
        print(f'Error scanning file {file_path}: {str(e)}')

def scan_smb_shares(host_ip):
    try:
        smb_connection = connect_to_samba(host_ip)
        shares = smb_connection.listShares()
        for share in shares:
            print(f"Scanning share '{share.name}' on {host_ip}")
            try:
                share_files = list_files(smb_connection, share.name, '/')
                for file_path in share_files:
                    if file_path.lower().endswith('.txt'):
                        scan_file_for_credentials(file_path)
            except Exception as e:
                print(f'Error scanning files on share {share.name}: {str(e)}')
    except Exception as e:
        print(f'Error scanning Samba shares on {host_ip}: {str(e)}')
    finally:
        disconnect_from_samba(smb_connection)
    
def scan_ip_range(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-p 445 --open')  

    for host in nm.all_hosts():
        print(f"Found Samba share on {host}")
        scan_smb_shares(host)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("-" * 40)
        print("(+) usage: python ./scangrab.py [TARGET_IP] ")
        print("-" * 40)
        sys.exit(1)

    target_ip_range = sys.argv[1]
    scan_ip_range(target_ip_range)

    