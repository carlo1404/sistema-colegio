#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de modificar materia de docente
"""

from colegio import Colegio
from docente import Docente

def test_modificar_materia():
    print("=== PRUEBA DE MODIFICAR MATERIA ===")
    
    # Crear instancia del colegio
    colegio = Colegio()
    
    # Crear un docente de prueba
    docente = Docente("Juan", "Pérez", "Matemáticas", 5, 1)
    colegio.adicionar_docente(docente)
    
    print("1. Docente creado:")
    print(f"   - Nombre: {docente.get_nombre_docente()}")
    print(f"   - Materia actual: {docente.get_materia_docente()}")
    
    # Mostrar materias disponibles
    print("\n2. Materias disponibles:")
    materias = colegio.get_materias()
    for i, materia in enumerate(materias, 1):
        print(f"   {i}. {materia}")
    
    # Simular modificación de materia
    print("\n3. Simulando modificación de materia...")
    
    # Verificar que el método get_materia_docente funciona
    materia_actual = colegio.get_materia_docente(1)
    print(f"   - Materia actual obtenida: {materia_actual}")
    
    if materia_actual != -1:
        print("   ✓ Método get_materia_docente funciona correctamente")
    else:
        print("   ✗ Error en get_materia_docente")
        return
    
    # Simular cambio de materia (tomando la primera disponible)
    if materias:
        nueva_materia = colegio.descontar_materias(1)
        resultado = colegio.establecer_nueva_materia_docente(nueva_materia, 1)
        
        if resultado:
            print(f"   ✓ Materia cambiada exitosamente a: {nueva_materia}")
        else:
            print("   ✗ Error al cambiar materia")
    else:
        print("   - No hay materias disponibles para cambiar")
    
    print("\n=== PRUEBA COMPLETADA ===")

if __name__ == "__main__":
    test_modificar_materia() 