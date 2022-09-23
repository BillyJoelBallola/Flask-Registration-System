import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret'


def get_db_connection():
    conn = sqlite3.connect('backend/studentRegDB.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_student_id(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?',
                           (student_id,)).fetchone()
    conn.close()

    if student is None:
        abort(404)
    return student


@app.route('/')
def home():
    return render_template('home.html')


# REGISTERED STUDENTS
@app.route('/Students')
def students():
    return render_template('students.html')


# NEW STUDENT
@app.route('/Add_Student', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        studNum = request.form['studNum']
        lrn = request.form['lrn']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        middlename = request.form['middlename']
        dob = request.form['dob']
        age = request.form['age']
        section = request.form['section']
        grade_level = request.form['grade-level']
        address = request.form['address']
        g_firstname = request.form['g_firstname']
        g_lastname = request.form['g_lastname']
        g_contact = request.form['contact']
        g_address = request.form['g_address']

        conn = get_db_connection()
        conn.execute('INSERT INTO students (s_studnum, s_firstname, s_lastname, s_middlename, s_dob, s_age, s_address, s_section, s_grade, s_lrn, sg_firstname, sg_lastname, sg_address, sg_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                     (
                         studNum,
                         firstname,
                         lastname,
                         middlename,
                         dob,
                         age,
                         address,
                         section,
                         grade_level,
                         lrn,
                         g_firstname,
                         g_lastname,
                         g_address,
                         g_contact
                     ))
        conn.commit()
        conn.close()
        flash('Student information successfully added.')
        return redirect(url_for('new_student'))
    return render_template('new_student.html')


# EDIT STUDENT
@app.route('/<int:id>/Edit_Student', methods=['GET', 'POST'])
def edit_student(id):
    student = get_student_id(id)

    if request.method == 'POST':
        studNum = request.form['studNum']
        lrn = request.form['lrn']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        middlename = request.form['middlename']
        dob = request.form['dob']
        age = request.form['age']
        section = request.form['section']
        grade_level = request.form['grade-level']
        address = request.form['address']
        g_firstname = request.form['g_firstname']
        g_lastname = request.form['g_lastname']
        g_contact = request.form['contact']
        g_address = request.form['g_address']

        conn = get_db_connection()
        conn.execute('UPDATE students SET s_studnum = ?, s_firstname = ?, s_lastname = ?, s_middlename = ?, s_dob = ?, s_age = ?, s_address = ?, s_section = ?, s_grade = ?, s_lrn = ?, sg_firstname = ?, sg_lastname = ?, sg_address = ?, sg_contact = ? WHERE id = ?',
                     (
                         studNum,
                         firstname,
                         lastname,
                         middlename,
                         dob,
                         age,
                         address,
                         section,
                         grade_level,
                         lrn,
                         g_firstname,
                         g_lastname,
                         g_address,
                         g_contact,
                         id
                     ))
        conn.commit()
        conn.close()
        flash('Student {} information successfully updated.'.format(
            student['s_studnum']))
        return redirect(url_for('students'))

    return render_template('edit_student.html', student=student)


# DELETE STUDENT DATA
@app.route('/<int:id>/delete_info', methods=('POST',))
def delete_student_info(id):
    student = get_student_id(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Student "{}" successfully deleted.'.format(
        student['s_studnum']))
    return redirect(url_for('students'))


@app.route('/Grade_1')
def grade_one():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC', (1,)).fetchall()
    return render_template('grade-levels/students_grade-one.html', students=students)


@ app.route('/Grade_2')
def grade_two():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC, s_section ASC', (2,)).fetchall()
    return render_template('grade-levels/students_grade-two.html', students=students)


@ app.route('/Grade_3')
def grade_three():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC, s_section ASC', (3,)).fetchall()
    return render_template('grade-levels/students_grade-three.html', students=students)


@ app.route('/Grade_4')
def grade_four():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC, s_section ASC', (4,)).fetchall()
    return render_template('grade-levels/students_grade-four.html', students=students)


@ app.route('/Grade_5')
def grade_five():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC, s_section ASC', (5,)).fetchall()
    return render_template('grade-levels/students_grade-five.html', students=students)


@ app.route('/Grade_6')
def grade_six():
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE s_grade = ? ORDER BY s_studnum ASC, s_section ASC', (6,)).fetchall()
    return render_template('grade-levels/students_grade-six.html', students=students)


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
