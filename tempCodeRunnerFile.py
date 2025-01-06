import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
width, height = 800, 600

# Pillar parameters
pillar_width = 50
pillar_gap = 150
pillar_speed = 2
pillars = []

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # Set 2D orthographic projection
    generate_pillars()

def generate_pillars():
    """Generate initial set of pillars."""
    global pillars
    x_position = width
    for _ in range(5):  # Generate 5 pillars to start with
        gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': x_position, 'gap_y': gap_y})
        x_position += 300  # Space between pillars

def draw_pillar(x, gap_y):
    """Draw a single pillar with gradient and shading."""
    # Draw lower pillar
    draw_pillar_section(x, 0, gap_y)
    # Draw upper pillar
    draw_pillar_section(x, gap_y + pillar_gap, height)

def draw_pillar_section(x, y_bottom, y_top):
    """Draw a pillar section with gradient and shading."""
    # Gradient color
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.7, 0.3)  # Lighter green
    glVertex2f(x, y_bottom)
    glVertex2f(x + pillar_width, y_bottom)
    glColor3f(0.1, 0.5, 0.2)  # Darker green
    glVertex2f(x + pillar_width, y_top)
    glVertex2f(x, y_top)
    glEnd()

    # Shading for the left side
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.25, 0.25)  # Darker green
    glVertex2f(x, y_bottom)
    glVertex2f(x + 5, y_bottom)
    glVertex2f(x + 5, y_top)
    glVertex2f(x, y_top)
    glEnd()

    # Grooves for design
    draw_pillar_grooves(x, y_bottom, y_top)

def draw_pillar_grooves(x, y_bottom, y_top):
    """Add horizontal grooves to the pillar for design."""
    glColor3f(0.8, 0.25, 0.25)  # Groove color
    groove_spacing = 20
    for y in range(y_bottom + groove_spacing, y_top, groove_spacing):
        glBegin(GL_LINES)
        glVertex2f(x + 5, y)
        glVertex2f(x + pillar_width - 5, y)
        glEnd()

def update_pillars():
    """Update pillar positions and generate new ones as needed."""
    global pillars
    for pillar in pillars:
        pillar['x'] -= pillar_speed  # Move pillars to the left

    # Remove pillars that move off-screen and add new ones
    if pillars and pillars[0]['x'] + pillar_width < 0:
        pillars.pop(0)  # Remove the first pillar
        new_x = pillars[-1]['x'] + 300  # Space between pillars
        new_gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': new_x, 'gap_y': new_gap_y})

def draw_pillars():
    """Draw all pillars."""
    for pillar in pillars:
        draw_pillar(pillar['x'], pillar['gap_y'])

def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.7, 1.0)  # Light blue
    glVertex2f(0, height)
    glVertex2f(width, height)
    glColor3f(1.0, 1.0, 1.0)  # White
    glVertex2f(width, height * 0.5)
    glVertex2f(0, height * 0.5)
    glColor3f(0.1, 0.6, 0.2)  # Green
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

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw the background
    draw_background()

    # Draw trees and house
    draw_tree(100, 200, 20, 80, 50)
    draw_tree(300, 180, 25, 100, 60, layers=4)
    draw_tree(500, 220, 20, 70, 45)

    # Draw pillars
    draw_pillars()

    glFlush()  # Render now

def timer(value):
    """Timer function to update game state."""
    update_pillars()
    glutPostRedisplay()  # Mark the current window as needing to be redisplayed
    glutTimerFunc(16, timer, 0)  # Call this function again in ~16ms (60 FPS)

# Initialize and run
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Game with Designed Pillars")

init()
glutDisplayFunc(display)
glutTimerFunc(16, timer, 0)  # Start the timer
glutMainLoop()
