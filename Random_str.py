import random
import string

length = 10
rand_string = ""

for i in range(length) :  
    random_printable =  random.choice(string.ascii_letters)
    rand_string = rand_string + random_printable

print(rand_string)