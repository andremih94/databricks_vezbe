SELECT
  match_id,
  home_team,
  away_team,
  kickoff_ts
FROM
  bootcamp.northern_star.matches_flat
WHERE
  kickoff_ts BETWEEN '2025-01-01 00:00:00' AND '2025-01-15 23:59:00'
SORT BY
  kickoff_ts;