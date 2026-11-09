# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# T1. safe_int(text: str, default: int) -> int
# Претвара ниску у цео број, а ако не може враћа default.
# safe_int('42', 0) → 42 · safe_int('abc', 0) → 0 · safe_int('', -1) → -1
def safe_int(text: str, default: int) -> int:
    try:
         return int(text)
    except ValueError:
        return default  
print(safe_int('42', 0))
print(safe_int('abc', 0))
print(safe_int('', -1))

# COMMAND ----------

# Т2 · safe_read(path: str) -> list
# Учитава CSV као листу речника; ако фајл не постоји, исписује поруку и враћа [].
# len(safe_read('data/raw/teams.csv')) → 4 · safe_read('data/raw/nema.csv') → []
import csv

def safe_read(path: str) -> list:
    try:
        with open(path, newline='', encoding='UTF-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f'Fajl ne postoji: {path}')
        return []
print(len(safe_read('data/raw/teams.csv')))
print(safe_read('data/raw/nema.csv'))

# COMMAND ----------

# Т3 · sum_salaries(path: str) -> tuple
# Сабира исправне плате и броји прескочене редове. Користи try око int(), без isdigit().
# sum_salaries('data/raw/employees.csv') → (295000, 2)
import csv

def sum_salaries(path: str) -> tuple:
    total = 0
    skipped = 0
    with open(path, newline='', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try: 
                total += int(row['salary'])
            except ValueError:
                skipped += 1
    return total, skipped     
print(sum_salaries('data/raw/employees.csv'))
