from os import system
from estudiante import Estudiante
from datetime import datetime, date
from docente import Docente

class Colegio:
    def __init__(self):
        self.__estudiantes = []
        self.__grados = []
        self.__docentes = []
        self.__aulas = []
        self.__asistencias = []
        self.__fecha = date.today()
        self.__materias = ["Matemáticas", "Lengua", "Ciencias Naturales", "Historia", "Geografía", "Educación Física", "Arte", "Inglés"]

    def adicionar_estudiante(self, estudiante):
        if self.verificar_id_estudiante_existe(estudiante.get_id()):
            print(f"Error - Ya existe un estudiante con el ID {estudiante.get_id()}")
            return False
        self.__estudiantes.append(estudiante)
        return True
    def adicionar_docente(self, docente):
        if self.verificar_id_docente_existe(docente.get_id_docente()):
            print(f"Error - Ya existe un docente con el ID {docente.get_id_docente()}")
            return False
        self.__docentes.append(docente)
        return True
    def adicionar_grado(self, grado):
        self.__grados.append(grado)
        return True
    def adicionar_aula(self, aula):
        self.__aulas.append(aula)
        return True
    def buscar_estudiante(self, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                estudiante =  self.__estudiantes[i].mostrar_estudiante()   
                return estudiante
        return -1
    def buscar_grado(self, id):
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                grado =  self.__grados[i].mostrar_grado()
                return grado
        return -1
    def buscar_aula(self, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                grado =  self.__aulas[i].mostrar_aula()
                return grado
        return -1
    def buscar_aulas(self, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_nombre_docente()
        return -1
    def get_estudiantes(self):
        return self.__estudiantes
    

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
        print("El estudiante ha sido agregado exitosamente.")
    
    def modificar_estudiante(self , id, nombre, apellido, edad, curso):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_estudiante(nombre, apellido, edad, curso)
                return True
            
    def get_estudiante(self, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_nombre()
        return -1


    def deshabilitar_habilitar_estudiante(self, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                if self.__estudiantes[i].get_habilitado() == "habilitado":
                    self.__estudiantes[i].establecer_estado("deshabilitado") 
                else:
                    self.__estudiantes[i].establecer_estado("habilitado")
                return True
    def deshabilitar_habilitar_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                if self.__docentes[i].get_habilitado() == "habilitado":
                    self.__docentes[i].establecer_estado_docente("deshabilitado") 
                else:
                    self.__docentes[i].establecer_estado_docente("habilitado")
                return True
    def deshabilitar_habilitar_grado(self, id):
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                if self.__grados[i].get_habilitado_grado() == "habilitado":
                    self.__grados[i].establecer_estado_grado("deshabilitado") 
                else:
                    self.__grados[i].establecer_estado_grado("habilitado")
                return True
    def deshabilitar_habilitar_aula(self, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                if self.__aulas[i].get_habilitado_aula() == "habilitado":
                    self.__aulas[i].establecer_estado_aula("deshabilitado") 
                else:
                    self.__aulas[i].establecer_estado_aula("habilitado")
                return True
    def establecer_nuevo_nombre_estudiante(self, nuevo_nombre, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_nombre_estudiante(nuevo_nombre)
                return True
            
    def get_curso_estudiante(self, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_curso()
        return -1
    
    def establecer_nuevo_curso_estudiante(self, nuevo_curso, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_curso_estudiante(nuevo_curso)
                return True
        return -1
    
    def get_edad_estudiante(self, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_edad()
        return -1
    def get_num_aula(self, id):
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id() == id:
                return self.__grados[i].get_aula_grado()
        return -1
    def establecer_nueva_edad_estudiante(self, nueva_edad, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nueva_edad_estudiante(nueva_edad)
                return True
        return -1
    
    def establecer_nuevo_apellido_estudiante(self, nuevo_apellido, id):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                self.__estudiantes[i].establecer_nuevo_apellido_estudiante(nuevo_apellido)
                return True 
    def establecer_nueva_aula(self, nueva_aula, id):
        for i in range(len(self.__estudiantes)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nueva_aula(nueva_aula)
                return True     
            
    def establecer_nueva_capacidad_aula(self, nueva_capacidad, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                self.__aulas[i].establecer_nueva_capacidad_aula(nueva_capacidad)
                return True
            
    
    def get_apellido_estudiante(self, id):  
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_apellido()
        return -1
    
    def get_grado_estudiante(self, id):  
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_id() == id:
                return self.__estudiantes[i].get_grado()
        return -1
    
    def get_materias(self):
        return self.__materias

    def descontar_materias(self,pos):
        materia = self.__materias[pos-1]
        self.__materias.pop(pos-1)
        return materia
    
    def buscar_docentes(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                docentes =  self.__docentes[i].mostrar_docentes()   
                return docentes
        return -1
    
    def buscar_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_nombre_docente()
        return -1

    def get_nombre_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_nombre_docente()
        return -1
    def get_nombre_grado(self, id):
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                return self.__grados[i].get_nombre_grado()
        return -1
    def get_nombre_aula(self, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_nombre_aula()
        return -1
    def get_apellido_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_apellido_docente()
        return -1
    
    def get_aula_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_aula()
        return -1
    
    def get_materia_docente(self, id):
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                return self.__docentes[i].get_materia()
        return -1

    def establecer_nuevo_nombre_docente(self, nuevo_nombre, id):    
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nuevo_nombre_docente(nuevo_nombre)
                return True
        return -1
    def establecer_nuevo_nombre_grado(self, nuevo_nombre, id):    
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nuevo_nombre_grado(nuevo_nombre)
                return True
        return -1
    def establecer_nuevo_nombre_aula(self,nueva_nombre, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                self.__aulas[i].establecer_nuevo_nombre_aula(nueva_nombre)
                return True
        return -1

    def establecer_nuevo_apellido_docente(self, nuevo_apellido, id):    
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nuevo_apellido_docente(nuevo_apellido)
                return True
        return -1

    def establecer_nueva_grado_docente(self, nueva_grado, id):    
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nueva_grado_docente(nueva_grado)
                return True
        return -1
    def establecer_nueva_cantidad_grado(self, nueva_cantidad, id):    
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                self.__grados[i].establecer_nueva_cantidad_grado(nueva_cantidad)
                return True
        return -1
    def establecer_nueva_materia_docente(self, nueva_materia, id):    
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_id_docente() == id:
                self.__docentes[i].establecer_nueva_materia_docente(nueva_materia)
                return True
        return -1
    def mostrar_grados_disponibles(self):
        lista_grados = []
        for i in range(len(self.__docentes)):
            if self.__docentes[i].get_habilitado() == "habilitado":
                lista_grados.append(self.__docentes[i].get_aula_docente())
        return lista_grados
    
    def get_cantidad_grados(self, id):
        for i in range(len(self.__grados)):
            if self.__grados[i].get_id_grado() == id:
                return self.__grados[i].get_cantidad_grado()
        return -1
    
    def get_capacidad_aula(self, id):
        for i in range(len(self.__aulas)):
            if self.__aulas[i].get_id_aula() == id:
                return self.__aulas[i].get_capacidad_aula()
        return -1
    
    def get_docentes_habilitados(self):
        """Retorna una lista de docentes habilitados"""
        docentes_habilitados = []
        for docente in self.__docentes:
            if docente.get_habilitado() == "habilitado":
                docentes_habilitados.append(docente)
        return docentes_habilitados
    
    def get_estudiantes_habilitados(self):
        """Retorna una lista de estudiantes habilitados"""
        estudiantes_habilitados = []
        for estudiante in self.__estudiantes:
            if estudiante.get_habilitado() == "habilitado":
                estudiantes_habilitados.append(estudiante)
        return estudiantes_habilitados
    
    def verificar_id_asistencia_existe(self, id_docente, fecha):
        """Verifica si ya existe una asistencia para el mismo docente en la misma fecha"""
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente and asistencia.get_fecha() == fecha:
                return True
        return False
    
    def registrar_asistencia(self, asistencia):
        # Verificar si ya existe una asistencia para el mismo docente en la misma fecha
        if self.verificar_id_asistencia_existe(asistencia.get_id_asistencia(), asistencia.get_fecha()):
            print(f"Error - Ya existe una asistencia registrada para este docente en la fecha {asistencia.get_fecha().strftime('%d/%m/%Y')}")
            return False
        self.__asistencias.append(asistencia)
        print("Asistencia registrada exitosamente!")
        return True

    def verificar_id_estudiante_existe(self, id):
        """Verifica si ya existe un estudiante con el ID dado"""
        for estudiante in self.__estudiantes:
            if estudiante.get_id() == id:
                return True
        return False
    
    def verificar_id_docente_existe(self, id):
        """Verifica si ya existe un docente con el ID dado"""
        for docente in self.__docentes:
            if docente.get_id_docente() == id:
                return True
        return False

    def buscar_asistencias_por_fecha(self, fecha):
        """Busca todas las asistencias de una fecha específica"""
        asistencias_encontradas = []
        for asistencia in self.__asistencias:
            if asistencia.get_fecha() == fecha:
                asistencias_encontradas.append(asistencia)
        return asistencias_encontradas
    
    def buscar_asistencias_por_docente(self, id_docente):
        """Busca todas las asistencias de un docente específico"""
        asistencias_encontradas = []
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente:
                asistencias_encontradas.append(asistencia)
        return asistencias_encontradas
    
    def get_asistencias(self):
        """Retorna todas las asistencias"""
        return self.__asistencias
    
    def modificar_inasistencia(self,  id_docente, fecha, cantidad_estudiantes):
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_docente and asistencia.get_fecha() == fecha:
                asistencia.establecer_asistencia(id_docente, fecha, cantidad_estudiantes)
                print("Asistencia modificada exitosamente!")
                return True
        print("No se encontró la asistencia a modificar.")
        return False
    
    def get_fechas_asistencias(self):
        fechas = []
        for asistencia in self.__asistencias:
            fechas.append(asistencia.get_fecha())
        return fechas
    

    def modificar_fecha(self, id_fecha, nueva_fecha):
        # Buscar la asistencia por ID y modificar su fecha
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_fecha:
                asistencia.establecer_asistencia(asistencia.get_id_asistencia(), nueva_fecha, asistencia.get_cantidad_estudiantes())
                return True
        return False
    
    def listar_estudiantes(self):
        print("Lista de estudiantes:")
        for estudiante in self.__estudiantes:
            estudiante.mostrar_estudiante()
        
    
    def listar_docentes(self):
        print("Lista de docentes:")
        for docente in self.__docentes:
            docente.mostrar_docente()
    
    def listar_grados(self):
        print("Lista de grados:")
        for grado in self.__grados:
            grado.mostrar_grado()    


    def listar_aulas(self):
        print("Lista de aulas:")
        for aula in self.__aulas:
            aula.mostrar_aula()
    
    def listar_asistencias(self):
        print("Lista de asistencias:")
        for asistencia in self.__asistencias:
            asistencia.mostrar_asistencia()

    def listar_fechas_asistencias(self):
        print("Lista de fechas de asistencias:")
        for asistencia in self.__asistencias: 
            print(asistencia.get_fecha().strftime("%d/%m/%Y"))


    def listar_asistencias_con_excusa(self):
        print("Lista de asistencias con excusa:")
        for asistencia in self.__asistencias:
            if asistencia.tiene_excusa():
                asistencia.mostrar_asistencia()

    def listar_asistencias_sin_excusa(self):
        print("Lista de asistencias sin excusa:")
        for asistencia in self.__asistencias:
            if not asistencia.tiene_excusa():
                asistencia.mostrar_asistencia()

    def get_grados(self):
        return self.__grados   
    
    def get_aulas(self):
        return self.__aulas
    
    def get_listar_asistencias_con_excusa(self):    
        return self.__asistencias
    
    def get_listar_asistencias_sin_excusa(self):  
        return self.__asistencias

    def registrar_excusa(self, id_asistencia, excusa):
        """Registra una excusa para una asistencia específica"""
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_asistencia:
                asistencia.establecer_excusa(excusa)
                return True
        return False
    
    def buscar_asistencias_con_excusa(self):
        """Retorna todas las asistencias que tienen excusa"""
        asistencias_con_excusa = []
        for asistencia in self.__asistencias:
            if asistencia.tiene_excusa():
                asistencias_con_excusa.append(asistencia)
        return asistencias_con_excusa
    
    def buscar_asistencias_sin_excusa(self):
        """Retorna todas las asistencias que no tienen excusa"""
        asistencias_sin_excusa = []
        for asistencia in self.__asistencias:
            if not asistencia.tiene_excusa():
                asistencias_sin_excusa.append(asistencia)
        return asistencias_sin_excusa
    
    def buscar_asistencia_por_id(self, id_asistencia):
        """Busca una asistencia específica por su ID"""
        for asistencia in self.__asistencias:
            if asistencia.get_id_asistencia() == id_asistencia:
                return asistencia
        return None