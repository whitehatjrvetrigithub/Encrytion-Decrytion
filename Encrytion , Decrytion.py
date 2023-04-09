import hashlib
from simplecrypt import encrypt,decrypt

value = "Peter:Hello"

def SHA256():
    result = hashlib.sha256(value.encode())
    print(result)
    print("sha256.encrypted data",result.hexdigest())

SHA256()

def MD5():
    result = hashlib.md5(value.encode())
    print(result)
    print("md5.encrypted data",result.hexdigest())
    
MD5()

message = "Peter:Hello"
hex_string = ""

def encrytion():
    global hex_string
    siphercode = encrypt('AIM', message)
    hex_string = siphercode.hex()
    print("encrytion=",hex_string)
    
encrytion()

def decrytion():
    global hex_string
    bytes_str = bytes.fromhex(hex_string)
    orignal = decrypt('AIM',bytes_str)
    final_message = orignal.decode("utf-8")
    print("decrytion=",final_message)

decrytion()