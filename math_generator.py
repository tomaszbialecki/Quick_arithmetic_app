#może na razie prosto, niech generuje zapytania i przechowuje wynik, potem zajmiemy się zbieraniem statystyk i tym jak będą dodawane
#dzialania z tabeli, należyt to zrobić jako klase

import random

def adding(limit):
    a = random.randint(1,limit)
    b = random.randint(1,limit)
    result = a+b
    response = int(input(f"{a}+{b}= "))
    if response == result:
        return print("ok")
    else:
        return print("not ok")
        
def subtracting(limit):
    a = random.randint(1,limit)
    b = random.randint(1,limit)
    result = a-b
    response = int(input(f"{a}-{b}= "))
    if response == result:
        return print("ok")
    else:
        return print("not ok")
    
def multiplying(limit):
    a = random.randint(2,limit)
    b = random.randint(2,limit)
    result = a*b
    response = int(input(f"{a}*{b}= "))
    if response == result:
        return print("ok")
    else:
        return print("not ok")

def dividing(limit):
    a = random.randint(2, limit)
    b = random.randint(2, limit)
    
    while a % b != 0 or a==b :
        a = random.randint(2, limit)
        b = random.randint(2, limit)
    result = a/b
    response = int(input(f"{a}/{b}= "))
    if response == result:
        return print("ok")
    else:
        return print("not ok")

    
adding(50)
subtracting(100)
multiplying(12)
dividing(100)

