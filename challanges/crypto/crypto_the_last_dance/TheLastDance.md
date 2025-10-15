To be accepted into the upper class of the Berford Empire, you had to attend the annual Cha-Cha Ball at the High Court. Little did you know that among the many aristocrats invited, you would find a burned enemy spy. Your goal quickly became to capture him, which you succeeded in doing after putting something in his drink. Many hours passed in your agency's interrogation room, and you eventually learned important information about the enemy agency's secret communications. Can you use what you learned to decrypt the rest of the messages?


C = P xor K  

repeated usage of the key 

C xor P  = K 

encode the msg /// .encode()
convert the msg to hex ///.hex

get only the length needed from the encrypted msg using the plain text msg = msg[:len(enc)]

decode again 
bytes.fromhex()




xor it /// from pwn import pwn 

keystream retrieve it 

decode it    // .hex()

get the encrypted flag 

get the keystream length out of the length of the encrypted flag needed 

return both of them to bytes 
xor them

get the flag








[[crypto]]