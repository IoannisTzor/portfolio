from app import app
from extensions import db
from models import Project


with app.app_context():
    db.create_all()
    project1 = Project(
        title="Scheduler App",
        description="A feature-rich native Android calendar application built to address the limitations of existing scheduling tools. Supports recurring events, project tracking with priority ratings, persistent reminders via boot receiver, and three calendar views.",
        technologies="Android Studio, Java",
        github_url="https://github.com/IoannisTzor/Scheduler-App",
        contributors=None
    )
    project2 = Project(
        title="Gravity Shift",
        description="A Unity game built around gravity manipulation mechanics, originally developed as a class project and currently being expanded. Demonstrates core game development principles including physics-based gameplay and level design.",
        technologies="Unity, C#",
        github_url="https://github.com/IoannisTzor/Gravity-Shift-Project",
        contributors=None 
    )
    project3 = Project(
        title="Airport Database Management System",
        description="A normalised relational database modelling a multi-airport network including flights, aircraft, passengers, gates, and ticketing. Built in Oracle SQL with PL/SQL stored procedures and functions for querying and updating flight data. Developed in collaboration with Ethan Phillips.",
        technologies="SQL,OracleSQL",
        github_url="https://github.com/IoannisTzor/ITC-341-project-Airport-Database-Management-System",
        contributors="Ethan Phillips" 
    )
    
    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.commit()
