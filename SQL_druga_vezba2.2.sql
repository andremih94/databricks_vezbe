SELECT
  coalesce(referee_name, 'Unknown') AS referee_name
FROM
  bootcamp.northern_star.matches_flat
ORDER BY
  match_id
LIMIT 20;