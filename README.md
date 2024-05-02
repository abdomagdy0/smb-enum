This Python script is designed to scan a range of IP addresses for open Samba shares and search for potential hardcoded credentials within files on those shares. Samba is a widely used protocol for file and printer sharing between Unix and Windows systems.

## Requirements

- Python 3.x
- `nmap` library (for network scanning)
- `smbprotocol` library (for interacting with Samba shares)
- `re` module (for regular expression pattern matching)

## Usage

To run the script, use the following command:

python scangrab.py [TARGET_IP_RANGE]


- `[TARGET_IP_RANGE]`: The IP range to scan for open Samba shares.

## Script Overview

1. **Imports**:
    - `sys`: for system-level operations and accessing command-line arguments.
    - `os`: for interacting with the operating system (e.g., file operations).
    - `re`: for regular expression pattern matching.
    - `nmap`: for network scanning.
    - `SMBConnection` from `smb.SMBConnection`: for establishing connections to Samba shares.


. **Functions**:
    - `connect_to_samba(server_ip)`: Connects to a Samba server at the specified IP address.
    - `disconnect_from_samba(connection)`: Disconnects from a Samba server.
    - `list_files(connection, share_name, directory)`: Lists all files in a directory on a Samba share.
    - `scan_file_for_credentials(file_path)`: Scans a file for potential hardcoded credentials (username and password).
    - `scan_smb_shares(host_ip)`: Scans all Samba shares on a given host for files with `.txt` extension and scans them for credentials.
    - `scan_ip_range(ip_range)`: Scans a range of IP addresses for open Samba shares.

. **Main Execution**:
    - Parses the command-line arguments.
    - Scans the specified IP range for open Samba shares.
    - For each host with an open Samba share, scans the files in the share for potential hardcoded credentials.

## Example

`python scangrab.py 192.168.1.0/24`


![cccc](https://github.com/abdomagdy0/SMB-Grab/assets/91535529/63e48e67-7190-441d-ba97-a065abc819dd)
