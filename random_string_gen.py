import random
import string

length = 10
rand_string = ""

for i in range(length) :  rand_string = rand_string + random.choice(string.printable)

print(rand_string)