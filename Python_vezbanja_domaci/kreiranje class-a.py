# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# 1. Написати класу Team са атрибутима name, city и points
# Метода is_top(min_points: int) -> bool враћа да ли тим има бар min_points бодова
# Метода __repr__ даје облик Team('FK Sloga', 19)
# Team('FK Sloga', 'Kraljevo', 19).is_top(30) враћа False
# print(Team('FK Sloga', 'Kraljevo', 19)) исписује Team('FK Sloga', 19)
class Team:
    def __init__(self, name, city, points):
        self.name = name
        self.city = city
        self.points = points

    def is_top(self, min_points: int) -> bool:
        return self.points >= min_points
    
    def __repr__(self):
        return f"Team('{self.name}', {self.points})"

# COMMAND ----------

team1 = Team('FK Sloga', 'Kraljevo', 19)
print(team1.is_top(30))
print(Team('FK Sloga', 'Kraljevo', 19))

# COMMAND ----------

# 2. Написати класу Employee са атрибутима name, department и salary
# Метода bonus() -> int враћа 10% плате као цео број (као у задатку 39)
# Employee('Ana Petrović', 'it', 120000).bonus() враћа 12000
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def bonus(self) -> int:
        return int(self.salary * 0.1)

# COMMAND ----------

employee1 = Employee('Ana Petrović', 'it', 120000)
print(employee1.bonus())

# COMMAND ----------

# 3. Додати класи Table две нове методе
# count() -> int враћа број редова
# head(n: int) -> Table враћа нову табелу са првих n редова
# read_table('data/raw/teams.csv').head(2).count() враћа 2
# Питање: зашто након count() више не можемо да наставимо ланац?
import csv

class Table:
    def __init__(self, rows):
        self.rows = rows

    def count(self)-> int:
        return int(len(self.rows))

    def head(self, n: int) -> 'Table':
        return Table(self.rows[:n])

def read_table(path):
    with open(path) as f:
        return Table(list(csv.DictReader(f)))

# COMMAND ----------

read_table('data/raw/teams.csv').head(2).count()

# Count() vraca samo broj Integer Int, a head(n) vraca Tabelu pa lanac moze da se nastavi. 
# Zato count() uvek stoji na kraju, jer nakon njega ti preostaje samo taj broj.