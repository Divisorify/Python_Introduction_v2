import string
import random

letter=random.choice(string.ascii_lowercase)
number=random.randint(0,1)

print("{}{}".format(letter,number))