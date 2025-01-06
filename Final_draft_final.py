from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

width, height = 800, 600
pillar_width = 50
gap_height = 150
pillar_speed = 5
pillars = []
bird_radius = 15
bird_x = 100
bird_y = height // 2
velocity = 0
gravity = -0.5
flap_strength = 10
game_running = True
score = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    generate_pillars()

def generate_pillars():
    global pillars
    pillars.clear()
    x_pos = width
    for _ in range(5):
        gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': x_pos, 'gap_y': gap_y})
        x_pos += 300

def draw_circle_midpoint(xc, yc, r):
    x, y = 0, r
    d = 1 - r
    glBegin(GL_POINTS)
    draw_circle_points(xc, yc, x, y)
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        draw_circle_points(xc, yc, x, y)
    glEnd()

def draw_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x),
    ]
    for px, py in points:
        glVertex2f(px, py)

def draw_pillar(x, gap_y):
    glColor3f(0.6, 0.8, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(x, 0)
    glVertex2f(x + pillar_width, 0)
    glVertex2f(x + pillar_width, gap_y)
    glVertex2f(x, gap_y)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(x, gap_y + gap_height)
    glVertex2f(x + pillar_width, gap_y + gap_height)
    glVertex2f(x + pillar_width, height)
    glVertex2f(x, height)
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

def check_collision():
    global bird_y
    bird_top = bird_y + bird_radius
    bird_bottom = bird_y - bird_radius
    for pillar in pillars:
        pillar_left = pillar['x']
        pillar_right = pillar['x'] + pillar_width
        if bird_x + bird_radius > pillar_left and bird_x - bird_radius < pillar_right:
            if bird_bottom < pillar['gap_y'] or bird_top > pillar['gap_y'] + gap_height:
                return True
    return False

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw pillars
    for pillar in pillars:
        draw_pillar(pillar['x'], pillar['gap_y'])

    # Draw bird
    glColor3f(1.0, 0.8, 0.2)
    draw_circle_midpoint(bird_x, bird_y, bird_radius)

    # Draw score
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(10, height - 30)
    for c in str(score):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

    glFlush()

def timer(value):
    global bird_y, velocity, game_running
    if game_running:
        velocity += gravity
        bird_y += velocity

        if bird_y - bird_radius <= 0:
            bird_y = bird_radius
            velocity = 0
        if bird_y + bird_radius >= height:
            bird_y = height - bird_radius
            velocity = 0

        update_pillars()

        if check_collision():
            game_running = False

    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def key_pressed(key, x, y):
    global velocity, game_running, score, bird_y
    if key == b' ':
        if not game_running:
            game_running = True
            score = 0
            bird_y = height // 2
            velocity = 0
            generate_pillars()
        velocity = flap_strength

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird with GL_POINTS")
init()
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glutTimerFunc(16, timer, 0)
glutMainLoop()
