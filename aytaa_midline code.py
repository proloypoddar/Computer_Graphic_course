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
        draw_circle_midpoint(x + trunk_width / 2, y + trunk_height + i * radius * 0.7, radius)

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
    glColor3f(1.0, 0.8, 0.2)
    draw_circle_midpoint(100 + bird_w // 2, y + bird_h // 2, bird_w // 2)

    glColor3f(0.0, 0.0, 0.0)
    draw_circle_midpoint(100 + bird_w // 1.5, y + bird_h // 1.5, bird_w // 8)

    glColor3f(1.0, 0.5, 0.0)
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
    glRasterPos2f(width - 100, height - 30)
    for char in str(score):
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def timer(value):
    global bird_y_axis, velosity, game_run

    if game_run:
        velosity += gravity
        bird_y_axis += velosity

        if bird_y_axis < 0:
            bird_y_axis = 0
            velosity = 0

        update_pilr()

        if check_collision():
            game_run = False
            print("Game Over")

    glutPostRedisplay()
    glutTimerFunc(20, timer, 0)

def keyboard(key, x, y):
    global bird_y_axis, velosity
    if key == b' ':
        velosity = 8
def draw_circle_midpoint(x_center, y_center, radius):

    x = radius
    y = 0
    p = 1 - radius  

    plot_circle_points(x_center, y_center, x, y)


    while x > y:
        y += 1
        if p <= 0:
            p += 2 * y + 1  
        else:
            x -= 1
            p += 2 * y - 2 * x + 1
        plot_circle_points(x_center, y_center, x, y)

def plot_circle_points(x_center, y_center, x, y):

    glVertex2f(x_center + x, y_center + y)
    glVertex2f(x_center - x, y_center + y)
    glVertex2f(x_center + x, y_center - y)
    glVertex2f(x_center - x, y_center - y)
    glVertex2f(x_center + y, y_center + x)
    glVertex2f(x_center - y, y_center + x)
    glVertex2f(x_center + y, y_center - x)
    glVertex2f(x_center - y, y_center - x)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Flappy Bird")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(20, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
