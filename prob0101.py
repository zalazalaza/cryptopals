import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_bytes(hex_string):
    try:
        bytes_from_hex = bytes.fromhex(hex_string)
    except:
        pass
    return bytes_from_hex

def bytes_to_base64(byte_string):
    try:
        base64_encoded = base64.b64encode(byte_string).decode("utf-8")
    except:
        pass
    return base64_encoded

if __name__ == "__main__":
    print(bytes_to_base64(hex_to_bytes(hex_string)))
