from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Window dimensions
width, height = 800, 600

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # Set 2D orthographic projection

def draw_background():
    glBegin(GL_QUADS)
    
    # Draw sky gradient (light blue to white)
    glColor3f(0.4, 0.7, 1.0)  # Light blue
    glVertex2f(0, height)
    glVertex2f(width, height)
    glColor3f(1.0, 1.0, 1.0)  # White
    glVertex2f(width, height * 0.5)
    glVertex2f(0, height * 0.5)
    
    # Draw ground (green)
    glColor3f(0.1, 0.6, 0.2)  # Green
    glVertex2f(0, height * 0.5)
    glVertex2f(width, height * 0.5)
    glVertex2f(width, 0)
    glVertex2f(0, 0)
    
    glEnd()

def draw_tree(x, y, trunk_width, trunk_height, foliage_radius, layers=3):
    # Draw the trunk
    glColor3f(0.55, 0.27, 0.07)  # Brown
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + trunk_width, y)
    glVertex2f(x + trunk_width, y + trunk_height)
    glVertex2f(x, y + trunk_height)
    glEnd()

    # Draw multiple layers of foliage
    glColor3f(0.0, 0.5, 0.0)  # Dark green
    for i in range(layers):
        radius = foliage_radius * (1 - 0.2 * i)
        cx, cy = x + trunk_width / 2, y + trunk_height + i * radius * 0.7
        draw_circle(cx, cy, radius)

def draw_circle(cx, cy, radius):
    num_segments = 100
    theta = 2 * 3.14159 / num_segments
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    px, py = radius, 0
    glBegin(GL_POLYGON)
    for _ in range(num_segments):
        glVertex2f(cx + px, cy + py)
        px, py = px * cos_theta - py * sin_theta, px * sin_theta + py * cos_theta
    glEnd()

def draw_house(x, y, width, height):
    # Draw the base of the house
    glColor3f(0.8, 0.4, 0.1)  # Brown
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    # Draw the roof (triangle)
    glColor3f(0.7, 0.0, 0.0)  # Red
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + height)
    glVertex2f(x + width, y + height)
    glVertex2f(x + width / 2, y + height + height * 0.5)
    glEnd()

    # Draw the door
    glColor3f(0.5, 0.25, 0.1)  # Dark brown
    door_width = width * 0.2
    door_height = height * 0.4
    door_x = x + width * 0.4
    door_y = y
    glBegin(GL_QUADS)
    glVertex2f(door_x, door_y)
    glVertex2f(door_x + door_width, door_y)
    glVertex2f(door_x + door_width, door_y + door_height)
    glVertex2f(door_x, door_y + door_height)
    glEnd()

    # Draw windows
    glColor3f(0.0, 0.7, 0.9)  # Light blue
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

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    draw_background()

    # Draw trees with varied placements
    draw_tree(100, 200, 20, 80, 50)
    draw_tree(300, 180, 25, 100, 60, layers=4)
    draw_tree(500, 220, 20, 70, 45)

    # Draw the house with details
    draw_house(600, 200, 120, 90)

    glFlush()  # Render now

# Initialize GLUT and set up the window
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Background with Details")

init()
glutDisplayFunc(display)
glutMainLoop()
