SELECT DISTINCT(location.location_id) AS Location_ID,
DataFlair.location AS Office_Location
FROM DataFlair RIGHT JOIN Location 
ON DataFlair.location=Location.location 
WHERE emp_id IS NOT NULL;