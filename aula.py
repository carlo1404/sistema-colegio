class Aula:
    def __init__(self, nombre, capacidad, id = 0):
        self.__id = id 
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__habilitado = "habilitado"


        
    def mostrar_aula(self):
        print("ID del aula:", self.__id)
        print("Nombre:", self.__nombre)
        print("Capacidad:", self.__capacidad)
        print("Estado:", self.__habilitado)

    def get_id_aula(self):
        return self.__id    
    def get_nombre_aula(self):
        return self.__nombre
    def get_habilitado(self):
        return self.__habilitado
    
    def establecer_estado(self, estado):
        self.__habilitado = estado

    def mostrar_aula(self):
        print("ID del aula:", self.__id)
        print("Nombre:", self.__nombre)
        print("Estado:", self.__habilitado)

    def establecer_nueva_capacidad_aula(self, nueva_capacidad):
        self.__capacidad = nueva_capacidad
    def get_capacidad_aula(self):
        return self.__capacidad
    def get_id_aula(self):
        return self.__id

    def get_habilitado_aula(self):
        return self.__habilitado

    def establecer_estado_aula(self, estado):
        self.__habilitado = estado

        print("Estado:", self.__habilitado)

    def get_nombre_docente(self):
        return self.__nombre
    
    def get_apellido_docente(self):
        return self.__apellido

    def get_materia(self):
        return self.__materia
    
    def get_aula(self):
        return self.__aula

    def establecer_nuevo_nombre_aula(self, nuevo_nombre):
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


    def get_aula_docente(self):
        return self.__aula