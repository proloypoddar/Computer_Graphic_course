# # ######## Task 1########
# # # part 1

# from OpenGL.GL import *

# from OpenGL.GLUT import *

# from OpenGL.GLU import *


# def draw_house():
#     glColor3f(1.0, 1.0, 1.0)
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

#     glVertex2f(200, 300)
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


# def inetial_cheak():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()

#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     inetial_cheak()
#     draw_house()

#     glutSwapBuffers()


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)

# glutInitWindowSize(500, 500)

# glutInitWindowPosition(0, 0)

# glutCreateWindow(b"MY HOUSE")

# glutDisplayFunc(display)

# glutMainLoop()


# # part 2
# import random
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# rain = []
# rain_dt = 0  


# def draw_house():
#     glColor3f(1.0, 1.0, 1.0)
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
#     glVertex2f(200, 300)
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


# def generate_i():
#     x = random.randint(50, 450)
#     y = 500
#     rain.append([x, y])


# def draw_rain():
#     glColor3f(0.0, 0.0, 1.0)
#     glPointSize(3)
#     glBegin(GL_POINTS)
#     for i in rain:
#         glVertex2f(i[0], i[1])
#     glEnd()


# def raining():
#     global rain_dt
#     for i in rain:
#         i[1] -= 2  
        
#         i[0] += rain_dt

        
#         if i[1] < 0 or i[0] < 0 or i[0] > 500:
#             rain.remove_flag(i)


# def press_key(key, x, y):
#     global rain_dt
#     if key == b'\x1b':
#         sys.exit()


# def key_val(key, x, y):
#     global rain_dt
#     if key == GLUT_KEY_LEFT:
#         rain_dt -= 1 
#     elif key == GLUT_KEY_RIGHT:
#         rain_dt += 1  


# def inetial_cheak():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     inetial_cheak()
#     draw_house()
#     draw_rain()
#     glutSwapBuffers()


# def timer(v):
#     generate_i()
#     raining()
#     glutPostRedisplay()
#     glutTimerFunc(50, timer, 0)


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# glutCreateWindow(b"MY HOUSE RAIN")
# glutDisplayFunc(display)
# glutTimerFunc(50, timer, 0)
# glutKeyboardFunc(press_key)
# glutSpecialFunc(key_val)
# glutMainLoop()

# # # Part 3
# import random
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import math

# rain = []
# rain_dt = 0
# bg_colour = [1.0, 1.0, 1.0]
# house = [0.0, 0.0, 0.0]
# color_step = 0.01

# def draw_house():
#     glColor3f(house[0], house[1], house[2])
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
#     glVertex2f(200, 300)
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


# def generate_i():
#     x = random.randint(50, 450)
#     y = 500
#     rain.append([x, y])


# def draw_rain():
#     glColor3f(0.0, 0.0, 1.0)
#     glPointSize(3)
#     glBegin(GL_POINTS)
#     for i in rain:
#         glVertex2f(i[0], i[1])
#     glEnd()


# def raining():
#     global rain_dt
#     for i in rain:
#         i[1] -= 2
#         i[0] += rain_dt

#         if i[1] < 0 or i[0] < 0 or i[0] > 500:
#             rain.remove_flag(i)


# def press_key(key, x, y):
#     global rain_dt
#     if key == b'\x1b':
#         sys.exit()


# def key_val(key, x, y):
#     global rain_dt, bg_colour, house
#     if key == GLUT_KEY_LEFT:
#         rain_dt -= 1
#     elif key == GLUT_KEY_RIGHT:
#         rain_dt += 1


# def space_key(key, x, y):
#     global bg_colour, house
#     if key == b' ':
#         if bg_colour == [1.0, 1.0, 1.0]:
#             bg_colour = [0.0, 0.0, 0.0]
#             house = [1.0, 1.0, 1.0]
#         else:
#             bg_colour = [1.0, 1.0, 1.0]
#             house = [0.0, 0.0, 0.0]


# def inetial_cheak():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()

#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


# def display():

#     glClearColor(bg_colour[0], bg_colour[1], bg_colour[2], 1.0)

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()

#     inetial_cheak()
#     draw_house()
#     draw_rain()
#     glutSwapBuffers()


# def timer(v):
#     generate_i()
#     raining()

#     glutPostRedisplay()

#     glutTimerFunc(50, timer, 0)


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)

# glutInitWindowPosition(0, 0)


# glutCreateWindow(b"MY HOUSE IN DAY NIGHT")

# glutDisplayFunc(display)

# glutTimerFunc(50, timer, 0)
# glutKeyboardFunc(press_key)

# glutSpecialFunc(key_val)

# glutKeyboardUpFunc(space_key)
# glutMainLoop()






################### Task 2 ###################


# Part 1

import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

points = []

def new_point(x, y):
    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    direction = random.choice(directions)
    color = [random.random(), random.random(), random.random()]
    points.append([x, y, direction[0], direction[1], color])

