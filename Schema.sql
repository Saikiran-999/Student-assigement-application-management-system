CREATE DATABASE saams;

USE saams;

CREATE TABLE assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100),
    assignment VARCHAR(100),
    due_date DATE
);
