SELECT
  match_id,
  first_goal_scorer
FROM
  bootcamp.northern_star.matches_flat
WHERE
  first_goal_scorer ILIKE '%Mattéo%O%Brien';

SELECT
  COUNT(*)
FROM
  bootcamp.northern_star.matches_flat
WHERE
  kickoff_ts >= '2024-12-01'
  AND kickoff_ts <= '2024-12-26';

SELECT
  COUNT(*)
FROM
  bootcamp.northern_star.matches_flat
WHERE
  kickoff_ts BETWEEN '2024-12-01' AND '2024-12-26';

SELECT
  CASE
    WHEN (home_goals + away_goals) < 2 THEN 'Тесно'
    WHEN (home_goals + away_goals) BETWEEN 2 AND 4 THEN 'Malo golova'
    ELSE 'Голеада'
  END AS bucket,
  COUNT(*) AS matches
FROM
  bootcamp.northern_star.matches_flat
GROUP BY
  bucket;


SELECT COUNT(*) AS broj_tekmi_sa_5_golova
FROM bootcamp.northern_star.matches_flat
WHERE (home_goals + away_goals) >=5;

-- 4. „Број домаћих утакмица сваког клуба у сезони 2024/25, укључујући клубове са 0 утакмица“:
SELECT t.team_name, COUNT(m.match_id) AS home_matches
FROM bootcamp.northern_star.teams t
LEFT JOIN matches m ON t.team_id = m.home_team_id AND m.season = '2024/25'
GROUP BY t.team_name;
