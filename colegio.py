from os import system
from estudiante import Estudiante
from datetime import datetime, date
from docente import Docente

class Colegio:
    """
    Clase principal que gestiona todo el sistema escolar.
    Maneja estudiantes, docentes, grados, aulas, asistencias e inasistencias.
    """
    
    def __init__(self):
        # Listas para almacenar todos los elementos del sistema
        self.__estudiantes = []      # Lista de estudiantes registrados
        self.__grados = []           # Lista de grados escolares
        self.__docentes = []         # Lista de docentes
        self.__aulas = []            # Lista de aulas físicas
        self.__asistencias = []      # Lista de registros de asistencia
        self.__inasistencias = []    # Lista de registros de inasistencia
        self.__fecha = date.today()  # Fecha actual del sistema
        
        # Lista de materias disponibles para asignar a docentes
        self.__materias = ["Matemáticas", "Lengua", "Ciencias Naturales", "Historia", "Geografía", "Educación Física", "Arte", "Inglés"]
    

    # ========================================
    # MÉTODOS PARA GESTIONAR ESTUDIANTES
    # ========================================
    
    def adicionar_estudiante(self, estudiante):
        """
        Agrega un nuevo estudiante al sistema.
        Verifica que el ID no esté duplicado antes de agregar.
        """
        if self.verificar_id_estudiante_existe(estudiante.get_id()):
            print(f"Error - Ya existe un estudiante con el ID {estudiante.get_id()}")
            return False
        self.__estudiantes.append(estudiante)
        return True
    
    def agregar_estudiante(self, estudiante):
        """
        Método alternativo para agregar estudiantes (sin verificación de duplicados).
        """
        self.__estudiantes.append(estudiante)
        print("El estudiante ha sido agregado exitosamente.")
    
    def buscar_estudiante(self, id):
        """
        Busca un estudiante por su ID y muestra su información.
        Retorna -1 si no se encuentra.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                estudiante =  self.__estudiantes[i].mostrar_estudiante()   
                return estudiante
        return -1
    
    def modificar_estudiante(self, id, nombre, apellido, edad, curso):
        """
        Modifica la información de un estudiante existente.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_estudiante(nombre, apellido, edad, curso)
                return True
    
    def get_estudiante(self, id):
        """
        Obtiene el nombre de un estudiante por su ID.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_nombre()
        return -1
    
    def deshabilitar_habilitar_estudiante(self, id):
        """
        Cambia el estado de un estudiante entre habilitado y deshabilitado.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                if self.__estudiantes[i].get_habilitado() == "habilitado":
                    self.__estudiantes[i].establecer_estado("deshabilitado") 
                else:
                    self.__estudiantes[i].establecer_estado("habilitado")
                return True
    
    def establecer_nuevo_nombre_estudiante(self, nuevo_nombre, id):
        """
        Establece un nuevo nombre para un estudiante específico.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_nombre_estudiante(nuevo_nombre)
                return True
    
    def get_curso_estudiante(self, id):
        """
        Obtiene el curso de un estudiante por su ID.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_curso()
        return -1
    
    def establecer_nuevo_curso_estudiante(self, nuevo_curso, id):
        """
        Establece un nuevo curso para un estudiante específico.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_curso_estudiante(nuevo_curso)
                return True
        return -1
    
    def get_edad_estudiante(self, id):
        """
        Obtiene la edad de un estudiante por su ID.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_edad()
        return -1
    
    def establecer_nueva_edad_estudiante(self, nueva_edad, id):
        """
        Establece una nueva edad para un estudiante específico.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nueva_edad_estudiante(nueva_edad)
                return True
        return -1
    
    def establecer_nuevo_apellido_estudiante(self, nuevo_apellido, id):
        """
        Establece un nuevo apellido para un estudiante específico.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_apellido_estudiante(nuevo_apellido)
                return True 
    
    def get_apellido_estudiante(self, id):  
        """
        Obtiene el apellido de un estudiante por su ID.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_apellido()
        return -1
    
    def get_grado_estudiante(self, id):  
        """
        Obtiene el grado de un estudiante por su ID.
        """
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_grado()
        return -1
    
    def get_nombre_estudiante(self, id):
        """
        Obtiene el nombre de un estudiante por su ID.
        """
        for estudiante in self.__estudiantes:
            if estudiante.get_id() == id:
                return estudiante.get_nombre()
        return -1
    
    def get_estudiantes(self):
        """
        Retorna la lista completa de estudiantes.
        """
        return self.__estudiantes
    
    def get_estudiantes_habilitados(self):
        """
        Retorna solo los estudiantes que están habilitados.
        """
        estudiantes_habilitados = []
        for estudiante in self.__estudiantes:
            if estudiante.get_habilitado() == "habilitado":
                estudiantes_habilitados.append(estudiante)
        return estudiantes_habilitados
    
    def verificar_id_estudiante_existe(self, id):
        """
        Verifica si ya existe un estudiante con el ID dado.
        """
        for estudiante in self.__estudiantes:
            if estudiante.get_id() == id:
                return True
        return False

    # ========================================
    # MÉTODOS PARA GESTIONAR DOCENTES
    # ========================================
    
    def adicionar_docente(self, docente):
        """
        Agrega un nuevo docente al sistema.
        Verifica que el ID no esté duplicado antes de agregar.
        """
        if self.verificar_id_docente_existe(docente.get_id_docente()):
            print(f"Error - Ya existe un docente con el ID {docente.get_id_docente()}")
            return False
        self.__docentes.append(docente)
        return True
    
    def buscar_docentes(self, id):
        """
        Busca un docente por su ID y muestra su información.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                docentes =  self.__docentes[i].mostrar_docentes()   
                return docentes
        return -1
    
    def buscar_docente(self, id):
        """
        Busca un docente por su ID y retorna su nombre.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_nombre_docente()
        return -1
    
    def get_nombre_docente(self, id):
        """
        Obtiene el nombre de un docente por su ID.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_nombre_docente()
        return -1
    
    def get_apellido_docente(self, id):
        """
        Obtiene el apellido de un docente por su ID.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_apellido_docente()
        return -1
    
    def get_aula_docente(self, id):
        """
        Obtiene el aula asignada a un docente por su ID.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_aula()
        return -1
    
    def get_materia_docente(self, id):
        """
        Obtiene la materia asignada a un docente por su ID.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_materia()
        return -1
    
    def establecer_nuevo_nombre_docente(self, nuevo_nombre, id):    
        """
        Establece un nuevo nombre para un docente específico.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nuevo_nombre_docente(nuevo_nombre)
                return True
        return -1
    
    def establecer_nuevo_apellido_docente(self, nuevo_apellido, id):    
        """
        Establece un nuevo apellido para un docente específico.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nuevo_apellido_docente(nuevo_apellido)
                return True
        return -1
    
    def establecer_nueva_grado_docente(self, nueva_grado, id):    
        """
        Establece un nuevo grado para un docente específico.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nueva_grado_docente(nueva_grado)
                return True
        return -1
    
    def establecer_nueva_materia_docente(self, nueva_materia, id):    
        """
        Establece una nueva materia para un docente específico.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nueva_materia_docente(nueva_materia)
                return True
        return -1
    
    def deshabilitar_habilitar_docente(self, id):
        """
        Cambia el estado de un docente entre habilitado y deshabilitado.
        """
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                if self.__docentes[i].get_habilitado() == "habilitado":
                    self.__docentes[i].establecer_estado_docente("deshabilitado") 
                else:
                    self.__docentes[i].establecer_estado_docente("habilitado")
                return True
    
    def verificar_id_docente_existe(self, id):
        """
        Verifica si ya existe un docente con el ID dado.
        """
        for docente in self.__docentes:
            if docente.get_id_docente() == id:
                return True
        return False
    
    def get_docentes_habilitados(self):
        """
        Retorna solo los docentes que están habilitados.
        """
        docentes_habilitados = []
        for docente in self.__docentes:
            if docente.get_habilitado() == "habilitado":
                docentes_habilitados.append(docente)
        return docentes_habilitados

    # ========================================
    # MÉTODOS PARA GESTIONAR GRADOS
    # ========================================
    
    def adicionar_grado(self, grado):
        """
        Agrega un nuevo grado al sistema.
        """
        self.__grados.append(grado)
        return True
    
    def buscar_grado(self, id):
        """
        Busca un grado por su ID y muestra su información.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                grado =  self.__grados[i].mostrar_grado()
                return grado
        return -1
    
    def get_nombre_grado(self, id):
        """
        Obtiene el nombre de un grado por su ID.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                return self.__grados[i].get_nombre_grado()
        return -1
    
    def establecer_nuevo_nombre_grado(self, nuevo_nombre, id):    
        """
        Establece un nuevo nombre para un grado específico.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nuevo_nombre_grado(nuevo_nombre)
                return True
        return -1
    
    def establecer_nueva_cantidad_grado(self, nueva_cantidad, id):    
        """
        Establece una nueva cantidad de estudiantes para un grado específico.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nueva_cantidad_grado(nueva_cantidad)
                return True
        return -1
    
    def deshabilitar_habilitar_grado(self, id):
        """
        Cambia el estado de un grado entre habilitado y deshabilitado.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                if self.__grados[i].get_habilitado_grado() == "habilitado":
                    self.__grados[i].establecer_estado_grado("deshabilitado") 
                else:
                    self.__grados[i].establecer_estado_grado("habilitado")
                return True
    
    def get_cantidad_grados(self, id):
        """
        Obtiene la cantidad de estudiantes de un grado por su ID.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                return self.__grados[i].get_cantidad_grado()
        return -1
    
    def get_grados(self):
        """
        Retorna la lista completa de grados.
        """
        return self.__grados

    # ========================================
    # MÉTODOS PARA GESTIONAR AULAS
    # ========================================
    
    def adicionar_aula(self, aula):
        """
        Agrega una nueva aula al sistema.
        """
        self.__aulas.append(aula)
        return True
    
    def buscar_aula(self, id):
        """
        Busca un aula por su ID y muestra su información.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                grado =  self.__aulas[i].mostrar_aula()
                return grado
        return -1
    
    def buscar_aulas(self, id):
        """
        Busca un aula por su ID y retorna su nombre.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_nombre_docente()
        return -1
    
    def get_nombre_aula(self, id):
        """
        Obtiene el nombre de un aula por su ID.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_nombre_aula()
        return -1
    
    def establecer_nuevo_nombre_aula(self, nueva_nombre, id):
        """
        Establece un nuevo nombre para un aula específica.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                self.__aulas[i].establecer_nuevo_nombre_aula(nueva_nombre)
                return True
        return -1
    
    def establecer_nueva_capacidad_aula(self, nueva_capacidad, id):
        """
        Establece una nueva capacidad para un aula específica.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                self.__aulas[i].establecer_nueva_capacidad_aula(nueva_capacidad)
                return True
    
    def get_capacidad_aula(self, id):
        """
        Obtiene la capacidad de un aula por su ID.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_capacidad_aula()
        return -1
    
    def deshabilitar_habilitar_aula(self, id):
        """
        Cambia el estado de un aula entre habilitado y deshabilitado.
        """
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                if self.__aulas[i].get_habilitado_aula() == "habilitado":
                    self.__aulas[i].establecer_estado_aula("deshabilitado") 
                else:
                    self.__aulas[i].establecer_estado_aula("habilitado")
                return True
    
    def get_aulas(self):
        """
        Retorna la lista completa de aulas.
        """
        return self.__aulas

    # ========================================
    # MÉTODOS PARA GESTIONAR MATERIAS
    # ========================================
    
    def get_materias(self):
        """
        Retorna la lista de materias disponibles.
        """
        return self.__materias

    def descontar_materias(self, pos):
        """
        Remueve una materia de la lista de materias disponibles.
        Se usa cuando se asigna una materia a un docente.
        """
        materia = self.__materias[pos-1]
        self.__materias.pop(pos-1)
        return materia

    # ========================================
    # MÉTODOS PARA GESTIONAR ASISTENCIAS
    # ========================================
    
    def registrar_asistencia(self, asistencia):
        """
        Registra una nueva asistencia en el sistema.
        Verifica que no exista una asistencia duplicada para el mismo docente en la misma fecha.
        """
        # Verificar si ya existe una asistencia para el mismo docente en la misma fecha
        if self.verificar_id_asistencia_existe(asistencia.get_id_asistencia(), asistencia.get_fecha()):
            print(f"Error - Ya existe una asistencia registrada para este docente en la fecha {asistencia.get_fecha().strftime('%d/%m/%Y')}")
            return False
        self.__asistencias.append(asistencia)
        print("Asistencia registrada exitosamente!")
        return True
    
    def verificar_id_asistencia_existe(self, id_docente, fecha):
        """
        Verifica si ya existe una asistencia para el mismo docente en la misma fecha.
        """
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente and asistencia.get_fecha() == fecha:
                return True
        return False
    
    def buscar_asistencias_por_fecha(self, fecha):
        """
        Busca todas las asistencias de una fecha específica.
        """
        asistencias_encontradas = []
        for asistencia in self.__asistencias:
            if asistencia.get_fecha() == fecha:
                asistencias_encontradas.append(asistencia)
        return asistencias_encontradas
    
    def buscar_asistencias_por_docente(self, id_docente):
        """
        Busca todas las asistencias de un docente específico.
        """
        asistencias_encontradas = []
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente:
                asistencias_encontradas.append(asistencia)
        return asistencias_encontradas
    
    def buscar_asistencia_por_id(self, id_asistencia):
        """
        Busca una asistencia específica por su ID.
        """
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_asistencia:
                return asistencia
        return None
    
    def registrar_excusa(self, id_asistencia, excusa):
        """
        Registra una excusa para una asistencia específica.
        """
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_asistencia:
                asistencia.establecer_excusa(excusa)
                return True
        return False
    
    def buscar_asistencias_con_excusa(self):
        """
        Retorna todas las asistencias que tienen excusa.
        """
        asistencias_con_excusa = []
        for asistencia in self.__asistencias:
            if asistencia.tiene_excusa():
                asistencias_con_excusa.append(asistencia)
        return asistencias_con_excusa
    
    def buscar_asistencias_sin_excusa(self):
        """
        Retorna todas las asistencias que no tienen excusa.
        """
        asistencias_sin_excusa = []
        for asistencia in self.__asistencias:
            if not asistencia.tiene_excusa():
                asistencias_sin_excusa.append(asistencia)
        return asistencias_sin_excusa
    
    def modificar_asistencia(self, id_docente, fecha, cantidad_estudiantes):
        """
        Modifica una asistencia existente.
        """
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente and asistencia.get_fecha() == fecha:
                asistencia.establecer_asistencia(id_docente, fecha, cantidad_estudiantes)
                print("Asistencia modificada exitosamente!")
                return True
        print("No se encontró la asistencia a modificar.")
        return False
    
    def get_asistencias(self):
        """
        Retorna todas las asistencias registradas.
        """
        return self.__asistencias
    
    def get_fechas_asistencias(self):
        """
        Retorna todas las fechas de asistencias registradas.
        """
        fechas = []
        for asistencia in self.__asistencias:
            fechas.append(asistencia.get_fecha())
        return fechas
    
    def modificar_fecha(self, id_fecha, nueva_fecha):
        """
        Modifica la fecha de una asistencia específica.
        """
        # Buscar la asistencia por ID y modificar su fecha
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_fecha:
                asistencia.establecer_asistencia(asistencia.get_id_asistencia(), nueva_fecha, asistencia.get_cantidad_estudiantes())
                return True
        return False

    # ========================================
    # MÉTODOS PARA GESTIONAR INASISTENCIAS
    # ========================================
    
    def registrar_inasistencia(self, id_fecha, id_docente, fecha_inasistencia, cantidad_estudiantes, id_estudiantes_inasistentes):
        """
        Registra una inasistencia en el sistema.
        Verifica que no exista una inasistencia con el mismo ID.
        """
        # Verificar si ya existe una inasistencia con el mismo ID
        for inasistencia in self.__inasistencias:
            if inasistencia.get_id() == id_fecha:
                print(f"Error - Ya existe una inasistencia con el ID {id_fecha}")
                return False
        
        # Crear nueva inasistencia
        from inasistencia import Inasistencia
        nueva_inasistencia = Inasistencia(id_fecha, id_docente, fecha_inasistencia, cantidad_estudiantes, id_estudiantes_inasistentes)
        self.__inasistencias.append(nueva_inasistencia)
        return True
    
    def modificar_inasistencia(self, id_docente, fecha, cantidad_estudiantes):
        """
        Modifica una inasistencia existente.
        """
        for inasistencia in self.__inasistencias:
            if inasistencia.get_id_inasistencia() == id_docente and inasistencia.get_fecha() == fecha:
                inasistencia.establecer_inasistencia(inasistencia.get_id(), id_docente, fecha, cantidad_estudiantes, inasistencia.get_id_estudiantes_inasistentes())
                print("Inasistencia modificada exitosamente!")
                return True
        print("No se encontró la inasistencia a modificar.")
        return False
    
    def buscar_inasistencias_sin_excusa(self):
        """
        Retorna todas las inasistencias que no tienen excusa.
        """
        if len(self.__inasistencias) == 0:
            return []
        return self.__inasistencias
    
    def get_inasistencias(self):
        """
        Retorna todas las inasistencias registradas.
        """
        return self.__inasistencias
    
    def agreagar_inasistencia(self, inasistencia):
        """
        Agrega una inasistencia a la lista (método alternativo).
        """
        self.__inasistencias.append(inasistencia)
        return True

    # ========================================
    # MÉTODOS PARA LISTAR INFORMACIÓN
    # ========================================
    
    def listar_estudiantes(self):
        """
        Muestra la lista completa de estudiantes.
        """
        print("Lista de estudiantes:")
        for estudiante in self.__estudiantes:
            estudiante.mostrar_estudiante()
    
    def listar_docentes(self):
        """
        Muestra la lista completa de docentes.
        """
        print("Lista de docentes:")
        for docente in self.__docentes:
            docente.mostrar_docente()
    
    def listar_grados(self):
        """
        Muestra la lista completa de grados.
        """
        print("Lista de grados:")
        for grado in self.__grados:
            grado.mostrar_grado()
    
    def listar_aulas(self):
        """
        Muestra la lista completa de aulas.
        """
        print("Lista de aulas:")
        for aula in self.__aulas:
            aula.mostrar_aula()
    
    def listar_asistencias(self):
        """
        Muestra la lista completa de asistencias.
        """
        print("Lista de asistencias:")
        for asistencia in self.__asistencias:
            asistencia.mostrar_asistencia()
    
    def listar_fechas_asistencias(self):
        """
        Muestra todas las fechas de asistencias registradas.
        """
        print("Lista de fechas de asistencias:")
        for asistencia in self.__asistencias: 
            print(asistencia.get_fecha().strftime("%d/%m/%Y"))
    
    def listar_asistencias_con_excusa(self):
        """
        Muestra todas las asistencias que tienen excusa.
        """
        print("Lista de asistencias con excusa:")
        for asistencia in self.__asistencias:
            if asistencia.tiene_excusa():
                asistencia.mostrar_asistencia()
    
    def listar_asistencias_sin_excusa(self):
        """
        Muestra todas las asistencias que no tienen excusa.
        """
        print("Lista de asistencias sin excusa:")
        for asistencia in self.__asistencias:
            if not asistencia.tiene_excusa():
                asistencia.mostrar_asistencia()
    
    def get_listar_asistencias_con_excusa(self):    
        """
        Retorna las asistencias con excusa (método alternativo).
        """
        return self.__asistencias
    
    def get_listar_asistencias_sin_excusa(self):  
        """
        Retorna las asistencias sin excusa (método alternativo).
        """
        return self.__asistencias
    
    def mostrar_grados_disponibles(self):
        """
        Retorna una lista de grados disponibles de docentes habilitados.
        """
        lista_grados = []
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_habilitado() == "habilitado":
                lista_grados.append(self.__docentes[i].get_aula_docente())
        return lista_grados
    
    def get_num_aula(self, id):
        """
        Obtiene el número de aula de un grado por su ID.
        """
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id() == id:
                return self.__grados[i].get_aula_grado()
        return -1
    
    def establecer_nueva_aula(self, nueva_aula, id):
        """
        Establece una nueva aula para un grado específico.
        """
        for i in range(len(self.__estudiantes)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nueva_aula(nueva_aula)
                return True

