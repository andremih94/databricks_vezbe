SELECT
  home_team,
  away_team,
  kickoff_ts,
  home_goals,
  away_goals
FROM
  bootcamp.northern_star.matches_flat
WHERE
  home_team IN ('Northport United', 'Northport City')
  AND away_team IN ('Northport United', 'Northport City')
ORDER BY
  kickoff_ts;