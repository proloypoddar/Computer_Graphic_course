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

# Bird parameters
bird_radius = 20
bird_x = 100
bird_y = height // 2
bird_velocity = 0
bird_gravity = -0.5
bird_lift = 10

# Game state
is_game_running = False
score = 0
lives = 3

# Initialize game
def init():
    global bird_x, bird_y, bird_velocity, score, lives
    bird_x = 100
    bird_y = height // 2
    bird_velocity = 0
    score = 0
    lives = 3
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # Set 2D orthographic projection
    generate_pillars()

# Generate initial set of pillars
def generate_pillars():
    global pillars
    x_position = width
    for _ in range(5):  # Generate 5 pillars to start with
        gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': x_position, 'gap_y': gap_y})
        x_position += 300  # Space between pillars

# Draw a single pillar with gradient and shading
def draw_pillar(x, gap_y):
    draw_pillar_section(x, 0, gap_y)
    draw_pillar_section(x, gap_y + pillar_gap, height)

# Draw the pillar section with gradient and shading
def draw_pillar_section(x, y_bottom, y_top):
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

# Add horizontal grooves to the pillar for design
def draw_pillar_grooves(x, y_bottom, y_top):
    glColor3f(0.8, 0.25, 0.25)  # Groove color
    groove_spacing = 20
    for y in range(y_bottom + groove_spacing, y_top, groove_spacing):
        glBegin(GL_LINES)
        glVertex2f(x + 5, y)
        glVertex2f(x + pillar_width - 5, y)
        glEnd()

# Update pillar positions and generate new ones as needed
def update_pillars():
    global pillars
    for pillar in pillars:
        pillar['x'] -= pillar_speed  # Move pillars to the left

    # Remove pillars that move off-screen and add new ones
    if pillars and pillars[0]['x'] + pillar_width < 0:
        pillars.pop(0)  # Remove the first pillar
        new_x = pillars[-1]['x'] + 300  # Space between pillars
        new_gap_y = random.randint(height // 4, height // 2)
        pillars.append({'x': new_x, 'gap_y': new_gap_y})

# Draw all pillars
def draw_pillars():
    for pillar in pillars:
        draw_pillar(pillar['x'], pillar['gap_y'])

# Draw background (sky and ground)
def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.7, 1.0)  # Light blue (sky)
    glVertex2f(0, height)
    glVertex2f(width, height)
    glColor3f(1.0, 1.0, 1.0)  # White (clouds)
    glVertex2f(width, height * 0.5)
    glVertex2f(0, height * 0.5)
    glColor3f(0.1, 0.6, 0.2)  # Green (ground)
    glVertex2f(0, height * 0.5)
    glVertex2f(width, height * 0.5)
    glVertex2f(width, 0)
    glVertex2f(0, 0)
    glEnd()

# Draw the bird (with more detail)
def draw_bird():
    # Bird body
    glColor3f(1.0, 1.0, 0.0)  # Yellow body
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = math.radians(i)
        x = bird_radius * math.cos(angle) + bird_x
        y = bird_radius * math.sin(angle) + bird_y
        glVertex2f(x, y)
    glEnd()

    # Bird beak
    glColor3f(1.0, 0.5, 0.0)  # Orange beak
    glBegin(GL_TRIANGLES)
    glVertex2f(bird_x + bird_radius, bird_y)
    glVertex2f(bird_x + bird_radius + 10, bird_y + 5)
    glVertex2f(bird_x + bird_radius + 10, bird_y - 5)
    glEnd()

    # Bird wings
    glColor3f(0.7, 0.7, 0.0)  # Lighter yellow for wings
    glBegin(GL_TRIANGLES)
    glVertex2f(bird_x - bird_radius, bird_y + 10)
    glVertex2f(bird_x - bird_radius - 15, bird_y + 25)
    glVertex2f(bird_x - bird_radius - 15, bird_y - 25)
    glEnd()

# Check for collision with pillars
def check_collision():
    global bird_y, bird_radius, pillars, score, lives
    for pillar in pillars:
        if pillar['x'] < bird_x + bird_radius < pillar['x'] + pillar_width:
            if bird_y - bird_radius < pillar['gap_y'] or bird_y + bird_radius > pillar['gap_y'] + pillar_gap:
                lives -= 1
                if lives <= 0:
                    print("Game Over!")
                    return True  # Return True for game over
            else:
                score += 1
    return False  # Continue the game if no collision

# Handle key presses
def key_pressed(key, x, y):
    global bird_velocity, is_game_running
    if key == b' ':
        if not is_game_running:
            is_game_running = True
        bird_velocity = bird_lift  # Lift the bird when space is pressed
        if is_game_running and (bird_y == 0 or bird_y == height):  # Reset if bird hit the ground or top
            init()  # Restart the game

# Timer function to update game state
def timer(value):
    global bird_y, bird_velocity, is_game_running  # Declare the global variables
    if is_game_running:
        bird_velocity += bird_gravity  # Apply gravity
        bird_y += bird_velocity  # Move bird based on velocity

        if bird_y < 0:
            bird_y = 0
        elif bird_y > height:
            bird_y = height

        update_pillars()

        if check_collision():  # Game over when bird hits pillar
            is_game_running = False

    glutPostRedisplay()  # Mark the current window as needing to be redisplayed
    glutTimerFunc(16, timer, 0)  # Call this function again in ~16ms (60 FPS)

# Display function to render the game scene
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw the background
    draw_background()

    # Draw trees and house (restored)
    draw_tree(100, 200, 20, 80, 50)
    draw_tree(300, 180, 25, 100, 60, layers=4)
    draw_tree(500, 220, 20, 70, 45)

    # Draw pillars
    draw_pillars()

    # Draw the bird
    draw_bird()

    # Draw the score and lives
    glColor3f(1.0, 1.0, 1.0)  # White text for score and lives
    render_text(10, height - 30, f"Score: {score}")
    render_text(10, height - 60, f"Lives: {lives}")

    glFlush()  # Render now

# Render text function for displaying score and lives
def render_text(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

# Draw tree (function missing in previous code)
def draw_tree(x, y, trunk_width, trunk_height, foliage_radius, layers=3):
    glColor3f(0.55, 0.27, 0.07)  # Brown for trunk
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + trunk_width, y)
    glVertex2f(x + trunk_width, y + trunk_height)
    glVertex2f(x, y + trunk_height)
    glEnd()

    glColor3f(0.0, 0.5, 0.0)  # Green for foliage
    for i in range(layers):
        radius = foliage_radius * (1 - 0.2 * i)
        draw_circle(x + trunk_width / 2, y + trunk_height + i * radius * 0.7, radius)

# Draw a circle for tree foliage
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

# Initialize and run
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Flappy Bird Game")

init()
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glutTimerFunc(16, timer, 0)  # Start the timer
glutMainLoop()
