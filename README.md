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
