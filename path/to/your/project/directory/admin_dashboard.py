import pygame
import mysql.connector

def get_employee_data():
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
    return data

def display_data(data):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for i, employee in enumerate(data):
            text = font.render(f"Employee {employee[0]}: {employee[3]} hours worked", True, (255, 255, 255))
            screen.blit(text, (20, 50 + i * 40))

        pygame.display.flip()
        clock.tick(60)

data = get_employee_data()
display_data(data)