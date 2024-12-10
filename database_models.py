from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Use the updated declarative_base() from sqlalchemy.orm
Base = declarative_base()

# Define the database URI
DATABASE_URI = "sqlite:///personal_tracker.db"

# Define the engine
engine = create_engine(DATABASE_URI)


# Course table
class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False)
    term = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    meeting_times = Column(String, nullable=False)

    # Relationships
    assignments = relationship("Assignment", back_populates="course", cascade="all, delete-orphan")
    exams = relationship("Exam", back_populates="course", cascade="all, delete-orphan")
    resources = relationship("Resource", back_populates="course", cascade="all, delete-orphan")


# Assignment table
class Assignment(Base):
    __tablename__ = "assignments"
    assignment_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

    # Relationships
    course = relationship("Course", back_populates="assignments")
    reminders = relationship("Reminder", back_populates="assignment", cascade="all, delete-orphan")


# Resource table
class Resource(Base):
    __tablename__ = "resources"
    resource_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    resource_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String, nullable=False)

    # Relationship
    course = relationship("Course", back_populates="resources")


# Exam table
class Exam(Base):
    __tablename__ = "exams"
    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    title = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    weight = Column(Integer, nullable=False)

    # Relationship
    course = relationship("Course", back_populates="exams")


# Reminder table
class Reminder(Base):
    __tablename__ = "reminders"
    reminder_id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignments.assignment_id"), nullable=False)
    reminder_message = Column(String(200), nullable=False)
    reminder_date = Column(String(50), nullable=False)

    # Relationship
    assignment = relationship("Assignment", back_populates="reminders")


# Database engine setup
engine = create_engine("sqlite:///personal_tracker.db")
Base.metadata.create_all(engine)
