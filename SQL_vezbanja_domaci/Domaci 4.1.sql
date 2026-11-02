-- 1. Koliko redova ima spoj matches i player_match_stats za sezonu 2024/25? Objasnite.
    SELECT COUNT(*) AS br_redova
    FROM matches AS m
    JOIN player_match_stats AS pms ON m.match_id = pms.match_id
    WHERE m.season = '2024/25';
    -- Ima 15200 redova zato sto u player_match_stats imamo podatke o svakom igracu na zasebnoj utakmici (npr. 10001), njegovu minutazu, broj dodavanja, itd. Veza izmedju matches i player_match_stats je 1 : vise. Dok u matches imamo jedan red za npr. match 1001 u player_match_stats 1001 ima 40 redova.

-- 2. Koliko puta je igrač u istoj sezoni igrao za dva različita kluba?
    -- sezona 2023/24
    SELECT DISTINCT p.player_id, p.first_name, p.last_name, m.season, COUNT(DISTINCT pms.team_id) AS broj_timova
    FROM players AS p
    JOIN player_match_stats AS pms ON pms.player_id = p.player_id
    JOIN matches AS m ON m.match_id = pms.match_id
    WHERE season = '2023/24'
    GROUP BY p.player_id, p.first_name, p.last_name, m.season
    HAVING broj_timova >= 2;
    -- sezona 2024/25
    SELECT DISTINCT p.player_id, p.first_name, p.last_name, m.season, COUNT(DISTINCT pms.team_id) AS broj_timova
    FROM players AS p
    JOIN player_match_stats AS pms ON pms.player_id = p.player_id
    JOIN matches AS m ON m.match_id = pms.match_id
    WHERE season = '2024/25'
    GROUP BY p.player_id, p.first_name, p.last_name, m.season
    HAVING broj_timova >= 2;

-- 3. Koliko utakmica ima više kartona od prosečne utakmice? Bez kartona računajte sa 0.
    WITH kartoni AS (
        SELECT m.match_id,
               COUNT(me.event_type) AS br_kartona
        FROM matches AS m
        LEFT JOIN match_events AS me ON me.match_id = m.match_id AND me.event_type IN('yellow_card', 'second_yellow', 'red_card')
        GROUP BY m.match_id
        ORDER BY match_id
    )
    SELECT match_id, br_kartona
    FROM kartoni
    WHERE br_kartona > (SELECT AVG(br_kartona) FROM kartoni)
    ORDER BY br_kartona DESC;

-- 4. Koliko igrača je odigralo više od 10 utakmica u sezoni 2024/25?
    SELECT pms.player_id, COUNT(DISTINCT pms.match_id) AS br_utakmica
    FROM player_match_stats AS pms
    JOIN matches AS m ON pms.match_id = m.match_id
    WHERE m.season = '2024/25'
    GROUP BY pms.player_id
    HAVING COUNT(DISTINCT pms.match_id) > 10
    ORDER BY br_utakmica DESC;

-- 5. Prikažite sve klubove koji su igrali u sezoni 2024/25, bilo kao domaćini ili kao gosti. Koristite UNION, a zatim izmenite upit tako da koristi UNION ALL. Objasnite razliku u broju redova koji dobijate.
 -- UNION
    SELECT t.team_name
    FROM teams AS t
    JOIN matches AS m ON t.team_id = m.home_team_id
    WHERE season = '2024/25'
    UNION
    SELECT t.team_name
    FROM teams AS t
    JOIN matches AS m ON t.team_id = m.away_team_id
    WHERE season = '2024/25';
 -- UNION ALL
    SELECT t.team_name
    FROM teams AS t
    JOIN matches AS m ON t.team_id = m.home_team_id
    WHERE season = '2024/25'
    UNION ALL
    SELECT t.team_name
    FROM teams AS t
    JOIN matches AS m ON t.team_id = m.away_team_id
    WHERE season = '2024/25';
-- UNION ponistava duplikate i vraca nam timove na koje naidje kroz to spajanje UNION, a UNION ALL zalepi sve timove i sve redove gde ih je pronasao u ulozi ili domacina ili gosta. I onda nam izbaci 760 redova. Kroz proveru se dodje da u sezoni 24/25 ima 380 utakmica.