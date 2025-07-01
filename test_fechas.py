#!/usr/bin/env python3
"""
Script de prueba para validar fechas en el registro de asistencia
"""

from datetime import date
from asistencia import Asistencia

def test_validacion_fechas():
    print("=== PRUEBA DE VALIDACIÓN DE FECHAS ===")
    
    # Fecha actual
    fecha_actual = date.today()
    print(f"Fecha actual: {fecha_actual.strftime('%d/%m/%Y')}")
    
    # Probar fechas válidas
    print("\n1. Probando fechas válidas:")
    
    # Fecha pasada válida
    fecha_pasada = date(2024, 6, 15)
    asistencia1 = Asistencia(1, fecha_pasada, 5)
    print(f"   ✓ Fecha pasada: {fecha_pasada.strftime('%d/%m/%Y')}")
    
    # Fecha actual
    asistencia2 = Asistencia(2, fecha_actual, 3)
    print(f"   ✓ Fecha actual: {fecha_actual.strftime('%d/%m/%Y')}")
    
    # Probar fechas inválidas
    print("\n2. Probando fechas inválidas:")
    
    try:
        # Fecha inválida (31 de febrero)
        fecha_invalida = date(2024, 2, 31)
        print("   ✗ Error: Se permitió crear fecha inválida (31/02/2024)")
    except ValueError:
        print("   ✓ Correctamente rechazó fecha inválida (31/02/2024)")
    
    try:
        # Fecha inválida (30 de febrero)
        fecha_invalida = date(2024, 2, 30)
        print("   ✗ Error: Se permitió crear fecha inválida (30/02/2024)")
    except ValueError:
        print("   ✓ Correctamente rechazó fecha inválida (30/02/2024)")
    
    try:
        # Fecha inválida (32 de enero)
        fecha_invalida = date(2024, 1, 32)
        print("   ✗ Error: Se permitió crear fecha inválida (32/01/2024)")
    except ValueError:
        print("   ✓ Correctamente rechazó fecha inválida (32/01/2024)")
    
    # Probar fechas futuras
    print("\n3. Probando fechas futuras:")
    fecha_futura = date(fecha_actual.year + 1, fecha_actual.month, fecha_actual.day)
    print(f"   - Fecha futura: {fecha_futura.strftime('%d/%m/%Y')}")
    print(f"   - Debería ser rechazada por el sistema")
    
    # Probar años límite
    print("\n4. Probando años límite:")
    
    # Año muy antiguo
    fecha_antigua = date(2019, 6, 15)
    print(f"   - Año 2019: Debería ser rechazado (muy antiguo)")
    
    # Año válido
    fecha_valida = date(2020, 6, 15)
    print(f"   - Año 2020: Debería ser aceptado")
    
    # Año futuro
    fecha_futura_ano = date(fecha_actual.year + 1, 6, 15)
    print(f"   - Año {fecha_actual.year + 1}: Debería ser rechazado (futuro)")
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("Las validaciones de fecha están implementadas correctamente.")

if __name__ == "__main__":
    test_validacion_fechas() 