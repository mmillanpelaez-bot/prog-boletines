# PROG-Boletines

> **Asignatura:** Programación — DAM1  
> **Alumno:** Manuel Felipe Millán Peláez  
> **Profesor:** Manuel Guimarei

---

## 📋 Índice

- [PROG-Boletines](#prog-boletines)
  - [📋 Índice](#-índice)
  - [Descripción](#descripción)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Instalación y uso](#instalación-y-uso)
  - [Estado de los boletines](#estado-de-los-boletines)

---

## Descripción

Repositorio con la entrega de los boletines de ejercicios de la asignatura de **Programación** (DAM1). Todos los boletines están resueltos en Python y son accesibles desde un menú principal interactivo.

---

## Estructura del proyecto

```
prog-boletines/
├── main.py                ← Menú principal (punto de entrada)
├── utils/menu.py          ← Menú generico de los boletines
└── boletines/
    ├── boletin_01/        ← Expresiones y booleanos
    ├── boletin_02/        ← Algoritmia
    ├── boletin_03/        ← Condicionales
    ├── boletin_04/        ← Condicionales avanzados
    ├── boletin_05/        ← Bucles
    ├── boletin_06/        ← Listas y tuplas
    ├── boletin_07/        ← Cadenas de caracteres
    ├── boletin_08/        ← Tuplas y listas avanzado
    ├── boletin_09/        ← Objetos (OOP)
    ├── boletin_10/        ← Excepciones
    └── boletin_11/        ← Ficheros
```

---

## Instalación y uso

Clonar el repositorio:

```bash
git clone https://github.com/mmillanpelaez-bot/prog-boletines.git
cd prog-boletines
```

Instalar dependencias (solo para el boletín 2):

```bash
pip install requests
```

Ejecutar el menú principal:

```bash
python main.py
```

O ejecutar un boletín directamente:

```bash
python boletines/boletin_05/bulletin_05.py
```

> Requiere **Python 3.10+**. No se necesitan más dependencias externas.

---

## Estado de los boletines

| #   | Tema                     | Ejercicios | Estado         |
| --- | ------------------------ | ---------- | -------------- |
| 1   | Expresiones y booleanos  | 5 / 5      | ✅ Completo    |
| 2   | Algoritmia               | 5 / 5      | ✅ Completo    |
| 3   | Condicionales            | 5 / 5      | ✅ Completo    |
| 4   | Condicionales avanzados  | 4 / 4      | ✅ Completo    |
| 5   | Bucles                   | 13 / 13    | ✅ Completo    |
| 6   | Listas y tuplas          | 11 / 11    | ✅ Completo    |
| 7   | Cadenas de caracteres    | 17 / 23    | 🔄 En progreso |
| 8   | Tuplas y listas avanzado | 11 / 11    | ✅ Completo    |
| 9   | Objetos Python           | 0 / 3      | 📋 Pendiente   |
| 10  | Excepciones              | 0 / 2      | 📋 Pendiente   |
| 11  | Ficheros Python          | 0 / 6      | 📋 Pendiente   |

**Leyenda:** ✅ Completo &nbsp;|&nbsp; 🔄 En progreso &nbsp;|&nbsp; 📋 Pendiente
