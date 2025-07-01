#!/usr/bin/env python3
"""
Script de prueba para verificar la validación de IDs duplicados
"""

from colegio import Colegio
from docente import Docente
from estudiante import Estudiante
from asistencia import Asistencia
from datetime import date

def test_ids_duplicados():
    print("=== PRUEBA DE VALIDACIÓN DE IDs DUPLICADOS ===")
    
    # Crear instancia del colegio
    colegio = Colegio()
    
    print("1. Probando IDs duplicados en estudiantes:")
    
    # Crear primer estudiante
    estudiante1 = Estudiante("Juan", "Pérez", 15, 9, 1)
    resultado1 = colegio.adicionar_estudiante(estudiante1)
    print(f"   - Estudiante 1 (ID: 1): {'✓ Agregado' if resultado1 else '✗ Error'}")
    
    # Intentar crear estudiante con ID duplicado
    estudiante_duplicado = Estudiante("María", "García", 14, 8, 1)  # Mismo ID
    resultado_duplicado = colegio.adicionar_estudiante(estudiante_duplicado)
    print(f"   - Estudiante duplicado (ID: 1): {'✗ Error (debería fallar)' if not resultado_duplicado else '✓ Error: Se permitió duplicado'}")
    
    # Crear estudiante con ID diferente
    estudiante2 = Estudiante("Carlos", "López", 16, 10, 2)
    resultado2 = colegio.adicionar_estudiante(estudiante2)
    print(f"   - Estudiante 2 (ID: 2): {'✓ Agregado' if resultado2 else '✗ Error'}")
    
    print("\n2. Probando IDs duplicados en docentes:")
    
    # Crear primer docente
    docente1 = Docente("Ana", "Martínez", "Matemáticas", 5, 1)
    resultado_doc1 = colegio.adicionar_docente(docente1)
    print(f"   - Docente 1 (ID: 1): {'✓ Agregado' if resultado_doc1 else '✗ Error'}")
    
    # Intentar crear docente con ID duplicado
    docente_duplicado = Docente("Pedro", "González", "Lengua", 3, 1)  # Mismo ID
    resultado_doc_duplicado = colegio.adicionar_docente(docente_duplicado)
    print(f"   - Docente duplicado (ID: 1): {'✗ Error (debería fallar)' if not resultado_doc_duplicado else '✓ Error: Se permitió duplicado'}")
    
    # Crear docente con ID diferente
    docente2 = Docente("Laura", "Rodríguez", "Historia", 7, 2)
    resultado_doc2 = colegio.adicionar_docente(docente2)
    print(f"   - Docente 2 (ID: 2): {'✓ Agregado' if resultado_doc2 else '✗ Error'}")
    
    print("\n3. Probando IDs duplicados en asistencias:")
    
    # Crear primera asistencia
    fecha1 = date(2024, 6, 15)
    asistencia1 = Asistencia(1, fecha1, 5)  # Docente ID 1, fecha 15/06/2024
    resultado_asist1 = colegio.registrar_asistencia(asistencia1)
    print(f"   - Asistencia 1 (Docente 1, 15/06/2024): {'✓ Registrada' if resultado_asist1 else '✗ Error'}")
    
    # Intentar crear asistencia duplicada (mismo docente, misma fecha)
    asistencia_duplicada = Asistencia(1, fecha1, 3)  # Mismo docente, misma fecha
    resultado_asist_duplicada = colegio.registrar_asistencia(asistencia_duplicada)
    print(f"   - Asistencia duplicada (Docente 1, 15/06/2024): {'✗ Error (debería fallar)' if not resultado_asist_duplicada else '✓ Error: Se permitió duplicado'}")
    
    # Crear asistencia válida (mismo docente, fecha diferente)
    fecha2 = date(2024, 6, 16)
    asistencia2 = Asistencia(1, fecha2, 4)  # Mismo docente, fecha diferente
    resultado_asist2 = colegio.registrar_asistencia(asistencia2)
    print(f"   - Asistencia 2 (Docente 1, 16/06/2024): {'✓ Registrada' if resultado_asist2 else '✗ Error'}")
    
    # Crear asistencia válida (docente diferente, misma fecha)
    asistencia3 = Asistencia(2, fecha1, 6)  # Docente diferente, misma fecha
    resultado_asist3 = colegio.registrar_asistencia(asistencia3)
    print(f"   - Asistencia 3 (Docente 2, 15/06/2024): {'✓ Registrada' if resultado_asist3 else '✗ Error'}")
    
    print("\n4. Resumen de validaciones:")
    print(f"   - Estudiantes en el sistema: {len(colegio.get_estudiantes())}")
    print(f"   - Docentes en el sistema: {len(colegio.get_docentes_habilitados())}")
    print(f"   - Asistencias registradas: {len(colegio._Colegio__asistencias)}")
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("Si todas las validaciones funcionan correctamente, no debería haber IDs duplicados.")

if __name__ == "__main__":
    test_ids_duplicados() 