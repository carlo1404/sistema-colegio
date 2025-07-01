class Grado:
    def __init__(self, nombre, aula , cantidad_estudiantes, id = 0):
        self.__id = id 
        self.__nombre = nombre
        self.__aula= aula
        self.__cantidad_estudiantes = cantidad_estudiantes
        self.__habilitado = "habilitado"

    def mostrar_docente(self):
        print("ID del docente:", self.__id)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Materia:", self.__materia)
        print("grado:", self.__grado)
        print("Estado:", self.__habilitado)

    def get_id_grado(self):
        return self.__id    
    
    def get_habilitado(self):
        return self.__habilitado
    
    def establecer_estado(self, estado):
        self.__habilitado = estado

    def mostrar_grado(self):
        print("ID del grado:", self.__id)
        print("Nombre:", self.__nombre)
        print("Capacidad:", self.__cantidad_estudiantes)
        print("Estado:", self.__habilitado)


    def get_habilitado_grado(self):
        return self.__habilitado

    def establecer_estado(self, estado):
        self.__habilitado = estado

        print("Estado:", self.__habilitado)

    def get_nombre_grado(self):
        return self.__nombre


    def get_materia(self):
        return self.__materia
    
    def get_grado(self):
        return self.__grado

    def establecer_nuevo_nombre_grado(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return True

    def establecer_nuevo_apellido_grado(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        return True

    def establecer_nueva_grado_docente(self, nueva_grado):
        self.__grado = nueva_grado
        return True

    def establecer_nueva_materia_docente(self, nueva_materia):
        self.__materia = nueva_materia
        return True


    def establecer_estado_grado(self, estado):
        self.__habilitado = estado


    def get_grado_docente(self):
        return self.__grado
    
    def get_aula_grado(self):
        return self.__aula
    
    def establecer_nueva_aula(self, nueva_aula):
        self.__aula = nueva_aula
        return True
    

    def get_cantidad_grado(self):
        return self.__cantidad_estudiantes
    

    def establecer_nueva_cantidad_grado(self, nueva_cantidad):
        self.__cantidad_estudiantes = nueva_cantidad
        return True
    
