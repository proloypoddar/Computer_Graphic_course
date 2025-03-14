import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 700

# Catcher settings
catcher_width = 100
catcher_x = width // 2 - catcher_width // 2
catcher_y = 50
catcher_speed = 20

# Diamond settings
diamond_x = random.randint(50, width - 50)
diamond_y = height
diamond_size = 10
diamond_speed = 2
score = 0
caught_count = 0  # Count of caught diamonds
game_over = False
paused = False

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(int(x), int(y))  # Ensure integer values
    glEnd()

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glEnd()

def draw_diamond(x, y, size):
    draw_line(int(x), int(y + size), int(x + size), int(y))
    draw_line(int(x + size), int(y), int(x), int(y - size))
    draw_line(int(x), int(y - size), int(x - size), int(y))
    draw_line(int(x - size), int(y), int(x), int(y + size))

def draw_catcher():
    left = catcher_x
    right = catcher_x + catcher_width
    bottom = catcher_y
    top = catcher_y + 10
    
    glColor3f(1, 1, 1) if not game_over else glColor3f(1, 0, 0)
    draw_line(left, top, right, top)
    draw_line(left, top, left + 10, bottom)
    draw_line(right, top, right - 10, bottom)
    draw_line(left + 10, bottom, right - 10, bottom)

def update(value):
    global diamond_y, game_over, score, diamond_x, diamond_speed, caught_count

    if not paused and not game_over:
        diamond_y -= diamond_speed
        diamond_speed *= 1.001  # Gradually increase speed over time

        if catcher_x <= diamond_x <= catcher_x + catcher_width and diamond_y <= catcher_y + 10:
            score += 1
            caught_count += 1
            print("Caught Diamonds:", caught_count)
            reset_diamond()
            diamond_speed *= 1.02
        elif diamond_y < 0:
            game_over = True
            print("Game Over! Final Score:", score)

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def draw_icons():
    glColor3f(0, 1, 1)  # Teal (Play/Restart)
    draw_line(50, height - 40, 30, height - 30)
    draw_line(50, height - 40, 30, height - 50)
    draw_line(30, height - 30, 30, height - 50)
    glColor3f(1, 1, 0)  # Yellow (Pause)
    draw_line(width // 2 - 10, height - 40, width // 2 - 10, height - 20)
    draw_line(width // 2 + 10, height - 40, width // 2 + 10, height - 20)
    glColor3f(1, 0, 0)  # Red (Exit)
    draw_line(width - 50, height - 40, width - 30, height - 20)
    draw_line(width - 30, height - 40, width - 50, height - 20)

def mouse_click(button, state, x, y):
    global paused, game_over, score, diamond_speed, caught_count
    
    if state == GLUT_DOWN:
        y = height - y  # Convert screen coordinates to OpenGL coordinates
        
        if 30 <= x <= 50 and height - 50 <= y <= height - 30:  # Play/Restart Button
            game_over = False
            score = 0
            caught_count = 0
            diamond_speed = 2
            reset_diamond()
            print("Game Restarted")
        elif width // 2 - 10 <= x <= width // 2 + 10 and height - 40 <= y <= height - 20:  # Pause Button
            paused = not paused
            print("Game Paused" if paused else "Game Resumed")
        elif width - 50 <= x <= width - 30 and height - 40 <= y <= height - 20:  # Exit Button
            print("Exiting Game...")
            glutLeaveMainLoop()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_catcher()
    draw_icons()
    glColor3f(1, 1, 0)
    draw_diamond(diamond_x, diamond_y, diamond_size)
    glFlush()

def reset_diamond():
    global diamond_x, diamond_y
    diamond_x = random.randint(20, width - 20)
    diamond_y = height

def keyboard(key, x, y):
    global catcher_x
    if key == GLUT_KEY_LEFT:
        catcher_x = max(0, catcher_x - catcher_speed)
    elif key == GLUT_KEY_RIGHT:
        catcher_x = min(width - catcher_width, catcher_x + catcher_speed)

def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(2)
    gluOrtho2D(0, width, 0, height)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Catch the Diamonds!")
    init()
    glutDisplayFunc(draw)
    glutSpecialFunc(keyboard)
    glutMouseFunc(mouse_click)  # Enable mouse input
    glutTimerFunc(0, update, 0)
    glutMainLoop()
