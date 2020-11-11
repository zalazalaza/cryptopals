
hex_string = "1c0111001f010100061a024b53535009181c"
reg_string = "686974207468652062756c6c277320657965"

def hex_to_int(hex_string):
    return int(hex_string, 16)

def fixed_xor(first, second):
    return first ^ second



if __name__ == "__main__":
    print(hex(fixed_xor(hex_to_int(hex_string), hex_to_int(reg_string)))[2:])
