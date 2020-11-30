from prob0209 import PKCS7

test_text = b"ICE ICE BABY\x04\x04\x04\x04"
test_text2 = b"ICE ICE BABY\x05\x05\x05\x05"
test_text3 = b"ICE ICE BABY\x01\x02\x03\x04"

def check_padding(text):
    my_pkcs7 = PKCS7()
    return my_pkcs7.is_it_padded(text)


if __name__ == '__main__':
    print(check_padding(test_text))
    print(check_padding(test_text2))
    print(check_padding(test_text3))
