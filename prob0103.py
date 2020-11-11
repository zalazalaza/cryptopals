from prob0102 import *

_data = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def single_byte_xor(hex_input):
    try:
        hex_to_int_array = [int(hex_input[i:i+2], 16) for i in range(0, len(hex_input), 2)]
    except:
        hex_to_int_array = hex_input
    string_array =[]
    for i in range(0,255):
        phrase = ""
        for j in hex_to_int_array:
            phrase += chr(j^i)
        string_array.append((phrase, chr(i)))
    return string_array




def score(answer):
    max_hp = {

        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182,
        "'": 0.0000001
    }
    codescore = 0
    for i in range(len(answer)):
        _scorechar = answer[i].lower()
        if _scorechar in max_hp:
            codescore += max_hp[_scorechar]
    return codescore

def sort_scored(answer_list):
    scored = (0, "")
    for answer in answer_list:
        a = score(answer[0])
        b = scored[0]
        if a > b:
            scored = (a,answer)
    return scored





if __name__ == "__main__":
    print(sort_scored(single_byte_xor(_data))[1][0])
