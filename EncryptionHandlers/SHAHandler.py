'''
    This file handles the sha encryption algorithms
'''
import hashlib

class GetSHAEncryption:
    #SHA1
    def sha1Handler(self, password):
        #encode message to bytes
        passwordBytes = password.encode('utf-8')

        #Create a sha hash object
        sha1 = hashlib.sha1()

        #Update the hash object with message bytes
        sha1.update(passwordBytes)

        #Get the hex output
        encryptedPassword = sha1.hexdigest()

        return encryptedPassword

    #SHA224
    def sha224Handler(self, password):
        #encode message to bytes
        passwordBytes = password.encode('utf-8')

        #Create a sha hash object
        sha224 = hashlib.sha224()

        #Update the hash object with message bytes
        sha224.update(passwordBytes)

        #Get the hex output
        encryptedPassword = sha224.hexdigest()

        return encryptedPassword

    #SHA256
    def sha256Handler(self, password):
        #encode message to bytes
        passwordBytes = password.encode('utf-8')

        #Create a sha hash object
        sha256 = hashlib.sha256()

        #Update the hash object with message bytes
        sha256.update(passwordBytes)

        #Get the hex output
        encryptedPassword = sha256.hexdigest()

        return encryptedPassword

    #SHA384
    def sha384Handler(self, password):
        #encode message to bytes
        passwordBytes = password.encode('utf-8')

        #Create a sha hash object
        sha384 = hashlib.sha384()

        #Update the hash object with message bytes
        sha384.update(passwordBytes)

        #Get the hex output
        encryptedPassword = sha384.hexdigest()

        return encryptedPassword

    #SHA512
    def sha512Handler(self, password):
        #encode message to bytes
        passwordBytes = password.encode('utf-8')

        #Create a sha hash object
        sha512 = hashlib.sha512()

        #Update the hash object with message bytes
        sha512.update(passwordBytes)

        #Get the hex output
        encryptedPassword = sha512.hexdigest()

        return encryptedPassword

