from app import app
from extensions import db
from models import Project


with app.app_context():
    db.create_all()
    project = Project(
        title="Scheduler App",
        description="App to keep track of my things",
        technologies="Android Studio, Java",
        github_url="https://github.com/IoannisTzor/Scheduler-App",
        contributors=None  # None means empty/null in Python
    )
    db.session.add(project)
    db.session.commit()
