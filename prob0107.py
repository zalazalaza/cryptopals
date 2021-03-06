import base64
from Cryptodome.Cipher import AES

data = base64.b64decode(open('7.txt', 'r').read())

key = b"YELLOW SUBMARINE"

class ECB:
    def decryptECB(self, ciphertext, key):
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.decrypt(ciphertext)

    def encryptECB(self, plaintext, key):
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(plaintext)

if __name__=="__main__":
    cipher = ECB()
    print(cipher.decryptECB(data, key), cipher.encryptECB(cipher.decryptECB(data, key),key))
