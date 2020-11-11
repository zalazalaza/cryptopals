phrase = "YELLOW SUBMARINE"

def PKCS7_padding(words, blocksize):
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

if __name__ == "__main__":
    print(PKCS7_padding(phrase,16), len(PKCS7_padding(phrase,16)))
