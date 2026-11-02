SELECT
  match_id,
  home_team,
  away_team,
  match_report
  FROM bootcamp.northern_star.matches_flat
  WHERE match_report ILIKE '%goal%';