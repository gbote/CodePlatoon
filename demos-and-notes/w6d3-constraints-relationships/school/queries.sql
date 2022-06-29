-- Get all of a professors offices
 SELECT * FROM professors 
JOIN offices 
ON professors.id = offices.professor_id ;