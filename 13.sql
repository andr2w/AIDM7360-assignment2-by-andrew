SELECT DISTINCT T1.title
FROM (Movies Join Rating USING (mID)) AS T1, (Movies Join Rating USING (mID)) AS T2
WHERE T1.mID = T2.mID AND T1.rID <> T2.rID



