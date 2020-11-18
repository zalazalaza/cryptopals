from prob0107 import ECB
from prob0209 import PKCS7
from Cryptodome import Random
from Cryptodome.Cipher.AES import block_size


first_business = "foo=bar&baz=qux&zap=zazzle"

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



if __name__ == "__main__":
    cipher = ECB()
    pkcs = PKCS7()
    key = Random.new().read(block_size)
    encoded_profile = profile_for("elliott@hashter.org",100)
    profile_json_object = parse_profile(profile_for("elliott@hashter.org",100))
    encrypted_profile = cipher.encryptECB(pkcs.PKCS7_padding(str.encode(encoded_profile), block_size), key)
    decrypted_profile = pkcs.unpadPKCS7(cipher.decryptECB(encrypted_profile, key))
    print(encrypted_profile)
    print(decrypted_profile.decode())
