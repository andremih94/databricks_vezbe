SELECT
  home_team,
  away_team,
  match_report,
  LENGTH(match_report) AS broj_znakova
FROM
  bootcamp.northern_star.matches_flat
WHERE
  LENGTH(match_report) >= 40;