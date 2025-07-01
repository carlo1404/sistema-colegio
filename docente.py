class Docente:
    def __init__(self, nombre , apellido , materia, aula,  id = 0):
        self.__id = id 
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materia = materia
        self.__aula = aula
        self.__habilitado = "habilitado"

    def mostrar_docente(self):
        print("ID del docente:", self.__id)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Materia:", self.__materia)
        print("aula:", self.__aula)
        print("Estado:", self.__habilitado)

    def get_id_docente(self):
        return self.__id    
    
    def get_habilitado(self):
        return self.__habilitado
    
    def establecer_estado(self, estado):
        self.__habilitado = estado

    def mostrar_docentes(self):
        print("ID del docente:", self.__id)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Materia", self.__materia)
        print("Salor (aula):", self.__aula)
        print("Estado:", self.__habilitado)

    def get_nombre_docente(self):
        return self.__nombre
    
    def get_apellido_docente(self):
        return self.__apellido

    def get_materia(self):
        return self.__materia
    
    def get_materia_docente(self):
        return self.__materia
    
    def get_aula(self):
        return self.__aula

    def get_aula_docente(self):
        return self.__aula

    def establecer_nuevo_nombre_docente(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return True

    def establecer_nuevo_apellido_docente(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        return True

    def establecer_nueva_aula_docente(self, nueva_aula):
        self.__aula = nueva_aula
        return True

    def establecer_nueva_materia_docente(self, nueva_materia):
        self.__materia = nueva_materia
        return True


    def establecer_estado_docente(self, estado):
        self.__habilitado = estado