# 🎓 Sistema de Gestión Escolar 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Estado-Finalizado-success" alt="Estado">
  <img src="https://img.shields.io/badge/Licencia-Educativa-green" alt="Licencia">
</p>

<p align="center">
  <img src="https://images.unsplash.com/photo-1523050854058-8df90110c9a1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80" alt="Sistema de Gestión Escolar" width="800" height="400">
</p>

---

<p align="center">
  <b>¡Bienvenido al sistema de gestión escolar más completo y fácil de usar para colegios e institutos! 🎒🏫</b>
</p>

---

## 📑 Tabla de Contenidos
- [Descripción](#descripción)
- [Características Principales](#características-principales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Clases Principales](#clases-principales)
- [Validaciones Implementadas](#validaciones-implementadas)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Menú Principal](#menú-principal)
- [Funcionalidades Mejoradas](#funcionalidades-mejoradas)
- [Notas Técnicas](#notas-técnicas)
- [Limitaciones Actuales](#limitaciones-actuales)
- [Futuras Mejoras](#futuras-mejoras)
- [Autor](#autor)
- [Licencia](#licencia)

---

## 📝 Descripción
Sistema de gestión escolar desarrollado en Python que permite administrar estudiantes, docentes, grados, aulas y asistencias de un colegio.

---

## 🚀 Características Principales

| Área                  | Funcionalidades                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| 👨‍🎓 Estudiantes      | Registrar, buscar, modificar, habilitar/deshabilitar, listar                   |
| 👩‍🏫 Docentes         | Registrar, buscar, modificar, habilitar/deshabilitar, listar                   |
| 🏫 Grados             | Registrar, buscar, modificar, habilitar/deshabilitar, listar                   |
| 🏠 Aulas              | Registrar, buscar, modificar, habilitar/deshabilitar, listar                   |
| 📅 Asistencias        | Registrar, buscar (por fecha/ID), modificar, excusas, listar con/sin excusa    |
| ❌ Inasistencias      | Registrar, buscar sin excusa, modificar, listar todas las inasistencias        |

---

## 🗂️ Estructura del Proyecto
```text
actividad/
├── menu.py              # Menú principal del sistema
├── colegio.py           # Clase principal que gestiona todo el sistema
├── estudiante.py        # Clase para manejar estudiantes
├── docente.py           # Clase para manejar docentes
├── grado.py             # Clase para manejar grados
├── aula.py              # Clase para manejar aulas
├── asistencia.py        # Clase para manejar asistencias
├── inasistencia.py      # Clase para manejar inasistencias
├── materia.py           # Clase para manejar materias
└── README.md            # Documentación del proyecto
```

---

## 🏗️ Clases Principales

- **Colegio**: Gestiona todas las operaciones del sistema.
- **Estudiante**: Maneja información y estado de los estudiantes.
- **Docente**: Maneja información, materias y grados asignados.
- **Grado**: Representa un grado escolar y su asociación con aulas.
- **Aula**: Representa un aula física y su capacidad.
- **Asistencia**: Registra asistencias, fechas, docentes y excusas.
- **Inasistencia**: Registra inasistencias, fechas, docentes y estudiantes que faltaron.

---

## ✅ Validaciones Implementadas

- **Estudiantes**: ID único, nombre y apellido válidos, edad (5-18), curso (1-11)
- **Docentes**: ID único, nombre y apellido válidos, grado (1-20), materias
- **Grados**: ID único, nombre válido, asociación con aulas, cantidad (1-10)
- **Aulas**: ID único, nombre válido, capacidad (1-15)
- **Asistencias**: ID único, fecha válida, docente habilitado, cantidad válida, excusas
- **Inasistencias**: ID único, fecha válida, docente habilitado, cantidad válida, IDs de estudiantes

---

## 🖥️ Cómo Ejecutar

### Requisitos Previos
- **Python 3.6+** instalado en tu sistema
- Terminal o línea de comandos

### Instalación y Uso

1. **Clona o descarga el proyecto**
   ```bash
   git clone https://github.com/tu-usuario/sistema-gestion-escolar.git
   cd sistema-gestion-escolar
   ```

2. **Ejecuta el sistema**
   ```bash
   python menu.py
   ```

3. **Navega por el menú**
   - Usa las letras (A-Z) para acceder a las funciones principales
   - Usa los números (1-8) para ver listados
   - Usa '0' para salir del sistema

### Ejemplo de Uso

```bash
# Ejecutar el sistema
python menu.py

# El sistema mostrará el menú principal:
# ╔══════════════════════════════════╗
# ║      Colegio Mazamorra           ║
# ╠══════════════════════════════════╣
# ║         MENÚ PRINCIPAL           ║
# ╚══════════════════════════════════╝
```

---

## 🧭 Menú Principal

<details>
<summary>Ver opciones del menú</summary>

- [A] Registrar Estudiante
- [B] Buscar Estudiante
- [C] Deshabilitar/Habilitar Estudiante
- [D] Modificar Estudiante
- [E] Registrar Docente
- [F] Buscar Docente
- [G] Modificar Docente
- [H] Deshabilitar/Habilitar Docente
- [I] Registrar Grado
- [J] Buscar Grado
- [K] Modificar Grado
- [L] Deshabilitar/Habilitar Grado
- [M] Registrar Aula
- [N] Buscar Aula
- [O] Modificar Aula
- [P] Deshabilitar/Habilitar Aula
- [Q] Registrar Asistencia
- [R] Buscar Asistencia por fecha
- [S] Modificar Asistencia
- [T] Deshabilitar/Habilitar Asistencia
- [U] Registrar Falta (con excusa)
- [V] Buscar Asistencias con Excusa
- [W] Buscar Asistencia por ID
- [1] Listar estudiantes
- [2] Listar docentes
- [3] Listar grados
- [4] Listar aulas
- [5] Listar asistencias con excusa
- [6] Listar asistencias sin excusa
- [7] Listar todas las asistencias
- [8] Listar todas las inasistencias
</details>

---

## ✨ Funcionalidades Mejoradas

- Listados en formato tabular con encabezados
- Estados claramente mostrados (Habilitado/Deshabilitado)
- Manejo de errores mejorado y mensajes descriptivos
- Validación robusta de datos y excepciones específicas
- Interfaz de usuario clara y organizada
- Confirmaciones de operaciones exitosas

## 📸 Capturas de Pantalla

<p align="center">
  <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&h=300&fit=crop&crop=center" alt="Menú Principal" width="600" height="300">
  <br>
  <em>Menú principal del sistema con todas las opciones disponibles</em>
</p>

<p align="center">
  <img src="https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&h=300&fit=crop&crop=center" alt="Gestión de Estudiantes" width="600" height="300">
  <br>
  <em>Interfaz para gestionar estudiantes del colegio</em>
</p>

---

## ⚙️ Notas Técnicas

- Programación orientada a objetos
- Métodos getter y setter en todas las clases
- Validaciones y manejo de excepciones
- Persistencia de datos en memoria durante la sesión

---

## 🚧 Limitaciones Actuales

- Los datos no se persisten entre sesiones
- Algunas funciones avanzadas no están implementadas (sistema de excusas)
- Solo interfaz de consola (sin GUI)
- No hay sistema de usuarios/autenticación

---

## 🛠️ Futuras Mejoras

- [ ] Persistencia de datos en archivos
- [ ] Base de datos para almacenamiento
- [ ] Sistema de excusas completo
- [ ] Interfaz gráfica
- [ ] Sistema de usuarios y roles
- [ ] Reportes y estadísticas
- [ ] Exportación de datos

---

## 👨‍💻 Autor
Sistema desarrollado para gestión escolar de un Colegio e Instituto.

**Desarrolladores:**
- Santiago Sanchez Hernandez
- Carlos Andres Reyes Grajales  
- Laura Cortez

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 🙏 Agradecimientos

- A todos los docentes y estudiantes que probaron el sistema
- A la comunidad de Python por las herramientas utilizadas
- A los desarrolladores de las librerías utilizadas

---

## 📄 Licencia
Este proyecto es de uso educativo.

---

## 🎉 ¡PROYECTO FINALIZADO! 

<p align="center">
  <img src="https://img.shields.io/badge/Estado-FINALIZADO-success?style=for-the-badge&logo=check-circle" alt="Proyecto Finalizado">
</p>

### 🏆 Logros Alcanzados

✅ **Sistema completo de gestión escolar**  
✅ **Todas las funcionalidades implementadas**  
✅ **Validaciones robustas y manejo de errores**  
✅ **Interfaz de usuario clara y organizada**  
✅ **Documentación completa**  
✅ **Código limpio y bien estructurado**  

### 🎯 Funcionalidades Implementadas

- **Gestión completa de estudiantes** (registrar, buscar, modificar, habilitar/deshabilitar)
- **Gestión completa de docentes** (registrar, buscar, modificar, habilitar/deshabilitar)
- **Gestión completa de grados** (registrar, buscar, modificar, habilitar/deshabilitar)
- **Gestión completa de aulas** (registrar, buscar, modificar, habilitar/deshabilitar)
- **Sistema de asistencias** (registrar, buscar por fecha/ID, modificar)
- **Sistema de inasistencias** (registrar, buscar, modificar, excusas)
- **Sistema de excusas** (registrar excusas por estudiante)
- **Listados completos** (estudiantes, docentes, grados, aulas, asistencias, inasistencias)
- **Validaciones exhaustivas** en todos los campos
- **Manejo de errores** mejorado

### 🚀 Estado del Proyecto

**¡PROYECTO 100% FUNCIONAL Y COMPLETO!**

El sistema de gestión escolar está completamente terminado y listo para ser utilizado. Todas las funcionalidades solicitadas han sido implementadas con éxito, incluyendo las mejoras y validaciones adicionales.

### 🎊 ¡Felicitaciones!

<p align="center">
  <strong>¡Excelente trabajo en equipo! 🎓👨‍💻👩‍💻</strong>
</p>

---

**Desarrollado con ❤️ para la gestión escolar** 
