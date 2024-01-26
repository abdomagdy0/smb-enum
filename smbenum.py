import nmap
import sys
from impacket import smb



nm = nmap.PortScanner()

if len(sys.argv) != 2:
    print("-"*40)
    print("(+) usage: python ./scangrab.py [TARGET_IP] ")
    print("-"*40)
    sys.exit(1)
target_ip_range = sys.argv[1]


nm.scan(hosts=target_ip_range, arguments =' --script smb-enum-shares -p 445,139')


for host in nm.all_hosts():
    if 'tcp' in nm[host]:
            print(f"scanning {host}")
            print(nm[host]['tcp'][139]['state'])
            print(nm[host])



