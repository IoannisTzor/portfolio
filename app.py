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
    return render_template('index.html',projects = projects)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)