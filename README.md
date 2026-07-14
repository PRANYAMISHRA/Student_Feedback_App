#  Student Feedback Management System

A Full-Stack Student Feedback Management System built using HTML, CSS, JavaScript, Flask, and SQLite.

## Features

- Student Feedback Form
- Course & Faculty Details
- 1–5 Rating System
- Anonymous Feedback Option
- Flask REST API
- SQLite Database
- Admin Dashboard to View Feedback
- Responsive UI

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- Python
- Flask
- Flask-CORS
- SQLite
- Git
- GitHub

## Project Structure

```
Student_Feedback_App/
│
├── backend/
│   ├── main.py
│   ├── feedback.db
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── script.js
│   ├── admin.js
│   └── style.css
│
├── .gitignore
├── package.json
└── README.md
```

# How to Run

# 1. Clone the repository

```bash
git clone https://github.com/PRANYAMISHRA/Student_Feedback_App.git
```

# 2. Install dependencies

```bash
pip install -r backend/requirements.txt
```

# 3. Run the Flask backend

```bash
cd backend
python main.py
```

# 4. Open the frontend

Open `frontend/index.html` using **Live Server** in VS Code.

## REST API Endpoints

### Submit Feedback

```
POST /submit-feedback
```

### Get Feedback

```
GET /get-feedback
```

# Database

SQLite (`feedback.db`)

Stores:

- Student Name
- Registration Number
- Department
- Semester
- Course
- Faculty
- Feedback
- Rating

# Future Improvements

- Search Feedback
- Delete Feedback
- User Authentication
- Export Feedback as CSV
- Analytics Dashboard

#Author

**Pranya Mishra**

B.Tech CSE (AI/ML)

SRM Institute of Science and Technology
