def square(x):
    return x*x

lista = [0,1,2,3]
result = map(square,lista)
print(list(result))

#  ---------------------------------------
def filtr(x):
    if(x == 2 or x == 8):
        return True
    return False
lista2 = [3,8,9,5,2,7]

twooreight = filter(filtr,lista2)
twooreightlist = list(twooreight)
print(twooreightlist)

#  ---------------------------------------
def filtr(x):
    if(x == 100 or x == 75 or x == 99 or x == 5000):
        return True
    return False
lista3 = [-2,100,49,3,25,75,99,5000]

result = filter(filtr,lista3)
resultlist = list(result)
print(resultlist)
#  ---------------------------------------
def filtr(x):
    if(x == 'a' or x == 'e' or x == 'f'):
        return True
    return False
lista4 = ['a','o','p','g','e','f','x','z']

result2 = filter(filtr,lista4)
result2list = list(result2)
print(result2list)