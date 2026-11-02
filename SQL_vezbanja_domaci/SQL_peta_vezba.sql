SELECT
  home_team,
  away_team,
  season,
  weather
FROM
  bootcamp.northern_star.matches_flat
WHERE
  season = '2023/24'
  AND weather IN ('snow', 'fog');