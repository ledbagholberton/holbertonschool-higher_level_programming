-- grroup rows with same score and shows how many are ...
-- database name come in Command  line
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;
