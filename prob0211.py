import base64, itertools
from Cryptodome.Cipher import AES
from prob0210 import CBC
from prob0107 import encryptECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Random import random
from Cryptodome.Cipher.AES import block_size

dummy_bytes = bytes([17]*61)

def random_key(blockSize):
    return Random.new().read(blockSize)

def score_for_ECB(ciphertext, blockSize):
    score = 0
    blocks = [ciphertext[i:i+blockSize] for i in range(0, len(ciphertext), blockSize)]
    pairs = itertools.combinations(blocks, 2)
    for x,y in pairs:
        if x == y:
            score += 1
    return score

def oracle(plaintext):
    mypkcs7 = PKCS7()
    key = random_key(block_size)
    pre_encryption_text = mypkcs7.PKCS7_padding(Random.new().read(random.randrange(5,11)) + plaintext + Random.new().read(random.randrange(5,11)), len(key))

    if random.randrange(2) == 1:
        device = CBC()
        print('*******CBC*****')
        encrypted = device.encrypt(pre_encryption_text, key, Random.new().read(16))
    else:
        print("*****NOT CBC******")
        encrypted = encryptECB(pre_encryption_text, key)

    if score_for_ECB(encrypted, len(key)) > 0:
        return 'ANSWER IS ECB'
    else:
        return 'ANSWER IS CBC'









if __name__=="__main__":
    encrypted = oracle(dummy_bytes)
    print(encrypted)
