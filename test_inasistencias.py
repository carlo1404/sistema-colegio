#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de registro de inasistencias
"""

from colegio import Colegio
from docente import Docente
from estudiante import Estudiante
from inasistencia import Inasistencia
from datetime import date

def test_registro_inasistencia():
    print("=== PRUEBA DE REGISTRO DE INASISTENCIAS ===")
    
    # Crear instancia del colegio
    colegio = Colegio()
    
    # Crear docentes de prueba
    docente1 = Docente("Juan", "Pérez", "Matemáticas", 5, 1)
    docente2 = Docente("María", "García", "Lengua", 3, 2)
    colegio.adicionar_docente(docente1)
    colegio.adicionar_docente(docente2)
    
    # Crear estudiantes de prueba
    estudiante1 = Estudiante("Carlos", "López", 15, 9, 1)
    estudiante2 = Estudiante("Ana", "Martínez", 14, 8, 2)
    estudiante3 = Estudiante("Pedro", "González", 16, 10, 3)
    colegio.adicionar_estudiante(estudiante1)
    colegio.adicionar_estudiante(estudiante2)
    colegio.adicionar_estudiante(estudiante3)
    
    print("1. Datos de prueba creados:")
    print(f"   - Docentes: {len(colegio.get_docentes_habilitados())}")
    print(f"   - Estudiantes: {len(colegio.get_estudiantes_habilitados())}")
    
    # Probar obtención de docentes habilitados
    print("\n2. Docentes habilitados:")
    docentes = colegio.get_docentes_habilitados()
    for i, docente in enumerate(docentes, 1):
        print(f"   {i}. {docente.get_nombre_docente()} {docente.get_apellido_docente()} - {docente.get_materia_docente()}")
    
    # Probar obtención de estudiantes habilitados
    print("\n3. Estudiantes habilitados:")
    estudiantes = colegio.get_estudiantes_habilitados()
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"   {i}. {estudiante.get_nombre()} {estudiante.get_apellido()} - Curso: {estudiante.get_curso()}")
    
    # Probar registro de inasistencia
    print("\n4. Probando registro de inasistencia...")
    
    # Crear una inasistencia de prueba
    fecha_prueba = date(2024, 1, 15)
    id_estudiantes_faltaron = ["1", "2"]  # IDs de estudiantes que faltaron
    
    # Registrar inasistencia
    resultado = colegio.registrar_inasistencia(1, 1, fecha_prueba, 2, id_estudiantes_faltaron)
    
    if resultado:
        print("✓ Inasistencia registrada exitosamente!")
        print(f"   - ID: 1")
        print(f"   - Docente: {docente1.get_nombre_docente()} {docente1.get_apellido_docente()}")
        print(f"   - Fecha: {fecha_prueba.strftime('%d/%m/%Y')}")
        print(f"   - Estudiantes que faltaron: 2")
        print(f"   - IDs: {id_estudiantes_faltaron}")
    else:
        print("✗ Error al registrar inasistencia")
    
    # Probar búsqueda de inasistencias sin excusa
    print("\n5. Probando búsqueda de inasistencias sin excusa...")
    inasistencias_sin_excusa = colegio.buscar_inasistencias_sin_excusa()
    
    if inasistencias_sin_excusa:
        print(f"✓ Se encontraron {len(inasistencias_sin_excusa)} inasistencias sin excusa")
        for i, inasistencia in enumerate(inasistencias_sin_excusa, 1):
            print(f"   {i}. ID: {inasistencia.get_id()}")
            print(f"      Fecha: {inasistencia.get_fecha().strftime('%d/%m/%Y')}")
            print(f"      Estudiantes: {inasistencia.get_cantidad_estudiantes()}")
            print(f"      IDs: {inasistencia.get_id_estudiantes_inasistentes()}")
    else:
        print("✗ No se encontraron inasistencias sin excusa")
    
    # Probar obtención de nombres de estudiantes
    print("\n6. Probando obtención de nombres de estudiantes...")
    for id_estudiante in id_estudiantes_faltaron:
        nombre = colegio.get_nombre_estudiante(int(id_estudiante))
        apellido = colegio.get_apellido_estudiante(int(id_estudiante))
        if nombre != -1 and apellido != -1:
            print(f"   ✓ Estudiante ID {id_estudiante}: {nombre} {apellido}")
        else:
            print(f"   ✗ No se encontró estudiante con ID {id_estudiante}")
    
    print("\n=== PRUEBA COMPLETADA ===")

if __name__ == "__main__":
    test_registro_inasistencia() 