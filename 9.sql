SELECT name, title, stars
FROM Movies
INNER JOIN Rating USING(mID)
INNER JOIN Reviewer USING(rID)
WHERE director = name