#ifndef OGLWIDGETS_OGLCOMMON_H
#define OGLWIDGETS_OGLCOMMON_H

#ifdef __ANDROID__
    #include <GLES2/gl2.h>
    #include <GLES2/gl2ext.h>
#elif WIN32
    #include <windows.h>
    #include <GL/gl.h>
    #include <gl/glext.h>
    #include <GL/glu.h>
#elif __APPLE__
    #include <stdint.h>
    #include <OpenGL/gl.h>
    #include <OpenGL/glu.h>
#else
    #include <GL/gl.h>
#endif

#include <stdio.h>

#include <GL/oglCommon.h>
#include <string.h>

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''

class oglWidgets:
    @staticmethod
    def glSetMatrix(self, matmode, data = 0 ):
        glMatrixMode( matmode )
        glLoadIdentity()
        if data != 0:
            glMultMatrixf( data )

    @staticmethod
    def glDrawQuad(self):
        glColor3f( 1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0);    glVertex3f(-1, -1, 0 );
        glTexCoord2f(0, 1);    glVertex3f(-1,  1, 0 );
        glTexCoord2f(1, 1);    glVertex3f( 1,  1, 0 );
        glTexCoord2f(1, 0);    glVertex3f( 1, -1, 0 );
        glEnd()

    @staticmethod
    def glErrorString( errCode ):
        if errCode == GL_INVALID_ENUM:        return "GL_INVALID_ENUM"
        if errCode == GL_INVALID_VALUE:       return "GL_INVALID_VALUE"
        if errCode == GL_INVALID_OPERATION:   return "GL_INVALID_OPERATION"
        if errCode == GL_OUT_OF_MEMORY:       return "GL_OUT_OF_MEMORY"
        if errCode == GL_STACK_OVERFLOW:      return "GL_STACK_OVERFLOW"
        if errCode == GL_STACK_UNDERFLOW:     return "GL_STACK_UNDERFLOW"
        return ""

    @staticmethod
    def glExtensionSupported(extName):
        return glGetString( GL_EXTENSIONS,extName) != 0 

    @staticmethod
    def glGetInteger(pname):
        return glGetIntegerv(pname)
        
    @staticmethod
    def checkGlError(op) :
        None
        '''
        do:
            #printf("after %s glError -- %s (0x%x)\n", op, glErrorString(error), error);
            None
        while error = glGetError():
        '''
        