import base64
from prob0107 import ECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Random import random
from Cryptodome.Cipher import AES
from Cryptodome.Cipher.AES import block_size



class HARDER_ECB_BREAKING_ORACLE:
    target = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    cipher = ECB()
    rand_padding = Random.new().read(Random.random.randrange(block_size, block_size*4))
    key = Random.new().read(block_size)
    thispkcs7 = PKCS7()

    def encrypt_ECB(self, plaintext):
        encrypted = self.cipher.encryptECB(self.thispkcs7.PKCS7_padding(self.rand_padding+plaintext+self.target, len(self.key)), self.key)
        return encrypted

def get_blocksize(ECBoracle):
    base_encrypted = len(ECBoracle.encrypt_ECB(b""))
    i = 0
    while True:
        i += 1
        if len(ECBoracle.encrypt_ECB(b"0"*i)) != base_encrypted:
            return len(ECBoracle.encrypt_ECB(b"0"*i)) - base_encrypted

def makeblocks(text, blocksize):
    return [text[i:i+blocksize] for i in range(0, len(text), blocksize)]

def break_ECB(oracle, prefix_size, blocksize):
    checker = False#check if this character has been completed so as not to give any false/double matches
    answer = b""
    addition = b"A"*((blocksize -(prefix_size%blocksize))+(blocksize-1))#one character less than full block
    ciphertext = oracle.encrypt_ECB(addition) #initial ciphertext before modifying our injected text
    length = len(ciphertext) #length of ciphertext to use in loop
    reference = prefix_size+len(addition)+len(answer)+1

    for i in range(length):
        if checker == True:
            addition =  b"A"*(((blocksize -(prefix_size%blocksize))+(blocksize-1)) - (len(answer)%blocksize)) #modify our adjustable string
            ciphertext = oracle.encrypt_ECB(addition) #create new ciphertext to match
            reference = prefix_size+len(addition)+len(answer)+1 #length to check sample and cipher text matches for
            checker = False
        for x in range(0,255):
            testword = addition +answer+ str.encode(chr(x))
            sample = oracle.encrypt_ECB(testword)
            cipher_blocks = makeblocks(ciphertext, blocksize)

            if (ciphertext[:reference] == sample[:reference]) & (checker == False):
                answer += chr(x).encode()
                checker = True

    return answer


def find_prefix_block_length(oracle, blocksize):
    first_encrypted = makeblocks(oracle.encrypt_ECB(b"a"), blocksize)
    second_encrypted = makeblocks(oracle.encrypt_ECB(b""), blocksize)
    for i in range(len(first_encrypted)):
        if first_encrypted[i] != second_encrypted[i]:
            blocks = i
            return (blocks*blocksize)+(get_prefix_mod_size(oracle, blocksize))


def get_prefix_mod_size(oracle, blocksize):
    for i in range(blocksize):
        sample = makeblocks(oracle.encrypt_ECB(b"0"*((blocksize*2)+i)), blocksize)
        for t in range(len(sample)-1):
            if sample[t] == sample[t+1]:
                return blocksize - i



if __name__ == "__main__" :
    oracle = HARDER_ECB_BREAKING_ORACLE()
    blocksize = get_blocksize(oracle)
    prefix_size = find_prefix_block_length(oracle,blocksize)
    print(break_ECB(oracle,prefix_size, blocksize))
