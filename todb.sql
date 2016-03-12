-- set uo csv importing settings
.mode csv
.header on
.import "merged.csv" accesslog

-- set up output settings
.mode column
.width 20

-- return count of unique IP / browser agent
-- grouped by url. limit output to top 10
-- most-viewed pages.

SELECT url1, COUNT(*)
FROM (
SELECT url1
FROM accesslog
WHERE url1 LIKE "/story/%"
OR url1 LIKE "/"
GROUP BY url1, remote_addr, agent)
GROUP BY url1
ORDER BY COUNT(*) DESC
LIMIT 10;

-- save databse
.save merged.db
