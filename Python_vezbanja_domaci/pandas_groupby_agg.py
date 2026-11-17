# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS bootcamp.northern_star.prodavnica

# COMMAND ----------

import pandas as pd
R = '/Volumes/bootcamp/northern_star/prodavnica/dostave.csv'

# COMMAND ----------

# Zadatak 1 – Analiza dostava po gradu. Izračunati prosečnu cenu dostave za svaki grad.
# Rezultat treba da sadrži:
# grad;
# prosečnu cenu dostave.
# Sortirati rezultat opadajuće prema prosečnoj ceni.
df = pd.read_csv(R)

df.groupby('city')['delivery_fee'].mean().sort_values(ascending=False)

# COMMAND ----------

# Zadatak 2 – Analiza kurirskih službi. Za svaku kurirsku službu izračunati:
# Broj obavljenih dostava.
# Ukupnu cenu svih dostava.
# Prosečnu cenu dostave.
# Prosečnu udaljenost dostave.
# Rezultat treba da bude jedan DataFrame sa odgovarajućim nazivima kolona
df.groupby(['courier']).agg(broj_dostava=('delivery_id', 'count'), ukupna_cena=('delivery_fee', 'sum'), prosecna_cena=('delivery_fee', 'mean'), prosecna_udaljenost=('distance_km', 'mean')
)

# COMMAND ----------

# Zadatak 4 – Povezivanje sa šifarnikom zona. Povezati tabelu dostava sa šifarnikom zona.
# Koristiti left spajanje.
# Rezultat treba da sadrži sve kolone iz obe tabele.
zones = pd.DataFrame({
    "zone_id": [1, 2, 3, 4],
    "region": ["Jug", "Centralna Srbija", "Vojvodina", "Centralna Srbija"],
    "zone_name": ["Zona A", "Zona B", "Zona C", "Zona D"]
})

merged = df.merge(
    zones,
    on="zone_id",
    how="left"
)

merged.head()

# COMMAND ----------

# Zadatak 5 – Analiza dostava po regionima. Povezati tabelu dostava sa šifarnikom zona.
# Zatim, za svaki region izračunati:
# Broj dostava.
# Prosečnu cenu dostave.
# Ukupnu cenu svih dostava.
# Prosečnu udaljenost dostave.
# Rezultat treba da bude jedan DataFrame.
zones = pd.DataFrame({
    "zone_id": [1, 2, 3, 4],
    "region": ["Jug", "Centralna Srbija", "Vojvodina", "Centralna Srbija"],
    "zone_name": ["Zona A", "Zona B", "Zona C", "Zona D"]
})

merged = df.merge(
    zones,
    on="zone_id",
    how="left"
)
merged.groupby(['region']).agg(broj_dostava=('delivery_id', 'count'), prosecna_cena=('delivery_fee', 'mean'), ukupna_cena=('delivery_fee', 'sum'), prosecna_udaljenost=('distance_km', 'mean'))