# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
import csv

with open('data/raw/employees.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'department', 'salary'])
    writer.writerows([
        [' Ana Petrović ', 'it', 120000],
        ['marko jovanović', 'HR', 80000],
        ['Jelena Ilić', 'IT',],
        ['Nikola Đorđević', ' finance ', 95000],
        ['Ivana Marković', 'hr', 'abc'],
    ])

# COMMAND ----------

# 1. Написати функцију clean_row(row: dict) -> dict која враћа нови речник у коме су свим
# вредностима уклоњени почетни и крајњи размаци
# Не мењати оригинални речник
# Помоћ: dict comprehension (слично као list comprehension, али може и без тога)
# Input: {'name': ' Ana Petrović ', 'department': ' finance ', 'salary':
# '120000'}
# Output: {'name': 'Ana Petrović', 'department': 'finance', 'salary': '120000'}
def clean_row(row: dict) -> dict:
    cleaned = {k: v.strip() if v is not None else '' for k, v in row.items()}
    return cleaned 
    
print(clean_row({'name': ' Ana Petrović ', 'department': ' finance ', 'salary': '120000'}))


# COMMAND ----------

# 2. Написати функцију valid_names(path: str) -> list која враћа имена запослених чија је плата
# исправна
# Користити csv.DictReader и функцију clean_row из задатка 36
# Плата је исправна ако је цео број (помоћ: isdigit())
# Input: 'data/raw/employees.csv'
# Output: ['Ana Petrović', 'marko jovanović', 'Nikola Đorđević']
import csv

def valid_names(path: str) -> list:
    with open(path, newline='', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            cleaned = clean_row(row)
            if cleaned['salary'].isdigit():
                result.append(cleaned['name'])
        return result

print(valid_names('data/raw/employees.csv'))


# COMMAND ----------

# 3. Написати функцију salary_by_department(path: str) -> dict која сабира плате по
# одељењима
# Редове са неисправном платом прескочити
# Назив одељења претворити у велика слова
# Помоћ: слично задатку (merge_inventories)
# Input: 'data/raw/employees.csv'
# Output: {'IT': 120000, 'HR': 80000, 'FINANCE': 95000}
import csv

def salary_by_department(path: str) -> dict:
    with open(path, newline='', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        totals = {}
        for row in reader:
            cleaned = clean_row(row)
            if not cleaned['salary'].isdigit():
                continue
            dept = cleaned['department'].upper()
            totals[dept] = totals.get(dept, 0) + int(cleaned['salary'])
        return totals
        
print(salary_by_department('data/raw/employees.csv'))
            


# COMMAND ----------

# 4. Написати функцију add_bonus(path_in: str, path_out: str) -> int која у нови фајл уписује
# само запослене са исправном платом, са додатом колоном bonus (10% плате, цео број)
# Користити csv.DictReader, csv.DictWriter и функцију clean_row
# Помоћ: fieldnames за нови фајл = reader.fieldnames + ['bonus']
# Враћа број уписаних редова
# Input: 'data/raw/employees.csv', 'data/processed/employees_bonus.csv'
# Output: 3
# Садржај фајла након позива:
# name,department,salary,bonus
# Ana Petrović,it,120000,12000
# marko jovanović,HR,80000,8000
# Nikola Đorđević,finance,95000,9500
import csv

def add_bonus(path_in: str, path_out: str) -> int:
    with open(path_in, newline='', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['bonus']
        rows = 0

        with open(path_out, 'w', newline='', encoding='UTF-8') as f_out:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                row = clean_row(row)
                try:
                    salary = float(row['salary'])
                except ValueError:
                    continue
                row['bonus'] = int(salary * 0.10)
                writer.writerow(row)
                rows += 1
    return rows
print(add_bonus('data/raw/employees.csv', 'data/processed/employees_bonus.csv'))

# COMMAND ----------

# 5. Написати функцију split_valid_invalid(path_in: str, valid_path: str, invalid_path:
# str) -> tuple која исправне и неисправне редове уписује у два различита фајла
# Сваки ред прво очистити функцијом clean_row
# Неисправни редови добијају нову колону reason:
# плата је празна → 'missing_salary'
# плата није цео број → 'invalid_salary'
# Враћа торку (број_исправних, број_неисправних)
# Input: 'data/raw/employees.csv', 'data/processed/valid.csv',
# 'data/processed/invalid.csv'
# Output: (3, 2)
# Садржај фајла invalid.csv након позива:
# name,department,salary,reason
# Jelena Ilić,IT,,missing_salary
# Ivana Marković,hr,abc,invalid_salary
import csv

def split_valid_invalid(path_in: str, valid_path: str, invalid_path: str) -> tuple:
    valid = []
    invalid = []

    with open(path_in, newline='', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            row = clean_row(row)
            if row['salary'] == '':
                row['reason'] = 'missing_salary'
                invalid.append(row)
            elif not row['salary'] .isdigit():
                row['reason'] = 'invalid_salary'
                invalid.append(row)
            else:
                valid.append(row)
    with open(valid_path, 'w', newline='', encoding='UTF-8') as f_valid:
        writer = csv.DictWriter(f_valid, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid)
    with open(invalid_path, 'w', newline='', encoding='UTF-8') as f_invalid:
        writer = csv.DictWriter(f_invalid, fieldnames=fieldnames + ['reason'])
        writer.writeheader()
        writer.writerows(invalid)
    return len(valid), len(invalid)
    
print(split_valid_invalid('data/raw/employees.csv', 'data/processed/valid.csv', 'data/processed/invalid.csv'))