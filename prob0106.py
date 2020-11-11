import base64
import prob0103
from prob0105 import *

test_1 = b"this is a test"
test_2 = b"wokka wokka!!!"
data = base64.b64decode(open('6.txt', 'r').read())

def hamming_distance(string1, string2):
    score = 0
    xorTuples = zip(string1,string2)
    for x,y in xorTuples:
        a = bin(x^y)
        numberstring = a[2:]
        for i in numberstring:
            score += int(i)
    return  score


def find_keylength(input_bytes):
    score_tuple = (0,0)
    for KEYSIZE in range(2,40):
        score = 0
        bytes_array = []
        for i in range(0, len(input_bytes), KEYSIZE):
            bytes_array.append(input_bytes[i:i+KEYSIZE])
        for x in range(0, len(bytes_array), 2):
            try:
                score += hamming_distance(bytes_array[x], bytes_array[x+1])
            except:
                pass
        if score_tuple == (0,0) or score_tuple[1] > score:
            score_tuple = (KEYSIZE, score)
    return score_tuple[0]

def get_key(size, input_bytes):
    answer = ""
    chunk_array = []
    repeating_chunk_array = []
    for i in range(0, len(input_bytes), size):
        chunk_array.append(input_bytes[i:i+size])
    for j in range(0,size):
        byte_array = []
        byte_string=b""
        for i in chunk_array:
            if(len(i) > j):
                byte_string += bytes([i[j]])
                byte_array.append(i[j])
            else:
                pass
        answer += sort_scored(single_byte_xor(byte_array))[1][1]
        repeating_chunk_array.append(byte_string)
    return answer

def make_repeating(key, string):
    return (key * int(len(string)/len(key))+ key[0:(len(string)%len(key))])

def equal_string_xor(rep_key, phrase):
    return bytes([phrase[i]^rep_key[i] for i in range(len(phrase))])

if __name__ == "__main__":
    print('\n','this is a test for hamming space. the test answer is ------', hamming_distance(test_1, test_2), '\n')
    print(equal_string_xor(bytes(make_repeating((get_key(find_keylength(data), data)), data), 'utf-8'), data).decode('utf-8'))
