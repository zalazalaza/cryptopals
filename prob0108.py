from Cryptodome.Cipher.AES import block_size
import itertools

data = open("8.txt", 'r')

def score_for_ECB(ciphertext):
    score_tuple = (0, "")
    for line in ciphertext:
        if len(line) > 1:
            score = 0
            pairs = itertools.combinations([line[i:i+block_size] for i in range(0, len(line), block_size)], 2)
            for x,y in pairs:
                if x == y:
                    score += 1
            if score > score_tuple[0]:
                score_tuple = (score, line)
    return score_tuple

if __name__=="__main__":
    print(score_for_ECB(data))
