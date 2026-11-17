# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# 1. Analiza rezultata utakmica:
# 1.Pronaći sve utakmice u kojima su oba tima postigla bar po jedan gol.
# 2.Pronaći sve utakmice u kojima je domaćin pobedio sa tačno jednim golom razlike.
# 3.Koliko utakmica je završeno rezultatom 0:0?
# 4.Prikazati 10 utakmica sa najviše ukupno postignutih golova.
import pandas as pd

R = '/Volumes/bootcamp/northern_star/raw_2025_26/'

m = pd.read_parquet(R + 'matches_2025_26.parquet')
# oba tima GG:
m.loc[(m['home_goals'] >= 1) & (m['away_goals'] >= 1)]
# #Domacin pobeda 1 gol razlike:
m.loc[(m['home_goals'] - m['away_goals']) == 1]
#tacan rez: 0:0
len(m.loc[(m['home_goals'] == 0) & (m['away_goals'] == 0)])
#top 10 utakmica sa najvise golova:
m['total_goals'] = m['home_goals'] + m['away_goals']
m.sort_values('total_goals', ascending=False).head(10)

# COMMAND ----------

# 2. Analiza jednog tima, za tim po izboru: 
# 1.Prikazati sve utakmice u kojima je učestvovao. 
# 2.Koliko je puta pobedio, izgubio i odigrao nerešeno? 
# 3.Koliko je golova postigao kao domaćin, a koliko kao gost? 
# 4.Pronaći utakmicu u kojoj je postigao najviše golova.

T = 'EKR'
tim = m.loc[(m['home_team'] == T) | (m['away_team'] == T)].copy()
display(tim)
# 2. Pobede, porazi, nerešeno
pobede = len(m.loc[(m['home_team'] == T) & (m['home_goals'] > m['away_goals'])]) \
        + len(m.loc[(m['away_team'] == T) & (m['away_goals'] > m['home_goals'])])
porazi = len(m.loc[(m['home_team'] == T) & (m['home_goals'] < m['away_goals'])]) \
        + len(m.loc[(m['away_team'] == T) & (m['away_goals'] < m['home_goals'])])
nereseno = len(tim.loc[tim['home_goals'] == tim['away_goals']])
print(pobede, porazi, nereseno)
# 3. Golovi kao domaćin i kao gost
golovi_kuci = m.loc[m['home_team'] == T, 'home_goals'].sum()
golovi_gost = m.loc[m['away_team'] == T, 'away_goals'].sum()
print(golovi_kuci, golovi_gost)
# # 4. Utakmica sa najviše postignutih golova tog tima
tim['golovi_tima'] = tim['home_goals'].where(tim['home_team'] == T, tim['away_goals'])
tim.loc[tim['golovi_tima'] == tim['golovi_tima'].max()]

# COMMAND ----------

# 3. Analiza stadiona 
# 1.Prikazati sve različite stadione na kojima su odigrane utakmice.
print(m['stadium'].unique())
print(m['stadium'].nunique())
# 2.Pronaći stadion na kojem je odigrano najviše utakmica:
broj_utakmica = m['stadium'].value_counts()
print(broj_utakmica.head(1))
# 3.Za svaki stadion izračunati prosečnu posećenost:
prosek = m.groupby('stadium')['attendance'].mean()
print(prosek)
# 4.Prikazati pet stadiona sa najvećom prosečnom posećenošću:
print(prosek.sort_values(ascending=False).head(5))