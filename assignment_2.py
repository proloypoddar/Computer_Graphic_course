
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Player (Shooter) properties
shooter_x = WIDTH // 2
shooter_width = 50
shooter_height = 30
shooter_speed = 100

# Bullet properties
bullets = []
bullet_speed = 50
bullet_radius = 10
# Falling Circle properties
falling_circles = []
circle_speed = 25

# Score and missed count
score = 0
missed = 0

# Game over flag
game_over = False

# Initialize the window
def init_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Shoot The Circles")
    glClearColor(0,0,0,1)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

# Draw the shooter (spaceship)
def draw_shooter():

    glColor3f(1, 1, 0)


    glBegin(GL_LINES)
    glVertex2f(shooter_x - shooter_width / 6, 50)
    glVertex2f(shooter_x - shooter_width / 6, 50 + shooter_height)

    glVertex2f(shooter_x + shooter_width / 6, 50)
    glVertex2f(shooter_x + shooter_width / 6, 50 + shooter_height)

    glVertex2f(shooter_x - shooter_width / 6, 50 + shooter_height)
    glVertex2f(shooter_x + shooter_width / 6, 50 + shooter_height)

    glVertex2f(shooter_x - shooter_width / 6, 50)
    glVertex2f(shooter_x + shooter_width / 6, 50)
    glEnd()


    glBegin(GL_LINES)
    glVertex2f(shooter_x - shooter_width / 2, 50 + shooter_height)
    glVertex2f(shooter_x, 50 + shooter_height + shooter_height / 1.5)

    glVertex2f(shooter_x + shooter_width / 2, 50 + shooter_height)
    glVertex2f(shooter_x, 50 + shooter_height + shooter_height / 1.5)

    glVertex2f(shooter_x - shooter_width / 2, 50 + shooter_height)
    glVertex2f(shooter_x + shooter_width / 2, 50 + shooter_height)
    glEnd()


    glBegin(GL_LINES)
    glVertex2f(shooter_x - shooter_width / 6, 50)
    glVertex2f(shooter_x - shooter_width / 3, 50 - 10)
    glVertex2f(shooter_x - shooter_width / 3, 50 - 10)
    glVertex2f(shooter_x, 50 - 10)  # Bottom-center
    glVertex2f(shooter_x, 50 - 10)  # Bottom-center
    glVertex2f(shooter_x - shooter_width / 6, 50)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(shooter_x + shooter_width / 6, 50)
    glVertex2f(shooter_x + shooter_width / 3, 50 - 10)
    glVertex2f(shooter_x + shooter_width / 3, 50 - 10)
    glVertex2f(shooter_x, 50 - 10)  # Bottom-center
    glVertex2f(shooter_x, 50 - 10)  # Bottom-center
    glVertex2f(shooter_x + shooter_width / 6, 50)
    glEnd()


# Draw the bullet
def draw_bullet(x, y):
    glColor3f(1, 0, 0)
    segments = 20
    angle_step = 2 * math.pi / segments

    glBegin(GL_POINTS)
    for i in range(segments):
        angle = i * angle_step
        dx = x + bullet_radius * math.cos(angle)
        dy = y + bullet_radius * math.sin(angle)
        glVertex2f(dx, dy)
    glEnd()


# Draw falling circles
def draw_circle(x, y, radius):
    glColor3f(0, 0, 1)  # Blue circles
    segments = 50
    angle_step = 2 * math.pi / segments
    glBegin(GL_POINTS)
    for i in range(segments):
        angle = i * angle_step
        dx = x + radius * math.cos(angle)
        dy = y + radius * math.sin(angle)
        glVertex2f(dx, dy)
    glEnd()

# Update the positions of bullets
def update_bullets():
    global missed
    for bullet in bullets[:]:
        bullet[1] += bullet_speed
        if bullet[1] > HEIGHT:
            bullets.remove(bullet)

# Update falling circles
def update_falling_circles():
    global score, missed, game_over

    for circle in falling_circles[:]:
        circle[1] -= circle_speed  # Fall down

        # Check if circle touches the spaceship directly
        if (circle[0] > shooter_x - shooter_width / 2 and
                circle[0] < shooter_x + shooter_width / 2 and
                circle[1] < 50 + shooter_height):
            game_over = True
            display_text(WIDTH // 2 - 50, HEIGHT // 2, "Game Over! (Touched the spaceship)")
            return


        if circle[1] < 0:
            missed += 1
            falling_circles.remove(circle)

            if missed >= 3:  # Game over if 3 misses occur
                game_over = True
                display_text(WIDTH // 2 - 50, HEIGHT // 2, "Game Over! (3 Misses)")
                return

        # Check for collision with bullets
        if check_collision(circle[0], circle[1], circle[2]):
            score += 1
            falling_circles.remove(circle)


# Check for collision between bullet and circle
def check_collision(cx, cy, radius):
    for bullet in bullets[:]:
        bx, by = bullet
        if (bx - cx)**2 + (by - cy)**2 <= radius**2:
            bullets.remove(bullet)
            return True
    return False

# Display the score and game over
def display_text(x, y, text):
    glColor3f(1, 1, 1)  # White
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))

# Keyboard input handling
def keyboard(key, x, y):
    global shooter_x, game_over
    if key == b'a' and shooter_x > shooter_width / 2:
        shooter_x -= shooter_speed  # Move left
    if key == b'd' and shooter_x < WIDTH - shooter_width / 2:
        shooter_x += shooter_speed  # Move right
    if key == b' ' and not game_over:
        bullets.append([shooter_x, 50 + shooter_height])  # Fire bullet
def idle():
    pass
# Main display function
def display():
    global game_over

    glClear(GL_COLOR_BUFFER_BIT)

    if not game_over:
        # Draw everything
        draw_shooter()
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])
        for circle in falling_circles:
            draw_circle(circle[0], circle[1], circle[2])

        update_bullets()
        update_falling_circles()

        display_text(10, HEIGHT - 20, f"Score: {score}")
        display_text(10, HEIGHT - 40, f"Missed: {missed}")

        if missed >= 3:
            game_over = True
            display_text(WIDTH // 2 - 50, HEIGHT // 2, "Game Over!")
        elif score >= 10:
            game_over = True
            display_text(WIDTH // 2 - 50, HEIGHT // 2, "You Win!")

    glutSwapBuffers()

# Timer to generate falling circles automatically
def timer(value):
    if not game_over:
        radius = random.randint(10, 30)
        x = random.randint(radius, WIDTH - radius)
        falling_circles.append([x, HEIGHT, radius])  # Add a new circle to the list
        glutPostRedisplay()
        glutTimerFunc(1000, timer, 0)

# Start the game
def main():
    init_window()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutTimerFunc(1000, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
