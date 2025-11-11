Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-14 17:25 

Nmap scan report for underpass.htb (10.10.11.48)
Host is up (0.27s latency).
Not shown: 998 closed tcp ports (reset), 997 closed udp ports (port-unreach)
PORT     STATE         SERVICE VERSION
22/tcp   open          ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp   open          http    Apache httpd 2.4.52 ((Ubuntu))
161/udp  open          snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
1812/udp open|filtered radius
1813/udp open|filtered radacct
Service Info: Host: UnDerPass.htb is the only daloradius server in the basin!; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Trying snmp 

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1172.31 seconds
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-14 17:57 EST

Nmap scan report for underpass.htb (10.10.11.48)
Host is up (0.075s latency).

PORT    STATE SERVICE
161/udp open  snmp
| snmp-brute: 
|_  public - Valid credentials

Nmap done: 1 IP address (1 host up) scanned in 172.59 seconds

use snmp_enum to enumerate with metasploit 

[+] 10.10.11.48, Connected.

[*] System information:

Host IP                       : 10.10.11.48
Hostname                      : UnDerPass.htb is the only daloradius server in the basin!
Description                   : Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
Contact                       : steve@underpass.htb
Location                      : Nevada, U.S.A. but not Vegas
Uptime snmp                   : 05:55:08.16
Uptime system                 : 05:54:57.92
System date                   : 2025-1-14 23:11:16.0


[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

looking for dolaradius server 

upon further investigation we found that .. theres a daloradius directory 
dirsearch revealed theres another entier git repo  by the exposed Dockerfile which is the original repo of the dolaradius server /
more investigation reveals a login page under 
/dolaradius/app/operators/login.php 

using the default creds found on the internet 
Administrator/radius 

we have access 

we have a 1 user svcMosh and he have an encrypted password 

412DD4759978ACFCC81DEAB01B382403

it appears to be an MD5 hash 

cracking it revealing the password 

underwaterfriends 

we have an ssh user :D 

user.txt:802604a7c05c8785050995cd0749a6ed

# Privilage Escalation 

```
svcMosh@underpass:~$ sudo -l 
Matching Defaults entries for svcMosh on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User svcMosh may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/bin/mosh-server

```

mosh-server !!  

using the command to init a new server 


root.txt:410743b071e8c2339215523193f250a1


[[machines]]