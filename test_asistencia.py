#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de registro de asistencia
"""

from colegio import Colegio
from docente import Docente
from estudiante import Estudiante
from asistencia import Asistencia
from datetime import date

def test_registro_asistencia():
    print("=== PRUEBA DE REGISTRO DE ASISTENCIA ===")
    
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
    
    # Probar registro de asistencia
    print("\n4. Probando registro de asistencia...")
    
    # Simular registro de asistencia
    fecha_actual = date.today()
    id_docente = docente1.get_id_docente()
    cantidad_asistentes = 2
    
    asistencia = Asistencia(id_docente, fecha_actual, cantidad_asistentes)
    resultado = colegio.registrar_asistencia(asistencia)
    
    if resultado:
        print(f"   ✓ Asistencia registrada exitosamente!")
        print(f"   - Docente ID: {id_docente}")
        print(f"   - Fecha: {fecha_actual.strftime('%d/%m/%Y')}")
        print(f"   - Cantidad de asistentes: {cantidad_asistentes}")
    else:
        print("   ✗ Error al registrar asistencia")
    
    # Probar validación de IDs duplicados
    print("\n5. Probando validación de IDs duplicados...")
    
    # Intentar crear un estudiante con ID duplicado
    estudiante_duplicado = Estudiante("Test", "Test", 15, 9, 1)  # Mismo ID que estudiante1
    resultado_duplicado = colegio.adicionar_estudiante(estudiante_duplicado)
    
    if not resultado_duplicado:
        print("   ✓ Validación de ID duplicado funciona correctamente")
    else:
        print("   ✗ Error: Se permitió crear estudiante con ID duplicado")
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("Para usar la funcionalidad completa, ejecute: python menu.py")

if __name__ == "__main__":
    test_registro_asistencia() 