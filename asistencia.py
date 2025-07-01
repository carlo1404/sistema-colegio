from datetime import date

class Asistencia:
    def __init__(self, id_fecha, id_docente, fecha, cantidad_estudiantes):
        self.__id_fecha = id_fecha
        self.__id_docente = id_docente
        self.__fecha = fecha  # Objeto date completo
        self.__cantidad_estudiantes = cantidad_estudiantes
        self.__habilitado = "habilitado"
        self.__excusa = None  # Nueva propiedad para excusas

    def mostrar_asistencia(self):
        print("ID:", self.__id_fecha)
        print("ID del docente:", self.__id_docente)
        print("Fecha:", self.__fecha.strftime("%d/%m/%Y"))
        print("Cantidad de estudiantes:", self.__cantidad_estudiantes)
        print("Estado:", self.__habilitado)
        if self.__excusa:
            print("Excusa:", self.__excusa)
    def get_id(self):
        return self.__id_fecha

    def get_id_asistencia(self):
        return self.__id_docente    
    
    def get_fecha(self):
        return self.__fecha
    
    def get_cantidad_estudiantes(self):
        return self.__cantidad_estudiantes
    
    def get_habilitado(self):
        return self.__habilitado
    
    def establecer_estado(self, estado):
        self.__habilitado = estado

    def establecer_asistencia(self, id_docente, fecha, cantidad_estudiantes):
        self.__id_docente = id_docente
        self.__fecha = fecha
        self.__cantidad_estudiantes = cantidad_estudiantes
        
    def get_fecha_asistencia(self):
        return self.__fecha
    
    # Métodos para manejar excusas
    def get_excusa(self):
        return self.__excusa
    
    def establecer_excusa(self, excusa):
        self.__excusa = excusa
    
    def tiene_excusa(self):
        return self.__excusa is not None