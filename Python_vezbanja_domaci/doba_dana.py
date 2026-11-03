# Databricks notebook source
# 1. Određivanje doba dana Napisati Python program koji za svaki sat u toku dana (od 0 do 23) 
# ispisuje odgovarajuće doba dana: noć (od 22 do 6 časova), jutro (od 6 do 12 časova), popodne (od # 12 do 18 časova) ili veče (od 18 do 22 časa).
for i in range(0, 24):
    if i >= 6 and i < 12:
        print(f'{i} jutro')
    elif i >= 12 and i < 18:
        print(f'{i} popodne')
    elif i >= 18 and i < 22:
        print(f'{i} veče')
    else:
        print(f'{i} noć')
    