SELECT year
FROM Movies, Rating 
WHERE Movies.mID = Rating.mID AND (stars = 4 or stars = 5)
ORDER BY year