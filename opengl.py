from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def desenhar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 1.0)  
    glVertex2f(-0.5, -0.5)

    glColor3f(0.0, 0.0, 0.0)  
    glVertex2f(0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)  # azul
    glVertex2f(0.0, 0.5)
    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Triangulo OpenGL")

    glutDisplayFunc(desenhar)
    glutIdleFunc(desenhar)

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutMainLoop()

if __name__ == "__main__":
    main()