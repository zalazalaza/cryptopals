import base64
from prob0107 import ECB
from prob0210 import CBC
from prob0211 import find_which_cipher, score_for_ECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Cipher.AES import block_size

class ECB_RANDKEY_ORACLE:
    cipher = ECB()
    key = Random.new().read(block_size)
    thispkcs7 = PKCS7()

    def encrypt_ECB(self, plaintext):
        encrypted = self.cipher.encryptECB(self.thispkcs7.PKCS7_padding(plaintext, len(self.key)), self.key)
        return encrypted

def get_blocksize(oracle, sample_byte):
    i=0
    while True:
        i += 1
        if i == len(oracle.encrypt_ECB(sample_byte*i)):
            return i

def break_ECB(oracle, plaintext):
    answer = ""
    for i in range(len(plaintext)):
        array_of_tuples = []
        length = (block_size - (len(answer)%block_size)) - 1
        testbytestring = str.encode("A")*length
        codewords = testbytestring + base64.b64decode(plaintext)
        ciphertext = oracle.encrypt_ECB(codewords)
        for x in range(255):
            testword = testbytestring +str.encode(answer)+ str.encode(chr(x))
            sample = oracle.encrypt_ECB(testword)
            array_of_tuples.append((chr(x), sample))
        for tuple in array_of_tuples:
            if ciphertext[:len(tuple[1])] == tuple[1]:
                answer += tuple[0]
    return answer


if __name__ =="__main__":
    variable = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK"""
    dummy_bytes = bytes([17]*61)
    oracle = ECB_RANDKEY_ORACLE()
    print("***********", get_blocksize(oracle, "A"), " bytes per block ", find_which_cipher(oracle.encrypt_ECB(dummy_bytes), block_size)," ***************** \n", (break_ECB(oracle,variable)))
