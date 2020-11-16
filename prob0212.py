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

dummy_bytes = bytes([17]*61)


class ECB_BREAKING_ORACLE:
    cipher = ECB()
    key = Random.new().read(block_size)
    thispkcs7 = PKCS7()

    def encrypt_ECB(self, plaintext):
        encrypted = self.cipher.encryptECB(self.thispkcs7.PKCS7_padding(plaintext, len(self.key)), self.key)
        return encrypted

    def get_blocksize(self, sample_byte):
        my_cipher = ECB()
        i=0
        while True:
            i += 1
            if i == len(self.encrypt_ECB(sample_byte*i)):
                return i

    def break_ECB(self, plaintext):
        answer = ""
        for i in range(len(plaintext)):
            array_of_tuples = []
            length = (block_size - (len(answer)%block_size)) - 1
            testbytestring = str.encode("A")*length
            codewords = testbytestring + base64.b64decode(plaintext)
            ciphertext = self.encrypt_ECB(codewords)
            for x in range(255):
                testword = testbytestring +str.encode(answer)+ str.encode(chr(x))
                sample = self.encrypt_ECB(testword)
                array_of_tuples.append((chr(x), sample))
            for tuple in array_of_tuples:
                if ciphertext[:len(tuple[1])] == tuple[1]:
                    answer += tuple[0]
        return answer


if __name__ =="__main__":
    oracle = ORACLE()
    breaking_oracle = ECB_BREAKING_ORACLE()
    print(breaking_oracle.break_ECB(variable), breaking_oracle.get_blocksize("A"), oracle.find_which_cipher(breaking_oracle.encrypt_ECB(dummy_bytes)))
