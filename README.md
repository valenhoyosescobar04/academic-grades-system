# Academic Grades System

| Campo | Detalle |
|---|---|
| **Autor** | Valentina Hoyos Escobar |
| **Asignatura** | Pruebas de Software — Semestre V |
| **Tecnología** | Python + uv + pytest + pytest-bdd |
| **Por qué Python** | Sintaxis clara, pytest facilita TDD y pytest-bdd conecta Gherkin con el código sin configuración compleja |


---

## Estructura del proyecto

```
academic-grades-system/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── academic_grades.py
├── tests/
│   ├── test_academic_grades.py
│   ├── features/
│   │   └── academic_grades.feature
│   └── step_defs/
│       └── test_academic_grades_bdd.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

## Parte 1 — Análisis inicial

### 1.1 Particiones de equivalencia

> Se agrupan los valores en clases. Si un valor de la clase funciona, todos los demás deberían comportarse igual.

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida reprobatoria | 0.0 ≤ nota < 3.0 | 1.5 | Nota registrada |
| Válida aprobatoria | 3.0 ≤ nota ≤ 5.0 | 4.2 | Nota registrada |
| Inválida por debajo | nota < 0.0 | -2.0 | Error: fuera de rango |
| Inválida por encima | nota > 5.0 | 7.0 | Error: fuera de rango |
| Tipo de dato incorrecto | no es número | "buena" | Error: tipo inválido |

---

### 1.2 Análisis de valores límite

> Los bordes son donde los sistemas fallan con más frecuencia. Se prueba el valor justo antes, el exacto y el justo después.

| Valor | Posición | ¿Dentro del rango? | Resultado esperado |
|---|---|---|---|
| -0.1 | Antes del mínimo | No | Error: fuera de rango |
| 0.0 | Mínimo exacto | Sí | Nota registrada |
| 0.1 | Después del mínimo | Sí | Nota registrada |
| 4.9 | Antes del máximo | Sí | Nota registrada |
| 5.0 | Máximo exacto | Sí | Nota registrada |
| 5.1 | Después del máximo | No | Error: fuera de rango |

---

### 1.3 Preguntas al Product Owner

| # | Pregunta | Por qué impacta las pruebas |
|---|---|---|
| 1 | ¿El nombre de la materia es sensible a mayúsculas? ¿"cálculo" y "Cálculo" son la misma materia? | Si el sistema no normaliza el texto, necesito casos que verifiquen que ambas versiones generan duplicado. Si sí normaliza, esos mismos casos deben pasar sin error. |
| 2 | ¿Puede un estudiante corregir una nota ya registrada en el mismo semestre o siempre se bloquea? | Si nunca se puede cambiar, los casos solo cubren el rechazo. Si existe una operación de actualización separada, necesito casos adicionales que verifiquen que actualizar funciona mientras que registrar duplicado falla. |

---
## Parte 2 — Casos de prueba

| ID | Req | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | REQ1 | Registrar nota válida en rango medio | Estudiante sin notas previas | Materia: Cálculo, Semestre: 2025-1, Nota: 3.8 | Registrar la nota | Nota guardada sin error | Positivo |
| CP-02 | REQ1 | Rechazar nota negativa | Estudiante creado | Nota: -1.0 | Intentar registrar | Error: fuera de rango | Negativo |
| CP-03 | REQ1 | Rechazar nota mayor a 5.0 | Estudiante creado | Nota: 6.5 | Intentar registrar | Error: fuera de rango | Negativo |
| CP-04 | REQ1 | Aceptar límite inferior exacto | Estudiante creado | Nota: 0.0 | Registrar la nota | Nota guardada sin error | Borde |
| CP-05 | REQ1 | Aceptar límite superior exacto | Estudiante creado | Nota: 5.0 | Registrar la nota | Nota guardada sin error | Borde |
| CP-06 | REQ1 | Rechazar primer valor fuera del límite superior | Estudiante creado | Nota: 5.1 | Intentar registrar | Error: fuera de rango | Borde |
| CP-07 | REQ2 | Aprobar con exactamente 3.0 | Estudiante con nota 3.0 en Cálculo | Materia: Cálculo | Consultar aprobación | Aprueba: verdadero | Borde |
| CP-08 | REQ2 | Reprobar con 2.9 | Estudiante con nota 2.9 en Física | Materia: Física | Consultar aprobación | Aprueba: falso | Borde |
| CP-09 | REQ2 | Reprobar con nota mínima | Estudiante con nota 0.0 en Historia | Materia: Historia | Consultar aprobación | Aprueba: falso | Negativo |
| CP-10 | REQ3 | Promedio con tres notas | Estudiante con notas 2.0, 4.0 y 3.0 | — | Calcular promedio | 3.0 | Positivo |
| CP-11 | REQ3 | Promedio con una sola nota | Estudiante con nota 4.5 | — | Calcular promedio | 4.5 | Positivo |
| CP-12 | REQ3 | Promedio sin notas registradas | Estudiante recién creado | — | Calcular promedio | 0.0 | Negativo |
| CP-13 | REQ4 | Bloquear duplicado misma materia y semestre | Nota de Biología en 2025-1 registrada | Materia: Biología, Semestre: 2025-1 | Intentar registrar de nuevo | Error: nota duplicada | Negativo |
| CP-14 | REQ4 | Permitir misma materia en semestre diferente | Nota de Biología en 2025-1 registrada | Materia: Biología, Semestre: 2025-2 | Registrar la nota | Nota guardada sin error | Positivo |
| CP-15 | REQ4 | Permitir dos materias distintas mismo semestre | Nota de Biología en 2025-1 registrada | Materia: Química, Semestre: 2025-1 | Registrar la nota | Nota guardada sin error | Positivo |

---