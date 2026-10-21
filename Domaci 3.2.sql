-- Osnovni nivo:
-- 1.Prikažite naziv svakog kluba i naziv stadiona na kojem igra domaće utakmice.
SELECT t.team_name, s.stadium_name
FROM teams AS t
LEFT JOIN stadiums AS s ON s.stadium_id = t.stadium_id;

-- 2.Prikažite ime i prezime igrača i naziv kluba za koji je igrao u sezoni 2024/25. Uklonite duplikate iz rezultata.
SELECT DISTINCT p.first_name, p.last_name, t.team_name, m.season
FROM players AS p
JOIN player_contracts AS pc ON pc.player_id = p.player_id
JOIN teams AS t ON t.team_id = pc.team_id
JOIN matches AS m ON m.home_team_id = t.team_id
WHERE season = '2024/25';

-- 3.Prikažite datum odigravanja utakmice, naziv stadiona i broj gledalaca za sve utakmice u sezoni 2024/25.
SELECT date(m.kickoff_ts), s.stadium_name, m.attendance
FROM matches AS m
JOIN stadiums AS s ON m.stadium_id = s.stadium_id
WHERE season = '2024/25';

-- Srednji nivo:
-- 1.Prikažite sve utakmice za koje nije evidentiran broj gledalaca. Prikažite datum, domaći klub i gostujući klub.
SELECT date(m.kickoff_ts) AS datum, t.team_name AS domacin, t2.team_name AS gost
FROM matches AS m
LEFT JOIN teams AS t ON m.home_team_id = t.team_id
LEFT JOIN teams AS t2 ON m.away_team_id = t2.team_id
WHERE m.attendance IS NULL;

-- 2.Pronađite stadione na kojima nije odigrana ni jedna utakmica u sezoni 2024/25. 
SELECT s.stadium_name, m.season
FROM stadiums AS s
LEFT JOIN matches AS m ON s.stadium_id = m.stadium_id AND m.season = '2024/25'
WHERE m.match_id IS NULL;

-- 3.Za svaki klub izračunajte ukupan broj žutih kartona koje su dobili njegovi igrači u sezoni 2024/25. Rezultat sortirajte opadajuće prema broju kartona.

SELECT t.team_name, SUM(CASE WHEN event_type = 'yellow_card' THEN 1 ELSE 0 END) AS ukupan_br_zutih_kartona
FROM teams AS t
JOIN match_events AS me ON t.team_id = me.team_id
JOIN matches AS m ON m.match_id = me.match_id
WHERE m.season = '2024/25'
GROUP BY t.team_name
ORDER BY ukupan_br_zutih_kartona DESC;

-- Napredni nivo:
-- 1.Pronađite pet igrača sa najvećim brojem asistencija u sezoni 2024/25. Prikažite ime igrača i broj asistencija.

SELECT p.first_name, p.last_name, COUNT(*) AS br_asistencija
FROM players AS p
JOIN match_events as me ON me.player_id = p.player_id
JOIN matches AS m ON me.match_id = m.match_id
WHERE me.event_type = 'goal' AND me.related_player_id IS NOT NULL AND m.season = '2024/25'
GROUP BY p.first_name, p.last_name
ORDER BY br_asistencija DESC
LIMIT 5;

-- 2.Pronađite tri igrača sa najvećim ukupnim brojem odigranih minuta u sezoni 2024/25. Prikažite ime igrača, klub i ukupan broj minuta.

SELECT p.first_name, p.last_name, t.team_name, SUM(minutes_played) AS ukupan_br_minuta
FROM player_match_stats as pms 
JOIN matches AS m ON m.match_id = pms.match_id
JOIN players AS p ON pms.player_id = p.player_id
JOIN teams AS t ON t.team_id = pms.team_id
WHERE m.season = '2024/25'
GROUP BY p.first_name, p.last_name, t.team_name
ORDER BY ukupan_br_minuta DESC
LIMIT 3;

-- 3.Za svaku sezonu prikažite broj isključenja po klubovima. Računajte događaje red_card i second_yellow. Uključite samo klubove koji su imali najmanje jedno isključenje.

SELECT t.team_name, m.season, COUNT(*) AS br_iskljucenja
FROM teams AS t
JOIN match_events AS me ON t.team_id = me.team_id
JOIN matches AS m ON m.match_id = me.match_id
WHERE me.event_type IN ('red_card', 'second_yellow')
GROUP BY t.team_name, m.season
HAVING COUNT(*) >=1
ORDER BY t.team_name, m.season;