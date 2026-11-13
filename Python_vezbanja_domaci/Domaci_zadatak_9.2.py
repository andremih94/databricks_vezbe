# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# 1.Kreirati klasu BankAccount koja predstavlja bankovni račun. Klasa treba da ima sledeće atribute: owner – ime vlasnika računa; balance – trenutno stanje na računu. Implementirati sledeće metode: 1.deposit(amount: float) -> BankAccount – uvećava stanje na računu za zadati iznos. Ako je iznos pozitivan, izvršava uplatu. Vraća objekat nad kojim je metoda pozvana. 2.withdraw(amount: float) -> BankAccount – umanjuje stanje na računu za zadati iznos. Isplata se izvršava samo ako je iznos pozitivan i ako na računu ima dovoljno novca. Vraća objekat nad kojim je metoda pozvana. 
# 3.display_balance() -> None – ispisuje trenutno stanje na računu. Kreirati objekat klase BankAccount i omogućiti izvršavanje sledećeg niza poziva: account = BankAccount("Ana", 10000) account.deposit(5000).withdraw(2000).deposit(1000) account.display_balance() Očekivani izlaz: Stanje na racunu: 14000
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> 'BankAccount':
        if amount > 0:
            self.balance += amount
        return self
    
    def withdraw(self, amount: float) -> 'BankAccount':
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        return self
    
    def display_balance(self) -> None:
        print(f'Stanje na racunu: {self.balance}')

account = BankAccount("Ana", 10000)
account.deposit(5000).withdraw(2000).deposit(1000)
account.display_balance()

# COMMAND ----------

# 2.Kreirati klasu UserProfile koja predstavlja profil korisnika. Klasa treba da ima sledeće atribute: username – korisničko ime; email – imejl adresa; city – grad; active – informacija o tome da li je profil aktivan. Prilikom kreiranja objekta, profil treba da bude aktivan. Implementirati sledeće metode: 1.change_email(email: str) -> UserProfile – menja imejl adresu korisnika i vraća objekat. 2.change_city(city: str) -> UserProfile – menja grad korisnika i vraća objekat. 3.deactivate() -> UserProfile – deaktivira profil i vraća objekat. 4.activate() -> UserProfile – aktivira profil i vraća objekat. 5.display_info() -> None – ispisuje sve informacije o korisniku. 
# Testirati metode tako da se mogu povezati u jedan izraz: 
# user = UserProfile("ana123", "ana@gmail.com", "Nis") 
# user.change_email("ana@yahoo.com").change_city("Beograd").d eactivate()
# user.display_info()
class UserProfile:
    def __init__(self, username, email, city):
        self.username = username
        self.email = email
        self.city = city
        self.active = True

    def change_email(self, email: str) -> 'UserProfile':
        self.email = email
        return self
    
    def change_city(self, city: str) -> 'UserProfile':
        self.city = city
        return self
    
    def deactivate(self) -> 'UserProfile':
        self.active = False
        return self
    
    def activate(self) -> 'UserProfile':
        self.active = True
        return self

    def display_info(self) -> None:
        print(f'Korisnik: {self.username}, email: {self.email}, grad: {self.city}, Aktivan: {self.active}')

user = UserProfile("ana123", "ana@gmail.com", "Nis")
user.change_email("ana@yahoo.com").change_city("Beograd").deactivate()
user.display_info()

# COMMAND ----------

# # 3.Kreirati klasu Product koja predstavlja proizvod u prodavnici. Klasa treba da ima sledeće atribute: name – naziv proizvoda; price – cena proizvoda; quantity – količina proizvoda na stanju. Implementirati sledeće metode: 1.change_price(new_price: float) -> Product – menja cenu proizvoda ako je nova cena pozitivna. Vraća objekat. 2.add_stock(amount: int) -> Product – povećava količinu proizvoda na stanju za zadati iznos ako je iznos pozitivan. Vraća objekat. 3.sell(amount: int) -> Product – umanjuje količinu proizvoda na stanju ako ima dovoljno proizvoda i ako je količina pozitivna. Vraća objekat. 4.display_info() -> None – ispisuje informacije o proizvodu.
# Kreirati objekat klase Product i omogućiti sledeći način korišćenja: product = Product("Laptop", 80000, 10) product.change_price(75000).sell(2).add_stock(5).sell(3) product.display_info()
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price: float) -> 'Product':
        if new_price > 0:
            self.price = new_price
        return self
    
    def add_stock(self, amount: int) -> 'Product':
        if amount > 0:
            self.quantity += amount
        return self
    
    def sell(self, amount: int) -> 'Product':
        if amount > 0 and self.quantity >= amount:
            self.quantity -= amount
        return self

    def display_info(self) -> None:
        print(f'Proizvod: {self.name}, Cena: {self.price}, Kolicina: {self.quantity}')

product = Product("Laptop", 80000, 10)
product.change_price(75000).sell(2).add_stock(5).sell(3)
product.display_info()