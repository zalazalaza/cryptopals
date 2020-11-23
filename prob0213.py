from prob0107 import ECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Cipher.AES import block_size

def parse_profile(string):
    parsed_dictionary = {}
    for i in string.split("&"):
        parsed_dictionary[i.split("=")[0]] = i.split("=")[1]
    return parsed_dictionary

def profile_for(email, recent_id):
    string=""
    for i in email:
        if i=="=" or i=="&":
            pass
        else:
            string+=i
    return 'email='+string+"&uid="+str(recent_id+1)+"&role=user"

def make_profile_from_encrypted(cipher, encrypted_profile, key):
    pkcs = PKCS7()
    decrypted_profile = pkcs.unpadPKCS7(cipher.decryptECB(encrypted_profile, key))
    for i in range (0, len(decrypted_profile)):
        partial_plaintext = decrypted_profile[:len(decrypted_profile)-i]
        if chr(partial_plaintext[-1]) == "=":
            return cipher.encryptECB(pkcs.PKCS7_padding(partial_plaintext+b"admin", block_size), key)

if __name__ == "__main__":
    cipher = ECB()
    pkcs = PKCS7()
    key = Random.new().read(block_size)
    encoded_profile = profile_for("elliott@hashter.org",100)
    profile_json_object = parse_profile(profile_for("elliott@hashter.org",100))
    encrypted_profile = cipher.encryptECB(pkcs.PKCS7_padding(str.encode(encoded_profile), block_size), key)
    decrypted_profile = pkcs.unpadPKCS7(cipher.decryptECB(encrypted_profile, key))
    pasted_and_encrypted = make_profile_from_encrypted(cipher,encrypted_profile, key)
    decrypted_pasted_profile = pkcs.unpadPKCS7(cipher.decryptECB(pasted_and_encrypted,key))
    parsed_admin = parse_profile(decrypted_pasted_profile.decode())
    print(encrypted_profile)
    print(parse_profile(decrypted_profile.decode()))
    print("*********\n", pasted_and_encrypted, " ********\n", decrypted_pasted_profile, " *********\n", parsed_admin)
