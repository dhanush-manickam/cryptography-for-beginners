from cryptography.fernet import Fernet
import base64

message = str(input("what message do you want to encrypt"))

key = 12 # private key

# Instance the Fernet class with the key

code_bytes = (message).encode("utf-8")
key = base64.urlsafe_b64encode(code_bytes.ljust(32)[:32])
fernet = Fernet(key)

# encrypt message
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt message

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
