from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

width, height = 800, 600
pilr_width = 50

gaph_pilr = 150

pilr_speed = 5.5
pilr = []

bird_w = 30
bird_h = 30

bird_y_axis = height // 2
velosity = 0

gravity = -0.5

bird_lft = 10

game_run = True
score = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    generate_pilr()

def generate_pilr():
    global pilr
    pos_x = width
    for _ in range(5):
        gap_y = random.randint(height // 4, height // 2)
        pilr.append({'x': pos_x, 'gap_y': gap_y})
        pos_x += 300

def draw_pillar(x, gap_y):
    glColor3f(0.6, 0.8, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(x, 0)
    glVertex2f(x + pilr_width, 0)
    glVertex2f(x + pilr_width, gap_y)
    glVertex2f(x, gap_y)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(x, gap_y + gaph_pilr)
    glVertex2f(x + pilr_width, gap_y + gaph_pilr)
    glVertex2f(x + pilr_width, height)
    glVertex2f(x, height)
    glEnd()

    glColor3f(0.5, 0.5, 0.5)
    line_space = 5
    for i in range(0, pilr_width, line_space):
        glBegin(GL_LINES)
        glVertex2f(x + i, gap_y)
        glVertex2f(x + i, gap_y + gaph_pilr)
        glEnd()

def update_pilr():
    global pilr, score
    for pillar in pilr:
        pillar['x'] -= pilr_speed

    if pilr and pilr[0]['x'] + pilr_width < 100:
        score += 1
        pilr.pop(0)
        new_x = pilr[-1]['x'] + 300
        new_gap_y = random.randint(height // 4, height // 2)
        pilr.append({'x': new_x, 'gap_y': new_gap_y})

def draw_pilr():
    for pillar in pilr:
        draw_pillar(pillar['x'], pillar['gap_y'])

def draw_mountain(base_x, base_y, width, height):

    glColor3f(0.5, 0.35, 0.05)  
    glBegin(GL_TRIANGLES)
    glVertex2f(base_x, base_y)
    glVertex2f(base_x + width / 2, base_y + height)
    glVertex2f(base_x + width, base_y)
    glEnd()

    
def draw_background():

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.7, 1.0) 
    glVertex2f(0, height)
    glVertex2f(width, height)
    glColor3f(1.0, 1.0, 1.0) 
    glVertex2f(width, height * 0.5)
    glVertex2f(0, height * 0.5)
    glEnd()


    draw_mountain(100, height * 0.2, 200, 300)
   
    draw_mountain(600, height * 0.5, 300, 350)


    glBegin(GL_QUADS)
    glColor3f(0.1, 0.6, 0.2)  
    glVertex2f(0, height * 0.5)
    glVertex2f(width, height * 0.5)
    glVertex2f(width, 0)
    glVertex2f(0, 0)
    glEnd()

def draw_tree(x, y, trunk_width, trunk_height, foliage_radius, layers=3):
    glColor3f(0.55, 0.27, 0.07)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + trunk_width, y)
    glVertex2f(x + trunk_width, y + trunk_height)
    glVertex2f(x, y + trunk_height)
    glEnd()

    glColor3f(0.0, 0.5, 0.0)
    for i in range(layers):
        radius = foliage_radius * (1 - 0.2 * i)
        draw_circle(x + trunk_width / 2, y + trunk_height + i * radius * 0.7, radius)

def draw_circle(cx, cy, radius):
    num_segments = 100
    theta = 2 * math.pi / num_segments
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    px, py = radius, 0
    glBegin(GL_POLYGON)
    for _ in range(num_segments):
        glVertex2f(cx + px, cy + py)
        px, py = px * cos_theta - py * sin_theta, px * sin_theta + py * cos_theta
    glEnd()

def draw_house(x, y, width, height):
    glColor3f(0.8, 0.4, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    glColor3f(0.7, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + height)
    glVertex2f(x + width, y + height)
    glVertex2f(x + width / 2, y + height + height * 0.5)
    glEnd()

    glColor3f(0.5, 0.25, 0.1)
    door_width = width * 0.2
    door_height = height * 0.4
    door_x = x + width * 0.4
    glBegin(GL_QUADS)
    glVertex2f(door_x, y)
    glVertex2f(door_x + door_width, y)
    glVertex2f(door_x + door_width, y + door_height)
    glVertex2f(door_x, y + door_height)
    glEnd()

    glColor3f(0.0, 0.7, 0.9)
    window_size = width * 0.2
    glBegin(GL_QUADS)
    glVertex2f(x + width * 0.2, y + height * 0.6)
    glVertex2f(x + width * 0.2 + window_size, y + height * 0.6)
    glVertex2f(x + width * 0.2 + window_size, y + height * 0.8)
    glVertex2f(x + width * 0.2, y + height * 0.8)
    glVertex2f(x + width * 0.6, y + height * 0.6)
    glVertex2f(x + width * 0.6 + window_size, y + height * 0.6)
    glVertex2f(x + width * 0.6 + window_size, y + height * 0.8)
    glVertex2f(x + width * 0.6, y + height * 0.8)
    glEnd()

def draw_bird(y):
    # Bird body
    glColor3f(1.0, 0.8, 0.2)  # Yellow body
    draw_circle(100 + bird_w // 2, y + bird_h // 2, bird_w // 2)



    # Bird eye
    glColor3f(0.0, 0.0, 0.0)  # Black eye
    draw_circle(100 + bird_w // 1.5, y + bird_h // 1.5, bird_w // 8)

    # Bird beak
    glColor3f(1.0, 0.5, 0.0)  # Orange beak
    glBegin(GL_TRIANGLES)
    glVertex2f(100 + bird_w, y + bird_h // 2)
    glVertex2f(100 + bird_w + bird_w // 4, y + bird_h // 2.5)
    glVertex2f(100 + bird_w, y + bird_h // 1.5)
    glEnd()


def check_collision():
    global bird_y_axis
    bird_x = 100
    bird_top = bird_y_axis + bird_h
    bird_bottom = bird_y_axis
    for pillar in pilr:
        pillar_left = pillar['x']
        pillar_right = pillar['x'] + pilr_width
        pillar_bottom = pillar['gap_y']
        pillar_top = pillar['gap_y'] + gaph_pilr
        if bird_x + bird_w > pillar_left and bird_x < pillar_right:
            if bird_bottom < pillar_bottom or bird_top > pillar_top:
                return True
    return False

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_background()
    draw_tree(100, 200, 20, 80, 50)
    draw_tree(300, 180, 25, 100, 60, layers=4)
    draw_tree(500, 220, 20, 70, 45)
    draw_house(600, 200, 120, 90)
    draw_pilr()
    draw_bird(bird_y_axis)
    draw_score()
    glFlush()

def draw_score():
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(20, height - 30)
    for c in str(score):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

def timer(value):
    global bird_y_axis, velosity, game_run

    if game_run:
        velosity += gravity
        bird_y_axis += velosity

        if bird_y_axis <= 0:
            bird_y_axis = 0
            velosity = 0
        if bird_y_axis + bird_h >= height:
            bird_y_axis = height - bird_h
            velosity = 0

        update_pilr()

        if check_collision():
            game_run = False

    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def key_pressed(key, x, y):
    global velosity, game_run, score, pilr

    if key == b' ' and not game_run:
        game_run = True
        bird_y_axis = height // 2
        velosity = 0
        score = 0
        pilr.clear()
        generate_pilr()

    if key == b' ' and game_run:
        velosity = bird_lft

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Game CSE 423 Lab Project")

init()
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glutTimerFunc(16, timer, 0)
glutMainLoop()
