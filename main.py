import sqlite3
 
# Connect to the database
conn = sqlite3.connect('personal_tracker.db')
cursor = conn.cursor()
 
# Function to display all courses
def view_courses():
    query = "SELECT * FROM Courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    print("\nCourses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}, Term: {course[2]}, Credits: {course[3]}")
 
# Function to add a new course
def add_course():
    name = input("Enter course name: ")
    term = input("Enter term (e.g., Fall 2024): ")
    credits = input("Enter credits: ")
    meeting_times = input("Enter meeting times: ")
    query = "INSERT INTO Courses (course_name, term, credits, meeting_times) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, term, credits, meeting_times))
    conn.commit()
    print("Course added successfully!")
 
# Function to view assignments for a course
def view_assignments():
    course_id = input("Enter the Course ID to view assignments: ")
    query = "SELECT * FROM Assignments WHERE course_id = ?"
    cursor.execute(query, (course_id,))
    assignments = cursor.fetchall()
    print("\nAssignments:")
    for assignment in assignments:
        print(f"ID: {assignment[0]}, Title: {assignment[2]}, Due: {assignment[3]}, Status: {assignment[4]}")
 
# Function to add a new assignment
def add_assignment():
    course_id = input("Enter Course ID: ")
    title = input("Enter assignment title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    status = input("Enter status (Pending/Completed): ")
    query = "INSERT INTO Assignments (course_id, title, due_date, status) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (course_id, title, due_date, status))
    conn.commit()
    print("Assignment added successfully!")
 
# Function to view resources for a course
def view_resources():
    course_id = input("Enter the Course ID to view resources: ")
    query = "SELECT * FROM Resources WHERE course_id = ?"
    cursor.execute(query, (course_id,))
    resources = cursor.fetchall()
    print("\nResources:")
    for resource in resources:
        print(f"ID: {resource[0]}, Type: {resource[2]}, Link: {resource[3]}")
 
# Function to add a new resource
def add_resource():
    course_id = input("Enter Course ID: ")
    resource_type = input("Enter resource type (e.g., Video, Document): ")
    link = input("Enter resource link: ")
    description = input("Enter a resource description: ")
    query = "INSERT INTO Resources (course_id, resource_type, link, description) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (course_id, resource_type, link, description))
    conn.commit()
    print("Resource added successfully!")
 
# Function to view exams for a course
def view_exams():
    course_id = input("Enter the Course ID to view exams: ")
    query = "SELECT * FROM Exams WHERE course_id = ?"
    cursor.execute(query, (course_id,))
    exams = cursor.fetchall()
    print("\nExams:")
    for exam in exams:
        print(f"ID: {exam[0]}, Title: {exam[2]}, Date: {exam[3]}, Weight: {exam[4]}")
 
# Function to add a new exam
def add_exam():
    course_id = input("Enter Course ID: ")
    title = input("Enter exam title: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    weight = input("Enter exam weight: ")
    query = "INSERT INTO Exams (course_id, title, date, weight) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (course_id, title, date, weight))
    conn.commit()
    print("Exam added successfully!")
 
# Function to view all reminders
def view_reminders():
    query = "SELECT * FROM Reminders"
    cursor.execute(query)
    reminders = cursor.fetchall()
    print("\nReminders:")
    for reminder in reminders:
        print(f"Date: {reminder[3]}, Message: {reminder[2]}")
 
# Function to add a new exam
def add_exam():
    course_id = input("Enter Course ID: ")
    title = input("Enter exam title: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    weight = input("Enter exam weight: ")
    query = "INSERT INTO Exams (course_id, title, date, weight) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (course_id, title, date, weight))
    conn.commit()
    print("Exam added successfully!")
 
# Main menu
def main_menu():
    while True:
        print("\nPersonal Tracker Menu:")
        print("1. View All Courses")
        print("2. Add a New Course")
        print("3. View Assignments for a Course")
        print("4. Add a New Assignment")
        print("5. View Resources for a Course")
        print("6. Add a New Resource")
        print("7. View Exams for a Course")
        print("8. Add a New Exam")
        print("9. View All Reminders")
        print("10. Exit")
        choice = input("Choose an option: ")
 
        if choice == "1":
            view_courses()
        elif choice == "2":
            add_course()
        elif choice == "3":
            view_assignments()
        elif choice == "4":
            add_assignment()
        elif choice == "5":
            view_resources()
        elif choice == "6":
            add_resource()
        elif choice == "7":
            view_exams()
        elif choice == "8":
            add_exam()
        elif choice == "9":
            view_reminders()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
 
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
 