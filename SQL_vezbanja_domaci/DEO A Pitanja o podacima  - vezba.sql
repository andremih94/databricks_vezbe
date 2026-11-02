-- Део А — питања о подацима
-- 1. Колико утакмица је одиграно у децембру 2024?
    SELECT COUNT(*) AS br_utakmica
    FROM matches
    WHERE kickoff_ts >= '2024-12-01' AND kickoff_ts < '2025-01-01'; -- 52 utakmice

-- 2. Која утакмица је имала највише голова? Прикажите датум, имена оба клуба и резултат.
    SELECT ht.team_name, at.team_name, m.kickoff_ts, home_goals, away_goals, home_goals + away_goals AS ukupno_golova
    FROM matches AS m
    JOIN teams AS ht ON ht.team_id = m.home_team_id
    JOIN teams AS at ON at.team_id = m.away_team_id 
    ORDER BY ukupno_golova DESC
    LIMIT 1; -- Utakmica izmedju Northport United-a i Newbury Forest-a 6:3 zavrsena, ukupno 9 golova.

-- 3. Колико различитих судија је судило утакмице лиге?
    SELECT r.*
    FROM referees AS r
    LEFT JOIN matches AS m ON m.referee_id = r.referee_id
    WHERE m.referee_id IS NULL; -- Provera sudije koji nije sudio ni jednu utakmicu.

    SELECT COUNT(DISTINCT referee_id) AS br_sudija
    FROM matches; -- 19 sudija

-- 4. Колико утакмица сезоне 2023/24 је одиграно по снегу или магли?
    SELECT match_id, 
           season, 
           weather
    FROM matches
    WHERE season = '2023/24' AND weather IN('snow', 'fog'); -- 25 utakmica

-- 5. Колико утакмица нема пријављену посету, а колико их је одиграно без публике?
    SELECT 
        SUM(CASE WHEN attendance IS NULL THEN 1 ELSE 0 END) AS bez_prijavljene_posete,
        SUM(CASE WHEN attendance = 0 THEN 1 ELSE 0 END) AS bez_publike
    FROM matches; -- 17 bez prijavljene posete, 1 utakmica bez publike.

-- 6. Колики је просечан број картона (жути, други жути и црвени) по утакмици у свакој сезони? Пазите на утакмице без иједног картона.
    SELECT m.season, 
           COUNT(me.match_id) AS ukupno_kartona, 
           COUNT(DISTINCT m.match_id) AS ukupno_utakmica,
           ROUND(COUNT(me.match_id) / COUNT(DISTINCT m.match_id), 2) AS prosek_kartona
    FROM matches AS m
    LEFT JOIN match_events AS me ON m.match_id = me.match_id AND me.event_type IN('yellow_card', 'second_yellow', 'red_card')
    GROUP BY season; -- sezona 2023/24 prosek kartona: 3.56, sezona 2024/25 3.47

-- 7. Колико играча је бар једном искључено (red_card или second_yellow)?
    SELECT COUNT(DISTINCT player_id) AS broj_igraca
    FROM match_events AS me
    WHERE event_type IN('second_yellow', 'red_card'); -- 81 igrac

-- 8. Који клуб је у сезони 2024/25 добио највише жутих картона (рачунајте и други жути)?
    SELECT t.team_name, COUNT(*) AS br_zutih
    FROM match_events AS me
    JOIN teams AS t ON me.team_id = t.team_id
    JOIN matches AS m ON m.match_id = me.match_id
    WHERE season = '2024/25' AND me.event_type IN('yellow_card', 'second_yellow')
    GROUP BY t.team_name
    ORDER BY br_zutih DESC; -- Ashford Rovers 77 kartona

-- 9. Колико одиграних утакмица има више картона од просечне утакмице? Утакмице без картона рачунајте са 0.
    WITH po_utakimci AS (
        SELECT m.match_id, COUNT(me.match_id) AS kartoni
        FROM matches AS m
        LEFT JOIN match_events AS me ON m.match_id = me.match_id AND me.event_type IN('yellow_card','second_yellow', 'red_card')
        GROUP BY m.match_id
    )
    SELECT COUNT(*) AS broj_utakmica
    FROM po_utakimci
    WHERE kartoni > (SELECT AVG(kartoni) FROM po_utakimci); -- 370 utakmica ima vise kartona od prosecne.

-- 10. Ко је освојио лигу у сезони 2023/24 и са колико бодова? Рачунајте и домаће и гостујуће
-- утакмице.
    WITH bodovi AS (
        SELECT home_team_id AS team_id,
            CASE WHEN home_goals > away_goals THEN 3
                 WHEN home_goals = away_goals THEN 1
                 ELSE 0 END AS bodovi
        FROM matches
        WHERE season = '2023/24'
        UNION ALL
        SELECT away_team_id AS team_id,
            CASE WHEN away_goals > home_goals THEN 3
                 WHEN away_goals = home_goals THEN 1
                 ELSE 0 END AS bodovi
        FROM matches
        WHERE season = '2023/24'
    )
    SELECT t.team_name, SUM(b.bodovi) AS ukupno_bodova
    FROM bodovi AS b
    JOIN teams AS t ON t.team_id = b.team_id
    GROUP BY t.team_name
    ORDER BY ukupno_bodova DESC; -- Castlebrook United, 77 bodova.