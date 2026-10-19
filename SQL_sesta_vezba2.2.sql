SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts,
  attendance,
  season
FROM
  bootcamp.northern_star.matches_flat
WHERE
  attendance BETWEEN 20000 AND 35000
  AND season = '2024/25'
  ORDER BY season, kickoff_ts;