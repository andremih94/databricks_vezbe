# Databricks notebook source
# Напишите функцију goals_per_match(goals, matches) која враћа просек голова по утакмици, заокружен на две децимале.
def goals_per_match(goals, matches):
    return round(goals / matches, 2)
goals_per_match(64, 20)

# COMMAND ----------

# Напишите функцију scoreline(home_team, home_goals, away_goals, away_team) која враћа текст Kingsbridge City 3-1 Ashford Rovers.
def scoreline(home_team, home_goals, away_goals, away_team):
    return f'{home_team} {home_goals}-{away_goals} {away_team}'
print(scoreline('Kingbridge City', 3, 1, 'Ashford Rovers'))

# COMMAND ----------

# Претворите разврставање посете из Сесије 1 у функцију crowd_category(attendance) која враћа категорију. Позовите је за None, 0, 15000 и 30000.
attendances = [None, 0, 15000, 30000]
def crowd_category(attendance):
    if attendance is None:
        return (f'Unknown')
    if attendance >= 30000:
        return (f'Large')
    elif attendance >= 15000:
        return (f'Medium')
    else:
        return (f'Small')
for attendance in attendances:
    print(crowd_category(attendance))



# COMMAND ----------

# Напишите функцију added_minute(minute, added=None) која враћа 90+3, или само 90 када надокнада није наведена.
def added_minute(minute, added=None):
    if added is not None:
        return (f'{minute}+{added}')
    elif added is None:
        return(f'{minute}')
print(added_minute(90, 5))
print(added_minute(90)) 

# COMMAND ----------

# Напишите функцију is_derby(home_city, away_city) која враћа True ако су оба клуба из истог града.
def is_derby(home_city, away_city):
    return home_city == away_city
is_derby('Beograd', 'Beograd')

# COMMAND ----------

# Zadatak: Rad sa datumima

# Koristeći modul datetime:

# Ispisati današnji datum.
import datetime
trenutno = datetime.datetime.now()
print(trenutno)
# Ispisati trenutnu godinu, mesec i dan.
from datetime import datetime, timedelta
trenutno = datetime.now()
print(trenutno.date())
# Izračunati koji će datum biti za 30 dana.
import datetime
danas = datetime.date.today()
za_30_dana = danas + timedelta(days=30)

# Izračunati koliko dana ima između 1. januara 2026. i današnjeg datuma.
# Ispisati današnji datum u formatu dd.mm.yyyy.

# COMMAND ----------

# Izračunati koji će datum biti za 30 dana.
import datetime
danas = datetime.date.today()
za_30_dana = danas + datetime.timedelta(days=30)
print(za_30_dana)

# COMMAND ----------

# Izračunati koliko dana ima između 1. januara 2026. i današnjeg datuma.
import datetime
datum1 = datetime.date.today()
datum2 = datetime.date(2026, 1, 1)
razlika = datum1 - datum2
print(razlika.days)

# COMMAND ----------

# Ispisati današnji datum u formatu dd.mm.yyyy.
import datetime
danas = datetime.date.today()
formatiran_datum = danas.strftime('%d.%m.%Y.')
print(formatiran_datum)

# COMMAND ----------

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