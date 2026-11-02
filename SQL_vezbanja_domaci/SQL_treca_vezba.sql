SELECT
  home_team,
  away_team,
  home_goals_ht,
  away_goals_ht,
  home_goals,
  away_goals
FROM
  bootcamp.northern_star.matches_flat
WHERE
  away_goals_ht > home_goals_ht
  AND home_goals > away_goals;