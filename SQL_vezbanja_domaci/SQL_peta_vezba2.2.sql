SELECT
  match_id,
  home_team,
  away_team,
  dayofweek(kickoff_ts) AS day_played,
  DATE(kickoff_ts) AS match_date
FROM
  bootcamp.northern_star.matches_flat
WHERE
  dayofweek(kickoff_ts) = 6;