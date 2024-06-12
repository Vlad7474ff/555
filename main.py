import random
import string
k=6
def generate_random_hash(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

random_hash = generate_random_hash(k)
print(random_hash)
