# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# 1. Napisati funkciju get_even_positions(data: tuple) -> tuple koja vraća elemente torke koji se nalaze na parnim indeksima (0, 2, 4...). Input: (10, 20, 30, 40, 50, 60) Output: (10, 30, 50)
def get_even_positions(data: tuple) -> tuple:
    return data[::2]
print(get_even_positions((10, 20, 30, 40, 50, 60)))

# COMMAND ----------

# 2. Napisati funkciju find_exclusive_students(group1: set, group2: set) -> set koja vraća studente koji se nalaze u prvoj grupi, ali ne i u drugoj. Input: {'Ana', 'Marko', 'Jovan', 'Milica'},       {'Marko', 'Milica', 'Petar'} Output: {'Ana', 'Jovan'}
def find_exclusive_students(group1: set, group2: set) -> set:
    return group1 - group2
print(find_exclusive_students({'Ana', 'Marko', 'Jovan', 'Milica'}, {'Marko', 'Milica', 'Petar'}))

# COMMAND ----------

# 3. Napisati funkciju clean_tags(text: str) -> str koja obrađuje tekst sa tagovima. Potrebno je: Razdvojiti tagove koji su odvojeni karakterom | Ukloniti početne i krajnje razmake svakog taga Sva slova pretvoriti u mala slova Spojiti tagove karakterom "-"
# Input: ' Python | DATA | SQL '
# Output: 'python-data-sql'
def clean_tags(text: str) -> str:
    parts = text.strip().lower().split('|')
    cleaned = [p.strip() for p in parts]
    return '-'.join(cleaned)
print(clean_tags(' Python | DATA | SQL '))


# COMMAND ----------

# 4. Napisati funkciju count_products(csv_lines: list) -> dict koja analizira porudžbine iz CSV podataka i vraća ukupan broj naručenih proizvoda. Svaki red sadrži ime kupca, naziv proizvoda i količinu, razdvojene zarezom. Prvi red predstavlja zaglavlje i treba ga zanemariti. Ako se isti proizvod pojavljuje u više redova, sabrati njegove količine. Input: [    'customer,product,quantity',    'Alice,laptop,2',    'Bob,mouse,3',    'Alice,laptop,1',    'Charlie,keyboard,2',    'Bob,mouse,1' ] Output: {    'laptop': 3,    'mouse': 4,    'keyboard': 2 }
def count_products(csv_lines: list) -> dict:
    counts = {}
    for line in csv_lines[1:]:
        parts = line.split(',')
        print(parts)
        product = parts[1]
        quantity = int(parts[2])
        counts[product] = counts.get(product, 0) + quantity
    return counts
print(count_products([    
            'customer,product,quantity',
            'Alice,laptop,2',
            'Bob,mouse,3',
            'Alice,laptop,1',
            'Charlie,keyboard,2',
            'Bob,mouse,1'
            ]))