# Personal Portfolio Website

A full stack personal portfolio website built with Flask and PostgreSQL, featuring a pixel art inspired design. Live at [portfolio-h2r9.onrender.com](https://portfolio-h2r9.onrender.com).

---

## Overview

This project is a fully deployed portfolio website that dynamically serves project data from a database. It includes a contact form, individual project pages, a skills filter, and a password-protected admin panel for managing content without touching the codebase.

Built from scratch as a summer project to learn Python backend development.

---

## Features

- **Dynamic project cards** — projects are stored in a database and served via Flask routes
- **Individual project pages** — each project has a dedicated detail page with technologies and links
- **Skills filter** — clicking a skill filters the project cards in real time using JavaScript
- **Contact form** — messages are saved to the database for review in the admin panel
- **Admin panel** — password-protected page to view messages and add or delete projects
- **Pixel art inspired design** — custom CSS with retro fonts, scanline texture, and animated terminal

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, SQLAlchemy |
| Database | PostgreSQL (production), SQLite (development) |
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Auth | Flask-HTTPAuth, Werkzeug password hashing |
| Deployment | Render, Gunicorn |

---

## Project Structure

```
portfolio/
├── app.py               # Flask routes and app configuration
├── models.py            # SQLAlchemy database models (Project, Message)
├── extensions.py        # SQLAlchemy instance
├── seed.py              # Database seeding script
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment configuration
├── static/
│   └── css/
│       └── style.css    # All styling
└── templates/
    ├── index.html       # Home page
    ├── project.html     # Project detail page
    ├── contact.html     # Contact form
    ├── admin.html       # Admin panel
    └── add_project.html # Add project form
```

---

## Running Locally

### Requirements
- Python 3.x
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/IoannisTzor/portfolio
cd portfolio

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create a .env file
echo SECRET_KEY=your-secret-key > .env
echo DATABASE_URL=sqlite:///portfolio.db >> .env
echo ADMIN_USERNAME=admin >> .env
echo ADMIN_PASSWORD=your-password >> .env

# Seed the database
python seed.py

# Run the app
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Deployment

Deployed on [Render](https://render.com) with a PostgreSQL database. The `render.yaml` file configures the build and start commands. Environment variables (`DATABASE_URL`, `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`) are set via the Render dashboard.

---

## Author

**Ioannis Tzortzatos** — [GitHub](https://github.com/IoannisTzor) · [LinkedIn](https://www.linkedin.com/in/ioannis-tzortzatos-659671282/)
