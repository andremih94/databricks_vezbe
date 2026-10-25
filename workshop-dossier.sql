-- Sezona u brojevima - statistika

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
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25'
    GROUP BY t.team_id, t.team_name;

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
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25'
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
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25'
    GROUP BY t.team_id, t.team_name;

-- 3. Стрелци: три најбоља стрелца клуба и најбољи асистент.
    -- tri najbolja strelca kluba
    (
        SELECT 'strelac' AS kategorija, p.first_name, p.last_name, p.position, COUNT(*) AS `broj_gol/asist`
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    JOIN match_events AS me ON me.match_id = m.match_id
    JOIN players AS p ON p.player_id = me.player_id
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY p.first_name, p.last_name, p.position
    ORDER BY `broj_gol/asist` DESC
    LIMIT 3
    )
    UNION ALL 
    (
        SELECT 'asistent' AS kategorija, p.first_name, p.last_name, p.position, COUNT(*) AS `broj_gol/asist`
    FROM teams AS t
    JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
    JOIN match_events AS me ON me.match_id = m.match_id
    JOIN players AS p ON p.player_id = me.related_player_id
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY p.first_name, p.last_name, p.position
    ORDER BY `broj_gol/asist` DESC
    LIMIT 1);

-- 4. Дисциплина: картони клуба по утакмици у поређењу са просеком лиге по тиму по утакмици.
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
    WHERE team_name = 'Thornbury City';

-- 5. Тренери: ко је водио клуб у сезони и са колико бодова по утакмици.
    SELECT
    ms.manager_name, m.season,
    ROUND(AVG(CASE WHEN (m.home_team_id = ms.team_id AND m.home_goals > m.away_goals)
                OR (m.away_team_id = ms.team_id AND m.away_goals > m.home_goals) THEN 3
            WHEN m.home_goals = m.away_goals THEN 1
            ELSE 0 END), 2) AS bodovi_po_utakmici
    FROM manager_spells AS ms
    JOIN teams AS t ON t.team_id = ms.team_id
    JOIN matches AS m
    ON (m.home_team_id = t.team_id OR m.away_team_id = t.team_id)
    AND DATE(m.kickoff_ts) BETWEEN ms.start_date AND coalesce(ms.end_date, '2099-12-31')
    WHERE t.team_name = 'Thornbury City'
    AND m.season = '2024/25'
    GROUP BY ms.manager_name, m.season;

-- 6. Највећа победа и најтежи пораз.

    (
  SELECT 'najveca pobeda' AS kategorija,
         DATE(m.kickoff_ts) AS datum_utakmice,
         h.team_name AS domacin,
         a.team_name AS gost,
         m.home_goals, m.away_goals,
    CASE WHEN m.home_team_id = t.team_id
         THEN m.home_goals - m.away_goals
         ELSE m.away_goals - m.home_goals END AS razlika_golova
  FROM teams AS t
  JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
  JOIN teams AS h ON h.team_id = m.home_team_id
  JOIN teams AS a ON a.team_id = m.away_team_id
  WHERE t.team_name = 'Thornbury City'
    AND m.season = '2024/25'
  ORDER BY razlika_golova DESC
  LIMIT 1
)
UNION ALL
(
  SELECT 'najtezi poraz' AS kategorija,
         DATE(m.kickoff_ts) AS datum_utakmice,
         h.team_name AS domacin,
         a.team_name AS gost,
         m.home_goals, m.away_goals,
         CASE WHEN m.home_team_id = t.team_id
              THEN m.home_goals - m.away_goals
              ELSE m.away_goals - m.home_goals END AS razlika_golova
  FROM teams AS t
  JOIN matches AS m ON m.home_team_id = t.team_id OR m.away_team_id = t.team_id
  JOIN teams AS h ON h.team_id = m.home_team_id
  JOIN teams AS a ON a.team_id = m.away_team_id
  WHERE t.team_name = 'Thornbury City'
    AND m.season = '2024/25'
  ORDER BY razlika_golova ASC
  LIMIT 1
);

-- 7. Публика: просечна посета и попуњеност на домаћим утакмицама, и колико утакмица нема податак о посети.
    SELECT t.team_name, ROUND(AVG(attendance), 0) AS prosecna_poseta, 
           s.capacity, ROUND(AVG(attendance) / s.capacity*100, 1) AS `popunjenost u %`,
           COUNT(*) - COUNT(attendance) AS utakmice_bez_podatka_o_poseti
    FROM matches AS m
    JOIN teams AS t ON m.home_team_id = t.team_id
    JOIN stadiums AS s ON s.stadium_id = m.stadium_id
    WHERE t.team_name = 'Thornbury City' AND m.season = '2024/25'
    GROUP BY t.team_name, s.capacity;

-- Ovaj tim, ako pogledamo statistiku iz prvog zadatka ima dosta neresenih utakmica kod kuce na domacem terenu pred domacom publikom, cak 9 sureta od od 16 kod kuce zavrsava neresenim rezultatom. Pritom, ima dobru publiku, tj. navijace sa popunjenoscu nesto manjom od 85% (83,9%) reklo bi se da bi mogli malo vise da se daju i jace da odigraju pred domacom publikom.
