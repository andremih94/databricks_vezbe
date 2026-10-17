-- Prvi dodatni zadatak: Prebrojte utakmice za koje nisu evidentirani ni sudija ni poseta.
SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts,
  attendance,
  referee_name
FROM
  bootcamp.northern_star.matches_flat
WHERE
  attendance IS NULL
  AND referee_name IS NULL;

-- 2. Prikažite sve utakmice odigrane između 1. i 31. marta 2025. godine, uključujući oba datuma. Rezultate sortirajte po datumu odigravanja.
SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts
FROM
  bootcamp.northern_star.matches_flat
WHERE
  DATE(kickoff_ts) BETWEEN '2025-03-01' AND '2025-03-31'
ORDER BY
  kickoff_ts;

-- 3. Koliko je utakmica odigrano u periodu od 20. decembra 2024. do 10. januara 2025. godine, uključujući oba datuma?
SELECT
  match_id,
  kickoff_ts,
  DATE(kickoff_ts) AS datum_utakmice
FROM
  bootcamp.northern_star.matches_flat
WHERE
  DATE(kickoff_ts) BETWEEN '2024-12-20' AND '2025-01-10';

-- 4. Napravite kolonu attendance_status koja prikazuje broj gledalaca ako je poseta evidentirana, a tekst Unknown ako podatak o poseti nedostaje. Prikažite datum utakmice, domaći tim, gostujući tim i novu kolonu.
SELECT
  DATE(kickoff_ts) AS datum_utakmice,
  home_team,
  away_team,
  coalesce(CAST(attendance AS STRING), 'Unknown') AS attendance_status
FROM
  bootcamp.northern_star.matches_flat;

-- 5. Prikažite utakmice odigrane u periodu od 1. do 30. aprila 2025. godine kod kojih je postignuto između 2 i 4 gola ukupno, uključujući obe granice. Rezultate sortirajte po datumu.
SELECT
  home_team,
  away_team,
  DATE(kickoff_ts) AS datum_utakmice,
  home_goals + away_goals AS ukupan_br_golova
FROM
  bootcamp.northern_star.matches_flat
WHERE
  DATE(kickoff_ts) BETWEEN '2025-04-01' AND '2025-04-30'
  AND (home_goals + away_goals) BETWEEN 2 AND 4
ORDER BY
  DATE(kickoff_ts);

-- 6.Pronađite utakmice kod kojih je rezultat na poluvremenu bio nerešen, ali je konačni rezultat bio različit. Prikažite datum, timove, rezultat na poluvremenu i konačni rezultat.
SELECT
  DATE(kickoff_ts) AS datum_utakmice,
  home_team,
  away_team,
  home_goals_ht,
  away_goals_ht,
  home_goals,
  away_goals
FROM
  bootcamp.northern_star.matches_flat
WHERE home_goals_ht = away_goals_ht AND home_goals <> away_goals; 