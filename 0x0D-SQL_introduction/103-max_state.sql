-- Maxx temp per state in hbtn** database
-- command SELECT and GROUP ...
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
