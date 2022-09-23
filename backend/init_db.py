import sqlite3

connection = sqlite3.connect('backend/studentRegDB.db')

with open('backend/schema.sql') as db:
    connection.executescript(db.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Billy Joel',
        'Ballola',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'B',
        '1',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)
cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Garry',
        'Bogs',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'A',
        '2',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)
cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Itchigo',
        'Kurosaki',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'C',
        '3',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)
cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Ken',
        'Kaneki',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'A',
        '4',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)
cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Chardy Marie Angel',
        'Navalta',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'B',
        '5',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)
cur.execute(
    "INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade,s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        '0120-1188',
        'Gojo',
        'Saturo',
        'Petremetre',
        '2002-06-01',
        '20',
        'Ibababng butnong, Magdalena, Laguna',
        'C',
        '6',
        '108343070016',
        'Gina',
        'Ballola',
        'Ibababng butnong, Magdalena, Laguna',
        '09059347477',
    )
)

connection.commit()
connection.close()
