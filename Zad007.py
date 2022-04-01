def square(x):
    return x*x

lista = [0,1,2,3]
result = []
for x in lista:
    result = map(square, lista)
print(list(result))

#  ---------------------------------------

lista2 = [3,8,9,5,2,7]
filtered = []

for x in lista2:
    if (x == 2 or x == 8):
        filtered.append(x)

print(filtered)

#  ---------------------------------------

lista3 = [-2,100,49,3,25,75,99,5000]
filtered2 = []

for x in lista3:
    if (x == 100 or x == 75 or x == 99 or x == 5000):
        filtered2.append(x)

print(filtered2)

#  ---------------------------------------

lista3 = ['a','o','p','g','e','f','x','z']
filtered3 = []

for x in lista3:
    if (x == 'a' or x == 'e' or x == 'f'):
        filtered3.append(x)

print(filtered3)