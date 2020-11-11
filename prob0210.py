import base64, prob0107
from prob0209 import PKCS7
from Cryptodome.Cipher import AES
from Cryptodome.Cipher.AES import block_size

KEY = b"YELLOW SUBMARINE"
IV = b'\x00'*AES.block_size
data = base64.b64decode(open('10.txt', 'r').read())

class CBC:

    def encrypt(self, plaintext, key, IV):
        answer = b""
        for i in range(0, len(plaintext), block_size):
            pre_block = bytes([x^y for x,y in zip(IV,plaintext[i:i+block_size])])
            ciphertext_block = prob0107.encryptECB(pre_block, key)
            answer += ciphertext_block
            IV = ciphertext_block
        return answer

    def decrypt(self, ciphertext, key, IV):
        mypkcs7 = PKCS7()
        plaintext = b""
        for i in range(0, len(ciphertext), block_size):
            pre_plaintext_block = mypkcs7.unpadPKCS7(prob0107.decryptECB(ciphertext[i:i+block_size], key))
            plaintext_block = bytes([x^y for x,y in zip(IV,pre_plaintext_block)])
            plaintext += plaintext_block
            IV = ciphertext[i:i+block_size]
        return mypkcs7.unpadPKCS7(plaintext).decode('utf-8')

if __name__ == "__main__":
    device = CBC()
    decrypted = device.decrypt(data,KEY,IV)
    print(decrypted)
