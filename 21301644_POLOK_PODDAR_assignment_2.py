from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

w_width = 800
w_height = 600

rocket_x = 0
rocket_width = 40
rocket_height = 60
rocket_speed = 10

projectiles = []
projectile_radius = 8

projectile_speed = 10

circle_fill = []

redious = 15
circle_speed = 3

timer = 0

blink_time = 10
colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]

score = 0
lives = 3
game_over = False

def draw_filled_circle(x, y, radius, color=(1.0, 0.0, 0.0)):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for angle in range(361):
        rad = math.radians(angle)
        glVertex2f(x + math.cos(rad) * radius, y + math.sin(rad) * radius)

    glEnd()

def draw_rocket(x, y):
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_POLYGON)

    glVertex2f(x - rocket_width / 4, y - rocket_height / 2)

    glVertex2f(x + rocket_width / 4, y - rocket_height / 2)

    glVertex2f(x + rocket_width / 4, y + rocket_height / 4)

    glVertex2f(x, y + rocket_height / 2)
    glVertex2f(x - rocket_width / 4, y + rocket_height / 4)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - rocket_width / 4, y - rocket_height / 2)

    glVertex2f(x - rocket_width / 2, y - rocket_height / 2)

    glVertex2f(x - rocket_width / 4, y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + rocket_width / 4, y - rocket_height / 2)
    glVertex2f(x + rocket_width / 2, y - rocket_height / 2)
    glVertex2f(x + rocket_width / 4, y)
    glEnd()

    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - rocket_width / 8, y - rocket_height / 2)

    glVertex2f(x + rocket_width / 8, y - rocket_height / 2)
    glVertex2f(x, y - rocket_height)
    glEnd()

def display_score_and_lives():
    glColor3f(1.0, 1.0, 1.0)
    
    glRasterPos2f(-w_width // 2 + 10, w_height // 2 - 20)
    for char in f"Score: {score} Lives: {lives}":

        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

keys = set()

def on_key_down(key, x, y):
    global keys
    keys.add(key.decode("utf-8"))

def on_key_up(key, x, y):
    global keys
    keys.discard(key.decode("utf-8"))

def move_shooter():
    global rocket_x
    if 'a' in keys and rocket_x - rocket_width / 2 > -w_width // 2:

        rocket_x -= rocket_speed
    if 'd' in keys and rocket_x + rocket_width / 2 < w_width // 2:
        rocket_x += rocket_speed

def shoot():
    if ' ' in keys:
        projectiles.append([rocket_x, -w_height // 2 + rocket_height / 2 + projectile_radius])

def update_projectiles():
    global projectiles, circle_fill, score, lives, game_over
    to_remove_projectiles = []
    to_remove_circles = []

    for projectile in projectiles:
        projectile[1] += projectile_speed

        if projectile[1] > w_height // 2:
            to_remove_projectiles.append(projectile)

        for circle in circle_fill:
            distance_squared = (circle[0] - projectile[0]) ** 2 + (circle[1] - projectile[1]) ** 2


            if distance_squared <= (redious + projectile_radius) ** 2:

                to_remove_circles.append(circle)

                to_remove_projectiles.append(projectile)
                score += 10
                break

    for projectile in to_remove_projectiles:
        if projectile in projectiles:
            projectiles.remove(projectile)
    for circle in to_remove_circles:

        if circle in circle_fill:

            circle_fill.remove(circle)

    for circle in circle_fill[:]:
        if circle[1] < -w_height // 2 - redious:
            circle_fill.remove(circle)
            lives -= 1
            if lives <= 0:
                game_over = True

def update_circles():
    global circle_fill, timer

    timer += 1
    for circle in circle_fill[:]:
        circle[1] -= circle_speed

    if timer >= blink_time:
        for circle in circle_fill:
            circle[2] = circle[2] * 1.1 if circle[2] < redious * 1.2 else redious
        timer = 0

    if random.random() < 0.02:
        x = random.randint(-w_width // 2 + redious, w_width // 2 - redious)
        y = w_height // 2
        circle_fill.append([x, y, redious])

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    if game_over:
        glColor3f(1.0, 0.0, 0.0)

        glRasterPos2f(-50, 0)

        for char in "GAME OVER":
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        glutSwapBuffers()
        return

    draw_rocket(rocket_x, -w_height // 2 + rocket_height / 2)

    for projectile in projectiles:
        draw_filled_circle(projectile[0], projectile[1], projectile_radius, color=(1.0, 0.0, 0.0))

    for circle in circle_fill:
        draw_filled_circle(circle[0], circle[1], circle[2], color=random.choice(colors))

    display_score_and_lives()

    glutSwapBuffers()

def update(value):
    move_shooter()
    shoot()

    update_projectiles()
    update_circles()
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-w_width // 2, w_width // 2, -w_height // 2, w_height // 2)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(w_width, w_height)
    glutCreateWindow(b"Rocket Shooter  ")
    glutDisplayFunc(display)

    glutKeyboardFunc(on_key_down)

    glutKeyboardUpFunc(on_key_up)
    glutTimerFunc(16, update, 0)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()