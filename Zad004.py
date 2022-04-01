list = [54, 3, 5, 76, 7, 4, 32, 2, 4, 6, 9, 9, 7, 3, 2, 3, 345, 5, 3, 3, 2]

print("Liczby podzielne przez 2: ")
for x in list:
    if(x%2 == 0):
        print(x)

print()
print("Liczby podzielne przez 2 i 3: ")
for x in list:
    if(x%2 == 0 and x%3 == 0):
        print(x)

print()
y= 0
print("Liczba liczb znajdująca się w przedziale (od 10 do 100) ")
for x in list:
    if(x>10 and x<100):
        y=y+1

print(y)
