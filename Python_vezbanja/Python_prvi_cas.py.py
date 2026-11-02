# Databricks notebook source
home_team = 'Partizan'
attendance = 52000
ticket_price = 18.5
has_roof = False
print(home_team, attendance, ticket_price, has_roof)
print(type(home_team), type(attendance), type(ticket_price), type(has_roof))
attendance = 41250
ticket_price = 18.5
print(attendance * ticket_price)
attendance = 41250
print(attendance // 1000)
print(attendance % 1000)
goals_home = '10'
goals_away = 2
# Не мењајте код изнад ове линије
#print(goals_home + goals_away) #TypeError: can only concatenate str (not "int") to str
print(int(goals_home) + goals_away)
print(goals_home + str(goals_away))
#. Направите листу са 5 назива стадиона. Испишите целу листу, а затим испишите колико
# карактера има име сваког стадиона
stadioni = ['stadion1', 'stadion2', 'stadion3', 'stadion4', 'stadion5']
print(type(stadioni))
print(len(stadioni))
attendances = [18200, 32454, 27890, 41020, 15300, 22750]
print(attendances)
print('Last element of the list: ', attendances[5])
#print('Last element of the list: ', attendances[6]) #IndexError: list index out of range
print('Last element of the list: ', attendances[-1])
print('Third element of the list: ', attendances[2])
print('Sum of first and last: ', attendances[0] + attendances[5])
print('Sum of first and last: ', attendances[0] + attendances[-1])

# COMMAND ----------

#7. Исход утакмице. Испишите Home win, Away win, Draw у зависности од вредности
# променљивих goals_home и goals_away
goals_home = 3
goals_away = 5
if goals_home > goals_away:
    print('Home win')
elif goals_away > goals_home:
    print('Away win')
else:
    print('Draw')

# COMMAND ----------

# 8. За дату температуру одредити категорију: (испод 5 - Cold, од 5 до 20 - Mild, од 20 до 30 -
# Warm, и од 30 навише - Hot)
# Напомена, лева вредност се увек укључује, док се десна не укључује (20 је Warm)
temperatures = [-5, 1, 5, 7, 20, 22, 36, 18, 42]
for temperature in temperatures:
    if temperature < 5:
        print(f'temperature: {temperature}, Cold')
    elif temperature >= 5 and temperature <= 20:
        print(f'temperature: {temperature}, Mild')
    elif temperature >= 20 and temperature <= 30:
        print(f'temperature: {temperature}, Warm')
    else:
        print(f'temperature: {temperature}, Hot')


# COMMAND ----------

#10. Одбројавање до почетка. Помоћу петље while одбројте од 10 до 1, исписујући сваки број, а
# затим испишите Kick-off!.
# Затим измените програм тако да се петља раније заустави помоћу break када стигне
# до 3 и уместо тога испише Match delayed

# COMMAND ----------

n = 11
while n > 0:
    n = n - 1
    print(n)
    if n == 3:
        print('Match delayed')
        break
        print('Kick-off!')

# COMMAND ----------

#11. Добродошлица тимовима, користите петљу и f-стринг да испишете по један ред за сваки тим
# Шаблон: Welcome to the league, <име_тима>
teams = ['Northport United', 'Riverside FC', 'Hillcrest City', 'Bayview Rovers']
for team in teams:
    print(f'Welcome to the league, {team}!')

# COMMAND ----------

#12. Генерисање SQL упита. Помоћу петље испишите по један упит за сваки стадион
# Шаблон: SELECT * FROM matches_flat WHERE stadium = '<име_стадиона>';
stadiums = ['Arena North', 'Lakeside Park', 'Old Mill Ground']
for stadium in stadiums:
    print(f'SELECT * FROM matches_flat WHERE stadium = \'{stadium}\'')


# COMMAND ----------

# Израчунајте укупну посећеност из листе attendances
# Израчунајте затим и просек
# За form = 'WWDLWDLLWW' пребројте све и израчунајте бодове
# Резултат треба да буде у следећој форми: W: 5, D: 2, L: 3, Points: 17
# attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]
# print(sum(attendances))
# print(sum(attendances) // 8)
form = 'WWDLWDLLWW'
w = 0
d = 0
l = 0
points = 0
for result in form:
    if result == 'W':
        w = w + 1
        points = points + 3
    elif result == "D":
        d = d + 1
        points = points + 1
    elif result == 'L':
        l = l + 1
print(f'W: {w}, D: {d}, L: {l}, Points: {points}')

# COMMAND ----------

# 9. Опсези. Помоћу for и range испишите сваки низ у једном реду:
# бројеве 0–9
# непарне бројеве од 1 до 20
# минуте полувремена у корацима од 15 (0 15 30 45)
# бројеве од 100 до 50 уназад у корацима од 10.
for i in range(10):
    print(i)
    
for i in range(1, 20, 2):
     print(i)

for i in range(0, 46, 15):
    print(i)

for i in range(100, 49, -10):
    print(i)

# COMMAND ----------

# Прођите кроз attendances и за сваку утакмицу испишите по један ред са њеним редним бројем и категоријом величине: Large (30.000 или више), Medium (15.000 или више) или Small. На крају испишите колико је утакмица било у категорији Large.
# Пример једног реда: Match 1: 18200 fans – Medium.
attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]
match = 0
large = 0
for attendance in attendances:
    match = match + 1
    if attendance >= 30000:
        print(f'Match {match}: {attendance} fans - Large')
        large = large + 1
    elif attendance >= 15000 and attendance < 30000:
        print(f'Match {match}: {attendance} fans - Medium')
    else:
        print(f'Match {match}: {attendance} fans - Small')
print(f'Large matches: {large}')

# COMMAND ----------

# Клуб жели укупно 100.000 навијача ове сезоне. Помоћу петље сабирајте посећеност утакмицу по утакмицу и зауставите се чим збир достигне 100.000.
# Испишите после које утакмице је циљ достигнут и колики је тада био збир.
attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]
total = 0
match = 0
for attendance in attendances:
    match = match + 1
    total = total + attendance
    if total >= 100000:
        print(f' Goal reached after match {match}, total fans: {total}')
        break