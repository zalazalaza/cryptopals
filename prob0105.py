from prob0104 import *

vanilla = b'''Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal'''
vanilla_key = b"ICE"
answer = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

def make_repeating(key, string):
    return (key * int(len(string)/len(key))+ key[0:(len(string)%len(key))])

def equal_string_xor(rep_key, phrase):
    return bytes([phrase[i]^rep_key[i] for i in range(len(phrase))])


if __name__ == "__main__":
    print(equal_string_xor(make_repeating(vanilla_key, vanilla), vanilla).hex())
    
