import os
import hashlib
from cryptography.fernet import Fernet
import base64
import zlib


class StealthCipher:
    def __init__(self, password):
        self.password = password.encode()
        self.key = self._generate_key()
        self.cipher = Fernet(self.key)

    def _generate_key(self):
        salt = b'special_salt_' + self.password[:4]
        dk = hashlib.pbkdf2_hmac('sha512', self.password, salt, 100000, dklen=32)
        twisted_key = bytes([(b + 53) % 256 for b in dk])
        return base64.urlsafe_b64encode(twisted_key[:32])

    def decrypt(self, encrypted_data) -> bytes:
        try:
            obfuscated = base64.b64decode(encrypted_data)
            encrypted = self._xor_transform(obfuscated)
            compressed = self.cipher.decrypt(encrypted)
            return zlib.decompress(compressed)
        except:
            return b''

    def _xor_transform(self, data):
        mask = hashlib.sha256(self.password).digest()
        return bytes([data[i] ^ mask[i % len(mask)] for i in range(len(data))])


def decrypt_file(input_path, password) -> str:
    cipher = StealthCipher(password)
    with open(input_path, 'rb') as f:
        encrypted = f.read()
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode('utf-8', errors='replace')