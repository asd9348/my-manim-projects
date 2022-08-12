from core.base import Base
from core.openGLUtils import OpenGLUtils

from OpenGL import GL


class Test(Base):
    def initialize(self):
        print('init...')

        # vertex shader code
        vsCode = """
        void main()
        {
            gl_Position=vec4(0.0,0.0,0.0,1.0);
        }
        """
        fsCode = """
        void main()
        {
            gl_FragColor=vec4(1.0, 1.0,0.0,1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        GL.glPointSize(16)


    def update(self):
        GL.glUseProgram(self.programRef)

        GL.glDrawArrays(GL.GL_POINTS, 0,1)


# create an instance of this class

Test().run()
