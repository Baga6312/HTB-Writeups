

def decrypt(ct): 
    decrypted_msg = [] 
    inv_123 = mod_inv(123 , 256) 

    for byte in ct : 
        cipher_adjust = ( byte - 18 ) % 256 

        char = ( cipher_adjust * inv_123 ) % 256 
        decrypted_msg.append(chr(char)) 
    
    return ''.join(decrypted_msg)





with open('./msg.enc') as f:  
    ct_hex = f.read() 

ct = bytes.fromhex(ct_hex)
decrypted_msg = decrypt(ct) 

