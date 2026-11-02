CREATE OR REPLACE VIEW bootcamp.prevrat2026.glasovi AS
-- Листе 19–30 нису биле на листићу: у CSV-у постоје само као колоне са нулама.
SELECT bm_uid, opstina, okrug_region, upisani_biraci, vreme_unosa_rezultata, lista, glasovi
FROM (
  SELECT bm_uid, opstina, okrug_region, upisani_biraci, vreme_unosa_rezultata,
         stack(18,
           'lista_1',  CAST(lista_1  AS INT), 'lista_2',  CAST(lista_2  AS INT), 'lista_3',  CAST(lista_3  AS INT),
           'lista_4',  CAST(lista_4  AS INT), 'lista_5',  CAST(lista_5  AS INT), 'lista_6',  CAST(lista_6  AS INT),
           'lista_7',  CAST(lista_7  AS INT), 'lista_8',  CAST(lista_8  AS INT), 'lista_9',  CAST(lista_9  AS INT),
           'lista_10', CAST(lista_10 AS INT), 'lista_11', CAST(lista_11 AS INT), 'lista_12', CAST(lista_12 AS INT),
           'lista_13', CAST(lista_13 AS INT), 'lista_14', CAST(lista_14 AS INT), 'lista_15', CAST(lista_15 AS INT),
           'lista_16', CAST(lista_16 AS INT), 'lista_17', CAST(lista_17 AS INT), 'lista_18', CAST(lista_18 AS INT)
         ) AS (lista, glasovi)
  FROM parlamentarni_izbori_2
);

-- 1. Колико бирачких места има у свакој општини? Која општина има највише?
  SELECT 
    opstina,
    COUNT (DISTINCT bm_broj) AS br_birackih_mesta
  FROM parlamentarni_izbori_2
  GROUP BY opstina
  ORDER BY br_birackih_mesta DESC;

-- 2. Колика је укупна излазност у целој табели? Рачунајте из сабраних бројева, не као просек излазности места.
  SELECT SUM(upisani_biraci) AS ukupno_biraca,
         SUM(glasali_biraci) AS ukupno_izasli,
         ROUND((ukupno_izasli / ukupno_biraca *100), 2) AS `izlaznost u %`
  FROM parlamentarni_izbori_2;

-- 3. Колико је гласова добила свака листа и колики је то удео у свим важећим гласовима? Прикажите првих пет листа.
  SELECT lista,
  SUM(glasovi) AS br_glasova,
  ROUND(SUM(glasovi) * 100 / (SELECT SUM(glasovi) FROM glasovi), 2) AS `udeo_u_%`
  FROM glasovi
  GROUP BY lista
  ORDER BY br_glasova DESC;

-- 4. Колико бирачких места има мање од 100 уписаних бирача?
  SELECT bm_broj, upisani_biraci
  FROM parlamentarni_izbori_2
  WHERE upisani_biraci < 100
  ORDER BY bm_broj;

-- 5. Која општина има највећи, а која најмањи удео неважећих листића? Рачунајте само општине са бар 1.000 листића.
  SELECT opstina,
  SUM(listici_u_kutiji) AS ukupno_listica,
  SUM(nevazeci_listici) AS ukupno_nevazecih,
  ROUND(100 * ukupno_nevazecih / ukupno_listica, 2) AS udeo_nevazecih 
  FROM bootcamp.prevrat2026.parlamentarni_izbori_2
  GROUP BY opstina
  HAVING ukupno_listica >= 1000
  ORDER BY udeo_nevazecih DESC;

-- Штрпце 6.43, Иностранство 0.21