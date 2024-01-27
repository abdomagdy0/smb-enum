## Setting up a samba share:
### installing samba
```
sudo apt update &&
sudo apt install samba
```
### check if samba is running
`sudo systemctl status smbd`
### create a directory of the files you want to share or if it already exists you can skip the first command.
my file will be in /home directory
```
mkdir directory_name && chmod 777 directory_name 
```
```
cd directory_name && echo "secret pass = 35634635" > secret.txt
```

### now its time to edit the samba config file to add your shared folder
here you can use gedit or nano
```
sudo nano /etc/samba/smb.conf
```
hold pgdown untill you get to the bottom and add this block
```
[directory_name] 
 comment = Samba share on Ubuntu
 path = /home/directory_name
 guest ok = yes
 guest account = ftp
 browsable = yes
```
press ctrl+O and hit Enter,
#### restart samba
`systemctl service smbd restart`


### check if you can access the share  using smbclient
```
smbclient //SERVER_IP/SHARE_RNAME/ -U guest
```
thats it our test environment is now ready

usage:
```
python3 smbenum.py <ip>
```
![cccc](https://github.com/abdomagdy0/SMB-Grab/assets/91535529/63e48e67-7190-441d-ba97-a065abc819dd)
