# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# Задаци са фајловима
# Kreiranje csv fajla u folderu:

import csv

with open('data/raw/teams.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(['team', 'city', 'points'])
    writer.writerows([
        ['FK Jedinstvo', 'Bela Palanka', 34],
        ['FK Radnički', 'Niš', 41],
        ['FK Rakovica', "Beograd, Rakovica", 28],
        ['FK Sloga', 'Kraljevo', 19]
    ])

# COMMAND ----------

# Citanje fajla - pregled, kao Lista:
import csv

with open ('data/raw/teams.csv', newline='', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# COMMAND ----------

# 16. Написати функцију count_lines(path: str) -> int која враћа број непразних редова у фајлу
# Input: 'data/raw/teams.csv'
# Output: 5
def count_lines(path: str) -> int:
    with open(path, encoding='UTF-8') as f:
        return sum(1 for line in f if line.strip())
print(count_lines('data/raw/teams.csv')) #broj nepraznih redova

# COMMAND ----------

# 7. Написати функцију read_column(path: str, column: str) -> list која враћа све вредности
# једне колоне CSV фајла
# Input: 'data/raw/teams.csv', 'city'
# Output: ['Bela Palanka', 'Niš', 'Beograd, Rakovica', 'Kraljevo']
# Ако колона не постоји, вратити празну листу []
def read_column(path: str, column: str) -> list:
    with open(path, encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        if column not in reader.fieldnames:
            return []
        return [row[column] for row in reader]
print(read_column('data/raw/teams.csv', 'city'))

# COMMAND ----------

# 18. Написати функцију write_key_value(path: str, data: dict, headers: list) -> None која
# речник уписује у CSV фајл са две колоне
# Input: 'data/processed/summary.csv', {'rows': 10, 'valid': 6}, ['metric', 'value']
# Садржај фајла након позива: 
# metric,value
# rows,10
# valid,6
import os
import csv

def write_key_value(path: str, data: dict, headers: list) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)   #kreiranje foldera
    with open(path, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({headers[0]: key, headers[1]: value})

write_key_value('data/processed/summary.csv', {'rows': 10, 'valid': 6}, ['metric', 'value'])

with open('data/processed/summary.csv', encoding='UTF-8') as f:
    print(f.read())     ## provera ispisa fajla

# COMMAND ----------

# Задаци са csv модулом
# 19. Написати функцију get_header(path: str) -> list која враћа заглавље CSV фајла
# Користити csv.reader и next()
# Input: 'data/raw/teams.csv'
# Output: ['team', 'city', 'points']
import csv

def get_header(path: str) -> list:
    with open(path, encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        return next(reader)
print(get_header('data/raw/teams.csv'))

# COMMAND ----------

# 20. Написати функцију read_rows(path: str) -> list која враћа све редове CSV фајла без
# заглавља, као листу листи
# Користити csv.reader
# Input: 'data/raw/teams.csv'
# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'],
# ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]
import csv

def read_rows(path: str) -> list:
    with open(path, encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)
print(read_rows('data/raw/teams.csv'))   

# COMMAND ----------

# 21. Написати функцију total_points(path: str) -> int која враћа збир бодова свих тимова
# Користити csv.DictReader
# Input: 'data/raw/teams.csv'
# Output: 122
import csv

def total_points(path: str) -> int:
    with open(path, encoding='UTF-8', newline='') as f:
        reader = csv.DictReader(f)
        return sum(int(row['points']) for row in reader)
print(total_points('data/raw/teams.csv'))

# COMMAND ----------

# 22. Написати функцију write_rows(path: str, rows: list) -> None која листу листи уписује у CSV
# фајл
# Input: 'data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22
import csv

def write_rows(path: str, rows: list) -> None:
    with open(path, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

print(write_rows('data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]])) 

with open('data/processed/people.csv', encoding='UTF-8') as f:
    print(f.read()) 

# COMMAND ----------

# 23. Написати функцију write_dicts(path: str, rows: list) -> None која листу речника уписује у CSV фајл
# Користити csv.DictWriter; заглавља су кључеви првог речника
# Input: 'data/processed/people.csv', [{'name': 'Ana', 'age': 20}, {'name':
# 'Marko', 'age': 22}]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22
import csv

def write_dicts(path: str, rows: list) -> None:
    with open(path, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

print(write_dicts(
    'data/processed/people.csv',
    [{'name': 'Ana', 'age': 20}, 
    {'name': 'Marko', 'age': 22}])
    )
with open('data/processed/people.csv', encoding='UTF-8') as f:
    print(f.read()) 