from cryptography.fernet import Fernet
import base64

# g is one of the small prime number used in public key
g = int(21)

# n is a composite number used in modulo operation
n = int(17*23)
n = int(391)

# printing g and n

print(f"g is {g} \nn is {n}")

# setting up private keys
# a -> private key 1
# b -> private key 2

a, b = int(input("type private key 1 (positive integer) ? ")), int(input("type private key 2 (positive integer) ? "))
# checking whether a and b are positive integer
while a <= 0:
    a =  int(input("type private key 1 (positive integer) ? "))
while b <=0:
    b =int(input("type private key 2 (positive integer) ? "))

# calculating (g^a (mod n)) and (g^b (mod n))
# g^a(mod n):
sendkey1 = pow(g,a) % n
# g^b(mod n):
sendkey2 = pow(g,b) % n

# calculating private keys
# private key 1
private_key1 = pow(sendkey1, b) % n
# private key 2
private_key2 = pow(sendkey2,a) % n

print(f'As you can see private key 1 = {private_key1} and \nprivate key 2 = {private_key2} are the same')

# message that you want to encrypt
message = str(input("what message do you want to encrypt"))

# No matter what key you put in (private key 1 or private key 2) both are same
key = private_key1 

'''converting  key to byte code so that computer can use it to encrypt and decrypt the given message
It can't work with regular strings and numbers'''

code_bytes = (message).encode("utf-8")
key = base64.urlsafe_b64encode(code_bytes.ljust(32)[:32])
fernet = Fernet(key)

# encrypt message
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt message
# do you want to decrypt
permission = str(input("Do you want to decrypt the message? (y/n): "))
permission = permission.lower()

def decrypt():
    if permission == "y":
        decMessage = fernet.decrypt(encMessage).decode()
        print("decrypted string: ", decMessage)
    elif permission == "n":
        print("No problem")
    else:
        print("type y for yes or n for no")
        decrypt()
