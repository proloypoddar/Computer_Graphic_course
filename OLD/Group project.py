from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# Window dimensions
width, height = 800, 600

# Pillar parameters
pillar_width = 50
pillar_gap = 150
pillar_speed = 2
pillars = []

# Bird parameters
bird_width = 30
bird_height = 30
bird_y = height // 2
bird_velocity = 0
bird_gravity = -0.5
bird_lift = 10

# Game state
is_game_running = True
score = 0

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
    """Draw a single pillar with a gap at the specified y-coordinate."""
    glColor3f(0.6, 0.8, 0.3)  # Green
    # Lower pillar
    glBegin(GL_QUADS)
    glVertex2f(x, 0)
    glVertex2f(x + pillar_width, 0)
    glVertex2f(x + pillar_width, gap_y)
    glVertex2f(x, gap_y)
    glEnd()

    # Upper pillar
    glBegin(GL_QUADS)
    glVertex2f(x, gap_y + pillar_gap)
    glVertex2f(x + pillar_width, gap_y + pillar_gap)
    glVertex2f(x + pillar_width, height)
    glVertex2f(x, height)
    glEnd()

    # Add some vertical lines for pillar detail
    glColor3f(0.5, 0.5, 0.5)  # Gray
    line_spacing = 5
    for i in range(0, pillar_width, line_spacing):
        glBegin(GL_LINES)
        glVertex2f(x + i, gap_y)
        glVertex2f(x + i, gap_y + pillar_gap)
        glEnd()

def update_pillars():
    """Update pillar positions and generate new ones as needed."""
    global pillars, score
    for pillar in pillars:
        pillar['x'] -= pillar_speed  # Move pillars to the left

    # Check for passing a pillar (increase score)
    if pillars and pillars[0]['x'] + pillar_width < 100:  # Bird's x position
        score += 1
        pillars.pop(0)  # Remove the first pillar
        new_x = pillars[-1]['x'] + 300  # Space between pillars
        new_gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': new_x, 'gap_y': new_gap_y})

def draw_pillars():
    """Draw all pillars."""
    for pillar in pillars:
        draw_pillar(pillar['x'], pillar['gap_y'])

def draw_background():
    """Draw the background."""
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
    """Draw a tree with multiple layers of foliage."""
    glColor3f(0.55, 0.27, 0.07)  # Brown trunk
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + trunk_width, y)
    glVertex2f(x + trunk_width, y + trunk_height)
    glVertex2f(x, y + trunk_height)
    glEnd()

    glColor3f(0.0, 0.5, 0.0)  # Green foliage
    for i in range(layers):
        radius = foliage_radius * (1 - 0.2 * i)
        draw_circle(x + trunk_width / 2, y + trunk_height + i * radius * 0.7, radius)

def draw_circle(cx, cy, radius):
    """Draw a circle for tree foliage."""
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
    """Draw a simple house with a roof and windows."""
    glColor3f(0.8, 0.4, 0.1)  # Brown walls
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    glColor3f(0.7, 0.0, 0.0)  # Red roof
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + height)
    glVertex2f(x + width, y + height)
    glVertex2f(x + width / 2, y + height + height * 0.5)
    glEnd()

    glColor3f(0.5, 0.25, 0.1)  # Door
    door_width = width * 0.2
    door_height = height * 0.4
    door_x = x + width * 0.4
    glBegin(GL_QUADS)
    glVertex2f(door_x, y)
    glVertex2f(door_x + door_width, y)
    glVertex2f(door_x + door_width, y + door_height)
    glVertex2f(door_x, y + door_height)
    glEnd()

    glColor3f(0.0, 0.7, 0.9)  # Windows
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
    """Draw the bird."""
    glColor3f(1.0, 0.2, 0.4)  # Yellow bird
    glBegin(GL_QUADS)
    glVertex2f(100, y)
    glVertex2f(100 + bird_width, y)
    glVertex2f(100 + bird_width, y + bird_height)
    glVertex2f(100, y + bird_height)
    glEnd()

def check_collision():
    """Check if the bird has collided with any pillar."""
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
                return True  # Bird hit a pillar
    return False

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw the background
    draw_background()

    # Draw trees and house
    draw_tree(100, 200, 20, 80, 50)
    draw_tree(300, 180, 25, 100, 60, layers=4)
    draw_tree(500, 220, 20, 70, 45)
    draw_house(600, 200, 120, 90)

    # Draw pillars
    draw_pillars()

    # Draw bird
    draw_bird(bird_y)

    # Draw score
    draw_score()

    glFlush()  # Render now

def draw_score():
    """Draw the score on the screen."""
    glColor3f(1.0, 1.0, 1.0)  # White text
    glRasterPos2f(20, height - 30)
    for c in str(score):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

def timer(value):
    """Timer function to update game state."""
    global bird_y, bird_velocity, is_game_running

    if is_game_running:
        # Update bird physics
        bird_velocity += bird_gravity
        bird_y += bird_velocity

        if bird_y <= 0:
            bird_y = 0
            bird_velocity = 0
        if bird_y + bird_height >= height:
            bird_y = height - bird_height
            bird_velocity = 0

        update_pillars()

        # Check for collisions
        if check_collision():
            is_game_running = False  # End game on collision

    glutPostRedisplay()  # Mark the current window as needing to be redisplayed
    glutTimerFunc(16, timer, 0)  # Call this function again in ~16ms (60 FPS)

def key_pressed(key, x, y):
    """Handle key press events."""
    global bird_velocity, is_game_running, score, pillars

    if key == b' ' and not is_game_running:  # Restart game on spacebar press
        is_game_running = True
        bird_y = height // 2
        bird_velocity = 0
        score = 0
        pillars.clear()
        generate_pillars()

    if key == b' ' and is_game_running:  # Make bird jump
        bird_velocity = bird_lift

# Initialize and run
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Game CSE 423 Lab Project")

init()
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)  # Listen for key presses
glutTimerFunc(16, timer, 0)  # Start the timer
glutMainLoop()
