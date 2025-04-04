#Task 1
########################################################################################################
import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rain = []
rain_direct = 0 
background_colur = [1.0, 1.0, 1.0]  
house_colr = [0.0, 0.0, 0.0]  
day_night = 0.02  


def my_house():
    glColor3f(house_colr[0], house_colr[1], house_colr[2])
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(100, 200)
    glVertex2f(300, 200)

    glVertex2f(300, 200)
    glVertex2f(300, 100)

    glVertex2f(300, 100)
    glVertex2f(100, 100)
    glVertex2f(100, 100)

    glVertex2f(100, 200)

    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 200)
    glVertex2f(200, 320)
    glVertex2f(300, 200)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(170, 100)
    glVertex2f(170, 150)

    glVertex2f(170, 150)
    glVertex2f(230, 150)
    glVertex2f(230, 150)
    glVertex2f(230, 100)
    glVertex2f(230, 100)
    glVertex2f(170, 100)
    glEnd()

    glBegin(GL_LINES)

    glVertex2f(120, 160)
    glVertex2f(160, 160)
    glVertex2f(160, 160)
    glVertex2f(160, 120)

    glVertex2f(160, 120)
    glVertex2f(120, 120)
    glVertex2f(120, 120)
    glVertex2f(120, 160)

    glVertex2f(140, 160)
    glVertex2f(140, 120)
    glVertex2f(120, 140)
    glVertex2f(160, 140)
    glEnd()

def tree():
    glColor3f(0.4, 0.2, 0.0)
    glBegin(GL_LINES)
    glVertex2f(350, 100)
    glVertex2f(350, 180)
    glEnd()
    glColor3f(0.0, 0.5, 0.0)

    glBegin(GL_TRIANGLES)
    glVertex2f(320, 180)
    glVertex2f(350, 250)
    glVertex2f(380, 180)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(320, 250)
    glVertex2f(350, 320)
    glVertex2f(380, 250)
    glEnd()



def rain_drop():
    x = random.randint(50, 450)

    y = 500
    rain.append([x, y])


def rainning():

    glColor3f(0.0, 0.0, 1.0)  

    glLineWidth(1)
    
    glBegin(GL_LINES)


    for drop in rain:
        glVertex2f(drop[0], drop[1])

        glVertex2f(drop[0] - rain_direct * 2, drop[1] - 10)
    glEnd()


def rain_add():
    global rain_direct

    for drop in rain:
        drop[1] -= 5 

        drop[0] += rain_direct  

        if drop[1] < 0 or drop[0] < 0 or drop[0] > 500:

            rain.remove(drop)


def key_board(key, x, y):
    global rain_direct

    if key == GLUT_KEY_LEFT:
        rain_direct -= 0.5 
        
    elif key == GLUT_KEY_RIGHT:
        rain_direct += 0.5  


def keybod(key, x, y):
    global background_colur, house_colr
    if key == b' ':


        if background_colur == [1.0, 1.0, 1.0]:
            background_colur = [0.0, 0.0, 0.0]  
            house_colr = [1.0, 1.0, 1.0]
        else:

            background_colur = [1.0, 1.0, 1.0] 
            house_colr = [0.0, 0.0, 0.0]
    elif key == b'd': 

        background_colur = [min(1.0, background_colur[0] + day_night)] * 3
        house_colr = [max(0.0, house_colr[0] - day_night)] * 3

    elif key == b'n':  


        background_colur = [max(0.0, background_colur[0] - day_night)] * 3
        house_colr = [min(1.0, house_colr[0] + day_night)] * 3


def projction():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display_setup():

    glClearColor(background_colur[0], background_colur[1], background_colur[2], 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    projction()
    tree()
    my_house()
    rainning()
    glutSwapBuffers()


def rander_time(v):
    rain_drop()
    rain_add()
    glutPostRedisplay()
    glutTimerFunc(50, rander_time, 0)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)

glutCreateWindow(b"Proloy Home :) ")
glutDisplayFunc(display_setup)

glutTimerFunc(50, rander_time, 0)
glutKeyboardFunc(keybod)

glutSpecialFunc(key_board)
glutMainLoop()




########################################################################################################
#task 2

########################################################################################################
# import random
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import time

# dots = []

# speed = 1.0

# flag = True  

# def dots_add(x, y):

#     directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]

#     direction = random.choice(directions)

#     color = [random.random(), random.random(), random.random()]  

#     dots.append([x, y, direction[0], direction[1], color, False, time.time()])

# def dot_motion():
#     global speed, flag
#     if flag:  
#         for i in dots:
#             i[0] += i[2] * speed

#             i[1] += i[3] * speed

#             if i[0] < 0 or i[0] > 500:
#                 i[2] *= -1

#             if i[1] < 0 or i[1] > 500:
#                 i[3] *= -1
#             if i[5]:  
#                 current_time = time.time()
#                 if current_time - i[6] >= 1:

#                     i[4] = [1.0, 0.0, 0.0] if i[4] == [0.0, 0.0, 0.0] else [0.0, 0.0, 0.0]

#                     i[6] = current_time

# def dots_drow():

#     glPointSize(5)
#     glBegin(GL_POINTS)

#     for i in dots:

#         glColor3f(i[4][0], i[4][1], i[4][2])

#         glVertex2f(i[0], i[1])
#     glEnd()

# def dots_display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glViewport(0, 0, 500, 500)

#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
    
#     dot_motion()
#     dots_drow()
#     glutSwapBuffers()

# def click_mouse(button, state, x, y):
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

#         x_gl = x
#         y_gl = 500 - y

#         for i in dots:
#             if abs(i[0] - x_gl) < 10 and abs(i[1] - y_gl) < 10:
#                 i[5] = True  
#                 i[6] = time.time() 
#                 return  
#     elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         dots_add(x, y)
#         print(f"Dot Region : ({x}, {y})") 

# def input_data(key, x, y):
#     global speed
#     if key == GLUT_KEY_UP:
#         speed += 0.1
#         print(f"Speed up:  {speed}")  
#     elif key == GLUT_KEY_DOWN:
#         speed = max(0.1, speed - 0.1)
#         print(f"Speed down : {speed}")  

# def keybod(key, x, y):
#     global flag
#     if key == b' ':  
#         flag = not flag
#         state = "freeze" if not flag else "unfreeze"
#         print(f"Status :  {state}.") 
# def code_run():
#     glutInit()
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(0, 0) 

#     glutCreateWindow(b"Amazing Box")
    
#     glutDisplayFunc(dots_display)

#     glutMouseFunc(click_mouse)

#     glutSpecialFunc(input_data)

#     glutKeyboardFunc(keybod)  
#     glutIdleFunc(dots_display)
    
#     glutMainLoop()

# code_run()
