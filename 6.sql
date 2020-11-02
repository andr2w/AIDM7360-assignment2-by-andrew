SELECT title, MAX(stars)
FROM Movies AS M INNER JOIN Rating AS R ON M.mID = R.mID
GROUP BY title
