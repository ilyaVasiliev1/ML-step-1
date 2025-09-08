#generation password 

import random
import string

def generation_password(length = 12):
    array = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(array) for _ in range(length))
    return password

print(generation_password())
print(generation_password(20))