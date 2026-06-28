# 1.1 Planteamiento del Problema — Informalidad laboral en el departamento de Lima (2024-2025)

Reconstrucción a nivel doctoral del apartado **1.1 Planteamiento del Problema** de la
tesis *"Factores socioeconómicos que influyen en la informalidad laboral en el
departamento de Lima en los años 2024-2025"* (Escuela Profesional de Economía,
Universidad Nacional Mayor de San Marcos).

## Entregable

- **`1.1_Planteamiento_del_Problema_Informalidad_Lima.docx`** — documento Word listo
  para insertarse en la tesis. Formato: Times New Roman 12, interlineado 1.5, texto
  justificado, márgenes 2.54 cm, 9 figuras insertadas (300 dpi) y referencias en
  formato APA 7.

## Estructura del apartado

1. Contextualización mundial de la informalidad laboral.
2. Situación de América Latina.
3. Situación del Perú (evolución y estructura).
4. Principales factores socioeconómicos (educación, ingresos, tamaño de empresa, edad,
   sexo, área de residencia).
5. Situación específica del departamento de Lima.
6. Vacíos de conocimiento en la literatura.
7. Importancia económica y social del problema.
8. Pertinencia de estudiar Lima durante 2024-2025.
9. Cierre que conduce a la formulación del problema.

## Figuras (datos reales, fuentes oficiales)

| Fig. | Contenido | Fuente |
|------|-----------|--------|
| 1 | Empleo informal mundial por nivel de ingreso | OIT (2024) |
| 2 | Informalidad laboral en América Latina por país | OIT (2024) |
| 3 | Evolución de la tasa de empleo informal en el Perú, 2011-2024 | INEI (2025); CEPLAN (2024) |
| 4 | Empleo informal por rama de actividad económica | INEI (2025) |
| 5 | Empleo informal por nivel educativo | INEI (2025) |
| 6 | Empleo informal por tamaño de empresa | INEI (2025) |
| 7 | Empleo informal por grupos de edad | INEI (2025) |
| 8 | Empleo informal por sexo y área de residencia | INEI (2025) |
| 9 | Informalidad de Lima frente a las principales ciudades | INEI (2025) |

> Todos los datos provienen de fuentes oficiales (OIT/ILOSTAT, INEI, CEPAL, CEPLAN).
> No se han inventado datos, estadísticas, citas, DOI ni referencias.

## Reproducir

```bash
cd build
python3 figuras_informalidad.py      # genera las 9 figuras en build/img/ (300 dpi)
python3 construir_planteamiento.py   # ensambla el .docx
```

Dependencias: `matplotlib`, `numpy`, `python-docx`, `Pillow`.
