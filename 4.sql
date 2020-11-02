SELECT name 
FROM Reviewer INNER JOIN Rating ON Reviewer.rID = Rating.rID
WHERE ratingDate IS NULL