import base64, itertools
from prob0107 import ECB
from prob0210 import CBC
from prob0211 import ORACLE
from Cryptodome.Cipher import AES
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Random import random
from Cryptodome.Cipher.AES import block_size

variable = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK"""

class ECB_ORACLE:
    key=random_key(block_size)
    thispkcs7 =PKCS7()

    def encrypt_ECB(self, plaintext):
        encrypted = encryptECB(self.thispkcs7.PKCS7_padding(plaintext, len(self.key)), self.key)
        return encrypted



def get_blocksize(sample_byte):
    my_cipher = ECB_ORACLE()
    i=0
    while True:
        i += 1
        if i == len(my_cipher.encrypt_ECB(sample_byte*i)):
            return i


def break_ECB(plaintext, blocksize):
    my_cipher =ECB_ORACLE()
    answer = ""
    for i in range(len(plaintext)):
        tuplesoftuples = []
        length = (blocksize - (len(answer)%blocksize)) - 1
        testbytestring = str.encode("A")*length
        codewords = testbytestring + base64.b64decode(plaintext)
        ciphertext = my_cipher.encrypt_ECB(codewords)
        for x in range(255):
            testword = testbytestring +str.encode(answer)+ str.encode(chr(x))
            sample = my_cipher.encrypt_ECB(testword)
            tuplesoftuples.append((chr(x), sample))
        for tuple in tuplesoftuples:
            if ciphertext[:len(tuple[1])] == tuple[1]:
                answer += tuple[0]
    return answer

if __name__ =="__main__":
    print(break_ECB(variable, get_blocksize("D")))
