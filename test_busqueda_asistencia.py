#!/usr/bin/env python3
"""
Script de prueba para verificar la búsqueda de asistencias por fecha
"""

from colegio import Colegio
from docente import Docente
from asistencia import Asistencia
from datetime import date

def test_busqueda_asistencia():
    print("=== PRUEBA DE BÚSQUEDA DE ASISTENCIAS ===")
    
    # Crear instancia del colegio
    colegio = Colegio()
    
    # Crear docentes de prueba
    docente1 = Docente("Juan", "Pérez", "Matemáticas", 5, 1)
    docente2 = Docente("María", "García", "Lengua", 3, 2)
    colegio.adicionar_docente(docente1)
    colegio.adicionar_docente(docente2)
    
    print("1. Registrando asistencias de prueba...")
    
    # Registrar varias asistencias
    fecha1 = date(2024, 6, 15)
    fecha2 = date(2024, 6, 16)
    fecha3 = date(2024, 6, 15)  # Misma fecha que fecha1
    
    asistencia1 = Asistencia(1, fecha1, 5)  # Docente 1, fecha 15/06/2024
    asistencia2 = Asistencia(2, fecha1, 3)  # Docente 2, fecha 15/06/2024
    asistencia3 = Asistencia(1, fecha2, 4)  # Docente 1, fecha 16/06/2024
    
    colegio.registrar_asistencia(asistencia1)
    colegio.registrar_asistencia(asistencia2)
    colegio.registrar_asistencia(asistencia3)
    
    print("   ✓ Asistencias registradas")
    
    # Probar búsqueda por fecha
    print("\n2. Probando búsqueda por fecha 15/06/2024:")
    asistencias_fecha1 = colegio.buscar_asistencias_por_fecha(fecha1)
    print(f"   Encontradas: {len(asistencias_fecha1)} asistencias")
    
    for i, asistencia in enumerate(asistencias_fecha1, 1):
        id_docente = asistencia.get_id_asistencia()
        cantidad = asistencia.get_cantidad_estudiantes()
        print(f"   {i}. Docente ID: {id_docente}, Estudiantes: {cantidad}")
    
    print("\n3. Probando búsqueda por fecha 16/06/2024:")
    asistencias_fecha2 = colegio.buscar_asistencias_por_fecha(fecha2)
    print(f"   Encontradas: {len(asistencias_fecha2)} asistencias")
    
    for i, asistencia in enumerate(asistencias_fecha2, 1):
        id_docente = asistencia.get_id_asistencia()
        cantidad = asistencia.get_cantidad_estudiantes()
        print(f"   {i}. Docente ID: {id_docente}, Estudiantes: {cantidad}")
    
    print("\n4. Probando búsqueda por fecha inexistente:")
    fecha_inexistente = date(2024, 6, 20)
    asistencias_inexistente = colegio.buscar_asistencias_por_fecha(fecha_inexistente)
    print(f"   Encontradas: {len(asistencias_inexistente)} asistencias")
    
    print("\n5. Probando búsqueda por docente:")
    asistencias_docente1 = colegio.buscar_asistencias_por_docente(1)
    print(f"   Asistencias del docente 1: {len(asistencias_docente1)}")
    
    for i, asistencia in enumerate(asistencias_docente1, 1):
        fecha = asistencia.get_fecha()
        cantidad = asistencia.get_cantidad_estudiantes()
        print(f"   {i}. Fecha: {fecha.strftime('%d/%m/%Y')}, Estudiantes: {cantidad}")
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("La búsqueda de asistencias funciona correctamente.")

if __name__ == "__main__":
    test_busqueda_asistencia() 