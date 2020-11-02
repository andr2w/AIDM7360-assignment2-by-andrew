SELECT title
FROM Movies
WHERE mID NOT IN (
  SELECT mID
  FROM Rating
  INNER JOIN Reviewer USING(rID)
  WHERE name = 'Chris Jackson'
)