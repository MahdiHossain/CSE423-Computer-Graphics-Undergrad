from OpenGL.GL import *
from OpenGL.GLUT import *
import random

xcor = []
ycor = []


def pixel_generator(x):
    for i in range(x):
        xcor.append(random.randint(0, 500))
    for j in range(x):
        ycor.append(random.randint(0, 500))


def draw_points(x):
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(x):
        glVertex2f(xcor[i], ycor[i])
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
    glColor3f(1.0, 0.0, 0.0)
    pixel_generator(50)
    draw_points(50)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(900, 0)
wind = glutCreateWindow(b"Lab Assignment 1: Randomly Generated Pixels")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
