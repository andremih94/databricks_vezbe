SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts,
  attendance
FROM
  bootcamp.northern_star.matches_flat
WHERE
  attendance BETWEEN 20000 AND 35000;