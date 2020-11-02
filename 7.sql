SELECT title, AVG(stars) AS avger
FROM Movies AS M INNER JOIN Rating AS R ON M.mID = R.mID
GROUP BY title
ORDER BY avger DESC, title