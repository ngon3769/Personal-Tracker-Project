# Personal-Tracker-Project
Built a personal tracker for college students for my Database Design class.

This project was a 2-part assignment. 

### Part 1: Backend

First, I chose a topic of interest: organizing work and deadlines as a college student. Once I knew what I wanted to work on, I used the [Lucid Charts](https://lucid.app/) website to create my schema diagram. For this, I had to think about what entities I wanted to represent in my database. After a few iterations, I settled on Courses, Resources, Assignments, Exams, and Reminders. I then went ahead to create the schema diagram, which can be found here: 

Personal Tracker Schema Diagram

Next, I used the SQLAlchemy ORM to set up the database in VSCode. I made a python script to create the database, defined the database models using the ORM (having each entity as a class), and used another python file to populate starter/dummy data into the database. To get the database created in VSCode after opening the project files:

- Activate a python virtual environment by running these commands in the project folder:
   `python -m venv ./venv/` `source ./venv/bin/Activate`
- Install SQLAlchemy in the virtual env:
    `pip install SQLAlchemy`
- Run create_db.py, database_models.py, and populate_data.py in that order using these commands in the terminal:
   `python create_db.py`
   `python database_models.py`
   `python populate_data.py`

The database should then be created. Install the SQLite extension in VSCode to access the database and verify that the data got populated.

### Part 2: User Interface/Frontend

Once the database was created, I set up a Flask app with a simple UI to allow my desired functionality. This included:

- Viewing, adding, and deleting courses
- Viewing, adding, and deleting resources
- Viewing, adding, and deleting assignments
- Viewing, adding, and deleting exams
- Viewing, adding, and deleting reminders.

For this, I needed to setup app routes with methods that actually interacted with the database to carry out these desired functionalities. 

For each page/route, I also created HTML templates that would be dynamically populated when the user clicks on a certain entry.

Once I had verified that all the functionality worked as expected, I revamped the UI and added CSS to improve the look and feel of the frontend. 
