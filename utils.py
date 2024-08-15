import smtplib
from email.mime.text import MIMEText

def send_message(student_name, assignment, due_date):
    msg = MIMEText(f"Reminder: Assignment '{assignment}' is due on {due_date}. Please submit it on time.")
    msg['Subject'] = 'Assignment Due Reminder'
    msg['From'] = 'no-reply@saams.com'
    msg['To'] = student_name + '@example.com'  # Example email address

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('username', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
      
