#!/usr/bin/env python3
from colegio import Colegio
from estudiante import Estudiante
from docente import Docente

def test_simple():
    print("=== PRUEBA SIMPLE DE IDs DUPLICADOS ===")
    
    colegio = Colegio()
    
    # Probar estudiantes
    print("1. Probando estudiantes:")
    e1 = Estudiante("Juan", "Pérez", 15, 9, 1)
    e2 = Estudiante("María", "García", 14, 8, 1)  # Mismo ID
    
    print("Agregando estudiante 1:", colegio.adicionar_estudiante(e1))
    print("Agregando estudiante duplicado:", colegio.adicionar_estudiante(e2))
    
    # Probar docentes
    print("\n2. Probando docentes:")
    d1 = Docente("Ana", "Martínez", "Matemáticas", 5, 1)
    d2 = Docente("Pedro", "González", "Lengua", 3, 1)  # Mismo ID
    
    print("Agregando docente 1:", colegio.adicionar_docente(d1))
    print("Agregando docente duplicado:", colegio.adicionar_docente(d2))
    
    print("\nEstudiantes en el sistema:", len(colegio.get_estudiantes()))
    print("Docentes en el sistema:", len(colegio.get_docentes_habilitados()))

if __name__ == "__main__":
    test_simple() 