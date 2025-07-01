#!/usr/bin/env python3
from colegio import Colegio
from docente import Docente
from asistencia import Asistencia
from datetime import date

def test_asistencias_duplicadas():
    print("=== PRUEBA DE ASISTENCIAS DUPLICADAS ===")
    
    colegio = Colegio()
    
    # Crear docente
    docente = Docente("Juan", "Pérez", "Matemáticas", 5, 1)
    colegio.adicionar_docente(docente)
    
    # Fecha de prueba
    fecha = date(2024, 6, 15)
    
    print("1. Registrando primera asistencia:")
    asistencia1 = Asistencia(1, fecha, 5)
    resultado1 = colegio.registrar_asistencia(asistencia1)
    print(f"   Resultado: {'✓ Registrada' if resultado1 else '✗ Error'}")
    
    print("\n2. Intentando registrar asistencia duplicada (mismo docente, misma fecha):")
    asistencia_duplicada = Asistencia(1, fecha, 3)
    resultado_duplicada = colegio.registrar_asistencia(asistencia_duplicada)
    print(f"   Resultado: {'✗ Error (debería fallar)' if not resultado_duplicada else '✓ Error: Se permitió duplicado'}")
    
    print("\n3. Registrando asistencia válida (mismo docente, fecha diferente):")
    fecha2 = date(2024, 6, 16)
    asistencia2 = Asistencia(1, fecha2, 4)
    resultado2 = colegio.registrar_asistencia(asistencia2)
    print(f"   Resultado: {'✓ Registrada' if resultado2 else '✗ Error'}")
    
    print(f"\nTotal de asistencias registradas: {len(colegio._Colegio__asistencias)}")

if __name__ == "__main__":
    test_asistencias_duplicadas() 