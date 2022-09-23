DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s_studnum NUMBER NOT NULL,
    s_firstname TEXT NOT NULL,
    s_lastname TEXT NOT NULL,
    s_middlename TEXT NOT NULL,
    s_dob DATE format 'YYYY-MM-DD' not null,
    s_age NUMBER NOT NULL,
    s_address VARCHAR NOT NULL,
    s_section TEXT NOT NULL,
    s_grade NUMBER NOT NULL,
    s_lrn NUMBER NOT NULL,
    sg_firstname TEXT NOT NULL,
    sg_lastname TEXT NOT NULL,
    sg_address VARCHAR NOT NULL,
    sg_contact NUMBER NOT NULL
);

