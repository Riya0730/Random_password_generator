import random
import string
pass_len = 12
characterval = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(characterval)


print("your password is:", password)