# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# У наредним задацима функције су задате у формату: func_name(var1: type, var2: type) ->
# type
# func_name означава тражено име функције
# var1: type и var2: type означавају параметре функције и њихове типове
# -> type означава тип повратне вредности функције
# На пример get_endpoints(data: tuple) -> tuple
# Функција мора да се зове get_endpoints, да прима један параметар типа tuple и да сама враћа tuple
def get_endpoints(data: tuple) -> tuple:
    return (data[0], data[-1])
print(get_endpoints((1, 2, 3, 4, 5)))

# COMMAND ----------

# 1. Написати функцију get_endpoints(data: tuple) -> tuple која враћа први и последњи елемент
# get_endpoints((10, 20, 30, 40)) враћа (10, 40)
def get_endpoints(parametar: tuple) -> tuple:
        return(parametar[0], parametar[-1])
print(get_endpoints((10, 20, 30, 40)))


# COMMAND ----------

# 2. Написати функцију get_unique_items(items: tuple) -> tuple која враћа торку без дупликата
# # get_unique_items((1, 2, 2, 3, 1, 4)) враћа (1, 2, 3, 4)
def get_unique_items(items: tuple) -> tuple:
    return tuple(set(items))
print(get_unique_items((1, 2, 2, 3, 1, 4)))

# COMMAND ----------

# 3. Написати функцију safe_lookup(data: dict, key: str) -> str која безбедно дохвата из
# речника
# Ако је кључ пронађен у речнику, вратити вредност за тај кључ
# safe_lookup({'name': 'Alice'}, 'name') враћа 'Alice'
# Ако кључ није пронађен у речнику, вратити 'Not Found'
# safe_lookup({'name': 'Alice'}, 'age') враћа 'Not Found'
def safe_lookup(data: dict, key: str) -> str:
    return data.get(key, 'Not Found')
recnik = {'name': 'Alice'}
print(safe_lookup(recnik, 'name'))
print(safe_lookup(recnik, 'age'))

# COMMAND ----------

# 4. Написати функцију find_difference(set1: set, set2: set) -> set која враћа разлику два
# скупа
# find_difference({1, 2, 3}, {2, 3, 4}) враћа {1}
# find_difference({1, 2, 3, 5, 6}, {2, 3, 4}) враћа {1, 5, 6}
def find_difference(set1: set, set2: set) -> set:
    return set1 - set2
print(find_difference({1, 2, 3}, {2, 3, 4}))

def find_difference(set1: set, set2: set) -> set:
    return set1 - set2
print(find_difference({1, 2, 3, 5, 6}, {2, 3, 4}))

# COMMAND ----------

# 5. Написати функцију merge_inventories(inv1: dict, inv2: dict) -> dict која спаја складишта
# две продавнице
# Input: {'apples': 3, 'bananas': 2}, {'bananas': 4, 'oranges': 1}
# Output: {'apples': 3, 'bananas': 6, 'oranges': 1}
def merge_inventories(inv1: dict, inv2: dict) -> dict:
    result = {}
    for key in inv1:
        result[key] = inv1[key]
    for key in inv2:
        if key in result:
            result[key] += inv2[key]
        else:
            result[key] = inv2[key]
    return result
print(merge_inventories({'apples': 3, 'bananas': 2}, {'bananas': 4, 'oranges': 1}))

# COMMAND ----------

# 6. Написати функцију filter_allowed_keys(data: dict, allowed: set) -> dict која филтрира
# дозвољене вредности (приватност података)
# Input: {'username': 'alice', 'email': 'a@test.com', 'password': '123'},
# {'username', 'email'}
# Output: {'username': 'alice', 'email': 'a@test.com'}
def filter_allowed_keys(data: dict, allowed: set) -> dict:
    result = {}
    for key in data:
        if key in allowed:
            result[key] = data[key]
    return result
print(filter_allowed_keys({'username': 'alice', 'email': 'a@test.com', 'password': '123'}, {'username', 'email'}))


# COMMAND ----------

# 7. *Написати функцију group_by_length(words: set) -> dict која групише речи по дужини
# Input 1: {'a', 'to', 'is', 'car', 'dog'}
# Output 1: {1: ['a'], 2: ['to', 'is'], 3: ['car', 'dog']}
# Input 2: {'team', 'score', 'goal', 'point', 'draw'}
# Output 2: {5: ['point', 'score'], 4: ['team', 'draw', 'goal']}
def group_by_length(words: set) -> dict:
    result = {}
    for word in words:
        length = len(word)

        if length not in result:
            result[length] = []

        result[length].append(word)

    return result


print(group_by_length({'a', 'to', 'is', 'car', 'dog'}))
print(group_by_length({'team', 'score', 'goal', 'point', 'draw'}))

# COMMAND ----------

# 8. Написати функцију clean_text(text: str) -> str која враћа текст без почетних и крајњих
# размака, и све карактере претвара у мала слова
# Input: ' DATA engineErinG '
# Output: 'data engineering'
def clean_text(text: str) -> str:
    return text.strip().lower()
print(clean_text(' DATA engineErinG '))

# COMMAND ----------

# 9. Написати функцију convert_to_commas(text: str) -> str која мења карактер | са , и враћа нови стринг:
# Input: 'apple|orange|cherry'
# Output: 'apple,orange,cherry'
def convert_to_commas(text: str) -> str:
    return text.replace('|', ',')
