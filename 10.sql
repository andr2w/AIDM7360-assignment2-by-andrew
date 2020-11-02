SELECT title FROM Movies
UNION
SELECT name FROM Reviewer
ORDER BY name, title