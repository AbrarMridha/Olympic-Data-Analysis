-- Query to get total medals by country
SELECT NOC AS Country, COUNT(Medal) AS Total_Medals
FROM athlete_data
WHERE Medal IS NOT NULL
GROUP BY NOC
ORDER BY Total_Medals DESC
LIMIT 10;


-- Query to analyze medal distribution by country and sport
SELECT NOC AS Country, Sport, COUNT(Medal) AS Medal_Count
FROM athlete_data
WHERE Medal IS NOT NULL
GROUP BY NOC, Sport
ORDER BY Medal_Count DESC;