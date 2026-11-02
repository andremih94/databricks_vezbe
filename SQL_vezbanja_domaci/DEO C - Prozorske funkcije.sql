-- Део C — прозорске функције
-- На пројекту у петак ће бити само питања, без додатних сугестија за решење (плавом бојом)
-- 1. SUM/AVG OVER: За сваку утакмицу у сезони 2023/24 прикажите посету и колико је изнад или испод просека свог стадиона. Која утакмица је била највише изнад просека свог стадиона?
    SELECT m.match_id, m.attendance, s.capacity, 
           ROUND(AVG(m.attendance) OVER (PARTITION BY s.stadium_id), 0) AS prosek_stadiona,
           ROUND(m.attendance - AVG(m.attendance) OVER (PARTITION BY s.stadium_id), 0) AS razlika_od_proseka
    FROM matches AS m
    JOIN stadiums AS s ON s.stadium_id = m.stadium_id
    WHERE m.season = '2023/24'
    ORDER BY razlika_od_proseka DESC;
-- 2. Рангирање са QUALIFY: Рангирајте играче по броју асистенција у сезони 2024/25 помоћу DENSE_RANK и прикажите прва два ранга.
    SELECT p.player_id, p.first_name, p.last_name, COUNT(*) AS br_asistencija,
           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rang
    FROM players AS p
    JOIN match_events AS me ON me.related_player_id = p.player_id
    JOIN matches AS m ON m.match_id = me.match_id
    WHERE m.season = '2024/25' AND me.event_type IN('goal')
    GROUP BY p.player_id, p.first_name, p.last_name
    QUALIFY rang <= 2
    ORDER BY rang;
-- 3. ROW_NUMBER, прво појављивање: За сваки клуб, ко је дао први гол клуба у сезони 2024/25 и када?
    SELECT t.team_name, p.first_name, p.last_name, m.kickoff_ts, 
           ROW_NUMBER() OVER (PARTITION BY me.team_id ORDER BY m.kickoff_ts) AS rn
    FROM match_events AS me
    JOIN players AS p ON me.player_id = p.player_id
    JOIN teams AS t ON me.team_id = t.team_id
    JOIN matches AS m ON me.match_id = m.match_id
    WHERE m.season = '2024/25' AND me.event_type IN('goal', 'penlaty_goal')
    QUALIFY rn = 1
    ORDER BY t.team_name;
-- 4. LAG: Број голова по месецима у сезони 2024/25 и промена у односу на претходни месец. Који месец има највећи раст?
    WITH mesecno AS (
        SELECT DATE_FORMAT(m.kickoff_ts, 'yyyy-MM') AS mesec,
           SUM(m.home_goals + m.away_goals) AS broj_golova
        FROM matches AS m
        WHERE m.season = '2024/25'
        GROUP BY mesec
    )
    SELECT mesec,
           broj_golova,
           LAG(broj_golova) OVER (ORDER BY mesec) AS prethodni_mesec,
           broj_golova - LAG(broj_golova) OVER (ORDER BY mesec) AS promena
    FROM mesecno
    ORDER BY promena DESC;
-- 5. Tекући збир са оквиром: Који клуб је први стигао до 50 голова у сезони 2024/25 и ког датума? (редови по клубу помоћу UNION ALL, па SUM OVER са ROWS BETWEEN)
   WITH po_klubu AS (
     SELECT m.home_team_id AS team_id, m.kickoff_ts, m.home_goals AS golovi
     FROM matches AS m
     WHERE m.season = '2024/25'
     UNION ALL
     SELECT m.away_team_id AS team_id, m.kickoff_ts, m.away_goals AS golovi
     FROM matches AS m
     WHERE m.season = '2024/25' 
   ),
   tekuci AS (
     SELECT team_id, kickoff_ts, 
            SUM(golovi) OVER (PARTITION BY team_id ORDER BY kickoff_ts ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ukupno
    FROM po_klubu
   )
   SELECT t.team_name, x.kickoff_ts, x.ukupno
   FROM tekuci AS x
   JOIN teams AS t ON t.team_id = x.team_id
   WHERE x.ukupno >= 50
   QUALIFY ROW_NUMBER() OVER (PARTITION BY x.team_id ORDER BY x.kickoff_ts) = 1
   ORDER BY x.kickoff_ts
   LIMIT 1;