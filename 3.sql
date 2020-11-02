SELECT title 
FROM Movies
 a left join Rating b 
 on a.mID = b.mID
WHERE stars is null