from prob0103 import *

def array_from_file(input_file):
    data = open(input_file, 'r')
    lines = []
    for line in data:
        cipher_line = ""
        for i in line:
            if i == '\n':
                break
            else:
                cipher_line += i
        lines.append(cipher_line)
    data.close()
    return lines

if __name__ == "__main__":
    duple =(0,0)
    for line in array_from_file('4.txt'):
        if sort_scored(single_byte_xor(line))[0] > duple[0]:
            duple = sort_scored(single_byte_xor(line))
    print(duple[1])
