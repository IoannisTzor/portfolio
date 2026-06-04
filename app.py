from flask import Flask, render_template, request, flash, redirect, url_for
from extensions import db
from models import Project, Message
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("changethislater")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
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
        flash('Message sent')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/admin')
@auth.login_required
def admin():
    projects = Project.query.all()
    messages = Message.query.all()
    return render_template('admin.html', projects = projects, messages = messages)
    
@app.route('/admin/delete/<int:project_id>', methods = ['POST']) 
@auth.login_required
def delete_Project(project_id):
    id = project_id
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    flash('project deleted')
    return redirect(url_for('admin'))

@app.route('/admin/add', methods=['GET', 'POST'])
@auth.login_required
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        tech = request.form['technologies']
        url = request.form['url']
        contri = request.form.get('contributors', None)
        new_project = Project(title=title, description=description, technologies = tech, github_url=url, contributors = contri)
        db.session.add(new_project)
        db.session.commit()
        flash('Project Created')
        return redirect(url_for('admin'))
    return render_template('add_project.html')
    
    
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)