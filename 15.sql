SELECT rID, name
FROM Reviewer
WHERE Reviewer.rID  NOT IN (	SELECT DISTINCT Reviewer.rID
									FROM Reviewer, Rating 
									WHERE Reviewer.rID = Rating.rID
									)
