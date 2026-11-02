-- Део Б — извештај о клубу Kingsbridge City, сезона 2024/25
-- Сезона у бројевима: утакмице, победе, нерешене, порази, дати и примљени голови, бодови.
    SELECT t.team_id, t.team_name, 
        COUNT(*) AS br_utakmica, 
        SUM(CASE
        WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals)
        OR (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) THEN 1 ELSE 0 END) AS br_pobeda,
        SUM(CASE
        WHEN (m.home_team_id = t.team_id AND m.home_goals < m.away_goals)
        OR (m.away_team_id = t.team_id AND m.away_goals < m.home_goals) THEN 1 ELSE 0 END) AS br_poraza,
        SUM(CASE WHEN m.home_goals = m.away_goals THEN 1 ELSE 0 END) AS br_neresenih,
        SUM(CASE WHEN m.home_team_id = t.team_id THEN m.home_goals ELSE m.away_goals END) AS dati_golovi,
        SUM(CASE WHEN m.home_team_id = t.team_id THEN m.away_goals ELSE m.home_goals END) AS primljeni_golovi,
        SUM(CASE WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals)
        OR (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) THEN 3
                WHEN m.home_goals = m.away_goals THEN 1 ELSE 0 END) AS bodovi
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25'
    GROUP BY t.team_id, t.team_name;
-- 2. Код куће и у гостима: исти бројеви, одвојено за домаће и гостујуће утакмице. Где је клуб био бољи?
   
    -- Statistika kada je klub igrao na domacem terenu za sezonu 2024/25
    SELECT t.team_id, t.team_name, 
        COUNT_IF(m.home_team_id = t.team_id) AS br_utakmica_kod_kuce, 
        SUM(CASE
        WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals) THEN 1 ELSE 0 END) AS br_pobeda_kod_kuce,
        SUM(CASE
        WHEN (m.home_team_id = t.team_id AND m.home_goals < m.away_goals) THEN 1 ELSE 0 END) AS br_poraza_kod_kuce,
        SUM(CASE WHEN m.home_team_id = t.team_id AND m.home_goals = m.away_goals THEN 1 ELSE 0 END) AS br_neresenih_kod_kuce,
        SUM(CASE WHEN m.home_team_id = t.team_id THEN m.home_goals ELSE 0 END) AS dati_golovi_kod_kuce,
        SUM(CASE WHEN m.home_team_id = t.team_id THEN m.away_goals ELSE 0 END) AS primljeni_golovi_kod_kuce,
        SUM(CASE WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals) THEN 3
                 WHEN (m.home_team_id = t.team_id AND m.home_goals = m.away_goals) THEN 1 ELSE 0 END) AS bodovi_kod_kuce
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25'
    GROUP BY t.team_id, t.team_name;


-- Statistika kada je igrao u gostima za sezonu 2024/25
    SELECT t.team_id, t.team_name, 
        COUNT_IF(m.away_team_id = t.team_id) AS br_utakmica_u_gostima, 
        SUM(CASE
        WHEN (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) THEN 1 ELSE 0 END) AS br_pobeda_u_gostima,
        SUM(CASE
        WHEN (m.away_team_id = t.team_id AND m.away_goals < m.home_goals) THEN 1 ELSE 0 END) AS br_poraza_u_gostima,
        SUM(CASE WHEN m.away_team_id = t.team_id AND m.home_goals = m.away_goals THEN 1 ELSE 0 END) AS br_neresenih_u_gostima,
        SUM(CASE WHEN m.away_team_id = t.team_id THEN m.away_goals ELSE 0 END) AS dati_golovi_u_gostima,
        SUM(CASE WHEN m.away_team_id = t.team_id THEN m.home_goals ELSE 0 END) AS primljeni_golovi_u_gostima,
        SUM(CASE WHEN (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) THEN 3
                 WHEN (m.away_team_id = t.team_id AND m.home_goals = m.away_goals) THEN 1 ELSE 0 END) AS bodovi_u_gostima
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25'
    GROUP BY t.team_id, t.team_name;

