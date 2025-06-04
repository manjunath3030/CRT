create database student_feedback;
use student_feedback;
create table  student(
	std_id varchar(20) primary key,
    name varchar(100),
    branch varchar(100),
    email varchar(200)
);
create table faculty(
	faculty_id varchar(100),
    name varchar(100)
);
create table feedback(
	std_id varchar(100),
    faculty_id varchar(200),
    rating int check (rating between 1 and 5),
    comments  varchar(200)
);