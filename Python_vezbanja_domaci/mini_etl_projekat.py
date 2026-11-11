# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
def write_key_value(path: str, data: dict, headers: list) -> None:
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data.items())

# COMMAND ----------

# 24. Extract. Написати функцију read_orders(path: str) -> list која враћа листу речника,
# један речник за сваки ред
# len(read_orders('data/raw/orders.csv')) враћа 10
# Све вредности су још увек ниске (str)
import csv

def read_orders(path: str) -> list:
    with open (path, newline='', encoding='UTF-8') as f:
        return list(csv.DictReader(f))

len(read_orders('data/raw/orders.csv'))

# COMMAND ----------

# 25. Clean. Написати функцију clean_order(order: dict) -> dict која враћа нови очишћени
# речник
# Свим вредностима уклонити почетне и крајње размаке
# invoice_id претворити у велика слова, а customer и city у облик „Велико почетно
# слово“ (title())
# Не мењати оригинални речник
# Input: {'invoice_id': 'itb-002', 'customer': 'ana jovanović', 'city': 'NOVI
# SAD', ...}
# Output: {'invoice_id': 'ITB-002', 'customer': 'Ana Jovanović', 'city':
# 'Novi Sad', ...}
import csv

def clean_order(order: dict) -> dict:
    cleaned = {k: v.strip() for k, v in order.items()}
    cleaned['invoice_id'] = cleaned['invoice_id'].upper()
    cleaned['customer'] = cleaned['customer'].title()
    cleaned['city'] = cleaned['city'].title()
    return cleaned
# print(clean_order({'invoice_id': ' itb-002 ', 'customer': 'ana jovanović', 'city': 'NOVI SAD'}))


# COMMAND ----------

# 26. Validate. Написати функцију validate_order(order: dict) -> str која враћа 'OK' за
# исправан ред, а у супротном разлог зашто је неисправан
# Провере радити овим редом и вратити први пронађени проблем:
# invoice_id не почиње са ITB (задатак 11!) → 'invalid_invoice'
# quantity је празно → 'missing_quantity'
# quantity није цео број већи од нуле → 'invalid_quantity'
# unit_price није цео број већи од нуле → 'invalid_price'
# Помоћ: '12'.isdigit() враћа True, а '-3'.isdigit() и 'abc'.isdigit() враћају
# False
# Ред ITB-007 (quantity -3) враћа 'invalid_quantity'
import csv

def validate_order(order: dict) -> str:
        if not order['invoice_id'].startswith('ITB'):
            return 'invalid_invoice'
        if order['quantity'] == '':
            return 'missing_quantity'
        if not order['quantity'].isdigit() or int(order['quantity']) <= 0:
            return 'invalid_quantity'
        if not order['unit_price'].isdigit() or int(order['unit_price']) <= 0:
            return 'invalid_price'
        return 'OK'

# COMMAND ----------

# 27. Transform. Написати функцију transform_order(order: dict) -> dict која прима
# исправан ред и враћа нови речник
# quantity претворити у int, unit_price у float
# Додати нови кључ total = quantity * unit_price
# Input: {..., 'invoice_id': 'ITB-008', 'quantity': '2', 'unit_price':
# '3500'}
# Output: {..., 'invoice_id': 'ITB-008', 'quantity': 2, 'unit_price':
# 3500.0, 'total': 7000.0}
import csv

def transform_order(order: dict) -> dict:
    new_dict = order.copy()
    new_dict['total'] = 0
    order['quantity'] = int(order['quantity'])
    order['unit_price'] = float(order['unit_price'])
    new_dict['total'] = order['quantity'] * order['unit_price']
    return new_dict

# COMMAND ----------

# 28. Раздвајање. Написати функцију split_orders(orders: list) -> tuple која сваки ред
# чисти, проверава и враћа торку (valid, rejected)
# Искористити функције 25, 26 и 27
# valid је листа трансформисаних редова; rejected је листа очишћених редова са
# додатим кључем reason
# За orders.csv: len(valid) је 6, len(rejected) је 4
def split_orders(orders: list) -> tuple:
    valid = []
    rejected = []
    for order in orders:
        cleaned = clean_order(order)
        result = validate_order(cleaned)
        if result == 'OK':
            valid.append(transform_order(cleaned))
        else: 
            cleaned['reason'] = result
            rejected.append(cleaned)
    return valid, rejected

# COMMAND ----------

# 29. Агрегација. Написати функцију revenue_by(orders: list, column: str) -> dict која
# сабира total по вредностима задате колоне
# Слично задатку 5 (merge_inventories)
# Input 1: valid, 'city'
# Output 1: {'Beograd': 85000.0, 'Novi Sad': 25000.0, 'Kragujevac': 85000.0,
# 'Niš': 99000.0}
# Input 2: valid, 'product'
# Output 2: {'Laptop': 262000.0, 'Miš': 3000.0, 'Monitor': 22000.0,
# 'Tastatura': 7000.0}
def revenue_by(orders: list, column: str) -> dict:
    result = {}

    for order in orders:
        key = order[column]
        result[key] = result.get(key, 0) + order['total']

    return result

# COMMAND ----------

# 30. Load. Написати функцију write_orders(path: str, orders: list) -> int која листу
# речника уписује у CSV фајл и враћа број уписаних редова
# Слично задатку 23
# Ако је листа празна, не правити фајл и вратити 0
# write_orders('data/processed/clean_orders.csv', valid) враћа 6
def write_orders(path: str, orders: list) -> int:
    if not orders:
        return 0
    
    with open(path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)
    
    return len(orders)

# COMMAND ----------

# 31. Run. Написати функцију run_pipeline(input_path: str, output_dir: str) -> dict
# која покреће цео pipeline
# У output_dir прави четири фајла: clean_orders.csv, rejected_orders.csv,
# revenue_by_city.csv (заглавље city,revenue) и summary.csv (заглавље
# metric,value)
# Искористити функције 18, 24, 28, 29 и 30
# Input: 'data/raw/orders.csv', 'data/processed'
# Output: {'total_rows': 10, 'valid_rows': 6, 'rejected_rows': 4,
# 'total_revenue': 294000.0}
def run_pipeline(input_path: str, output_dir: str) -> dict:
    orders = read_orders(input_path)
    valid, rejected = split_orders(orders)

    write_orders(output_dir + '/clean_orders.csv', valid)
    write_orders(output_dir + '/rejected_orders.csv', rejected)

    write_key_value(
        output_dir + '/revenue_by_city.csv',
        revenue_by(valid, 'city'),
        ['city', 'revenue']
    )

    summary = {
        'total_rows': len(orders),
        'valid_rows': len(valid),
        'rejected_rows': len(rejected),
        'total_revenue': sum(order['total'] for order in valid)
    }

    write_key_value(
        output_dir + '/summary.csv',
        summary,
        ['metric','value']
    )

    return summary

# COMMAND ----------

run_pipeline('./data/raw/orders.csv', './data/processed')