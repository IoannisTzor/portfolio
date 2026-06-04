from flask import Flask, render_template
from extensions import db
from models import Project

app = Flask(__name__)

# Database config — we'll fill this in properly later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    projects = Project.query.all()
    skills = set()
    for project in projects:
        for tech in project.technologies.split(','):
            skills.add(tech.strip())
    return render_template('index.html', projects=projects, skills=skills)
@app.route('/project/<int:project_id>')
def project(project_id):
    project = Project.query.get(project_id)
    return render_template('project.html', project=project)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)