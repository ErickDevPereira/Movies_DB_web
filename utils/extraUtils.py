from hashlib import sha256

def cryptograph_msg(msg: str) -> str:
    byte_msg = msg.encode()
    crypt_msg = sha256(byte_msg).hexdigest()
    return crypt_msg