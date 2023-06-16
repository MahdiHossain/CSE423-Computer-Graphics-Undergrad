from OpenGL.GL import *
from OpenGL.GLUT import *


def student_id():
    glBegin(GL_LINES)
    # Two
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(50, 275)
    glVertex2f(80, 275)
    glVertex2f(80, 275)
    glVertex2f(80, 250)
    glVertex2f(80, 250)
    glVertex2f(50, 250)
    glVertex2f(50, 250)
    glVertex2f(50, 225)
    glVertex2f(50, 225)
    glVertex2f(80, 225)

    # Zero
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(100, 275)
    glVertex2f(130, 275)
    glVertex2f(130, 275)
    glVertex2f(130, 225)
    glVertex2f(130, 225)
    glVertex2f(100, 225)
    glVertex2f(100, 225)
    glVertex2f(100, 275)

    # Three
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(150, 275)
    glVertex2f(180, 275)
    glVertex2f(180, 275)
    glVertex2f(180, 225)
    glVertex2f(180, 250)
    glVertex2f(150, 250)
    glVertex2f(180, 225)
    glVertex2f(150, 225)

    # Zero
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(200, 275)
    glVertex2f(230, 275)
    glVertex2f(230, 275)
    glVertex2f(230, 225)
    glVertex2f(230, 225)
    glVertex2f(200, 225)
    glVertex2f(200, 225)
    glVertex2f(200, 275)

    # One
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(250, 260)
    glVertex2f(270, 275)
    glVertex2f(270, 275)
    glVertex2f(270, 225)
    glVertex2f(250, 225)
    glVertex2f(290, 225)

    # One
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(300, 260)
    glVertex2f(320, 275)
    glVertex2f(320, 275)
    glVertex2f(320, 225)
    glVertex2f(300, 225)
    glVertex2f(340, 225)

    # Nine
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(360, 275)
    glVertex2f(390, 275)
    glVertex2f(390, 275)
    glVertex2f(390, 225)
    glVertex2f(390, 250)
    glVertex2f(360, 250)
    glVertex2f(360, 250)
    glVertex2f(360, 275)
    glVertex2f(390, 225)
    glVertex2f(360, 225)

    # Four
    glColor3f(0.10, 0.20, 0.5)
    glVertex2f(410, 275)
    glVertex2f(410, 250)
    glVertex2f(410, 250)
    glVertex2f(440, 250)
    glVertex2f(440, 275)
    glVertex2f(440, 225)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    student_id()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(900, 0)
wind = glutCreateWindow(b"Lab Assignment 1: Student ID in Different Colors")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
