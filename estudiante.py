
class Estudiante:
    def __init__(self, nombre , apellido , edad, curso ,  id = 0):
        self.__id = id 
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__curso = curso
        self.__habilitado = "habilitado"

    def mostrar_estudiante(self):
        print("ID del estudiante:", self.__id)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Edad:", self.__edad)
        print("Curso:", self.__curso)
        print("Estado:", self.__habilitado)

    def get_id(self):
        return self.__id    
    
    def get_habilitado(self):
        return self.__habilitado
    
    def establecer_estado(self, estado):
        self.__habilitado = estado

    def establecer_estudiante(self, nombre, apellido, edad, curso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__curso = curso
        
    def get_nombre(self):
        return self.__nombre
    
    def establecer_nuevo_nombre_estudiante(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return True
    
    def get_curso(self):
        return self.__curso
    
    def establecer_nuevo_curso_estudiante(self, nuevo_curso):
        self.__curso = nuevo_curso
        return True
    
    def get_edad(self): 
        return self.__edad
    def establecer_nueva_edad_estudiante(self, nueva_edad):
        self.__edad = nueva_edad
        return True

    def establecer_nuevo_apellido_estudiante(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        return True 
    def get_apellido(self):  
        return self.__apellido
