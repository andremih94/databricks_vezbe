--Zadatak 5.2
-- 1. Prosek datih golova u poslednjih 5 utakmica, uz izričit okvir prozora. Koja je najveća vrednost? Računajte samo kada prozor zaista ima 5 utakmica.
        SELECT 
            team_id,
            season,
            kickoff_ts AS na_dan_utakmice,
            COUNT(*) OVER (PARTITION BY team_id, season ORDER BY kickoff_ts ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS 5_poslednjih_tekmi,
            AVG(goals_for) OVER (PARTITION BY team_id, season ORDER BY kickoff_ts ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)  AS prosek_golova_do_tad
        FROM team_matches
        QUALIFY 5_poslednjih_tekmi = 5
        ORDER BY prosek_golova_do_tad DESC;

-- 2. Tekući zbir datih golova svakog kluba u sezoni 2024/25: ko je prvi stigao do 50 golova i kada?
    WITH tekuci_zbir AS(
        SELECT  team_id,
                kickoff_ts, 
                SUM(goals_for) OVER (PARTITION BY team_id, season ORDER BY kickoff_ts ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)  AS tekuci_zbir_golova
    FROM team_matches
    WHERE season = '2024/25'
        )
        SELECT 
            team_id,
            MIN(kickoff_ts) AS datum_50og_gola
        FROM tekuci_zbir
        WHERE tekuci_zbir_golova >= 50
        GROUP BY team_id
        ORDER BY datum_50og_gola ASC;
-- 3. Za svaku domaću utakmicu izračunajte promenu posećenosti u odnosu na prethodnu domaću utakmicu istog kluba u istoj sezoni. Gde je najveći pad i zašto?
    WITH poseta AS(
        SELECT
        home_team_id,
        attendance,
        LAG(attendance) OVER (PARTITION BY home_team_id, season ORDER BY kickoff_ts) AS posecenost_na_prethodnoj_tekmi,
        attendance - LAG(attendance) OVER (PARTITION BY home_team_id, season ORDER BY kickoff_ts) AS razlika_u_poseti
    FROM matches_flat
         )
        SELECT home_team_id, MIN(razlika_u_poseti) AS najveci_pad
    FROM poseta
    GROUP BY home_team_id
    ORDER BY najveci_pad ASC;