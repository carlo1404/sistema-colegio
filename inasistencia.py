from datetime import date


class Inasistencia:
    def __init__(self, id_fecha, id_docente, fecha_inasistencia, cantidad_estudiantes, id_estudiantes_inasistentes):
        self.__id_fecha = id_fecha
        self.__id_docente = id_docente
        self.__fecha = fecha_inasistencia  # Usar la fecha pasada como parámetro
        self.__cantidad_estudiantes = cantidad_estudiantes
        self.__id_estudiantes_inasistentes = id_estudiantes_inasistentes

    def establecer_inasistencia(self, id_fecha, id_docente, fecha_inasistencia, cantidad_estudiantes, id_estudiantes_inasistentes):
        self.__id_fecha = id_fecha
        self.__id_docente = id_docente
        self.__fecha = fecha_inasistencia
        self.__cantidad_estudiantes = cantidad_estudiantes
        self.__id_estudiantes_inasistentes = id_estudiantes_inasistentes

    def mostrar_inasistencia(self):
        print("ID de la fecha:", self.__id_fecha)
        print("ID del docente:", self.__id_docente)
        print("Fecha:", self.__fecha.strftime('%d/%m/%Y'))
        print("Cantidad de estudiantes:", self.__cantidad_estudiantes)
        print("ID de los estudiantes inasistentes:", self.__id_estudiantes_inasistentes)
        print("Estudiantes que faltaron: ", self.__id_estudiantes_inasistentes)

    def get_id(self):
        return self.__id_fecha
    
    def get_id_inasistencia(self):
        return self.__id_docente    
    
    def get_fecha(self):
        return self.__fecha
    
    def get_cantidad_estudiantes(self):
        return self.__cantidad_estudiantes
    
    def get_id_estudiantes_inasistentes(self):
        return self.__id_estudiantes_inasistentes
