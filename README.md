# 🎓 Sistema de Gestión Escolar 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-yellow" alt="Estado">
  <img src="https://img.shields.io/badge/Licencia-Educativa-green" alt="Licencia">
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

---

## ✅ Validaciones Implementadas

- **Estudiantes**: ID único, nombre y apellido válidos, edad (5-18), curso (1-11)
- **Docentes**: ID único, nombre y apellido válidos, grado (1-20), materias
- **Grados**: ID único, nombre válido, asociación con aulas, cantidad (1-10)
- **Aulas**: ID único, nombre válido, capacidad (1-15)
- **Asistencias**: ID único, fecha válida, docente habilitado, cantidad válida, excusas

---

## 🖥️ Cómo Ejecutar

1. Asegúrate de tener **Python 3.6+** instalado
2. Navega al directorio del proyecto
3. Ejecuta el archivo principal:

```bash
python menu.py
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
</details>

---

## ✨ Funcionalidades Mejoradas

- Listados en formato tabular con encabezados
- Estados claramente mostrados (Habilitado/Deshabilitado)
- Manejo de errores mejorado y mensajes descriptivos
- Validación robusta de datos y excepciones específicas
- Interfaz de usuario clara y organizada
- Confirmaciones de operaciones exitosas

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
Sistema desarrollado para gestión escolar de un Colegio y Instituto Elaborado por Santiago Sanchez lopez Carlos Andres Reyes Grajales y Laura Cortez.

---

## 📄 Licencia
Este proyecto es de uso educativo. 