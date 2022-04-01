def functiona(x):
    return x**2

lista = [0,1,2,3]
result = map(functiona,lista)
print(list(result))

def functionb(x):
    if(x%3==0):
        return True
    return False
lista = [3,8,9,5]
result = map(functionb,lista)
print(list(result))

def functionc(x):
    print([x[0].upper() for x in lista])
lista = ['mapple','acacia','oak']
result = map(functionc,lista)
print(list(result))