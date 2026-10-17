SELECT
  match_id,
  kickoff_ts,
  home_team,
  away_team,
  first_goal_scorer
FROM
  bootcamp.northern_star.matches_flat
WHERE
  first_goal_scorer = "Sean O'Neill";