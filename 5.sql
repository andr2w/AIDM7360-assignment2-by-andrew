SELECT DISTINCT M.title 
FROM Movies AS M, Rating AS R
WHERE M.mID = R.mID AND R.stars = (
			SELECT max(stars)
			FROM Rating)