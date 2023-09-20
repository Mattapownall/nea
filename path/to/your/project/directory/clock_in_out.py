import mysql.connector

def clock_in_out(employee_id, action):
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="TimeManagement"
    )
    cursor = db.cursor()

    if action == "in":
        cursor.execute(f"UPDATE Employees SET clock_in_time = NOW() WHERE ID = {employee_id}")
    elif action == "out":
        cursor.execute(f"UPDATE Employees SET clock_out_time = NOW(), total_hours_worked = TIMESTAMPDIFF(HOUR, clock_in_time, NOW()) WHERE ID = {employee_id}")

    db.commit()
    db.close()