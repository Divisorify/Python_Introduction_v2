lista = [1,2,'A','B',3,4,'Cc',5.1,'D',True,False,None,True,3,1,'A','B']
dict = {i:lista.count(i) for i in lista}
print(dict)
print('{} {}'.format(dict,type(lista[2])))
a=5
print(type(a))