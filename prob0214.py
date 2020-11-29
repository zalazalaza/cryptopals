import base64
from prob0107 import ECB
from prob0210 import CBC
from prob0211 import ORACLE
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Cipher.AES import block_size
from random import randint




class HARDER_ECB_BREAKING_ORACLE:
    cipher = ECB()
    key = Random.new().read(block_size)
    thispkcs7 = PKCS7()

    def encrypt_ECB(self, plaintext):
        padded_plaintext = Random.new().read(Random.random.randrange(32)) + plaintext
        print(plaintext,"\n\n*********\n\n", padded_plaintext, "\n\n***********\n\n")
        encrypted = self.cipher.encryptECB(self.thispkcs7.PKCS7_padding(padded_plaintext, len(self.key)), self.key)
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

    def find_randbytes_length(self, ciphertext):
        pass


if __name__ =="__main__":
    oracle = HARDER_ECB_BREAKING_ORACLE()
    variable = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"""
    print(oracle.encrypt_ECB(base64.b64decode(variable)))
