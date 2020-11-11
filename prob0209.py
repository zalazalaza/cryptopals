phrase = "YELLOW SUBMARINE"

class PKCS7:
    def PKCS7_padding(self, words, blocksize):
        try:
            words = bytes(words, "utf-8")
        except:
            pass
        if len(words) % blocksize == 0:
            return words
        else:
            if len(words) > blocksize:
                size_adjust = blocksize - (len(words) % blocksize)
            elif len(words) < blocksize:
                size_adjust = blocksize - len(words)
            return words + bytes([size_adjust]*size_adjust)

    def is_it_padded(self, decryptedtext):
        padding = decryptedtext[-decryptedtext[-1]:]
        return all(padding[i] == len(padding) for i in range(0, len(padding)))

    def unpadPKCS7(self, decryptedtext):
        if self.is_it_padded(decryptedtext) == True:
            return decryptedtext[0:len(decryptedtext) - decryptedtext[-1]]
        else:
            return decryptedtext

if __name__ == "__main__":
    padding = PKCS7()
    print(padding.PKCS7_padding(phrase,20), len(padding.PKCS7_padding(phrase,20)))
