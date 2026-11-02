--Zadatak 5.1:
--  1. Za sezonu 2024/25 prikažite igrače i ukupan broj golova koje su postigli. Prikažite samo igrače koji su postigli bar jedan gol. Pomoću DENSE_RANK() rangirajte igrače prema ukupnom broju golova, od najvećeg ka najmanjem. Igrači sa istim brojem golova treba da imaju isti rang.
    SELECT p.player_id, p.first_name, p.last_name, 
           COUNT(*) AS broj_golova,
           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rang
    FROM players AS p
    JOIN match_events AS me ON me.player_id =  p.player_id
    JOIN matches AS m ON m.match_id = me.match_id
    WHERE m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY p.player_id, p.first_name, p.last_name
    HAVING broj_golova >= 1
    ORDER BY broj_golova DESC;

-- 2. Za sezonu 2024/25 prikažite tri igrača sa najviše postignutih golova za svaki klub. Prikažite naziv kluba, ime i prezime igrača i broj postignutih golova. Pomoću ROW_NUMBER() odredite redosled igrača unutar svakog kluba, od najvećeg ka najmanjem broju golova.
    SELECT t.team_name, p.first_name, p.last_name,
           COUNT(*) AS broj_golova,
           ROW_NUMBER() OVER (PARTITION BY t.team_name ORDER BY COUNT(*) DESC) AS rang
    FROM players AS p
    JOIN match_events AS me ON me.player_id =  p.player_id
    JOIN matches AS m ON m.match_id = me.match_id
    JOIN teams AS t ON t.team_id = me.team_id
    WHERE m.season = '2024/25' AND me.event_type IN('goal', 'penalty_goal')
    GROUP BY t.team_name, p.first_name, p.last_name
    QUALIFY rang IN(1, 2, 3);

-- 3. Za sezonu 2024/25 prikažite sve utakmice svakog kluba, broj golova koje je klub postigao i broj golova koje je postigao u svojoj prethodnoj utakmici. Pomoću LAG() pronađite broj golova iz prethodne utakmice. Izračunajte i razliku između broja golova na tekućoj i prethodnoj utakmici. Rezultate sortirajte po nazivu kluba i datumu utakmice.
    SELECT t.team_name, kickoff_ts,
           goals_for AS broj_golova,
           LAG(goals_for) OVER (PARTITION BY tm.team_id ORDER BY kickoff_ts) AS golovi_u_prethodnoj_utakmici,
           broj_golova - golovi_u_prethodnoj_utakmici AS razlika
    FROM team_matches AS tm
    JOIN teams AS t ON tm.team_id = t.team_id
    WHERE tm.season = '2024/25'
    ORDER BY t.team_name, kickoff_ts;