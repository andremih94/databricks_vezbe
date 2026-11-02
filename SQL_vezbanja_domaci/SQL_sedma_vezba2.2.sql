SELECT DISTINCT
  first_goal_scorer
FROM
  bootcamp.northern_star.matches_flat
WHERE
  first_goal_scorer LIKE ('A%')
  OR first_goal_scorer LIKE ('%-%');