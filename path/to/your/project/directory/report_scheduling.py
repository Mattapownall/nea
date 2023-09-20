import schedule
import time
import mysql.connector

def generate_report():
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="TimeManagement"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Employees")
    data = cursor.fetchall()
    db.close()

    with open("/path/to/your/project/directory/report.txt", "w") as file:
        for employee in data:
            file.write(f"Employee {employee[0]}: {employee[3]} hours worked\n")

schedule.every().day.at("00:00").do(generate_report)

while True:
    schedule.run_pending()
    time.sleep(1)