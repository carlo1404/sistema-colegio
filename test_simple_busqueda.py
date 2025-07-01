#!/usr/bin/env python3
"""
Script simple para probar la búsqueda de asistencias
"""

print("Iniciando prueba...")

try:
    from colegio import Colegio
    print("✓ Colegio importado")
    
    from docente import Docente
    print("✓ Docente importado")
    
    from asistencia import Asistencia
    print("✓ Asistencia importado")
    
    from datetime import date
    print("✓ datetime importado")
    
    # Crear instancia del colegio
    colegio = Colegio()
    print("✓ Colegio creado")
    
    # Crear docentes de prueba
    docente1 = Docente("Juan", "Pérez", "Matemáticas", 5, 1)
    docente2 = Docente("María", "García", "Lengua", 3, 2)
    print("✓ Docentes creados")
    
    colegio.adicionar_docente(docente1)
    colegio.adicionar_docente(docente2)
    print("✓ Docentes agregados al colegio")
    
    # Registrar asistencias
    fecha1 = date(2024, 6, 15)
    asistencia1 = Asistencia(1, fecha1, 5)
    colegio.registrar_asistencia(asistencia1)
    print("✓ Asistencia registrada")
    
    # Probar búsqueda
    asistencias = colegio.buscar_asistencias_por_fecha(fecha1)
    print(f"✓ Búsqueda completada. Encontradas: {len(asistencias)} asistencias")
    
    print("\n=== PRUEBA EXITOSA ===")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

print("Script terminado.") 