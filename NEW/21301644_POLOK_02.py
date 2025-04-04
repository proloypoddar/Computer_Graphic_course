import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 700

catc_width = 100
catc_x = width // 2 - catc_width // 2
catc_y = 50
catc_speed = 20

x_dimond = random.randint(50, width - 50)
y_dimond = height
diamond_size = 10
diamond_speed = 2
score = 0
caught_count = 0 
game_over = False
paused = False

def pixel_draw(x, y, r=1, g=1, b=1):
    glColor3f(r, g, b)
    glBegin(GL_POINTS)
    glVertex2i(int(x), int(y))  
    glEnd()

def midpoint_line(x1, y1, x2, y2, r=1, g=1, b=1):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    
    while True:
        pixel_draw(x1, y1, r, g, b)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def draw_diamond(x, y, size):
    midpoint_line(int(x), int(y + size), int(x + size), int(y), 1, 1, 0)
    midpoint_line(int(x + size), int(y), int(x), int(y - size), 1, 1, 0)
    midpoint_line(int(x), int(y - size), int(x - size), int(y), 1, 1, 0)
    midpoint_line(int(x - size), int(y), int(x), int(y + size), 1, 1, 0)

def busket_draw():
    midpoint_line(catc_x, catc_y + 10, catc_x + catc_width, catc_y + 10, 0, 1, 0)
    midpoint_line(catc_x, catc_y + 10, catc_x + 10, catc_y, 0, 1, 0)
    midpoint_line(catc_x + catc_width, catc_y + 10, catc_x + catc_width - 10, catc_y, 0, 1, 0)
    midpoint_line(catc_x + 10, catc_y, catc_x + catc_width - 10, catc_y, 0, 1, 0)

def icon_draw():
    midpoint_line(50, height - 40, 30, height - 30, 0, 1, 1)  
    midpoint_line(50, height - 40, 30, height - 50, 0, 1, 1)
    midpoint_line(30, height - 30, 30, height - 50, 0, 1, 1)
    midpoint_line(width // 2 - 10, height - 40, width // 2 - 10, height - 20, 1, 1, 0)
    midpoint_line(width // 2 + 10, height - 40, width // 2 + 10, height - 20, 1, 1, 0)
    midpoint_line(width - 50, height - 40, width - 30, height - 20, 1, 0, 0)
    midpoint_line(width - 30, height - 40, width - 50, height - 20, 1, 0, 0)

def mouse_click(button, state, x, y):
    global paused, game_over, score, diamond_speed, caught_count
    if state == GLUT_DOWN:
        y = height - y  
        if 30 <= x <= 50 and height - 50 <= y <= height - 30:
            game_over = False
            score = 0
            caught_count = 0
            diamond_speed = 2
            reset_dimnd()

            print("Game Restart")

        elif width // 2 - 10 <= x <= width // 2 + 10 and height - 40 <= y <= height - 20:

            paused = not paused
            print("Game Pause" if paused else "Game Resume")
        elif width - 50 <= x <= width - 30 and height - 40 <= y <= height - 20:
            print("Tata Bye Bye!\nKhatam Shesh!")
            glutLeaveMainLoop()

def update_value(value):
    global y_dimond, game_over, score, x_dimond, diamond_speed, caught_count
    if not paused and not game_over:
        y_dimond -= diamond_speed
        diamond_speed *= 1.001  
        if catc_x <= x_dimond <= catc_x + catc_width and y_dimond <= catc_y + 10:
            score += 1
            caught_count += 1
            print("Score :", caught_count)
            reset_dimnd()
            diamond_speed *= 1.02
        elif y_dimond < 0:
            game_over = True
            print("Game Over \nFinal Score:", score)
    glutPostRedisplay()
    glutTimerFunc(16, update_value, 0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    busket_draw()
    draw_diamond(x_dimond, y_dimond, diamond_size)
    icon_draw()
    glFlush()

def reset_dimnd():
    global x_dimond, y_dimond
    x_dimond = random.randint(20, width - 20)
    y_dimond = height

def keyboard(key, x, y):
    global catc_x
    if key == GLUT_KEY_LEFT:
        catc_x = max(0, catc_x - catc_speed)
    elif key == GLUT_KEY_RIGHT:
        catc_x = min(width - catc_width, catc_x + catc_speed)

def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(2)
    gluOrtho2D(0, width, 0, height)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"I am PROLOY :) ")
    init()
    glutDisplayFunc(draw)
    glutSpecialFunc(keyboard)
    glutMouseFunc(mouse_click)
    glutTimerFunc(0, update_value, 0)
    glutMainLoop()