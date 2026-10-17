SELECT
  match_id,
  kickoff_ts,
  DATE(kickoff_ts) AS date_of_game,
  match_report
  FROM bootcamp.northern_star.matches_flat
  WHERE DATE(kickoff_ts) BETWEEN '2025-03-01' AND '2025-05-31' AND match_report ILIKE('%win%') 
  ORDER BY kickoff_ts;