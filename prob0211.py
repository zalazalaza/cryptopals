import base64, itertools
from Cryptodome.Cipher import AES
from prob0210 import CBC
from prob0107 import ECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Random import random
from Cryptodome.Cipher.AES import block_size

dummy_bytes = bytes([17]*61)

class ORACLE:

    def random_key(self, blockSize):
        return Random.new().read(blockSize)


    def prep_plaintext(self, plaintext):
        mypkcs7 = PKCS7()
        key = self.random_key(block_size)
        return (mypkcs7.PKCS7_padding(Random.new().read(random.randrange(5,11)) + plaintext + Random.new().read(random.randrange(5,11)), len(key)))

    def choose_cipher(self, pre_encryption_text):
        if random.randrange(2) == 1:
            device = CBC()
            print('*******CBC*****')
            return device.encrypt(pre_encryption_text, self.random_key(block_size), Random.new().read(16))
        else:
            device = ECB()
            print("*****NOT CBC******")
            return device.encryptECB(pre_encryption_text, self.random_key(block_size))



def find_which_cipher(encrypted, blockSize):
    if score_for_ECB(encrypted, blockSize) > 0:
        return 'CIPHER USED WAS ECB'
    else:
        return 'CIPHER USED WAS CBC'


def score_for_ECB(ciphertext, blockSize):
    score = 0
    blocks = [ciphertext[i:i+blockSize] for i in range(0, len(ciphertext), blockSize)]
    pairs = itertools.combinations(blocks, 2)
    for x,y in pairs:
        if x == y:
            score += 1
    return score






if __name__=="__main__":
    oracle = ORACLE()
    print(find_which_cipher(oracle.choose_cipher(oracle.prep_plaintext(dummy_bytes)), block_size))
