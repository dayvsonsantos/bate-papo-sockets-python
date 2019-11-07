from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto import Random
from base64 import b64encode

import random, string, base64


class AESciph:
    def __init__(self):
        self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
        self.iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

    def get_key(self):
        return self.key

    def encrypto(self, msg, key, iv):
        enc_s = AES.new(key, AES.MODE_CFB, iv)
        cipher_text = enc_s.encrypt(msg)
        encoded_cipher_text = base64.b64encode(cipher_text)
        return encoded_cipher_text, key, iv

    def decrypto(self, msg_enc, key, iv):
        decryption_suite = AES.new(key, AES.MODE_CFB, iv)
        plain_text = decryption_suite.decrypt(base64.b64decode(msg_enc))
        return plain_text

class RSAciph:
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()
        #self.__save_keys__()
    
    def __show_keys__(self):
        print(self.private_key.exportKey('PEM'))
        print(self.public_key.exportKey('PEM'))

    def __save_keys__(self):
        pr_key = self.private_key.exportKey('PEM')
        pb_key = self.public_key.exportKey('PEM')
        f = open('pr_key.pem','w')
        f.write(pr_key.decode('utf-8'))
        f.close()
        f = open('pb_key.pem', 'w')
        f.write(pb_key.decode('utf-8'))
        f.close()

    def get_private_key(self):
        # f = open('pr_key.pem','r')
        # pr_key = RSA.importKey(f.read())
        # f.close()
        pr_key = self.private_key
        return pr_key
    
    def get_public_key(self):
        # f = open('pb_key.pem','r')
        # pb_key = RSA.importKey(f.read())
        # f.close()
        pb_key = self.public_key
        return pb_key

    def encrypto(self, msg, key):
        new_msg = bytes(msg, 'utf-8')
        h = SHA.new(new_msg)
        cipher = PKCS1_v1_5.new(key)
        ciphertext = cipher.encrypt(new_msg+h.digest())
        return ciphertext

    def decrypto(self, ciphertext):
        try:
            key = self.private_key
            dsize = SHA.digest_size
            sentinel = Random.new().read(15+dsize)
            cipher = PKCS1_v1_5.new(key)
            message = cipher.decrypt(ciphertext, sentinel)
            digest = SHA.new(message[:-dsize]).digest()
            return message[:-dsize]
        except:
            print("Erro: A mensagem não foi descriptografada")


# if __name__ == "__main__":
#     r = RSAciph()
#     a = AESciph()

#     m = 'oi, A VIDA E BELA MORADA DA CIDADE'
#     e,k = a.encrypto(m)

#     print(e, k)

#     ee = r.encrypto(k, r.get_public_key())
#     de = r.decrypto(ee)

#     print(ee)
#     print(de)

#     ee = a.decrypto(e, de)
    
#     print(ee)
