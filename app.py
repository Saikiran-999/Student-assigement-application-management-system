from flask import Flask, request, jsonify
import mysql.connector
from utils import send_message

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localInstances2",
    user="root",
    password="password2",
    database="saams"
)

@app.route('/submit', methods=['POST'])
def submit_assignment():
    data = request.json
    student_name = data.get('studentName')
    assignment = data.get('assignment')
    due_date = data.get('dueDate')
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO assignments (student_name, assignment, due_date) VALUES (%s, %s, %s)", 
                   (student_name, assignment, due_date))
    db.commit()
    cursor.close()
    
    send_message(student_name, assignment, due_date)
    
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
