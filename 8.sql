SELECT DISTINCT name
FROM Movies
INNER JOIN Rating USING(mID)
INNER JOIN Reviewer USING(rID)
WHERE title = 'Gone with the Wind'