from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.json

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO feedback
    (student_name, reg_no, department, semester, course, faculty, feedback, rating)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["studentName"],
        data["regNo"],
        data["department"],
        data["semester"],
        data["course"],
        data["faculty"],
        data["feedback"],
        data["rating"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Feedback saved successfully!"
    })

@app.route("/get-feedback", methods=["GET"])
def get_feedback():

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student_name, reg_no, department,
           semester, course, faculty,
           feedback, rating
    FROM feedback
    """)

    rows = cursor.fetchall()
    conn.close()

    feedback_list = []

    for row in rows:
        feedback_list.append({
            "studentName": row[0],
            "regNo": row[1],
            "department": row[2],
            "semester": row[3],
            "course": row[4],
            "faculty": row[5],
            "feedback": row[6],
            "rating": row[7]
        })

    return jsonify(feedback_list)


def init_db():
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_name TEXT,
                   reg_no TEXT,
                   department TEXT,
                   semester TEXT,
                   course TEXT,
                   faculty TEXT,
                   feedback TEXT,
                   rating TEXT
     )               
    """ )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)    
        