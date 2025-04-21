from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random

GRID_SIZE = 20
TILE_SIZE = 40
fovY = 120

my_player = [0, 0, 0]
plyr_angl = 0
cam_x = 0
cam_y = 30
cam_mode = "third_person"

cheat_mode = False
auto_gan = False
cheat_angl_stp = 2
fire_dealy = 0
bullets = []
enemies = []

life_line = 5
score = 0
miss_fire = 0
speed_enemy = 0.5
game_over = False

def emeny_start():
    global enemies
    enemies = []
    for _ in range(5):
        x = random.randint(-GRID_SIZE * TILE_SIZE//2, GRID_SIZE * TILE_SIZE//2)
        z = random.randint(200, GRID_SIZE * TILE_SIZE)
        enemies.append({'x': x, 'z': z, 'size': 20, 'expand': True})

def text_add(x, y, text, color=(1, 1, 1), font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(*color)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def make_player():
    glPushMatrix()
    glTranslatef(*my_player)
    glRotatef(-plyr_angl, 0, 1, 0)
    glColor3f(0.2, 0.6, 0.2)
    glPushMatrix()
    glTranslatef(0, 40, 0)
    glScalef(1, 2, 0.5)
    glutSolidCube(40)
    glPopMatrix()
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslatef(0, 90, 0)
    glutSolidSphere(15, 20, 20)
    glPopMatrix()
    for offset in [-10, 10]:
        glColor3f(0.1, 0.1, 0.9)
        glPushMatrix()
        glTranslatef(offset, 0, 10)
        glRotatef(20, 1, 0, 0)
        glScalef(0.3, 1.5, 0.3)
        glutSolidCube(40)
        glPopMatrix()
    for side in [-1, 1]:
        glColor3f(1, 0.8, 0.6)
        glPushMatrix()
        glTranslatef(25 * side, 65, 0)
        glRotatef(-90 * side, 0, 0, 1)
        gluCylinder(gluNewQuadric(), 5, 5, 25, 20, 20)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(50 * side, 65, 0)
        glutSolidSphere(6, 20, 20)
        glPopMatrix()
    glColor3f(0.5, 0.5, 0.5)
    glPushMatrix()
    glTranslatef(0, 75, 20)
    gluCylinder(gluNewQuadric(), 3, 3, 30, 10, 10)
    glPopMatrix()
    glPopMatrix()

def make_bullet():
    global bullets, enemies, score, miss_fire
    if game_over:
        return
    speed = 30
    hit_radius = 25
    new_bullet = []
    for b in bullets:
        b['x'] += speed * math.sin(math.radians(b['angle']))
        b['z'] += speed * math.cos(math.radians(b['angle']))
        hit = False
        for e in enemies:
            dx = b['x'] - e['x']
            dz = b['z'] - e['z']
            dist = math.sqrt(dx*dx + dz*dz)
            if dist < hit_radius:
                e['x'] = random.randint(-GRID_SIZE*TILE_SIZE//2, GRID_SIZE*TILE_SIZE//2)
                e['z'] = random.randint(200, GRID_SIZE*TILE_SIZE)
                score += 1
                hit = True
                break
        if not hit and abs(b['x']) <= GRID_SIZE*TILE_SIZE and abs(b['z']) <= GRID_SIZE*TILE_SIZE:
            new_bullet.append(b)
        elif not hit:
            miss_fire += 1
        if not hit:
            glPushMatrix()
            glTranslatef(b['x'], 20, b['z'])
            glColor3f(1, 0, 0)
            glScalef(1.5, 1.5, 1.5)
            glutSolidCube(10)
            glPopMatrix()
    bullets = new_bullet

def make_enemy():
    global life_line, game_over
    if game_over:
        return
    for e in enemies:
        if e['expand']:
            e['size'] += 0.3
            if e['size'] > 25: e['expand'] = False
        else:
            e['size'] -= 0.3
            if e['size'] < 15: e['expand'] = True
        dx = my_player[0] - e['x']
        dz = my_player[2] - e['z']
        dist = math.sqrt(dx**2 + dz**2)
        if dist > 2:
            e['x'] += speed_enemy * dx / dist
            e['z'] += speed_enemy * dz / dist
        if dist < 40:
            life_line -= 1
            e['x'] = random.randint(-GRID_SIZE*TILE_SIZE//2, GRID_SIZE*TILE_SIZE//2)
            e['z'] = random.randint(200, GRID_SIZE*TILE_SIZE)
        glPushMatrix()
        glTranslatef(e['x'], 20, e['z'])
        glColor3f(1, 0, 0)
        glutSolidSphere(e['size'], 20, 20)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(e['x'], 20 + e['size'] + 10, e['z'])
        glColor3f(0, 0, 0)
        glutSolidSphere(e['size'] / 2.5, 20, 20)
        glPopMatrix()

def make_grid():
    for i in range(-GRID_SIZE, GRID_SIZE):
        for j in range(-GRID_SIZE, GRID_SIZE):
            glColor3f(0.9, 0.85, 1.0) if (i + j) % 2 == 0 else glColor3f(1, 1, 1)
            x = i * TILE_SIZE
            z = j * TILE_SIZE
            glBegin(GL_QUADS)
            glVertex3f(x, 0, z)
            glVertex3f(x + TILE_SIZE, 0, z)
            glVertex3f(x + TILE_SIZE, 0, z + TILE_SIZE)
            glVertex3f(x, 0, z + TILE_SIZE)
            glEnd()

def walls_added():
    colors = [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 1)]
    positions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i, (wx, wz) in enumerate(positions):
        glColor3f(*colors[i])
        if wx:
            x = wx * GRID_SIZE * TILE_SIZE
            glBegin(GL_QUADS)
            glVertex3f(x, 0, -GRID_SIZE * TILE_SIZE)
            glVertex3f(x, 0, GRID_SIZE * TILE_SIZE)
            glVertex3f(x, 100, GRID_SIZE * TILE_SIZE)
            glVertex3f(x, 100, -GRID_SIZE * TILE_SIZE)
            glEnd()
        else:
            z = wz * GRID_SIZE * TILE_SIZE
            glBegin(GL_QUADS)
            glVertex3f(-GRID_SIZE * TILE_SIZE, 0, z)
            glVertex3f(GRID_SIZE * TILE_SIZE, 0, z)
            glVertex3f(GRID_SIZE * TILE_SIZE, 100, z)
            glVertex3f(-GRID_SIZE * TILE_SIZE, 100, z)
            glEnd()

def camera_setup():
    global cam_x, cam_y
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 2000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    px, py, pz = my_player
    rad = math.radians(plyr_angl)
    if cam_mode == "first_person":
        view_x = px
        view_y = py + 75
        view_z = pz
        target_x = px + 100 * math.sin(rad)
        target_y = view_y
        target_z = pz + 100 * math.cos(rad)
        gluLookAt(view_x, view_y, view_z, target_x, target_y, target_z, 0, 1, 0)
    else:
        cam_radius = 800
        view_x = cam_radius * math.sin(math.radians(cam_x)) * math.cos(math.radians(cam_y))
        view_y = cam_radius * math.sin(math.radians(cam_y))
        view_z = cam_radius * math.cos(math.radians(cam_x)) * math.cos(math.radians(cam_y))
        gluLookAt(view_x, view_y, view_z, 0, 0, 0, 0, 1, 0)

def show_screen():
    global game_over
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera_setup()
    make_grid()
    walls_added()
    make_enemy()
    make_player()
    make_bullet()
    if life_line <= 0 or miss_fire >= 10:
        game_over = True
        text_add(300, 420, "GAME OVER", (1, 0.4, 0))
        text_add(270, 340, "Press R to Restart", (1, 1, 0.5))
    text_add(10, 770, f"Player Life Remaining: {life_line}")
    text_add(10, 740, f"Game Score: {score}")
    text_add(10, 710, f"Bullet Missed: {miss_fire}")
    glutSwapBuffers()

def keyboard_data(key, x, y):
    global my_player, plyr_angl, cheat_mode, auto_gan
    global life_line, score, miss_fire, game_over
    if game_over and key == b'r':
        my_player[:] = [0, 0, 0]
        plyr_angl = 0
        life_line = 5
        score = 0
        miss_fire = 0
        emeny_start()
        game_over = False
        return
    if game_over:
        return
    step = 20
    rad = math.radians(plyr_angl)
    right_rad = math.radians(plyr_angl + 90)
    if key == b'w':
        my_player[0] += step * math.sin(rad)
        my_player[2] += step * math.cos(rad)
    elif key == b's':
        my_player[0] -= step * math.sin(rad)
        my_player[2] -= step * math.cos(rad)
    elif key == b'd':
        my_player[0] += step * math.sin(right_rad)
        my_player[2] += step * math.cos(right_rad)
    elif key == b'a':
        my_player[0] -= step * math.sin(right_rad)
        my_player[2] -= step * math.cos(right_rad)
    elif key == b'c':
        cheat_mode = not cheat_mode
    elif key == b'v':
        auto_gan = not auto_gan

def special_key_data(key, x, y):
    global cam_x, cam_y
    if key == GLUT_KEY_LEFT: cam_x -= 5
    elif key == GLUT_KEY_RIGHT: cam_x += 5
    elif key == GLUT_KEY_UP: cam_y += 5
    elif key == GLUT_KEY_DOWN: cam_y -= 5

def mouse_data(button, state, x, y):
    global bullets, cam_mode
    if game_over:
        return
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        px, _, pz = my_player
        rad = math.radians(plyr_angl)
        bx = px + 40 * math.sin(rad)
        bz = pz + 40 * math.cos(rad)
        bullets.append({'x': bx, 'z': bz, 'angle': plyr_angl})
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        cam_mode = "first_person" if cam_mode == "third_person" else "third_person"

def idle_state():
    global plyr_angl, cheat_mode, fire_dealy
    if cheat_mode and not game_over:
        plyr_angl = (plyr_angl + cheat_angl_stp) % 360
        fire_dealy += 1
        if fire_dealy >= 10:
            fire_dealy = 0
            px, _, pz = my_player
            rad = math.radians(plyr_angl)
            bx = px + 40 * math.sin(rad)
            bz = pz + 40 * math.cos(rad)
            bullets.append({'x': bx, 'z': bz, 'angle': plyr_angl})
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"Bullet Frenzy ")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    emeny_start()
    glutDisplayFunc(show_screen)
    glutIdleFunc(idle_state)
    glutKeyboardFunc(keyboard_data)
    glutSpecialFunc(special_key_data)
    glutMouseFunc(mouse_data)
    glutMainLoop()

if __name__ == "__main__":
    main()
