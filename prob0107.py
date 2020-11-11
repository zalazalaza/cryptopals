import base64
from Cryptodome.Cipher import AES

data = base64.b64decode(open('7.txt', 'r').read())

key = b"YELLOW SUBMARINE"

def decryptECB(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def encryptECB(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)

if __name__=="__main__":
    print(decryptECB(data, key), encryptECB(decryptECB(data, key),key))
