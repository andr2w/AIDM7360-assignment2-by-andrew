SELECT title 
FROM Movies 
WHERE mID IN (  	SELECT mID 
							FROM Rating R1
							INNER JOIN Rating R2 USING (mID)
							GROUP BY R1.mID 
							HAVING COUNT(*) >1)
							