def point_movement ():
    for point in points:
        point[0] += point[2]
        point[1] += point[3]
        if point[0] < 0 or point[0] > 500:
            point[2] *= -1
        if point[1] < 0 or point[1] > 500:
            point[3] *= -1

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
    point_movement ()
    point_draw()
    glutSwapBuffers()

def right_click(button, state, x, y):

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_point(x, y)

def code_run():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Amazing Box")
    glutDisplayFunc(display)
    glutMouseFunc(right_click)
    glutMainLoop()

code_run()

######
# Part 2
# import random
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# points = []

# speed = 1.0

# def new_point(x, y):
#     directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
#     direction = random.choice(directions)
#     color = [random.random(), random.random(), random.random()]
#     points.append([x, y, direction[0], direction[1], color])

# def point_movement ():
#     global speed
#     for point in points:
#         point[0] += point[2] * speed
#         point[1] += point[3] * speed
        
#         if point[0] < 0 or point[0] > 500:
#             point[2] *= -1
#         if point[1] < 0 or point[1] > 500:
#             point[3] *= -1

# def point_draw():
#     glPointSize(5)
#     glBegin(GL_POINTS)
#     for point in points:
#         glColor3f(point[4][0], point[4][1], point[4][2])
#         glVertex2f(point[0], point[1])
#     glEnd()

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     point_movement ()
#     point_draw()
#     glutSwapBuffers()

# def right_click(button, state, x, y):
#     if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         new_point(x, y)

# def key(key, x, y):
#     global speed
#     if key == GLUT_KEY_UP:
#         speed += 0.1
#     elif key == GLUT_KEY_DOWN:
#         speed = max(0.1, speed - 0.1)

# def code_run():
#     glutInit()
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(0, 0)
#     glutCreateWindow(b"Amazing Box with Speed Control")
#     glutDisplayFunc(display)
#     glutMouseFunc(right_click)
#     glutSpecialFunc(key)
#     glutIdleFunc(display)  
#     glutMainLoop()

# code_run()







# # Part 3
# import random
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import time

# points = []
# speed = 1.0

# def new_point(x, y):
#     directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
#     direction = random.choice(directions)
#     color = [1.0, 0.0, 0.0]  # Initially red color
#     points.append([x, y, direction[0], direction[1], color, False, time.time()])

# def point_movement ():
#     global speed
#     for point in points:
#         point[0] += point[2] * speed
#         point[1] += point[3] * speed
        
#         if point[0] < 0 or point[0] > 500:
#             point[2] *= -1
#         if point[1] < 0 or point[1] > 500:
#             point[3] *= -1
        

#         if point[5]:  
#             current_time = time.time()
#             if current_time - point[6] >= 1:
#                 point[4] = [1.0, 0.0, 0.0] if point[4] == [0.0, 0.0, 0.0] else [0.0, 0.0, 0.0]
#                 point[6] = current_time  

# def point_draw():
#     glPointSize(5)
#     glBegin(GL_POINTS)
#     for point in points:

#         glColor3f(point[4][0], point[4][1], point[4][2])

#         glVertex2f(point[0], point[1])
#     glEnd()

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glViewport(0, 0, 500, 500)

#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()

#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     point_movement ()
#     point_draw()
#     glutSwapBuffers()

# def left_click(button, state, x, y):
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

#         x_gl = x
#         y_gl = 500 - y
       
#         for point in points:
            
#             if abs(point[0] - x_gl) < 10 and abs(point[1] - y_gl) < 10:

#                 point[5] = True  

#                 point[6] = time.time() 

# def right_click(button, state, x, y):

#     if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         new_point(x, y)

# def key(key, x, y):
#     global speed
#     if key == GLUT_KEY_UP:
#         speed += 0.1

#     elif key == GLUT_KEY_DOWN:

#         speed = max(0.1, speed - 0.1)

# def code_run():

#     glutInit()
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(0, 0)

#     glutCreateWindow(b"Amazing Blinking Box")

#     glutDisplayFunc(display)
#     glutMouseFunc(left_click) 

#     glutMouseFunc(right_click)  

#     glutSpecialFunc(key)
#     glutIdleFunc(display)
#     glutMainLoop()

# code_run()


# Part 4

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

def point_movement ():
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
    point_movement ()
    point_draw()
    glutSwapBuffers()

def left_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x_gl = x
        y_gl = 500 - y
       
        for point in points:
            if abs(point[0] - x_gl) < 10 and abs(point[1] - y_gl) < 10:

                point[5] = True 
                
                point[6] = time.time() 

def right_click(button, state, x, y):
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
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
    
    glutMouseFunc(left_click) 

    glutMouseFunc(right_click)  

    glutSpecialFunc(key)

    glutKeyboardFunc(keyboard_data)  
    
    glutIdleFunc(display)
    glutMainLoop()

code_run()