-- 3. Публика: просечна посета и попуњеност стадиона на домаћим утакмицама, и број домаћих утакмица без податка о посети.
        SELECT t.team_name, 
               ROUND(AVG(attendance), 0) AS prosecna_poseta, 
               s.capacity, ROUND(AVG(attendance) / s.capacity*100, 1) AS `popunjenost u %`,
           COUNT(*) - COUNT(attendance) AS utakmice_bez_podatka_o_poseti
    FROM matches AS m
    JOIN teams AS t ON m.home_team_id = t.team_id
    JOIN stadiums AS s ON s.stadium_id = m.stadium_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25'
    GROUP BY t.team_name, s.capacity;
-- 4. Играчи: три најбоља стрелца клуба и најбољи асистент.
        (
        SELECT 'strelac' AS kategorija, p.player_id, p.first_name, p.last_name, p.position, COUNT(*) AS `broj_gol/asist`
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    JOIN match_events AS me ON me.match_id = m.match_id
    JOIN players AS p ON p.player_id = me.player_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY p.player_id, p.first_name, p.last_name, p.position
    ORDER BY `broj_gol/asist` DESC
    LIMIT 3
    )
    UNION ALL 
    (
        SELECT 'asistent' AS kategorija, p.player_id, p.first_name, p.last_name, p.position, COUNT(*) AS `broj_gol/asist`
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    JOIN match_events AS me ON me.match_id = m.match_id
    JOIN players AS p ON p.player_id = me.related_player_id
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY p.player_id, p.first_name, p.last_name, p.position
    ORDER BY `broj_gol/asist` DESC
    LIMIT 1);
-- 5. Дисциплина и тренери: картони клуба по утакмици у поређењу са просеком лиге по тиму по утакмици; 
        WITH kartoni AS (
            SELECT me.match_id, t.team_name, COUNT(*) AS broj_kartona
            FROM match_events AS me
            JOIN teams AS t ON t.team_id = me.team_id
            JOIN matches AS m ON m.match_id = me.match_id
            WHERE m.season = '2024/25' AND me.event_type IN('yellow_card', 'red_card', 'second_yellow')
            GROUP BY me.match_id, t.team_name
            ORDER BY broj_kartona DESC
        )
    SELECT match_id, team_name, broj_kartona, ROUND((SELECT AVG(broj_kartona) FROM kartoni), 2) AS prosek_lige
    FROM kartoni
    WHERE team_name = 'Kingsbridge City';

-- Kо је водио клуб и са колико бодова по утакмици.
    SELECT 
        ms.manager_name, m.season,
        ROUND(AVG(CASE WHEN (m.home_team_id = ms.team_id AND m.home_goals > m.away_goals)
                OR (m.away_team_id = ms.team_id AND m.away_goals > m.home_goals) THEN 3
            WHEN m.home_goals = m.away_goals THEN 1
            ELSE 0 END), 2) AS bodovi_po_utakmici
    FROM manager_spells AS ms
    JOIN teams AS t ON t.team_id = ms.team_id
    JOIN matches AS m ON (m.home_team_id = t.team_id OR m.away_team_id = t.team_id) AND DATE(m.kickoff_ts) BETWEEN ms.start_date AND coalesce(ms.end_date, '2099-12-31')
    WHERE t.team_name = 'Kingsbridge City' AND m.season = '2024/25'
    GROUP BY ms.manager_name, m.season;

-- 6. Квалитет података: бар један проблем на који сте наишли у подацима лиге, са упитом који га проналази.

    SELECT ms.team_id, team_name, ms.manager_name, ms.start_date, ms.end_date
    FROM teams AS t
    JOIN manager_spells AS ms ON ms.team_id = t.team_id 
    WHERE ms.team_id = 7 
    ORDER BY ms.start_date; -- Tim Castlebrook United uporno ima problem sa trenerima iz sezone u sezonu, po vise njih vode ekipu.

    SELECT r.*
    FROM referees AS r
    LEFT JOIN matches AS m ON m.referee_id = r.referee_id
    WHERE m.referee_id IS NULL; -- Sudija koji u obe sezone, 761 utakmici nije sudio ni jednu jedinu utakmicu.