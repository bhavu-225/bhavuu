SELECT emp_id , name, 
location.location_id,DataFlair.location 
FROM DataFlair RIGHT JOIN Location 
ON DataFlair.location=Location.location 
WHERE emp_id IS NOT NULL;