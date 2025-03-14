#Task 1
########################################################################################################
# import random
# import sys
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# rain = []
# rain_direct = 0 
# background_colur = [1.0, 1.0, 1.0]  
# house_colr = [0.0, 0.0, 0.0]  
# day_night = 0.02  


# def my_house():
#     glColor3f(house_colr[0], house_colr[1], house_colr[2])
#     glLineWidth(2)
#     glBegin(GL_LINES)
#     glVertex2f(100, 200)
#     glVertex2f(300, 200)

#     glVertex2f(300, 200)
#     glVertex2f(300, 100)

#     glVertex2f(300, 100)
#     glVertex2f(100, 100)
#     glVertex2f(100, 100)

#     glVertex2f(100, 200)

#     glEnd()
#     glBegin(GL_TRIANGLES)
#     glVertex2f(100, 200)
#     glVertex2f(200, 320)
#     glVertex2f(300, 200)
#     glEnd()
#     glBegin(GL_LINES)
#     glVertex2f(170, 100)
#     glVertex2f(170, 150)

#     glVertex2f(170, 150)
#     glVertex2f(230, 150)
#     glVertex2f(230, 150)
#     glVertex2f(230, 100)
#     glVertex2f(230, 100)
#     glVertex2f(170, 100)
#     glEnd()

#     glBegin(GL_LINES)

#     glVertex2f(120, 160)
#     glVertex2f(160, 160)
#     glVertex2f(160, 160)
#     glVertex2f(160, 120)

#     glVertex2f(160, 120)
#     glVertex2f(120, 120)
#     glVertex2f(120, 120)
#     glVertex2f(120, 160)

#     glVertex2f(140, 160)
#     glVertex2f(140, 120)
#     glVertex2f(120, 140)
#     glVertex2f(160, 140)
#     glEnd()

# def tree():
#     glColor3f(0.4, 0.2, 0.0)
#     glBegin(GL_LINES)
#     glVertex2f(350, 100)
#     glVertex2f(350, 180)
#     glEnd()
#     glColor3f(0.0, 0.5, 0.0)

#     glBegin(GL_TRIANGLES)
#     glVertex2f(320, 180)
#     glVertex2f(350, 250)
#     glVertex2f(380, 180)
#     glEnd()
#     glBegin(GL_TRIANGLES)
#     glVertex2f(320, 250)
#     glVertex2f(350, 320)
#     glVertex2f(380, 250)
#     glEnd()



# def rain_drop():
#     x = random.randint(50, 450)

#     y = 500
#     rain.append([x, y])


# def rainning():

#     glColor3f(0.0, 0.0, 1.0)  

#     glLineWidth(1)
    
#     glBegin(GL_LINES)


#     for drop in rain:
#         glVertex2f(drop[0], drop[1])

#         glVertex2f(drop[0] - rain_direct * 2, drop[1] - 10)
#     glEnd()


# def rain_add():
#     global rain_direct

#     for drop in rain:
#         drop[1] -= 5 

#         drop[0] += rain_direct  

#         if drop[1] < 0 or drop[0] < 0 or drop[0] > 500:

#             rain.remove(drop)


# def key_board(key, x, y):
#     global rain_direct

#     if key == GLUT_KEY_LEFT:
#         rain_direct -= 0.5 
        
#     elif key == GLUT_KEY_RIGHT:
#         rain_direct += 0.5  


# def keyboard_data(key, x, y):
#     global background_colur, house_colr
#     if key == b' ':


#         if background_colur == [1.0, 1.0, 1.0]:
#             background_colur = [0.0, 0.0, 0.0]  
#             house_colr = [1.0, 1.0, 1.0]
#         else:

#             background_colur = [1.0, 1.0, 1.0] 
#             house_colr = [0.0, 0.0, 0.0]
#     elif key == b'd': 

#         background_colur = [min(1.0, background_colur[0] + day_night)] * 3
#         house_colr = [max(0.0, house_colr[0] - day_night)] * 3

#     elif key == b'n':  


#         background_colur = [max(0.0, background_colur[0] - day_night)] * 3
#         house_colr = [min(1.0, house_colr[0] + day_night)] * 3


# def projction():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


# def display_setup():

#     glClearColor(background_colur[0], background_colur[1], background_colur[2], 1.0)

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#     glLoadIdentity()
#     projction()
#     tree()
#     my_house()
#     rainning()
#     glutSwapBuffers()


# def rander_time(v):
#     rain_drop()
#     rain_add()
#     glutPostRedisplay()
#     glutTimerFunc(50, rander_time, 0)


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)

# glutCreateWindow(b"Proloy Home :) ")
# glutDisplayFunc(display_setup)

# glutTimerFunc(50, rander_time, 0)
# glutKeyboardFunc(keyboard_data)

# glutSpecialFunc(key_board)
# glutMainLoop()





########################################################################################################
#task 2

########################################################################################################
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

points = []
speed = 1.0
move_flag = True  

def new_point(x, y):
    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    direction = random.choice(directions)
    color = [random.random(), random.random(), random.random()]  
    points.append([x, y, direction[0], direction[1], color, False, time.time()])

def point_movement():
    global speed, move_flag
    if move_flag:  
        for point in points:
            point[0] += point[2] * speed
            point[1] += point[3] * speed
            if point[0] < 0 or point[0] > 500:
                point[2] *= -1
            if point[1] < 0 or point[1] > 500:
                point[3] *= -1
            if point[5]:  
                current_time = time.time()
                if current_time - point[6] >= 1:
                    point[4] = [1.0, 0.0, 0.0] if point[4] == [0.0, 0.0, 0.0] else [0.0, 0.0, 0.0]
                    point[6] = current_time

def point_draw():
    glPointSize(5)
    glBegin(GL_POINTS)
    for point in points:
        glColor3f(point[4][0], point[4][1], point[4][2])
        glVertex2f(point[0], point[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    point_movement()
    point_draw()
    glutSwapBuffers()

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x_gl = x
        y_gl = 500 - y
        for point in points:
            if abs(point[0] - x_gl) < 10 and abs(point[1] - y_gl) < 10:
                point[5] = True
                point[6] = time.time()
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_point(x, y)

def key(key, x, y):
    global speed
    if key == GLUT_KEY_UP:
        speed += 0.1
    elif key == GLUT_KEY_DOWN:
        speed = max(0.1, speed - 0.1)

def keyboard_data(key, x, y):
    global move_flag
    if key == b' ':  
        move_flag = not move_flag 

def code_run():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Blinking Box")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    glutSpecialFunc(key)
    glutKeyboardFunc(keyboard_data)  
    glutIdleFunc(display)
    glutMainLoop()

code_run()
