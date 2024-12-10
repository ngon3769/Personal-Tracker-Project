from sqlalchemy.orm import sessionmaker
from database_models import engine, Course, Assignment, Resource, Exam, Reminder
from datetime import datetime

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Reminder).delete()
session.query(Resource).delete()
session.query(Assignment).delete()
session.query(Exam).delete()
session.query(Course).delete()
session.commit()

# Add sample courses
courses = [
    Course(course_name="Data Structures", term="Fall 2024", credits=4, meeting_times="MWF 9-10 AM"),
    Course(course_name="Calculus III", term="Fall 2024", credits=3, meeting_times="TR 11-12:30 PM"),
    Course(course_name="Physics Lab", term="Fall 2024", credits=1, meeting_times="W 2-4 PM"),
    Course(course_name="Biology 101", term="Fall 2024", credits=4, meeting_times="MWF 11-12 PM"),
    Course(course_name="Organic Chemistry", term="Fall 2024", credits=4, meeting_times="MWF 1-2 PM"),
]

session.add_all(courses)
session.commit()

# Add sample assignments
assignments = [
    Assignment(course_id=1, title="Binary Trees", description="Implement binary search trees", due_date=datetime(2024, 12, 10, 23, 59), status="Not Started"),
    Assignment(course_id=1, title="Graph Algorithms", description="Implement Dijkstra's Algorithm", due_date=datetime(2024, 12, 15, 23, 59), status="In Progress"),
    Assignment(course_id=2, title="Calculus Homework 3", description="Solve integrals", due_date=datetime(2024, 12, 12, 23, 59), status="Completed"),
    Assignment(course_id=3, title="Physics Lab Report", description="Submit lab report on motion", due_date=datetime(2024, 12, 14, 23, 59), status="Not Started"),
    Assignment(course_id=4, title="Biology Research Paper", description="Write a paper on ecosystems", due_date=datetime(2024, 12, 20, 23, 59), status="In Progress"),
]

session.add_all(assignments)
session.commit()

# Add sample course resources
resources = [
    Resource(course_id=1, resource_type="Lecture Notes", description="Chapter 5 Trees", link="http://example.com/trees"),
    Resource(course_id=1, resource_type="Video", description="Binary Trees Explained", link="http://example.com/binary-trees"),
    Resource(course_id=2, resource_type="Worksheet", description="Integration Practice", link="http://example.com/integration"),
    Resource(course_id=3, resource_type="Lab Manual", description="Physics Lab Guide", link="http://example.com/physics-lab"),
    Resource(course_id=4, resource_type="Research Article", description="Ecosystem Studies", link="http://example.com/ecosystems"),
]

session.add_all(resources)
session.commit()

# Add sample exams
exams = [
    Exam(course_id=1, title="Midterm Exam", date=datetime(2024, 10, 20, 9, 0), weight=30),
    Exam(course_id=1, title="Final Exam", date=datetime(2024, 12, 15, 14, 0), weight=50),
    Exam(course_id=2, title="Midterm Exam", date=datetime(2024, 10, 25, 10, 0), weight=40),
    Exam(course_id=3, title="Lab Final", date=datetime(2024, 12, 10, 8, 0), weight=20),
    Exam(course_id=4, title="Final Exam", date=datetime(2024, 12, 22, 13, 0), weight=50),
]

session.add_all(exams)
session.commit()

# Add sample reminders
reminders = [
    Reminder(assignment_id=1, reminder_date=datetime(2024, 12, 5, 10, 0), reminder_message="Don't forget Binary Trees!"),
    Reminder(assignment_id=2, reminder_date=datetime(2024, 12, 12, 9, 0), reminder_message="Graph Algorithms due soon!"),
    Reminder(assignment_id=3, reminder_date=datetime(2024, 12, 10, 8, 0), reminder_message="Calculus Homework due!"),
    Reminder(assignment_id=4, reminder_date=datetime(2024, 12, 13, 14, 0), reminder_message="Submit Physics Lab Report."),
    Reminder(assignment_id=5, reminder_date=datetime(2024, 12, 19, 16, 0), reminder_message="Biology Research Paper due tomorrow!"),
]

session.add_all(reminders)
session.commit()

print("Database populated with sample data successfully!")