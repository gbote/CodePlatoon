-- Select all rows from the classes table.
SELECT * FROM classes;

-- Select the name and credits from the classes table where the number of credits is greater than 3.
SELECT classes.name, classes.credits FROM classes WHERE classes.credits > 3;

-- All rows from the classes table where credits is an even number.
SELECT * FROM classes WHERE credits % 2 = 0;

-- All of Tianna's enrollments that she hasn't yet received a grade for.
SELECT * FROM enrollments LEFT JOIN students on enrollments.student_id = students.id WHERE students.id = 1 AND enrollments.grade IS NULL;


-- All of Tianna's enrollments that she hasn't yet received a grade for, selected by her first name, not her student.id
SELECT * FROM enrollments LEFT JOIN students ON enrollments.student_id = students.id WHERE students.first_name = 'Tianna' AND enrollments.grade IS NULL;

-- All of Tianna's enrollments that she hasn't yet received a grade for, selected by her first name, not her student.id, with the class name included in the result set. -- listing all data from enrollments and class name
SELECT *, classes.name FROM enrollments LEFT JOIN students ON enrollments.student_id = students.id LEFT JOIN classes ON classes.id = enrollments.class_id WHERE students.first_name = 'Tianna' AND enrollments.grade IS NULL\gx

-- All of Tianna's enrollments that she hasn't yet received a grade for, selected by her first name, not her student.id, with the class name included in the result set. -- listing only class name
SELECT classes.name FROM enrollments LEFT JOIN students ON enrollments.student_id = students.id LEFT JOIN classes ON classes.id = enrollments.class_id WHERE students.first_name = 'Tianna' AND enrollments.grade IS NULL;

-- All students born before 1986 who have a 't' in their first or last name.
SELECT students.first_name, students.last_name FROM students WHERE date_part('year', birthdate) < 1986 AND students.first_name ILIKE '%T%' OR students.last_name ILIKE '%T%';

-- The average age of all the students.
SELECT AVG(AGE(birthdate)) FROM students;

-- Addresses that have a space in their city name.
SELECT * FROM addresses WHERE city LIKE '% %';

-- Students & their addresses that live in a city with more than one word in the city name.
SELECT students.first_name, students.last_name, addresses.line_1, addresses.city, addresses.state, addresses.zipcode FROM addresses LEFT JOIN students ON students.address_id = addresses.id WHERE addresses.city LIKE '% %';


-- The average number of credits for classes offered at the school.
SELECT AVG(credits) FROM classes;

-- The first and last name of all students who have received an 'A'.
SELECT students.first_name, students.last_name FROM students LEFT JOIN enrollments ON students.id = enrollments.student_id WHERE enrollments.grade = 'A';

-- Each student's first name and the total credits they've enrolled in
SELECT students.first_name, SUM(classes.credits) FROM classes LEFT JOIN enrollments ON enrollments.class_id = classes.id LEFT JOIN students ON students.id = enrollments.student_id GROUP BY students.first_name;

-- The total number of credits each student has received a grade for.
SELECT SUM(classes.credits), students.first_name, students.last_name FROM classes LEFT JOIN enrollments ON classes.id = enrollments.class_id LEFT JOIN students ON enrollments.student_id = students.id WHERE enrollments.grade IS NOT NULL GROUP BY students.first_name, students.last_name;

-- All enrollments, including the class name.
SELECT enrollments.student_id, classes.id, classes.name, enrollments.grade FROM enrollments LEFT JOIN classes ON enrollments.class_id = classes.id;

-- Students born between 1982-1985 (inclusive).
SELECT first_name, last_name FROM students WHERE date_part('year', birthdate) BETWEEN 1982 AND 1985;

-- Insert a new enrollment recording that Andre Rohan took PHYS 218 and got an A.
INSERT INTO enrollments (student_id, class_id, grade) VALUES
((SELECT students.id FROM students WHERE students.first_name = 'Andre'),
(SELECT classes.id FROM classes WHERE classes.name = 'PHYS 218'),
'A');

-- Accidentally added Andre Rohan's PHYS 218 enrollment twice so needed to delete
DELETE FROM enrollments WHERE id = 19;