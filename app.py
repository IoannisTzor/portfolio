from flask import Flask, render_template, request, flash, redirect, url_for
from extensions import db
from models import Project, Message

app = Flask(__name__)
app.secret_key = 'dev-key-change-this-later'

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_message = Message(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        flash('Message sent!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)