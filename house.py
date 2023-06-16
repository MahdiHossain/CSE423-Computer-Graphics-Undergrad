from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_house():
    glBegin(GL_LINES)

    # Base
    glVertex2f(100, 275)
    glVertex2f(100, 10)
    glVertex2f(380, 10)
    glVertex2f(380, 275)
    glVertex2f(100, 10)
    glVertex2f(380, 10)

    # Roof
    glVertex2f(100, 275)
    glVertex2f(380, 275)
    glVertex2f(240, 450)
    glVertex2f(380, 275)
    glVertex2f(240, 450)
    glVertex2f(100, 275)

    # Windowleft
    glVertex2f(120, 220)
    glVertex2f(200, 220)
    glVertex2f(200, 220)
    glVertex2f(200, 170)
    glVertex2f(200, 170)
    glVertex2f(120, 170)
    glVertex2f(120, 170)
    glVertex2f(120, 220)

    # WindowRight
    glVertex2f(350, 220)
    glVertex2f(270, 220)
    glVertex2f(270, 220)
    glVertex2f(270, 170)
    glVertex2f(270, 170)
    glVertex2f(350, 170)
    glVertex2f(350, 170)
    glVertex2f(350, 220)

    # Door
    glVertex2f(210, 10)
    glVertex2f(210, 100)
    glVertex2f(210, 100)
    glVertex2f(260, 100)
    glVertex2f(260, 100)
    glVertex2f(260, 10)

    # Knob
    # glPointSize(2)

    glEnd()


def door_knob():
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(250, 45)
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
    glColor3f(1.0, 1.0, 1.0)
    draw_house()
    door_knob()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(900, 0)
wind = glutCreateWindow(b"Lab Assignment 1: House Drawing Task")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
