from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

width, height = 800, 600
pillar_width = 50
pillar_gap = 150
pillar_speed = 10
pillars = []

bird_width = 30
bird_height = 30
bird_y = height // 2
bird_velocity = 0
bird_gravity = -0.5
bird_lift = 10

is_game_running = True
score = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    generate_pillars()

def generate_pillars():
    global pillars
    x_position = width
    for _ in range(5):
        gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': x_position, 'gap_y': gap_y})
        x_position += 300

def draw_circle(cx, cy, radius):
    x, y = 0, radius
    d = 1 - radius
    plot_circle_points(cx, cy, x, y)

    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        plot_circle_points(cx, cy, x, y)

def plot_circle_points(cx, cy, x, y):
    points = [
        (cx + x, cy + y), (cx - x, cy + y),
        (cx + x, cy - y), (cx - x, cy - y),
        (cx + y, cy + x), (cx - y, cy + x),
        (cx + y, cy - x), (cx - y, cy - x)
    ]
    glBegin(GL_POINTS)
    for px, py in points:
        glVertex2f(px, py)
    glEnd()

def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    glBegin(GL_POINTS)
    while True:
        glVertex2f(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    glEnd()

def draw_pillar(x, gap_y):
    # Top rectangle
    for i in range(pillar_width):
        for j in range(gap_y):
            glBegin(GL_POINTS)
            glVertex2f(x + i, j)
            glEnd()

    # Bottom rectangle
    for i in range(pillar_width):
        for j in range(gap_y + pillar_gap, height):
            glBegin(GL_POINTS)
            glVertex2f(x + i, j)
            glEnd()

def update_pillars():
    global pillars, score
    for pillar in pillars:
        pillar['x'] -= pillar_speed

    if pillars and pillars[0]['x'] + pillar_width < 0:
        score += 1
        pillars.pop(0)
        new_x = pillars[-1]['x'] + 300
        new_gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': new_x, 'gap_y': new_gap_y})

def draw_pillars():
    for pillar in pillars:
        draw_pillar(pillar['x'], pillar['gap_y'])

def draw_bird(y):
    # Bird body
    glColor3f(1.0, 0.8, 0.2)  # Yellow body
    draw_circle(100 + bird_width // 2, y + bird_height // 2, bird_width // 2)

    # Bird eye
    glColor3f(0.0, 0.0, 0.0)  # Black eye
    draw_circle(100 + bird_width // 1.5, y + bird_height // 1.5, bird_width // 8)

    # Bird beak (line representation)
    glColor3f(1.0, 0.5, 0.0)  # Orange beak
    draw_line(100 + bird_width, y + bird_height // 2, 100 + bird_width + bird_width // 4, y + bird_height // 2.5)
    draw_line(100 + bird_width, y + bird_height // 2, 100 + bird_width + bird_width // 4, y + bird_height // 1.5)

def check_collision():
    global bird_y
    bird_x = 100
    bird_top = bird_y + bird_height
    bird_bottom = bird_y
    for pillar in pillars:
        pillar_left = pillar['x']
        pillar_right = pillar['x'] + pillar_width
        pillar_bottom = pillar['gap_y']
        pillar_top = pillar['gap_y'] + pillar_gap
        if bird_x + bird_width > pillar_left and bird_x < pillar_right:
            if bird_bottom < pillar_bottom or bird_top > pillar_top:
                return True
    return False

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    draw_pillars()
    draw_bird(bird_y)
    draw_score()
    glFlush()

def draw_score():
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(20, height - 30)
    for c in str(score):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

def timer(value):
    global bird_y, bird_velocity, is_game_running

    if is_game_running:
        bird_velocity += bird_gravity
        bird_y += bird_velocity

        if bird_y <= 0:
            bird_y = 0
            bird_velocity = 0
        if bird_y + bird_height >= height:
            bird_y = height - bird_height
            bird_velocity = 0

        update_pillars()

        if check_collision():
            is_game_running = False

    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def key_pressed(key, x, y):
    global bird_velocity, is_game_running, score, pillars

    if key == b' ' and not is_game_running:
        is_game_running = True
        bird_y = height // 2
        bird_velocity = 0
        score = 0
        pillars.clear()
        generate_pillars()

    if key == b' ' and is_game_running:
        bird_velocity = bird_lift

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Game CSE 423 Lab Project")

init()
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glutTimerFunc(16, timer, 0)
glutMainLoop()
