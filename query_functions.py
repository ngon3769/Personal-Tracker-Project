from sqlalchemy.orm import sessionmaker
from database_models import engine, Course, Assignment, Resource, Exam, Reminder

Session = sessionmaker(bind=engine)
session = Session()

def get_assignments_by_course(course_id):
    """Retrieve all assignments for a specific course."""
    return session.query(Assignment).filter(Assignment.course_id == course_id).all()

def get_resources_by_course(course_id):
    """Retrieve all resources for a specific course."""
    return session.query(Resource).filter(Resource.course_id == course_id).all()

def get_exams_by_course(course_id):
    """Retrieve all exams for a specific course."""
    return session.query(Exam).filter(Exam.course_id == course_id).all()

def get_reminders_by_assignment(assignment_id):
    """Retrieve all reminders for a specific assignment."""
    return session.query(Reminder).filter(Reminder.assignment_id == assignment_id).all()

def get_all_courses():
    """Retrieve all courses."""
    return session.query(Course).all()