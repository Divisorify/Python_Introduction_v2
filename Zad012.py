def wypisz():
    for cyfra, nazwa in slownik.items():
        print(f"{cyfra}-{nazwa}")

slownik = {1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"pięć",6:"sześć",7:"siedem",8:"osiem",9:"dziewięć"}

wypisz()