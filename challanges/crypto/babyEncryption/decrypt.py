# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Decryption function
def decryption(ct):
    decrypted_msg = []
    inv_123 = mod_inv(123, 256)  # Find modular inverse of 123 mod 256

    for byte in ct:
        # Step 1: Subtract 18 and take mod 256
        ciphertext_adjusted = (byte - 18) % 256
        # Step 2: Multiply by the modular inverse and take mod 256
        char = (ciphertext_adjusted * inv_123) % 256
        decrypted_msg.append(chr(char))  # Convert to character

    return ''.join(decrypted_msg)

# Reading the encrypted file
with open('./msg.enc', 'r') as f:
    ct_hex = f.read()

# Convert hex string back to bytes
ct = bytes.fromhex(ct_hex)

# Decrypt the message
decrypted_msg = decryption(ct)
print("Decrypted message:", decrypted_msg)