print(convert_to_commas('apple|orange|cherry'))

# COMMAND ----------

# 10. Написати функцију get_extension(filename: str) -> str која враћа екстензију прослеђеног фајла:
# Input: 'annual_report_2025.md'
# Output: 'md'
def get_extension(filename: str) -> str:
    return filename.split('.')[-1]
print(get_extension('annual_report_2025.md'))

# COMMAND ----------

# 11. Префикси наших фактура увек почињу са ITB, написати функцију is_valid_invoice(invoice:
# str) -> bool која проверава да ли је име фактуре валидно
# Input1: 'ITB-01'
# Output1: True
# Input2: 'CSV-01'
# Output2: False
def is_valid_invoice(invoice:str) -> bool:
    return invoice.startswith("ITB")
print(is_valid_invoice('ITB-01'))
print(is_valid_invoice('CSV-01'))

# COMMAND ----------

# 12. Написати функцију combine_tags(tags: list) -> str која враћа тагове спојене са -
# Input: ['python', 'data', 'structures']
# Output: 'python-data-structures'
def combine_tags(tags: list) -> str:
    return '-'.join(tags)
print(combine_tags(['python', 'data', 'structures']))

# COMMAND ----------

# 13. Написати функцију format_team_info(csv_line: str) -> str која лепо исписује информације
# о тиму
# Input: 'FK Jedinstvo', Bela Palanka\n
# Output: 'FK Jedinstvo is from Bela Palanka.'
def format_team_info(csv_line: str) -> str:
    parts = csv_line.strip().replace("'", "")
    return f'{parts[0]} is from {parts[1]}.'
print(format_team_info("'FK Jedinstvo', Bela Palanka\n"))

# COMMAND ----------

# 14. Написати функцију extract_username(csv_line: str) -> str која из email поља извлачи
# username
# Сваки csv ред ће имати форму из примера (редослед колона је исти)
# Input: 101,alice@company.com,IT\n
# Output: 'alice
def extract_username(csv_line: str) -> str:
    email = csv_line.split(',')[1]
    return email.split('@')[0]
print(extract_username('101,alice@company.com,IT\n'))

# COMMAND ----------

# 15. Написати функцију average_salary(csv_lines: list) -> float која рачуна просечну плату
# Input: ["name,salary", "Alice,50000", "Bob,60000"]
# Output: 55000.
def average_salary(csv_lines: list) -> float:
    total = 0
    count = 0
    for line in csv_lines[1:]:
        total += int(line.split(',')[1])
        count += 1
    return total / count
print(average_salary(["name,salary", "Alice,50000", "Bob,60000"]))

# COMMAND ----------

# Написати конвертор валута. Сачувај курсеве у односу на евро: {'USD': 1.08, 'RSD': 117.2, 'GBP': 0.85}
# Функција прима валуту (str) и количину за конверзију (float)
kurs = {'USD': 1.08, 'RSD': 117.2, 'GBP': 0.85}
def convert(valuta: str, kolicina: float) -> float:
    return kolicina * kurs[valuta]
print(convert('GBP', 15))
print(convert('RSD', 200))
print(convert('USD', 150))

# COMMAND ----------

# Написати функцију available_books(library: dict) -> list која враћа листу књига које се могу позајмити
# Вредност True означава да је књига доступна, а False да је позајмљена
# available_books({'1984': True, 'Дина': False, 'Хобит': True}) враћа ['1984', 'Хобит']
def available_books(library: dict) -> list:
    result = []
    for book in library:
        if library[book] == True:
            result.append(book)
    return result
print(available_books({'1984': True, 'Дина': False, 'Хобит': True}))

# COMMAND ----------

# Написати функцију grades_average(grades: list) -> float која враћа просек описних оцена
# За податке, користити речник: {'одличан': 5, 'врлодобар': 4, 'добар': 3, 'довољан': 2, 'недовољан': 1}
# grades_average(['одличан', 'добар', 'врлодобар']) враћа 4.0
prosek = {'одличан': 5, 'врлодобар': 4, 'добар': 3, 'довољан': 2, 'недовољан': 1}
def grades_average(grades: list) -> float:
    total = 0
    count = 0
    for grade in grades:
            total += prosek[grade]
            count += 1
    return total / count
print(grades_average(['одличан', 'добар', 'врлодобар']))

# COMMAND ----------

# Написати функцију count_votes(votes: list) -> dict која враћа број гласова за сваку опцију
# count_votes(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']) враћа {'пица': 3, 'бургер': 2, 'такос': 1}
def count_votes(votes: list) -> dict:
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts
print(count_votes(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']))  

# COMMAND ----------

# Користећи функцију count_votes, написати функцију winner(votes: list) -> str која враћа опцију са највише гласова
# winner(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']) враћа 'пица'
def winner(votes: list) -> str:
    counts = count_votes(votes)
    return max(counts, key=counts.get)
print(winner(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']))

# COMMAND ----------

# Написати функцију translate(dictionary: dict, word: str) -> str која враћа превод енглеске речи на српски
# Ако реч не постоји у речнику, функција враћа None
# translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'water') враћа 'вода'
# translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'bread') враћа None
def translate(dictionary: dict, word: str) -> str | None:
    return dictionary.get(word)
print(translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'water'))
print(translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'bread'))
        