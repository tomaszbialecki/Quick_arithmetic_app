#może na razie prosto, niech generuje zapytania i przechowuje wynik, potem zajmiemy się zbieraniem statystyk i tym jak będą dodawane dzialania z tabeli, należyt to zrobić jako klase
#wyniki muszą być tylko na liczby całkowite
import random

def adding():
    a = random.randint(1,9)
    b = random.randint(1,9)
    result = a+b
    if isinstance(result, int):
        response = int(input(f"{a}+{b}= "))
        if response == result:
            return print("ok")
        else:
            return print("not ok")
        
def subtracting():
    a = random.randint(1,9)
    b = random.randint(1,9)
    result = a-b
    if isinstance(result, int):
        response = int(input(f"{a}-{b}= "))
        if response == result:
            return print("ok")
        else:
            return print("not ok")
    
def multiplying():
    a = random.randint(1,9)
    b = random.randint(1,9)
    result = a*b
    if isinstance(result, int):
        response = int(input(f"{a}*{b}= "))
        if response == result:
            return print("ok")
        else:
            return print("not ok")

#trzeba zrobić tak żeby program wygenerował tylko wynik jako liczbę całkowitą, średnio z tym w zakresie 1-9. Dajmy tej funkcji troche szerszy zasięg 
def dividing():
    while True:
        a = random.randint(1,9)
        b = random.randint(1,9)
        result = a/b
        
        if isinstance(result, int):
            response = int(input(f"{a}/{b}= "))
            if response == result:
                print("ok")
            else:
                print("not ok")
            break
        else:
            continue
    
adding()
subtracting()
multiplying()
dividing()