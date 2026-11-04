# Databricks notebook source
# 0.1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu,
# ako je odgovarajuca formula oblika T [◦F] = T [◦C] · 1.80 + 32. Na ulazu se unosi vrednost
# temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima
# Farenhajta.
def program():
    c = 25.5
    f = c * 1.80 +32
    print(f)
program()



# COMMAND ----------

# 0.2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog
# dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmed¯u 1 i 7, ispisati Pogresan
# unos
def program():
    broj = 2
    dani = ('ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja')
    if broj < 1 or broj > 7:
        print('Pogresan unos')
    else:
        print(dani[broj - 1])
program()

# COMMAND ----------

# 0.3. Napisati program koji racuna najveci negativni element u listi
lista = (-6, -5, 3, -2, 5, 7, -10)
def program():
    najveci = None
    for x in lista:
        if x < 0:
            if najveci is None or x > najveci:
                najveci = x
    return najveci
print(program())




# COMMAND ----------

# 0.5. Napisati program koji raˇcuna broj parnih elemenata date liste.
lista = (6, 5, 3, 2, 12, 7, 10)
def program():
    parni = 0
    for x in lista:
        if x % 2 == 0:
            parni = parni + 1
    return parni
print(program())

# COMMAND ----------

# 0.6. Napisati program koji raˇcuna sume elemenata liste celih brojeva koji su deljivi sa 2 odnosno sa 3.
lista = (6, 5, 3, 2, 12, 7, 10)
def program():
    deljivisa2 = []
    deljivisa3 = []
    for x in lista:
        if x % 2 == 0:
            deljivisa2.append(x)
        if x % 3 == 0:
            deljivisa3.append(x)
    return sum(deljivisa2), sum(deljivisa3)
print(program())