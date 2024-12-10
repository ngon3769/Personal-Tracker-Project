import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for

# Define a Blueprint
app = Blueprint('app', __name__)

# Database connection helper
DB_PATH = 'personal_tracker.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enable accessing columns by name
    return conn

# Home route
@app.route('/')
def home():
    conn = get_db_connection()
    courses_count = conn.execute("SELECT COUNT(*) FROM Courses").fetchone()[0]
    assignments_count = conn.execute("SELECT COUNT(*) FROM Assignments").fetchone()[0]
    exams_count = conn.execute("SELECT COUNT(*) FROM Exams").fetchone()[0]

    upcoming_deadlines = conn.execute("""
        SELECT 'Assignment' AS type, title, due_date
        FROM Assignments
        WHERE due_date > CURRENT_TIMESTAMP
        UNION ALL
        SELECT 'Exam', title, date
        FROM Exams
        WHERE date > CURRENT_TIMESTAMP
        ORDER BY due_date ASC
        LIMIT 5
    """).fetchall()

    conn.close()

    return render_template(
        'index.html',
        courses_count=courses_count,
        assignments_count=assignments_count,
        exams_count=exams_count,
        upcoming_deadlines=upcoming_deadlines
    )

# View all courses
@app.route('/courses')
def view_courses():
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM Courses").fetchall()
    conn.close()
    return render_template('courses.html', courses=courses)

# View assignments for a specific course
@app.route('/assignments/<int:course_id>')
def view_assignments(course_id):
    conn = get_db_connection()
    assignments = conn.execute("SELECT * FROM Assignments WHERE course_id = ?", (course_id,)).fetchall()
    conn.close()
    return render_template('assignments.html', assignments=assignments, course_id=course_id)

# Add a new assignment
@app.route('/assignments/add/<int:course_id>', methods=['GET', 'POST'])
def add_assignment(course_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        status = request.form['status']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Assignments (course_id, title, description, due_date, status) VALUES (?, ?, ?, ?, ?)",
            (course_id, title, description, due_date, status)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('app.view_assignments', course_id=course_id))
    return render_template('add_assignments.html', course_id=course_id)

# View resources for a specific course
@app.route('/resources/<int:course_id>')
def view_resources(course_id):
    conn = get_db_connection()
    resources = conn.execute("SELECT * FROM Resources WHERE course_id = ?", (course_id,)).fetchall()
    conn.close()
    return render_template('resources.html', resources=resources, course_id=course_id)

# View exams for a specific course
@app.route('/exams/<int:course_id>')
def view_exams(course_id):
    conn = get_db_connection()
    exams = conn.execute("SELECT * FROM Exams WHERE course_id = ?", (course_id,)).fetchall()
    conn.close()
    return render_template('exams.html', exams=exams, course_id=course_id)

# View reminders for a specific assignment
@app.route('/reminders/<int:assignment_id>')
def view_reminders(assignment_id):
    print(f"Accessing reminders for assignment_id: {assignment_id}")  # Debugging
    conn = get_db_connection()
    reminders = conn.execute(
        "SELECT * FROM Reminders WHERE assignment_id = ?",
        (assignment_id,)
    ).fetchall()
    conn.close()
    return render_template('reminders.html', reminders=reminders, assignment_id=assignment_id)

# Add a new reminder
@app.route('/reminders/add/<int:assignment_id>', methods=['GET', 'POST'])
def add_reminder(assignment_id):
    conn = get_db_connection()

    # Optional: Query to fetch assignment details if needed in the template
    assignment = conn.execute(
        "SELECT * FROM Assignments WHERE assignment_id = ?",
        (assignment_id,)
    ).fetchone()

    if request.method == 'POST':
        reminder_date = request.form['reminder_date']
        reminder_message = request.form['reminder_message']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Reminders (assignment_id, reminder_date, reminder_message) VALUES (?, ?, ?)",
            (assignment_id, reminder_date, reminder_message)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('app.view_reminders', assignment_id=assignment_id))
    conn.close()

    return render_template('add_reminder.html', assignment_id=assignment_id, assignment=assignment)

@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        term = request.form['term']
        credits = request.form['credits']
        meeting_times = request.form['meeting_times']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Courses (course_name, term, credits, meeting_times) VALUES (?, ?, ?, ?)",
            (course_name, term, credits, meeting_times)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('app.view_courses'))
    return render_template('add_course.html')

@app.route('/resources/add/<int:course_id>', methods=['GET', 'POST'])
def add_resource(course_id):
    if request.method == 'POST':
        resource_type = request.form['resource_type']
        description = request.form['description']
        link = request.form['link']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Resources (course_id, resource_type, description, link) VALUES (?, ?, ?, ?)",
            (course_id, resource_type, description, link)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('app.view_resources', course_id=course_id))
    return render_template('add_resources.html', course_id=course_id)

@app.route('/exams/add/<int:course_id>', methods=['GET', 'POST'])
def add_exam(course_id):
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        weight = request.form['weight']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Exams (course_id, title, date, weight) VALUES (?, ?, ?, ?)",
            (course_id, title, date, weight)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('app.view_exams', course_id=course_id))
    return render_template('add_exam.html', course_id=course_id)

