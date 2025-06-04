create database student_management;
use student_management;
create table students(
     roll_no varchar(20) primary key,
     name varchar(100),
     class varchar(200),
     section varchar(5),
	 password varchar(100),
     email varchar(100)
);
create table if not exists marks (
     roll_no varchar(20),
     subject varchar(50),
     marks int,
     primary key (roll_no, subject),
     foreign key(roll_no) references
students(roll_no)
);
create table timetable (
     class varchar(20),
     section varchar(5),
     day varchar(20),
     period1 varchar(50),
     period2 varchar(50),
     period3 varchar(50),
     period4 varchar(50),
     primary key (class, section, day)
);