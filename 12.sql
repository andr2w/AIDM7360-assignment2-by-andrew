SELECT DISTINCT M.title
FROM Movies AS M
WHERE M.mID IN (
				SELECT  RA.mID
				FROM Rating AS RA, Reviewer AS RE
				WHERE RE.rID = RA.rID AND re.name = 'Sarah Martinez') AND M.title NOT IN (
							SELECT DISTINCT M.title
							FROM Movies AS M
							WHERE M.mID IN (
							SELECT  RA.mID
							FROM Rating AS RA, Reviewer AS RE
							WHERE RE.rID = RA.rID AND re.name = 'Chris Jackson'))






