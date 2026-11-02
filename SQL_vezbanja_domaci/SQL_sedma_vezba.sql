SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts,
  season
FROM
  bootcamp.northern_star.matches_flat
WHERE
  season = '2024/25'
ORDER BY
  kickoff_ts ASC, match_id ASC
LIMIT 3;