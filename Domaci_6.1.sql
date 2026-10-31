-- Domaci 6.1.
-- 1. Kreiranje dimenzije igrača Na osnovu tabele players napravite tabelu dim_player koja sadrži sledeće kolone: player_id, ime, prezime, poziciju i nacionalnost igrača. Koliko redova ima novokreirana tabela?

    CREATE OR REPLACE TABLE dim_player AS 
    SELECT player_id, 
           first_name AS ime, 
           last_name AS prezime, 
           position AS pozicija,
           nationality AS nacionalnost 
    FROM players;

    SELECT COUNT(*) FROM dim_player; --Nova tabela dim_players ima 681 red.
    SELECT * FROM dim_player;

-- 2. Kreiranje dimenzije datuma i činjenične tabele Napravite tabelu dim_date na isti način kao na predavanju. Zatim napravite tabelu fact_player_match na osnovu tabela player_match_stats i matches. Tabela treba da sadrži sledeće kolone: match_id, date_key, player_id, team_id, minutes_played, shots, passes i rating. U tabelu uključite samo podatke koji se odnose na odigrane utakmice. Kolika je granularnost tabele fact_player_match, odnosno šta predstavlja jedan njen red? Koliko redova ima ova tabela?

    CREATE OR REPLACE TABLE dim_date AS
SELECT CAST(DATE_FORMAT(d, 'yyyyMMdd') AS INT) AS date_key,
       d                                       AS full_date,
       DATE_FORMAT(d, 'EEEE')                  AS weekday_name,
       DAYOFWEEK(d) IN (1, 7)                  AS is_weekend,
       CASE WHEN MONTH(d) >= 7 THEN CONCAT(YEAR(d), '/', SUBSTRING(CAST(YEAR(d) + 1 AS STRING), 3, 2))
            ELSE CONCAT(YEAR(d) - 1, '/', SUBSTRING(CAST(YEAR(d) AS STRING), 3, 2))
       END                                     AS season
FROM (SELECT EXPLODE(SEQUENCE(DATE'2023-07-01', DATE'2025-06-30', INTERVAL 1 DAY)) AS d);

    SELECT * FROM dim_date;

    CREATE OR REPLACE TABLE fact_player_match AS
SELECT
  s.match_id,
  CAST(DATE_FORMAT(m.kickoff_ts, 'yyyyMMdd') AS INT) AS date_key,
  s.player_id,
  s.team_id,
  s.minutes_played,
  s.shots,
  s.passes,
  TRY_CAST(s.rating AS DOUBLE) AS rating
FROM player_match_stats s
JOIN matches m ON s.match_id = m.match_id
WHERE m.status = 'played';

SELECT * FROM fact_player_match; -- Jedan red predstavlja match_id + player_id, tj. jednog igraca na jednoj utakmici i njegovu statistiku u toj utakmici.
SELECT COUNT(*) FROM fact_player_match; -- 30400 redova ima fact_player_match.
DESCRIBE fact_player_match;

-- 3. Prosečna ocena igrača po poziciji Koristeći napravljene dimenzije i činjeničnu tabelu, izračunajte prosečnu ocenu (rating) igrača za svaku poziciju tokom sezone 2024/25. Prikažite poziciju i odgovarajuću prosečnu ocenu.
    SELECT p.pozicija, 
           ROUND(AVG(f.rating), 2) AS prosecna_ocena
    FROM fact_player_match AS f
    JOIN dim_player AS p ON f.player_id = p.player_id
    JOIN dim_date AS d ON f.date_key = d.date_key
    WHERE d.season = '2024/25' AND NOT isnan(f.rating)
    GROUP BY p.pozicija;

-- 4. Dodavanje broja golova u činjeničnu tabelu Proširite tabelu fact_player_match dodavanjem kolone koja predstavlja broj golova koje je svaki igrač postigao na određenoj utakmici. Koliki je ukupan zbir golova svih igrača u tabeli fact_player_match?
    
    ALTER TABLE fact_player_match ADD COLUMN goals INT;
    
    UPDATE fact_player_match AS f
    SET goals = (
        SELECT COUNT(*)
        FROM match_events AS me
        WHERE me.match_id = f.match_id AND me.player_id = f.player_id AND me.event_type IN('goal', 'penalty_goal')
    );
    SELECT * FROM fact_player_match;
    SELECT SUM(goals) FROM fact_player_match; -- 2043 gola.