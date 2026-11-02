SELECT
  home_team,
  away_team,
  home_goals_ht,
  away_goals_ht,
  home_goals,
  away_goals,
  (home_goals - home_goals_ht) + (away_goals - away_goals_ht) AS drugo_poluvreme_golovi
FROM
  bootcamp.northern_star.matches_flat
ORDER BY
  drugo_poluvreme_golovi DESC
LIMIT 1;