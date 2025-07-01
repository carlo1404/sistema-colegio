from os import system
from estudiante import Estudiante
from datetime import datetime, date 
from colegio import Colegio
from docente import Docente 
from grado import Grado 
from aula import Aula 
from asistencia import Asistencia

class Menu:
    def __init__(self):
        self.colegio = Colegio()
        self.grados = 0


    def deshabilitar_habilitar_estudiante(self):
        system("cls")
        print("=== Deshabilitar/Habilitar estudiante ===")
        try:
            id = int(input("ID del estudiante: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return  
                
            # Verificar si el estudiante existe
            estudiante_existe = self.colegio.buscar_estudiante(id)
            if estudiante_existe == -1:
                print("No se encontró el estudiante con ese ID")
                input("Presione Enter para continuar...")
                return
                
            self.colegio.deshabilitar_habilitar_estudiante(id)
            print("Estado del estudiante actualizado exitosamente!")
            input("Presione Enter para continuar...")
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")

    def deshabilitar_habilitar_docente(self):
        system("cls")
        print("=== Deshabilitar/Habilitar docente ===")
        try:
            id = int(input("ID del docente: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            # Verificar si el docente existe
            docente_existe = self.colegio.buscar_docente(id)
            if docente_existe == -1:
                print("No se encontró el docente con ese ID")
                input("Presione Enter para continuar...")
                return
                
            self.colegio.deshabilitar_habilitar_docente(id)
            print("Estado del docente actualizado exitosamente!")
            input("Presione Enter para continuar...")

        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")
    def deshabilitar_habilitar_grado(self):
        system("cls")
        print("=== Deshabilitar/Habilitar grado ===")
        try:
            id = int(input("ID del grado: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            grado_existe = self.colegio.buscar_grado(id)
            if grado_existe == -1:
                print("No se encontró el grado con ese ID")
                input("Presione Enter para continuar...")
                return

            self.colegio.deshabilitar_habilitar_grado(id)
            print("Estado del grado actualizado exitosamente!")
            input("Presione Enter para continuar...")
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")
    
    def deshabilitar_habilitar_aula(self):
        system("cls")
        print("=== Deshabilitar/Habilitar aula ===")
        try:
            id = int(input("ID del aula: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            aula_existente = self.colegio.buscar_aulas(id)
            if aula_existente == -1:
                print("No se encontró el aula con ese ID")
                input("Presione Enter para continuar...")
                return
            self.colegio.deshabilitar_habilitar_aula(id)
            print("Estado del grado actualizado exitosamente!")
            input("Presione Enter para continuar...")
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")
    def registrar_estudiante(self):
        system("cls")
        try:
            print("=== Registro de Estudiante ===")
            
            # Validar ID
            id = int(input("ID del estudiante: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            
            # Verificar que el ID no exista ya
            estudiantes_existentes = self.colegio.get_estudiantes()
            for estudiante_existente in estudiantes_existentes:
                if estudiante_existente.get_id() == id:
                    print("Error - El ID ya existe")
                    input("Presione Enter para continuar...")
                    return

            # Validar nombre
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(nombre) < 2:
                print("Error - El nombre debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not nombre.replace(' ', '').isalpha():
                print("Error - El nombre solo puede contener letras")
                input("Presione Enter para continuar...")
                return
                
            # Validar apellido
            apellido = input("Apellido: ").strip()
            if not apellido:
                print("Error - El apellido no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(apellido) < 2:
                print("Error - El apellido debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not apellido.replace(' ', '').isalpha():
                print("Error - El apellido solo puede contener letras")
                input("Presione Enter para continuar...")
                return
                
            # Validar edad
            edad = int(input("Edad (5-18): "))
            if edad < 5 or edad > 18:
                print("Error - La edad debe estar entre 5 y 18 años")
                input("Presione Enter para continuar...")
                return
                
            # Validar curso
            curso = int(input("Curso (1-11): "))
            if curso < 1 or curso > 11:
                print("Error - El curso debe estar entre 1 y 11")
                input("Presione Enter para continuar...")
                return
                
            # Crear y registrar estudiante
            estudiante = Estudiante(nombre, apellido, edad, curso, id)
            if self.colegio.adicionar_estudiante(estudiante):
                print("✓ Estudiante registrado exitosamente!")
                print(f"  - ID: {id}")
                print(f"  - Nombre: {nombre} {apellido}")
                print(f"  - Edad: {edad}")
                print(f"  - Curso: {curso}")
                input("Presione Enter para continuar...")
                return
            else:
                print("Error - No se pudo registrar el estudiante")
                input("Presione Enter para continuar...")
                return
                
        except ValueError:
            print("Error - Se esperaba un número válido")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione Enter para continuar...")


    def modificar_estudiante(self):
        system('cls')
        print('*')
        print('Modificar estudiante')
        print('*')
        
        try:
            print('Ingrese id del estudiante')
            id = int(input('-> '))
            if id <= 0:
                print('Error - El ID debe ser mayor a cero')
                input('Presione Enter para continuar...')
                return
                
            validar = self.colegio.buscar_estudiante(id)
            if validar == -1:
                print('No se encuentra el estudiante con ese ID')
                input('Presione Enter para continuar...')
                return
                
            system('cls')
            print('*')
            print('Elija entre las siguientes opciones')
            
            while True:               
                print('*')
                print('a. Nombre del estudiante.')
                print('b. Apellido del estudiante.')
                print('c. Edad del estudiante.')
                print('d. Curso del estudiante.')
                print('e. Salir')
                print('*')

                try:
                    opcion = str(input("Ingrese opcion: "))
                    opcion = opcion.lower()
                    
                    if opcion == 'a':
                        get_nombre = self.colegio.get_estudiante(id)
                        
                        if get_nombre == -1:
                            print('No se encontró el estudiante')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Nombre actual: {get_nombre}')
                        print('Ingrese el nuevo nombre: ')
                        nuevo_nombre = str(input('-> '))
                        
                        if nuevo_nombre == '':
                            print('El nombre no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_nombre) < 2:
                            print('El nuevo nombre debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_nombre.replace(' ', '').isalpha():
                            print('El nombre solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_nombre = self.colegio.establecer_nuevo_nombre_estudiante(nuevo_nombre, id)
                        if establecer_nuevo_nombre == True:
                            print('Nombre actualizado exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'b':
                        get_apellido = self.colegio.get_apellido_estudiante(id)
                        
                        if get_apellido == -1:
                            print('No se encontró el estudiante')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Apellido actual: {get_apellido}')
                        print('Ingrese el nuevo apellido: ')
                        nuevo_apellido = str(input('-> '))
                        
                        if nuevo_apellido == '':
                            print('El apellido no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_apellido) < 2:
                            print('El apellido debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_apellido.replace(' ', '').isalpha():
                            print('El apellido solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_apellido = self.colegio.establecer_nuevo_apellido_estudiante(nuevo_apellido, id)
                        if establecer_nuevo_apellido == True:
                            print('Apellido actualizado exitosamente!')
                            input('Presione Enter para continuar...')
                            return True

                    elif opcion == 'c':
                        get_edad = self.colegio.get_edad_estudiante(id)
                        
                        if get_edad == -1:
                            print('No se encontró el estudiante')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Edad actual: {get_edad}')
                        print('Ingrese la nueva edad: ')
                        nueva_edad = int(input('-> '))
                        
                        if nueva_edad < 5 or nueva_edad > 18:
                            print('Ingrese una edad válida (5-18 años)')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nueva_edad = self.colegio.establecer_nueva_edad_estudiante(nueva_edad, id)
                        if establecer_nueva_edad == True:
                            print('Edad actualizada exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'd':
                        get_curso = self.colegio.get_curso_estudiante(id)
                        
                        if get_curso == -1:
                            print('No se encontró el estudiante')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Curso actual: {get_curso}')
                        print('Ingrese el nuevo curso: ')
                        nuevo_curso = int(input('-> '))
                        
                        if nuevo_curso < 1 or nuevo_curso > 11:
                            print('Ingrese un curso válido (1-11)')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_curso = self.colegio.establecer_nuevo_curso_estudiante(nuevo_curso, id)
                        if establecer_nuevo_curso == True:
                            print('Curso actualizado exitosamente!')
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'e':
                        system('cls')
                        print('Saliendo del menú de modificación')
                        return True
                    
                    else:
                        print('Opción inválida')
                        input('Presione Enter para continuar...')
                        
                except ValueError:
                    print('Error, debe ingresar un dato válido')
                    input('Presione Enter para continuar...')
                    
        except ValueError:
            print('Error - El ID debe ser un número válido')
            input('Presione Enter para continuar...')

    def buscar_estudiante(self):
        system("cls")
        print("=== Buscar estudiante ===")
        try:
            id = int(input("ID del estudiante: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            resultado = self.colegio.buscar_estudiante(id)
            input()
            if resultado == -1:
                print("No se encontró el estudiante con ese ID")
                input("Presione Enter para continuar...")
                return -1
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")

    def buscar_docentes(self):
        system("cls")
        print("=== Buscar docente ===")
        try:
            id = int(input("ID del docente: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            resultado = self.colegio.buscar_docentes(id)
            input()
            if resultado == -1:
                print("No se encontró el docente con ese ID")
                input("Presione Enter para continuar...")
                return -1
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")
            return -1

    def buscar_grado(self):
        system("cls")
        print("=== Buscar grado ===")
        try:
            id = int(input("ID del grado: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            resultado = self.colegio.buscar_grado(id)
            input()
            if resultado == -1:
                print("No se encontró el grado con ese ID")
                input("Presione Enter para continuar...")
                return -1
            print(resultado)
            return
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")


    def buscar_aula(self):
        system("cls")
        print("=== Buscar aula  ===")
        try:
            id = int(input("ID del aula: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            resultado = self.colegio.buscar_aula(id)
            input()
            if resultado == -1:
                print("No se encontró el grado con ese ID")
                input("Presione Enter para continuar...")
                return -1
            print(resultado)
            return
        except ValueError:
            print("Error - El ID debe ser un número válido")
            input("Presione Enter para continuar...")

    def registrar_docente(self):
        system("cls")
        try:
            print("=== Registro de Docente ===")
            id = int(input("ID del docente: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            nombre = str(input("Nombre: "))
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(nombre) < 2:
                print("Error - El nombre debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not nombre.replace(' ', '').isalpha():
                print("Error - El nombre solo puede contener letras")
                input("Presione Enter para continuar...")
                return
                
            apellido = str(input("Apellido: "))
            if apellido == "":
                print("Error - El apellido no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(apellido) < 2:
                print("Error - El apellido debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not apellido.replace(' ', '').isalpha():
                print("Error - El apellido solo puede contener letras")
                input("Presione Enter para continuar...")
                return
            
            grado = int(input("grado (1-20): "))
            if self.grados >= 20:
                print("No se peuden crear mas de 20 grados")
                input()
                return -1
            if grado < 1 or grado > 20:
                print("Error - El grado debe ser un número entre 1 y 20")
                input("Presione Enter para continuar...")
                return
            
            lista_materias = self.colegio.get_materias()
            if not lista_materias:
                print("Error - No hay materias disponibles")
                input("Presione Enter para continuar...")
                return
                
            print("Materias disponibles:")
            for i, materia in enumerate(lista_materias, 1):
                print(f"{i}. {materia}")
                
            materia = int(input("Elija el número de la materia: "))
            if materia < 1 or materia > len(lista_materias):
                print(f"Error - La materia debe ser un número entre 1 y {len(lista_materias)}")
                input("Presione Enter para continuar...")
                return
                
            materia_seleccionada = self.colegio.descontar_materias(materia)
            docente = Docente(nombre, apellido, materia_seleccionada, grado, id)
            if self.colegio.adicionar_docente(docente) == True:
                self.grados += 1
                print("Docente registrado exitosamente!")
                input("Presione Enter para continuar...")
                return
                
        except ValueError:
            print('Error - Debe ingresar un dato válido')
            input('Presione Enter para continuar...')
    def registrar_grado(self):
        system("cls")
        try:
            print("=== Registro de grado ===")
            id = int(input("ID del grado: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            # Verificar que el ID no exista ya
            grados_existentes = self.colegio.get_grados()
            for grado_existente in grados_existentes:
                if grado_existente.get_id_grado() == id:
                    print("Error - El ID ya existe")
                    input("Presione Enter para continuar...")
                    return
                
            nombre = str(input("Nombre: "))
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(nombre) < 2:
                print("Error - El nombre debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not nombre.replace(' ', '').isalpha():
                print("Error - El nombre solo puede contener letras")
                input("Presione Enter para continuar...")
                return
                
            # Mostrar aulas disponibles
            aulas_disponibles = self.colegio.get_aulas()
            if not aulas_disponibles:
                print("Error - No hay aulas disponibles")
                input("Presione Enter para continuar...")
                return
                
            print("Aulas disponibles:")
            for i, aula in enumerate(aulas_disponibles, 1):
                print(f"{i}. {aula.get_nombre_aula()} - Capacidad: {aula.get_capacidad_aula()}")
                
            aula_seleccionada = int(input("Seleccione el número del aula: "))
            if aula_seleccionada <= 0 or aula_seleccionada > len(aulas_disponibles):
                print(f"Error - Debe seleccionar un número entre 1 y {len(aulas_disponibles)}")
                input("Presione Enter para continuar...")
                return
                
            aula = aulas_disponibles[aula_seleccionada - 1].get_id_aula()
            
            cantidad_estudiantes = int(input("Cantidad de estudiantes (max-10): "))
            if cantidad_estudiantes < 1 or cantidad_estudiantes > 10:
                print("Error - La cantidad debe ser un número entre 1 y 10")
                input("Presione Enter para continuar...")
                return
            
            grado = Grado(nombre, aula, cantidad_estudiantes, id)
            if self.colegio.adicionar_grado(grado) == True:
                self.grados += 1
                print("Grado registrado exitosamente!")
                input("Presione Enter para continuar...")
                return
                
        except ValueError:
            print('Error - Debe ingresar un dato válido')
            input('Presione Enter para continuar...') 

    def registrar_aula(self):
        system("cls")
        try:
            print("=== Registro de aula ===")
            id = int(input("ID del aula: "))
            if id <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
                
            # Verificar que el ID no exista ya
            aulas_existentes = self.colegio.get_aulas()
            for aula_existente in aulas_existentes:
                if aula_existente.get_id_aula() == id:
                    print("Error - El ID ya existe")
                    input("Presione Enter para continuar...")
                    return
                
            nombre = str(input("Nombre: "))
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            if len(nombre) < 2:
                print("Error - El nombre debe tener al menos 2 letras")
                input("Presione Enter para continuar...")
                return
            if not nombre.replace(' ', '').isalpha():
                print("Error - El nombre solo puede contener letras")
                input("Presione Enter para continuar...")
                return

            capacidad = int(input("Capacidad del aula: "))
            if capacidad < 1 or capacidad > 15:
                print("Error - La capacidad debe ser un número entre 1 y 15")
                input("Presione Enter para continuar...")
                return
            
            aula = Aula(nombre, capacidad, id)
            if self.colegio.adicionar_aula(aula) == True:
                print("Aula registrada exitosamente!")
                input("Presione Enter para continuar...")
                return
                
        except ValueError:
            print('Error - Debe ingresar un dato válido')
            input('Presione Enter para continuar...') 

    def modificar_docente(self):
        system('cls')
        print('*')
        print('Modificar docente')
        print('*')
        
        try:
            print('Ingrese id del docente')
            id = int(input('-> '))
            if id <= 0:
                print('Error - El ID debe ser mayor a cero')
                input('Presione Enter para continuar...')
                return
                
            validar = self.colegio.buscar_docente(id)
            if validar == -1:
                print('No se encuentra el docente con ese ID')
                input('Presione Enter para continuar...')
                return
                
            system('cls')
            print('*')
            print('Elija entre las siguientes opciones')
            
            while True:               
                print('*')
                print('a. Nombre del docente.')
                print('b. Apellido del docente.')
                print('c. grado del docente')
                print('d. Materia del docente.')
                print('e. Salir')
                print('*')

                try:
                    opcion = str(input("Ingrese opcion: "))
                    opcion = opcion.lower()
                    
                    if opcion == 'a':
                        get_nombre_docente = self.colegio.get_nombre_docente(id)
                        
                        if get_nombre_docente == -1:
                            print('No se encontró el docente')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Nombre actual: {get_nombre_docente}')
                        print('Ingrese el nuevo nombre: ')
                        nuevo_nombre = str(input('-> '))
                        
                        if nuevo_nombre == '':
                            print('El nombre no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_nombre) < 2:
                            print('El nuevo nombre debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_nombre.replace(' ', '').isalpha():
                            print('El nombre solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_nombre = self.colegio.establecer_nuevo_nombre_docente(nuevo_nombre, id)
                        if establecer_nuevo_nombre == True:
                            print('Nombre actualizado exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'b':
                        get_apellido = self.colegio.get_apellido_docente(id)
                        
                        if get_apellido == -1:
                            print('No se encontró el docente')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Apellido actual: {get_apellido}')
                        print('Ingrese el nuevo apellido: ')
                        nuevo_apellido = str(input('-> '))
                        
                        if nuevo_apellido == '':
                            print('El apellido no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_apellido) < 2:
                            print('El apellido debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_apellido.replace(' ', '').isalpha():
                            print('El apellido solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_apellido = self.colegio.establecer_nuevo_apellido_docente(nuevo_apellido, id)
                        if establecer_nuevo_apellido == True:
                            print('Apellido actualizado exitosamente!')
                            input('Presione Enter para continuar...')
                            return True

                    elif opcion == 'c':
                        get_grado = self.colegio.get_aula_docente(id)
                        
                        if get_grado == -1:
                            print('No se encontró el docente')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'grado actual: {get_grado}')
                        print('Ingrese la nueva grado: ')
                        nueva_grado = int(input('-> '))
                        
                        if nueva_grado < 1 or nueva_grado > 20:
                            print('Ingrese un grado válida (1-20)')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nueva_grado = self.colegio.establecer_nueva_grado_docente(nueva_grado, id)
                        if establecer_nueva_grado == True:
                            print('grado actualizada exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'd':
                        get_materia = self.colegio.get_materia_docente(id)
                        
                        if get_materia == -1:
                            print('No se encontró el docente')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Materia actual: {get_materia}')
                        
                        # Obtener materias disponibles
                        lista_materias = self.colegio.get_materias()
                        if not lista_materias:
                            print('No hay materias disponibles para asignar')
                            input('Presione Enter para continuar...')
                            return
                            
                        print('Materias disponibles:')
                        for i, materia in enumerate(lista_materias, 1):
                            print(f'{i}. {materia}')
                            
                        print('Ingrese el número de la nueva materia: ')
                        try:
                            nueva_materia_num = int(input('-> '))
                            
                            if nueva_materia_num <= 0:
                                print('Error - Debe ingresar un número mayor a 0')
                                input('Presione Enter para continuar...')
                                return
                                
                            if nueva_materia_num > len(lista_materias):
                                print(f'Error - Debe ingresar un número entre 1 y {len(lista_materias)}')
                                input('Presione Enter para continuar...')
                                return
                                
                            # Obtener la materia seleccionada
                            nueva_materia = self.colegio.descontar_materias(nueva_materia_num)
                            
                            establecer_nueva_materia = self.colegio.establecer_nueva_materia_docente(nueva_materia, id)
                            if establecer_nueva_materia == True:
                                print('Materia actualizada exitosamente!')
                                input('Presione Enter para continuar...')
                                return True
                                
                        except ValueError:
                            print('Error - Debe ingresar un número válido')
                            input('Presione Enter para continuar...')
                            return
                            
                    elif opcion == 'e':
                        system('cls')
                        print('Saliendo del menú de modificación')
                        return True
                    
                    else:
                        print('Opción inválida')
                        input('Presione Enter para continuar...')
                        
                except ValueError:
                    print('Error, debe ingresar un dato válido')
                    input('Presione Enter para continuar...')
                    
        except ValueError:
            print('Error - El ID debe ser un número válido')
            input('Presione Enter para continuar...')

    def modificar_grado(self):
        system('cls')
        print('*')
        print('Modificar grado')
        print('*')
        
        try:
            print('Ingrese id del grado')
            id = int(input('-> '))
            if id <= 0:
                print('Error - El ID debe ser mayor a cero')
                input('Presione Enter para continuar...')
                return
                
            validar = self.colegio.buscar_grado(id)
            if validar == -1:
                print('No se encuentra el grado con ese ID')
                input('Presione Enter para continuar...')
                return
                
            system('cls')
            print('*')
            print('Elija entre las siguientes opciones')
            
            while True:               
                print('*')
                print('a. Nombre del grado.')
                print('b. Numero del aula.')
                print('c. Cantidad estudiantes')
                print('d. Salir')
                print('*')

                try:
                    opcion = str(input("Ingrese opcion: "))
                    opcion = opcion.lower()
                    
                    if opcion == 'a':
                        get_nombre_grado = self.colegio.get_nombre_grado(id)
                        
                        if get_nombre_grado == -1:
                            print('No se encontró el grado')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Nombre actual: {get_nombre_grado}')
                        print('Ingrese el nuevo nombre: ')
                        nuevo_nombre = str(input('-> '))
                        
                        if nuevo_nombre == '':
                            print('El nombre no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_nombre) < 2:
                            print('El nuevo nombre debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_nombre.replace(' ', '').isalpha():
                            print('El nombre solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_nombre = self.colegio.establecer_nuevo_nombre_grado(nuevo_nombre, id)
                        if establecer_nuevo_nombre == True:
                            print('Nombre actualizado exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'b':
                        get_num_aula = self.colegio.get_num_aula(id)
                        
                        if get_num_aula == -1:
                            print('No se encontró el grado')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Aula actual: {get_num_aula}')
                        
                        # Mostrar aulas disponibles
                        aulas_disponibles = self.colegio.get_aulas()
                        if not aulas_disponibles:
                            print('No hay aulas disponibles')
                            input('Presione Enter para continuar...')
                            return
                            
                        print('Aulas disponibles:')
                        for i, aula in enumerate(aulas_disponibles, 1):
                            print(f'{i}. {aula.get_nombre_aula()} - Capacidad: {aula.get_capacidad_aula()}')
                            
                        nueva_aula = int(input('Seleccione el número del aula: '))
                        
                        if nueva_aula <= 0 or nueva_aula > len(aulas_disponibles):
                            print(f'Error - Debe seleccionar un número entre 1 y {len(aulas_disponibles)}')
                            input('Presione Enter para continuar...')
                            return
                            
                        aula_seleccionada = aulas_disponibles[nueva_aula - 1].get_id_aula()
                        establecer_nueva_aula = self.colegio.establecer_nueva_aula(aula_seleccionada, id)
                        
                        if establecer_nueva_aula == True:
                            print('Aula actualizada exitosamente!')
                            input('Presione Enter para continuar...')
                            return True

                    elif opcion == 'c':
                        get_cantidad = self.colegio.get_cantidad_grados(id)
                        
                        if get_cantidad == -1:
                            print('No se encontró el grado')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Cantidad actual: {get_cantidad}')
                        nueva_cantidad = int(input('Ingrese la nueva cantidad: '))
                        
                        if nueva_cantidad <= 0 or nueva_cantidad > 10:
                            print('La cantidad debe ser un número entre 1 y 10')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nueva_cantidad = self.colegio.establecer_nueva_cantidad_grado(nueva_cantidad, id)
                        if establecer_nueva_cantidad == True:
                            print('Cantidad de estudiantes actualizada exitosamente!')
                            input('Presione Enter para continuar...')
                            return True

                    elif opcion == 'd':
                        system('cls')
                        print('Saliendo del menú de modificación')
                        return True
                    
                    else:
                        print('Opción inválida')
                        input('Presione Enter para continuar...')
                        
                except ValueError:
                    print('Error, debe ingresar un dato válido')
                    input('Presione Enter para continuar...')
                    
        except ValueError:
            print('Error - El ID debe ser un número válido')
            input('Presione Enter para continuar...')
    def modificar_aula(self):
        system('cls')
        print('*')
        print('Modificar aula')
        print('*')
        
        try:
            print('Ingrese id del aula')
            id = int(input('-> '))
            if id <= 0:
                print('Error - El ID debe ser mayor a cero')
                input('Presione Enter para continuar...')
                return
                
            validar = self.colegio.buscar_aula(id)
            if validar == -1:
                print('No se encuentra el aula con ese ID')
                input('Presione Enter para continuar...')
                return
                
            system('cls')
            print('*')
            print('Elija entre las siguientes opciones')
            
            while True:               
                print('*')
                print('a. Nombre del aula.')
                print('b. Capacidad del aula.')
                print('c. Salir')
                print('*')

                try:
                    opcion = str(input("Ingrese opcion: "))
                    opcion = opcion.lower()
                    
                    if opcion == 'a':
                        get_nombre_aula = self.colegio.get_nombre_aula(id)
                        
                        if get_nombre_aula == -1:
                            print('No se encontró el aula')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Nombre actual: {get_nombre_aula}')
                        print('Ingrese el nuevo nombre: ')
                        nuevo_nombre = str(input('-> '))
                        
                        if nuevo_nombre == '':
                            print('El nombre no puede estar vacío')
                            input('Presione Enter para continuar...')
                            return
                            
                        if len(nuevo_nombre) < 2:
                            print('El nuevo nombre debe tener al menos 2 letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        if not nuevo_nombre.replace(' ', '').isalpha():
                            print('El nombre solo puede contener letras')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nuevo_nombre = self.colegio.establecer_nuevo_nombre_aula(nuevo_nombre, id)
                        if establecer_nuevo_nombre == True:
                            print('Nombre actualizado exitosamente!')                           
                            input('Presione Enter para continuar...')
                            return True
                            
                    elif opcion == 'b':
                        get_capacidad = self.colegio.get_capacidad_aula(id)
                        
                        if get_capacidad == -1:
                            print('No se encontró el aula')
                            input('Presione Enter para continuar...')
                            return
                            
                        print(f'Capacidad actual: {get_capacidad}')
                        nueva_capacidad = int(input('Ingrese la nueva capacidad: '))
                        
                        if nueva_capacidad < 1 or nueva_capacidad > 15:
                            print('La capacidad debe ser un número entre 1 y 15')
                            input('Presione Enter para continuar...')
                            return
                            
                        establecer_nueva_capacidad = self.colegio.establecer_nueva_capacidad_aula(nueva_capacidad, id)
                        
                        if establecer_nueva_capacidad == True:
                            print('Capacidad actualizada exitosamente!')
                            input('Presione Enter para continuar...')
                            return True
                
                    elif opcion == 'c':
                        system('cls')
                        print('Saliendo del menú de modificación')
                        return True
                    
                    else:
                        print('Opción inválida')
                        input('Presione Enter para continuar...')
                        
                except ValueError:
                    print('Error, debe ingresar un dato válido')
                    input('Presione Enter para continuar...')
                    
        except ValueError:
            print('Error - El ID debe ser un número válido')
            input('Presione Enter para continuar...')

    def registrar_asistencia(self):
        system('cls')
        print("=== Registrar Asistencia ===")
        
        try:
            # 1. Validar ID de fecha
            id_fecha = int(input("Ingresa el id de la fecha a registrar: "))
            if id_fecha <= 0:
                print("Error - El ID debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
            
            # Verificar que el ID no exista ya
            asistencias_existentes = self.colegio.get_asistencias()
            for asistencia_existente in asistencias_existentes:
                if asistencia_existente.get_id_asistencia() == id_fecha:
                    print("Error - El ID de fecha ya existe")
                    input("Presione Enter para continuar...")
                    return
            
            # 2. Mostrar docentes disponibles
            docentes_habilitados = self.colegio.get_docentes_habilitados()
            
            if not docentes_habilitados:
                print("No hay docentes habilitados para registrar asistencia")
                input("Presione Enter para continuar...")
                return
                
            print("\nDocentes disponibles:")
            for i, docente in enumerate(docentes_habilitados, 1):
                print(f"{i}. {docente.get_nombre_docente()} {docente.get_apellido_docente()} - {docente.get_materia_docente()}")
            
            # 3. Seleccionar docente
            print("\nSeleccione el docente encargado:")
            docente_seleccionado = int(input("-> "))
            
            if docente_seleccionado <= 0 or docente_seleccionado > len(docentes_habilitados):
                print(f"Error - Debe seleccionar un número entre 1 y {len(docentes_habilitados)}")
                input("Presione Enter para continuar...")
                return
            
            docente = docentes_habilitados[docente_seleccionado - 1]
            id_docente = docente.get_id_docente()
            
            # 4. Ingresar fecha completa
            print("Ingrese la fecha de la asistencia:")
            
            print("Año:")
            año = int(input("-> "))
            
            if año <= 0:
                print("Error - El año debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if año > date.today().year:
                print("Error - No puede registrar asistencia para años futuros")
                input("Presione Enter para continuar...")
                return
                
            if año < 2020:  
                print("Error - El año debe ser mayor a 2020")
                input("Presione Enter para continuar...")
                return
            
            print("Mes (1-12):")
            mes = int(input("-> "))
            
            if mes <= 0:
                print("Error - El mes debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if mes > 12:
                print("Error - El mes debe estar entre 1 y 12")
                input("Presione Enter para continuar...")
                return
            
            print("Día (1-31):")
            dia = int(input("-> "))
            
            if dia <= 0:
                print("Error - El día debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if dia > 31:
                print("Error - El día debe estar entre 1 y 31")
                input("Presione Enter para continuar...")
                return
            
            # Validar que la fecha sea válida
            try:
                fecha_asistencia = date(año, mes, dia)
            except ValueError:
                print("Error - Fecha inválida (ej: 31 de febrero no existe)")
                input("Presione Enter para continuar...")
                return
            
            # Validar que no sea fecha futura
            if fecha_asistencia > date.today():
                print("Error - No puede registrar asistencia para fechas futuras")
                input("Presione Enter para continuar...")
                return
            
            # 5. Mostrar estudiantes disponibles
            estudiantes_habilitados = self.colegio.get_estudiantes_habilitados()
            
            if not estudiantes_habilitados:
                print("No hay estudiantes habilitados para registrar asistencia")
                input("Presione Enter para continuar...")
                return
                
            print(f"\nEstudiantes disponibles (Total: {len(estudiantes_habilitados)}):")
            for i, estudiante in enumerate(estudiantes_habilitados, 1):
                print(f"{i}. {estudiante.get_nombre()} {estudiante.get_apellido()} - Curso: {estudiante.get_curso()}")
            
            # 6. Ingresar cantidad de estudiantes que asistieron
            print(f"\n¿Cuántos estudiantes asistieron? (máximo {len(estudiantes_habilitados)}):")
            cantidad_asistentes = int(input("-> "))
            
            if cantidad_asistentes <= 0:
                print("Error - La cantidad de asistentes debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if cantidad_asistentes > len(estudiantes_habilitados):
                print(f"Error - No puede haber más asistentes ({cantidad_asistentes}) que estudiantes disponibles ({len(estudiantes_habilitados)})")
                input("Presione Enter para continuar...")
                return
            
            # 7. Registrar la asistencia
            asistencia = Asistencia(id_fecha, id_docente, fecha_asistencia, cantidad_asistentes)

            if self.colegio.registrar_asistencia(asistencia):
                print(f"\n✓ Asistencia registrada exitosamente!")
                print(f"  - Docente: {docente.get_nombre_docente()} {docente.get_apellido_docente()}")
                print(f"  - Materia: {docente.get_materia_docente()}")
                print(f"  - Fecha: {fecha_asistencia.strftime('%d/%m/%Y')}")
                print(f"  - Estudiantes que asistieron: {cantidad_asistentes}")
                input("Presione Enter para continuar...")
                return
            else:
                print("Error - No se pudo registrar la asistencia")
                input("Presione Enter para continuar...")
                
        except ValueError:
            print("Error - Debe ingresar un número válido")
            input("Presione Enter para continuar...")

    def buscar_asistencia(self):
        system('cls')
        print("=== Buscar Asistencia por Fecha ===")
        
        try:
            print("Ingrese la fecha a buscar:")
            
            print("Año:")
            año = int(input("-> "))
            
            if año <= 0:
                print("Error - El año debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if año < 2020:
                print("Error - El año debe ser mayor a 2020")
                input("Presione Enter para continuar...")
                return
            
            print("Mes (1-12):")
            mes = int(input("-> "))
            
            if mes <= 0:
                print("Error - El mes debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if mes > 12:
                print("Error - El mes debe estar entre 1 y 12")
                input("Presione Enter para continuar...")
                return
            
            print("Día (1-31):")
            dia = int(input("-> "))
            
            if dia <= 0:
                print("Error - El día debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            if dia > 31:
                print("Error - El día debe estar entre 1 y 31")
                input("Presione Enter para continuar...")
                return
            
            # Validar que la fecha sea válida
            try:
                fecha_busqueda = date(año, mes, dia)
            except ValueError:
                print("Error - Fecha inválida (ej: 31 de febrero no existe)")
                input("Presione Enter para continuar...")
                return
            
            # Buscar asistencias
            asistencias_encontradas = self.colegio.buscar_asistencias_por_fecha(fecha_busqueda)
            
            if not asistencias_encontradas:
                print(f"\nNo se encontraron asistencias para la fecha {fecha_busqueda.strftime('%d/%m/%Y')}")
                input("Presione Enter para continuar...")
                return
            
            print(f"\nAsistencias encontradas para {fecha_busqueda.strftime('%d/%m/%Y')}:")
            print("=" * 60)
            
            for i, asistencia in enumerate(asistencias_encontradas, 1):
                id_docente = asistencia.get_id_asistencia()
                cantidad = asistencia.get_cantidad_estudiantes()
                
                # Buscar información del docente
                nombre_docente = self.colegio.get_nombre_docente(id_docente)
                apellido_docente = self.colegio.get_apellido_docente(id_docente)
                materia_docente = self.colegio.get_materia_docente(id_docente)
                
                if nombre_docente != -1:
                    print(f"{i}. Docente: {nombre_docente} {apellido_docente}")
                    print(f"   Materia: {materia_docente}")
                    print(f"   Estudiantes que asistieron: {cantidad}")
                    print(f"   Estado: {asistencia.get_habilitado()}")
                    print("-" * 40)
                else:
                    print(f"{i}. Docente ID: {id_docente} (no encontrado)")
                    print(f"   Estudiantes que asistieron: {cantidad}")
                    print(f"   Estado: {asistencia.get_habilitado()}")
                    print("-" * 40)
            
            print(f"\nTotal de asistencias: {len(asistencias_encontradas)}")
            input("Presione Enter para continuar...")
            
        except ValueError:
            print("Error - Debe ingresar un número válido")
            input("Presione Enter para continuar...")

    def buscar_asistencia_por_id(self):
        system('cls')
        print("=== Buscar Asistencia por ID ===")
        
        try:
            id_asistencia = int(input("Ingrese el ID de la asistencia: "))
            if id_asistencia <= 0:
                print("Error - El ID debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
            
            # Buscar la asistencia
            asistencias = self.colegio.get_asistencias()
            asistencia_encontrada = None
            for asistencia in asistencias:
                if asistencia.get_id_asistencia() == id_asistencia:
                    asistencia_encontrada = asistencia
                    break
            
            if not asistencia_encontrada:
                print(f"No se encontró la asistencia con ID {id_asistencia}")
                input("Presione Enter para continuar...")
                return
            
            # Mostrar información de la asistencia
            print(f"\nAsistencia encontrada:")
            print("=" * 50)
            print(f"ID: {asistencia_encontrada.get_id_asistencia()}")
            print(f"Fecha: {asistencia_encontrada.get_fecha_asistencia().strftime('%d/%m/%Y')}")
            print(f"Estudiantes que asistieron: {asistencia_encontrada.get_cantidad_estudiantes()}")
            
            # Obtener información del docente
            id_docente = asistencia_encontrada.get_id_asistencia()
            nombre_docente = self.colegio.get_nombre_docente(id_docente)
            apellido_docente = self.colegio.get_apellido_docente(id_docente)
            materia_docente = self.colegio.get_materia_docente(id_docente)
            
            if nombre_docente != -1:
                print(f"Docente: {nombre_docente} {apellido_docente}")
                print(f"Materia: {materia_docente}")
            else:
                print(f"Docente ID: {id_docente} (no encontrado)")
            
            input("Presione Enter para continuar...")
            
        except ValueError:
            print("Error - Debe ingresar un número válido")
            input("Presione Enter para continuar...")

    def modificar_inasistencia(self):
        system('cls')
        print("=== Modificar Asistencia ===")
        try:
            print("Ingresa el id de la asistencia a modificar:")
            id_asistencia = int(input("-> "))
            if id_asistencia <= 0:
                print("Error - El ID debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            # Verificar si la asistencia existe
            asistencias = self.colegio.get_asistencias()
            asistencia_encontrada = None
            for asistencia in asistencias:
                if asistencia.get_id_asistencia() == id_asistencia:
                    asistencia_encontrada = asistencia
                    break
                    
            if not asistencia_encontrada:
                print("Error - No se encontró la asistencia con ese ID")
                input("Presione Enter para continuar...")
                return
            
            print(f"Asistencia actual:")
            print(f"  - Docente ID: {asistencia_encontrada.get_id_asistencia()}")
            print(f"  - Fecha: {asistencia_encontrada.get_fecha_asistencia().strftime('%d/%m/%Y')}")
            print(f"  - Estudiantes: {asistencia_encontrada.get_cantidad_estudiantes()}")
            
            print("\nIngrese la nueva cantidad de estudiantes:")
            nueva_cantidad = int(input("-> "))
            if nueva_cantidad <= 0:
                print("Error - La cantidad debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
                
            # Obtener estudiantes habilitados para validar
            estudiantes_habilitados = self.colegio.get_estudiantes_habilitados()
            if nueva_cantidad > len(estudiantes_habilitados):
                print(f"Error - No puede haber más estudiantes ({nueva_cantidad}) que estudiantes disponibles ({len(estudiantes_habilitados)})")
                input("Presione Enter para continuar...")
                return
            
            # Modificar la asistencia
            if self.colegio.modificar_inasistencia(asistencia_encontrada.get_id_asistencia(), 
                                                  asistencia_encontrada.get_fecha_asistencia(), 
                                                  nueva_cantidad):
                print("Asistencia modificada exitosamente!")
                input("Presione Enter para continuar...")
            else:
                print("Error - No se pudo modificar la asistencia")
                input("Presione Enter para continuar...")
                
        except ValueError:
            print("Error - Debe ingresar un número válido")
            input("Presione Enter para continuar...")


    def listar_estudiantes(self):
        system("cls")
        print("=== Listar estudiantes ===")
        try:
            lista_estudiantes = self.colegio.get_estudiantes()
            if not lista_estudiantes:
                print("No hay estudiantes registrados")
                input("Presione Enter para continuar...")
                return

            print("ID\tNombre\tApellido\tEdad\tCurso\tEstado")
            print("-" * 60)
            contador = 0
            for estudiante in lista_estudiantes:
                try:
                    id_est = estudiante.get_id()
                    nombre = estudiante.get_nombre()
                    apellido = estudiante.get_apellido()
                    edad = estudiante.get_edad()
                    curso = estudiante.get_curso()
                    estado = estudiante.get_habilitado()
                    
                    # Validar que todos los datos estén presentes
                    if all([id_est, nombre, apellido, edad, curso, estado]):
                        print(f"{id_est}\t{nombre}\t{apellido}\t{edad}\t{curso}\t{estado}")
                        contador += 1
                    else:
                        print(f"Error en datos del estudiante ID: {id_est}")
                except Exception as e:
                    print(f"Error al procesar estudiante: {e}")
                    continue

            print(f"\nTotal de estudiantes listados: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar estudiantes: {e}")
            input("Presione Enter para continuar...")

    def listar_docentes(self):
        system("cls")
        print("=== Listar docentes ===")
        try:
            lista_docentes = self.colegio.get_docentes_habilitados()
            if not lista_docentes:
                print("No hay docentes registrados")
                input("Presione Enter para continuar...")
                return

            print("ID\tNombre\tApellido\tMateria\tAula\tEstado")
            print("-" * 60)
            contador = 0
            for docente in lista_docentes:
                try:
                    id_doc = docente.get_id_docente()
                    nombre = docente.get_nombre_docente()
                    apellido = docente.get_apellido_docente()
                    materia = docente.get_materia_docente()
                    aula = docente.get_aula_docente()
                    estado = docente.get_habilitado()
                    
                    # Validar que todos los datos estén presentes
                    if all([id_doc, nombre, apellido, materia, aula, estado]):
                        print(f"{id_doc}\t{nombre}\t{apellido}\t{materia}\t{aula}\t{estado}")
                        contador += 1
                    else:
                        print(f"Error en datos del docente ID: {id_doc}")
                except Exception as e:
                    print(f"Error al procesar docente: {e}")
                    continue

            print(f"\nTotal de docentes listados: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar docentes: {e}")
            input("Presione Enter para continuar...")

    def listar_grados(self):
        system("cls")
        print("=== Listar grados ===")
        try:
            lista_grados = self.colegio.get_grados()
            if not lista_grados:
                print("No hay grados registrados")
                input("Presione Enter para continuar...")
                return

            print("ID\tNombre\tAula\tCantidad\tEstado")
            print("-" * 50)
            contador = 0
            for grado in lista_grados:
                try:
                    id_grado = grado.get_id_grado()
                    nombre = grado.get_nombre_grado()
                    aula = grado.get_aula_grado()
                    cantidad = grado.get_cantidad_grado()
                    estado = grado.get_habilitado()
                    
                    # Validar que todos los datos estén presentes
                    if all([id_grado, nombre, aula, cantidad, estado]):
                        print(f"{id_grado}\t{nombre}\t{aula}\t{cantidad}\t{estado}")
                        contador += 1
                    else:
                        print(f"Error en datos del grado ID: {id_grado}")
                except Exception as e:
                    print(f"Error al procesar grado: {e}")
                    continue

            print(f"\nTotal de grados listados: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar grados: {e}")
            input("Presione Enter para continuar...")

    def listar_aulas(self):
        system("cls")
        print("=== Listar aulas ===")
        try:
            lista_aulas = self.colegio.get_aulas()
            if not lista_aulas:
                print("No hay aulas registradas")
                input("Presione Enter para continuar...")
                return

            print("ID\tNombre\tCapacidad\tEstado")
            print("-" * 40)
            contador = 0
            for aula in lista_aulas:
                try:
                    id_aula = aula.get_id_aula()
                    nombre = aula.get_nombre_aula()
                    capacidad = aula.get_capacidad_aula()
                    estado = aula.get_habilitado()
                    
                    # Validar que todos los datos estén presentes
                    if all([id_aula, nombre, capacidad, estado]):
                        print(f"{id_aula}\t{nombre}\t{capacidad}\t{estado}")
                        contador += 1
                    else:
                        print(f"Error en datos del aula ID: {id_aula}")
                except Exception as e:
                    print(f"Error al procesar aula: {e}")
                    continue

            print(f"\nTotal de aulas listadas: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar aulas: {e}")
            input("Presione Enter para continuar...")

    def listar_asistencias_con_excusa(self):
        system("cls")
        print("=== Listar asistencias con excusa ===")
        
        try:
            asistencias_con_excusa = self.colegio.buscar_asistencias_con_excusa()
            
            if not asistencias_con_excusa:
                print("No hay asistencias con excusa registradas")
                input("Presione Enter para continuar...")
                return

            print("ID\tFecha\tDocente\tEstudiantes\tExcusa")
            print("-" * 80)
            contador = 0
            for asistencia in asistencias_con_excusa:
                try:
                    id_asist = asistencia.get_id_asistencia()
                    fecha = asistencia.get_fecha_asistencia()
                    estudiantes = asistencia.get_cantidad_estudiantes()
                    excusa = asistencia.get_excusa()
                    
                    # Obtener información del docente
                    nombre_docente = self.colegio.get_nombre_docente(id_asist)
                    apellido_docente = self.colegio.get_apellido_docente(id_asist)
                    docente_info = f"{nombre_docente} {apellido_docente}" if nombre_docente != -1 else f"ID: {id_asist}"
                    
                    # Truncar excusa si es muy larga
                    if excusa and len(excusa) > 30:
                        excusa = excusa[:27] + "..."
                    
                    # Validar que todos los datos estén presentes
                    if all([id_asist, fecha, estudiantes, excusa]):
                        print(f"{id_asist}\t{fecha.strftime('%d/%m/%Y')}\t{docente_info}\t{estudiantes}\t{excusa}")
                        contador += 1
                    else:
                        print(f"Error en datos de la asistencia ID: {id_asist}")
                except Exception as e:
                    print(f"Error al procesar asistencia: {e}")
                    continue
            
            print(f"\nTotal de asistencias con excusa listadas: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar asistencias con excusa: {e}")
            input("Presione Enter para continuar...")
    
    def listar_asistencias_sin_excusa(self):
        system("cls")
        print("=== Listar asistencias sin excusa ===")
        try:
            asistencias_sin_excusa = self.colegio.buscar_asistencias_sin_excusa()
            
            if not asistencias_sin_excusa:
                print("No hay asistencias sin excusa registradas")
                input("Presione Enter para continuar...")
                return

            print("ID\tFecha\tDocente\tEstudiantes\tEstado")
            print("-" * 60)
            contador = 0
            for asistencia in asistencias_sin_excusa:
                try:
                    id_asist = asistencia.get_id_asistencia()
                    fecha = asistencia.get_fecha_asistencia()
                    estudiantes = asistencia.get_cantidad_estudiantes()
                    estado = asistencia.get_habilitado()
                    
                    # Obtener información del docente
                    nombre_docente = self.colegio.get_nombre_docente(id_asist)
                    apellido_docente = self.colegio.get_apellido_docente(id_asist)
                    docente_info = f"{nombre_docente} {apellido_docente}" if nombre_docente != -1 else f"ID: {id_asist}"
                    
                    # Validar que todos los datos estén presentes
                    if all([id_asist, fecha, estudiantes, estado]):
                        print(f"{id_asist}\t{fecha.strftime('%d/%m/%Y')}\t{docente_info}\t{estudiantes}\t{estado}")
                        contador += 1
                    else:
                        print(f"Error en datos de la asistencia ID: {id_asist}")
                except Exception as e:
                    print(f"Error al procesar asistencia: {e}")
                    continue
            
            print(f"\nTotal de asistencias sin excusa listadas: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar asistencias sin excusa: {e}")
            input("Presione Enter para continuar...")

    def deshabilitar_habilitar_asistencia(self):
        system("cls")
        print("=== Deshabilitar/Habilitar asistencia ===")
        print("Función no implementada - Las asistencias no tienen estado habilitado/deshabilitado")
        input("Presione Enter para continuar...")

    def registrar_falta_con_excusa(self):
        system("cls")
        print("=== Registrar Falta con Excusa ===")
        try:
            # Mostrar asistencias disponibles
            asistencias = self.colegio.get_asistencias()
            if not asistencias:
                print("No hay asistencias registradas")
                input("Presione Enter para continuar...")
                return
            
            print("Asistencias disponibles:")
            print("ID\tFecha\tDocente\tEstudiantes")
            print("-" * 50)
            for asistencia in asistencias:
                # Obtener información del docente
                id_docente = asistencia.get_id_asistencia()
                nombre_docente = self.colegio.get_nombre_docente(id_docente)
                apellido_docente = self.colegio.get_apellido_docente(id_docente)
                docente_info = f"{nombre_docente} {apellido_docente}" if nombre_docente != -1 else f"ID: {id_docente}"
                
                print(f"{asistencia.get_id_asistencia()}\t{asistencia.get_fecha_asistencia().strftime('%d/%m/%Y')}\t{docente_info}\t{asistencia.get_cantidad_estudiantes()}")
            
            # Seleccionar asistencia
            id_asistencia = int(input("\nIngrese el ID de la asistencia: "))
            if id_asistencia <= 0:
                print("Error - El ID debe ser mayor a 0")
                input("Presione Enter para continuar...")
                return
            
            # Verificar si la asistencia existe
            asistencia_encontrada = None
            for asistencia in asistencias:
                if asistencia.get_id_asistencia() == id_asistencia:
                    asistencia_encontrada = asistencia
                    break
            
            if not asistencia_encontrada:
                print("Error - No se encontró la asistencia con ese ID")
                input("Presione Enter para continuar...")
                return
            
            # Verificar si ya tiene excusa
            if asistencia_encontrada.tiene_excusa():
                print("Error - Esta asistencia ya tiene una excusa registrada")
                input("Presione Enter para continuar...")
                return
            
            # Ingresar excusa
            excusa = input("Descripción de la excusa: ")
            if excusa.strip() == "":
                print("Error - La excusa no puede estar vacía")
                input("Presione Enter para continuar...")
                return
            
            # Registrar la excusa
            if self.colegio.registrar_excusa(id_asistencia, excusa):
                print("Excusa registrada exitosamente!")
                input("Presione Enter para continuar...")
                return
            else:
                print("Error - No se pudo registrar la excusa")
                input("Presione Enter para continuar...")
                
        except ValueError:
            print("Error - Debe ingresar un número válido")
            input("Presione Enter para continuar...")

    def buscar_inasistencias(self):
        system("cls")
        print("=== Buscar Asistencias con Excusa ===")
        try:
            # Obtener asistencias con excusa
            asistencias_con_excusa = self.colegio.buscar_asistencias_con_excusa()
            
            if not asistencias_con_excusa:
                print("No hay asistencias con excusa registradas")
                input("Presione Enter para continuar...")
                return
            
            print("Asistencias con excusa encontradas:")
            print("=" * 60)
            
            for i, asistencia in enumerate(asistencias_con_excusa, 1):
                # Obtener información del docente
                id_docente = asistencia.get_id_asistencia()
                nombre_docente = self.colegio.get_nombre_docente(id_docente)
                apellido_docente = self.colegio.get_apellido_docente(id_docente)
                materia_docente = self.colegio.get_materia_docente(id_docente)
                docente_info = f"{nombre_docente} {apellido_docente}" if nombre_docente != -1 else f"ID: {id_docente}"
                
                print(f"{i}. ID: {asistencia.get_id_asistencia()}")
                print(f"   Fecha: {asistencia.get_fecha_asistencia().strftime('%d/%m/%Y')}")
                print(f"   Docente: {docente_info}")
                if materia_docente != -1:
                    print(f"   Materia: {materia_docente}")
                print(f"   Estudiantes: {asistencia.get_cantidad_estudiantes()}")
                print(f"   Excusa: {asistencia.get_excusa()}")
                print("-" * 40)
            
            print(f"\nTotal de asistencias con excusa: {len(asistencias_con_excusa)}")
            input("Presione Enter para continuar...")
            
        except Exception as e:
            print(f"Error al buscar inasistencias: {e}")
            input("Presione Enter para continuar...")

    def mostrar_menu_principal(self):
        while True:
            system("cls")
            print("╔══════════════════════════════════╗")
            print("║      Colegio Mazamorra           ║")
            print("╠══════════════════════════════════╣")
            print("║         MENÚ PRINCIPAL           ║")
            print("╠══════════════════════════════════╣")
            print("║ [A] Registrar Estudiante         ║")
            print("║ [B] Buscar Estudiante            ║")
            print("║ [C] Deshabilitar/Habilitar Est.  ║")
            print("║ [D] Modificar Estudiante         ║")
            print("╠══════════════════════════════════╣")
            print("║ [E] Registrar Docente            ║")
            print("║ [F] Buscar Docente               ║")
            print("║ [G] Modificar Docente            ║")
            print("║ [H] Deshabilitar/Habilitar Doc.  ║")
            print("╠══════════════════════════════════╣")
            print("║ [I] Registrar Grado              ║")
            print("║ [J] Buscar Grado                 ║")
            print("║ [K] Modificar Grado              ║")
            print("║ [L] Deshabilitar/Habilitar Grad. ║")
            print("╠══════════════════════════════════╣")
            print("║ [M] Registrar Aula               ║")
            print("║ [N] Buscar Aula                  ║")
            print("║ [O] Modificar Aula               ║")
            print("║ [P] Deshabilitar/Habilitar Aula  ║")
            print("╠══════════════════════════════════╣")
            print("║ [Q] Registrar Asistencia         ║")
            print("║ [R] Buscar Asistencia por fecha  ║")
            print("║ [S] Modificar Asistencia         ║")
            print("║ [T] Deshabilitar/Habilitar Asis. ║")
            print("╠══════════════════════════════════╣")
            print("║ [U] Registrar Falta (con excusa) ║")
            print("║ [V] Buscar Inasistencias         ║")
            print("║ [W] Buscar Asistencia por ID     ║")
            print("╠══════════════════════════════════╣")
            print("║ [1] Listar estudiantes           ║")
            print("║ [2] Listar docentes              ║")
            print("║ [3] Listar grados                ║")
            print("║ [4] Listar aulas                 ║")
            print("╠══════════════════════════════════╣")
            print("║ [5] Listar asistencias con excusa║")
            print("║ [6] Listar asistencias sin excusa║")
            print("║ [7] Listar todas las asistencias ║")
            print("╠══════════════════════════════════╣")
            print("║ [0] Salir                        ║")
            print("╚══════════════════════════════════╝")
            opcion = input("Seleccione una opción: ").lower()
            if opcion == "a":
                self.registrar_estudiante()
            elif opcion == "b":
                self.buscar_estudiante()
            elif opcion == "c":
                self.deshabilitar_habilitar_estudiante()
            elif opcion == "d":
                self.modificar_estudiante()
            elif opcion == "e":
                self.registrar_docente()
            elif opcion == "f":
                self.buscar_docentes()
            elif opcion == "g":
                self.modificar_docente()
            elif opcion == "h":
                self.deshabilitar_habilitar_docente()
            elif opcion == "i":
                self.registrar_grado()
            elif opcion == "j":
                self.buscar_grado()
            elif opcion == "k":
                self.modificar_grado()
            elif opcion == "l":
                self.deshabilitar_habilitar_grado()
            elif opcion == "m":
                self.registrar_aula()
            elif opcion == "n":
                self.buscar_aula()
            elif opcion == "o":
                self.modificar_aula()
            elif opcion == "p":
                self.deshabilitar_habilitar_aula()
            elif opcion == "q":
                self.registrar_asistencia()
            elif opcion == "r":
                self.buscar_asistencia()
            elif opcion == "s":
                self.modificar_inasistencia()
            elif opcion == "t":
                self.deshabilitar_habilitar_asistencia()
            elif opcion == "u":
                self.registrar_falta_con_excusa()
            elif opcion == "v":
                self.buscar_inasistencias()
            elif opcion == "w":
                self.buscar_asistencia_por_id()
            elif opcion == "1":
                self.listar_estudiantes()
            elif opcion == "2":
                self.listar_docentes()
            elif opcion == "3":
                self.listar_grados()
            elif opcion == "4":
                self.listar_aulas()
            elif opcion == "5":
                self.listar_asistencias_con_excusa()
            elif opcion == "6":
                self.listar_asistencias_sin_excusa()
            elif opcion == "7":
                self.listar_todas_asistencias()
            elif opcion == "0" or opcion == "exit":
                system("cls")
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Presione Enter para continuar...")
                input()

    def listar_todas_asistencias(self):
        system("cls")
        print("=== Listar todas las asistencias ===")
        try:
            todas_asistencias = self.colegio.get_asistencias()
            
            if not todas_asistencias:
                print("No hay asistencias registradas")
                input("Presione Enter para continuar...")
                return

            print("ID\tFecha\tDocente\tEstudiantes\tEstado\tExcusa")
            print("-" * 90)
            contador = 0
            for asistencia in todas_asistencias:
                try:
                    id_asist = asistencia.get_id_asistencia()
                    fecha = asistencia.get_fecha_asistencia()
                    estudiantes = asistencia.get_cantidad_estudiantes()
                    estado = asistencia.get_habilitado()
                    excusa = asistencia.get_excusa()
                    
                    # Obtener información del docente
                    nombre_docente = self.colegio.get_nombre_docente(id_asist)
                    apellido_docente = self.colegio.get_apellido_docente(id_asist)
                    docente_info = f"{nombre_docente} {apellido_docente}" if nombre_docente != -1 else f"ID: {id_asist}"
                    
                    # Truncar excusa si es muy larga
                    if excusa and len(excusa) > 20:
                        excusa = excusa[:17] + "..."
                    elif not excusa:
                        excusa = "Sin excusa"
                    
                    # Validar que todos los datos estén presentes
                    if all([id_asist, fecha, estudiantes, estado]):
                        print(f"{id_asist}\t{fecha.strftime('%d/%m/%Y')}\t{docente_info}\t{estudiantes}\t{estado}\t{excusa}")
                        contador += 1
                    else:
                        print(f"Error en datos de la asistencia ID: {id_asist}")
                except Exception as e:
                    print(f"Error al procesar asistencia: {e}")
                    continue
            
            print(f"\nTotal de asistencias listadas: {contador}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"Error al listar asistencias: {e}")
            input("Presione Enter para continuar...")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()                                               