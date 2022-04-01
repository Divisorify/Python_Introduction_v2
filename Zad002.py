import random

x=0
list = []

while (x!=100):
    list.append(random.randint(3, 333))
    x+=1

print(sorted(list,reverse=True))

