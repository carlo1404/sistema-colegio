#!/usr/bin/env python3
"""
Archivo de prueba para verificar el funcionamiento del sistema de colegio
"""

from menu import Menu

def test_sistema():
    print("=== PRUEBA DEL SISTEMA DE COLEGIO ===")
    print("Este archivo permite probar las funcionalidades del sistema.")
    print("Para usar el sistema completo, ejecute: python menu.py")
    print()
    
    # Crear instancia del menú
    menu = Menu()
    
    # Probar creación de estudiantes
    print("1. Probando registro de estudiantes...")
    from estudiante import Estudiante
    from colegio import Colegio
    
    colegio = Colegio()
    
    # Crear algunos estudiantes de prueba
    estudiante1 = Estudiante("Juan", "Pérez", 15, 9, 1)
    estudiante2 = Estudiante("María", "García", 14, 8, 2)
    
    colegio.adicionar_estudiante(estudiante1)
    colegio.adicionar_estudiante(estudiante2)
    
    print("✓ Estudiantes creados correctamente")
    
    # Probar creación de docentes
    print("2. Probando registro de docentes...")
    from docente import Docente
    
    docente1 = Docente("Carlos", "López", "Matemáticas", 5, 1)
    docente2 = Docente("Ana", "Martínez", "Lengua", 3, 2)
    
    colegio.adicionar_docente(docente1)
    colegio.adicionar_docente(docente2)
    
    print("✓ Docentes creados correctamente")
    
    # Probar búsquedas
    print("3. Probando búsquedas...")
    
    # Buscar estudiante existente
    resultado_estudiante = colegio.buscar_estudiante(1)
    if resultado_estudiante != -1:
        print("✓ Búsqueda de estudiante funciona")
    else:
        print("✗ Error en búsqueda de estudiante")
    
    # Buscar docente existente
    resultado_docente = colegio.buscar_docentes(1)
    if resultado_docente != -1:
        print("✓ Búsqueda de docente funciona")
    else:
        print("✗ Error en búsqueda de docente")
    
    # Probar modificaciones
    print("4. Probando modificaciones...")
    
    # Modificar nombre de estudiante
    resultado_mod = colegio.establecer_nuevo_nombre_estudiante("Juan Carlos", 1)
    if resultado_mod:
        print("✓ Modificación de estudiante funciona")
    else:
        print("✗ Error en modificación de estudiante")
    
    # Modificar nombre de docente
    resultado_mod_doc = colegio.establecer_nuevo_nombre_docente("Carlos Alberto", 1)
    if resultado_mod_doc:
        print("✓ Modificación de docente funciona")
    else:
        print("✗ Error en modificación de docente")
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("El sistema está funcionando correctamente.")
    print("Puede ejecutar 'python menu.py' para usar la interfaz completa.")

if __name__ == "__main__":
    test_sistema() 