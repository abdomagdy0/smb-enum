import nmap
import sys
from impacket import smb



nm = nmap.PortScanner()

if len(sys.argv) != 4:
    print("-"*40)
    print("(+) usage: python ./scangrab.py [TARGET_IP] [CLIENT_NAME] [SERVER_NAME]")
    print("-"*40)
    sys.exit(1)
target_ip = sys.argv[1]
client_name = sys.argv[2]
server_name = sys.argv[3]

nm.scan(target_ip, 445,139)
open_smb_shares = []
for host in nm.all_hosts():
    if 'open' in nm[host]['tcp'][139]['state']:
        open_smb_shares.appened(host)

print(f"(+) Open SMB shares: {open_smb_shares}")

client_name = sys.argv[2]
for smb_target_ip in  open_smb_shares:
    smb_connection = smb.SMBconnection(
        smb_target_ip,
        smb_target_ip,
        client_name,
        server_name,
        sess_port=445
        )
        # attempt to login
    if smb_connection.login(username, password):
        print(f"(+) Logged in to {smb_target_ip} successfully")
        
        # Now you can perform actions on the SMB share
        # ...

        # Logout when done
        smb_connection.logout()
    else:
        print(f"(-) Failed to log in to {smb_target_ip}")


