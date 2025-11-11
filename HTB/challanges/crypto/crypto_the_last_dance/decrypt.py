f = open('out.txt').read().split()
message = b"Our counter agencies have intercepted your messages and a lot of your agent's identities have been exposed. In a matter of days all of them will be captured".hex()
enc_message = f[1][:len(message)] 

def decrypt(hex1 , hex2): 
    min_length = min(len(hex1), len(hex2))
    bytes1 = bytes.fromhex(hex1[:min_length])
    bytes2 = bytes.fromhex(hex2[:min_length])
    xor_result = ''.join(f"{b1 ^ b2:02x}" for b1, b2 in zip(bytes1, bytes2))
    return xor_result


def decrypt2(hex1 , hex2) : 
    xor_reslt =  "" 
    for i in range(len(hex1)): 
        xor_reslt += ord(bytes.fromhex(hex1[i])) ^ bytes.fromhex(ord(hex2[i]))
    return xor_reslt 

print(decrypt(enc_message , message ))
print(decrypt2(enc_message , message ))
