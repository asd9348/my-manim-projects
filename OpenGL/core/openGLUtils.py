from OpenGL import GL



#static methods to load/compile OpenGL shaders and link to create GPU programs

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        #specify IpenGL ver and requirements
        extension = '#extension GL_ARB_shading_language_420pack: require \n'
        shaderCode = '#version 130 \n' + extension + shaderCode

        # create empty shader obj and return ref val

        shaderRef = GL.glCreateShader(shaderType)

        GL.glShaderSource(shaderRef,shaderCode)

        GL.glCompileShader(shaderRef)

        compileSuccess = GL.glGetShaderiv(shaderRef,GL.GL_COMPILE_STATUS)

        if not compileSuccess:
            error_msg = GL.glGetShaderInfoLog(shaderRef)

            GL.glDeleteShader(shaderRef)

            error_msg = "\n" + error_msg.decode('utf-8')

            raise Exception(error_msg)


        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL.GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL.GL_FRAGMENT_SHADER)

        programRef= GL.glCreateProgram()
        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)

        GL.glLinkProgram(programRef)

        linkSuccess= GL.glGetProgramiv(programRef, GL.GL_LINK_STATUS)

        if not linkSuccess:
            error_msg = GL.glGetProgramInfoLog(programRef)

            GL.glDeleteProgram(programRef)

            error_msg = "\n" + error_msg.decode('utf-8')

            raise Exception(error_msg)

        return programRef






