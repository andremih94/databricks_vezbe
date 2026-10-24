-- 1. Za svaku sezonu prikažite ukupan broj utakmica, ukupan broj postignutih golova i prosečan broj golova po utakmici.
SELECT
  season,
  COUNT(*) AS broj_utakmica,
  SUM(home_goals + away_goals) AS ukupan_broj_golova,
  ROUND(SUM(home_goals + away_goals) / COUNT(*), 2) AS prosecni_broj_golova_po_utakmici
FROM
  matches_flat
GROUP BY
  season
ORDER BY
  season;

SELECT season, COUNT(*) total_matches, SUM(home_goals + away_goals) total_goals, ROUND(AVG(home_goals + away_goals), 2) avg_goals_per_match FROM matches GROUP BY season;

-- 2. Za svaki stadion prikažite najmanju, najveću i prosečnu zabeleženu posetu, kao i broj utakmica za koje je poseta poznata.
SELECT
  stadium_name,
  MIN(attendance) AS najmanji_broj_poseta,
  MAX(attendance) AS najveci_broj_poseta,
  ROUND(AVG(attendance), 1) AS prosecni_broj_poseta,
  COUNT(match_id) AS broj_utakmica
FROM
  matches_flat
GROUP BY
  stadium_name
ORDER BY
  stadium_name;

-- 3. Prikažite sudije koje su sudile najmanje 10 utakmica i koje su ukupno pokazale najmanje 20 žutih kartona. Prikažite ime sudije, broj utakmica i ukupan broj žutih kartona.
SELECT
  referee_name,
  COUNT(*) AS broj_utakmica,
  SUM(home_yellow_cards + away_yellow_cards) AS ukupan_broj_zutih_kartona
FROM
  matches_flat
GROUP BY
  referee_name
HAVING
  COUNT(*) >= 10
  AND SUM(home_yellow_cards + away_yellow_cards) >= 20
ORDER BY
  ukupan_broj_zutih_kartona DESC;

-- 4. Podelite utakmice prema ukupnom broju golova na kategorije Bez golova (0), Malo golova (1 ili 2) i Mnogo golova (3 ili više). Prikažite broj utakmica u svakoj kategoriji i najveći broj golova na utakmici u toj kategoriji.
SELECT
  CASE
    WHEN (home_goals + away_goals) = 0 THEN 'Bez golova'
    WHEN (home_goals + away_goals) <= 2 THEN 'Malo golova'
    ELSE 'Mnogo golova'
  END AS kategorija_po_golovima,
  COUNT(match_id) AS broj_utakmica,
  MAX(home_goals + away_goals) AS najveci_br_golova
FROM
  matches_flat
GROUP BY
  kategorija_po_golovima;

-- 5. Za svaki klub prikažite broj utakmica koje je odigrao kao domaćin, broj pobeda kod kuće i broj poraza kod kuće. U rezultat uključite samo klubove koji su kod kuće odigrali najmanje 10 utakmica.

SELECT
  (home_team) AS domacin, 
  COUNT(match_id) AS broj_utakmica,
  SUM(CASE WHEN home_goals > away_goals THEN 1 ELSE 0 END) AS br_pobeda, 
  SUM(CASE WHEN home_goals < away_goals THEN 1 ELSE 0 END) AS br_poraza
FROM matches_flat
GROUP BY domacin
HAVING broj_utakmica >= 10;

-- 6. Za svakog sudiju prikažite ukupan broj utakmica, broj utakmica u kojima je pokazao bar jedan crveni karton i procenat takvih utakmica u odnosu na sve utakmice koje je sudio.

SELECT 
  referee_name, 
  COUNT(*) AS ukupan_br_utakmica, 
  SUM(CASE WHEN (home_red_cards + away_red_cards) >= 1  THEN 1 ELSE 0 END) AS utakmice_sa_crvenim, 
  SUM(CASE WHEN (home_red_cards + away_red_cards) >= 1  THEN 1 ELSE 0 END)/COUNT(*)*100 AS procenat_takvih_utakmica
FROM matches_flat
GROUP BY referee_name
ORDER BY utakmice_sa_crvenim DESC;

-- 7. Za svaku sezonu prikažite broj pobeda domaćina, broj nerešenih utakmica i broj pobeda gostiju. Takođe prikažite procenat utakmica koje su završene nerešenim rezultatom.
SELECT 
  season, 
  SUM(CASE WHEN home_goals > away_goals THEN 1 ELSE 0 END) AS br_pobeda_domacina,
  SUM(CASE WHEN home_goals = away_goals THEN 1 ELSE 0 END) AS br_neresenih,
  SUM(CASE WHEN home_goals < away_goals THEN 1 ELSE 0 END) AS br_pobeda_gosta,
  ROUND(SUM(CASE WHEN home_goals = away_goals THEN 1 ELSE 0 END)/COUNT(*)*100, 2) AS procenat_neresenih_utakmica
FROM matches_flat
GROUP BY season;