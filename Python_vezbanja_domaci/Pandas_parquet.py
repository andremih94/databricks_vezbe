# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS bootcamp.northern_star.raw_2025_26;

# COMMAND ----------

import zipfile
zipfile.ZipFile('/Volumes/bootcamp/northern_star/raw_2025_26/nsl_2025_26.zip') \
     .extractall('/Volumes/bootcamp/northern_star/raw_2025_26/')

# COMMAND ----------

# 1. Учитати matches_2025_26.parquet у DataFrame m и одговорити: колико има редова и
# колона, како се зову колоне и како изгледа првих пет редова?
# Output: (380, 17)

import pandas as pd

R = '/Volumes/bootcamp/northern_star/raw_2025_26/'

m = pd.read_parquet(R + 'matches_2025_26.parquet')

m.shape
m.head(5)

# COMMAND ----------

# 2. Помоћу info() и isna().sum() пронаћи које колоне имају празне вредности и колико

# m.info()

m.isna().sum()

# COMMAND ----------

# 3. Учитати исте податке из matches_2025_26.csv и упоредити dtypes колона kickoff_ts,
# original_kickoff_ts и attendance са Parquet верзијом
# Затим CSV учитати поново са parse_dates=[...]
# Питање: зашто је attendance и даље float64, а у Parquet фајлу цео број?

m = pd.read_parquet(R + 'matches_2025_26.parquet')
c = pd.read_csv(R + 'matches_2025_26.csv', parse_dates=['kickoff_ts', 'original_kickoff_ts'])

m.dtypes
c.dtypes

# COMMAND ----------

# 4. Помоћу os.path.getsize упоредити величину CSV и Parquet фајла са утакмицама
# Колико пута је CSV већи?
import os

csv = os.path.getsize(R + 'matches_2025_26.csv')
parket = os.path.getsize(R + 'matches_2025_26.parquet')

print(csv, parket)

print(csv / parket)

# COMMAND ----------

# 5. Помоћу describe() одговорити: колико голова у просеку дају домаћини, а колико гости, и
# колика је највећа посета?   	prosek home 1.384211   prosek away0.963158    max att=30419
m.describe()

# COMMAND ----------

# 6. Помоћу value_counts() одговорити: какво време је било најчешће и која три судије су
# судила највише утакмица?   'Cloudy' najcesce vremenske prilike 
# sudije:
# Lukas Brenner       34
# Milica Jovanović    32
# Pieter de Vries     32

# m.value_counts(['weather'])
m.value_counts(['referee'])

# COMMAND ----------

# 7. Приказати само колоне matchday, home_team, away_team, home_goals и away_goals за
# утакмицу са match_id 2526134
# Помоћ: m.loc[услов, листа_колона]
m.loc[m['match_id'] == 2526134, ['matchday', 'home_team', 'away_team', 'home_goals', 'away_goals']]

# COMMAND ----------

# 8. Филтрирање
# Додати колону total_goals и избројати утакмице са бар 5 голова
# Колико утакмица је NPM добио на свом терену?
# Колико утакмица је одиграно у децембру 2025? (помоћ: поређење са датумима '2025-
# 12-01')
# *Издвој утакмице које су почеле пре 14 или од 19 часова, по киши или снегу, са
# посетом већом од 15.000, и прикажи их сортиране по посети. Пази на заграде и
# знакове & и |.

# print(len(m.loc[m['home_team'].isin(['NPM']) & (m['home_goals'] > m['away_goals'])])) # 9 utakmica

# m['total_goals'] = m['home_goals'] + m['away_goals']
# print((m['total_goals'] >= 5).sum())    ## 28 takvih utakmica

# len(m.loc[m['kickoff_ts'].between('2025-12-01', '2025-12-31 23:59:59')])  ## 20 utakmica
# m['month'] = m['kickoff_ts'].dt.month
# m['month'].value_counts()

utakmice_filter = (((m['kickoff_ts'].dt.hour < 14) | (m['kickoff_ts'].dt.hour == 19)) & (m['weather'].isin(['Snow', 'Rain'])) & (m['attendance'] > 15000))

m.loc[utakmice_filter].sort_values('attendance', ascending=False)

# COMMAND ----------

# 9. Сортирање
# Пет утакмица са највећом посетом: match_id, тимови, стадион и посета
# Када је одиграна прва, а када последња утакмица сезоне?
m.loc[:, ['match_id', 'home_team', 'away_team', 'attendance']].sort_values('attendance', ascending=False).head(5)

# COMMAND ----------

# 10. Додати колоне goal_diff (голови домаћина минус голови госта) и result са вредностима 'H',
# 'D' или 'A'
# Помоћ: почетна вредност па m.loc[услов, 'result'] = ...
# Колико је било домаћих победа, нерешених и гостујућих победа? Колико је голова
# пало у целој сезони?
m['goal_diff'] = m['home_goals'] - m['away_goals']
m['result'] = 'D'
m['total_goals'] = m['home_goals'] + m['away_goals']
m.loc[m['home_goals'] > m['away_goals'], 'result'] = 'H'
m.loc[m['home_goals'] < m['away_goals'], 'result'] = 'A'

m.loc[:, ['home_team', 'away_team', 'home_goals', 'away_goals', 'total_goals', 'goal_diff', 'result']]
print(m['result'].value_counts())
print(m['total_goals'].sum())

# COMMAND ----------

# 11. Додати колону weekday са именом дана почетка утакмице (помоћ: .dt.day_name())
# Колико утакмица је играно којим даном?
# Питање: зашто постоји тачно 7 утакмица уторком? (погледати original_kickoff_ts)
# m['weekday'] = m['kickoff_ts'].dt.day_name()
# m['weekday'].value_counts()

print(m['original_kickoff_ts'].dt.day_name().value_counts())


# COMMAND ----------

# 12. Пронаћи све померене утакмице (оне које имају original_kickoff_ts) и додати колону
# delay_days: за колико дана је утакмица померена
# Помоћ: разлика два датума па .dt.days
# Колико их има, и какво је време било на тим утакмицама?
pomerene_utakmice = m.loc[m['original_kickoff_ts'].notna()]
m['delay_days'] = (m['kickoff_ts'] - m['original_kickoff_ts']).dt.days

print(pomerene_utakmice[['home_team', 'away_team', 'home_goals', 'away_goals', 'weather', 'delay_days']])
