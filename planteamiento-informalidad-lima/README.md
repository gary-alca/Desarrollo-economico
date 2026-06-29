# 1.1 Planteamiento del Problema — Informalidad laboral en el departamento de Lima (2024-2025)

Reconstrucción a nivel doctoral del apartado **1.1 Planteamiento del Problema** de la
tesis *"Factores socioeconómicos que influyen en la informalidad laboral en el
departamento de Lima en los años 2024-2025"* (Escuela Profesional de Economía,
Universidad Nacional Mayor de San Marcos).

## Entregables

- **`1.1_Planteamiento_del_Problema_6pag_graficos_oficiales.docx`** — **versión
  solicitada (~6 páginas)**. Usa gráficos **oficiales tomados tal cual** (no de
  elaboración propia): el esquema conceptual del INEI, la tasa de empleo informal
  mundial de ILOSTAT/OIT (2004-2022) y la PEA ocupada formal/informal del INEI (2024).
  Formato: Times New Roman 12, interlineado 1.5, texto justificado, márgenes 2.54 cm,
  referencias en APA 7. Los gráficos oficiales están en `oficial_img/`.
- **`1.1_Planteamiento_del_Problema_Informalidad_Lima.docx`** — versión extendida con
  9 figuras de elaboración propia (300 dpi) construidas con datos oficiales.
- **`1.2.1_Justificacion_Teorica.docx`** — justificación teórica (~2 páginas): texto del
  autor en negro y tres teorías añadidas en rojo (ingreso, desarrollo y capital
  humano/demografía), con citas y referencias APA 7.
- **`Capitulo_III_Metodologia_Informalidad_Lima.docx`** — **Capítulo III. Metodología
  (~25 páginas, A4)**. Tipo aplicada/cuantitativa, diseño no experimental transversal,
  población y muestra (ENAHO-INEI), operacionalización de variables, modelo **Logit/Probit**,
  efectos marginales y razón de momios, validación (ROC, pseudo-R², VIF, Hosmer-Lemeshow),
  contraste de hipótesis, robustez, limitaciones, ética y matriz de consistencia. Incluye
  7 tablas y 16 ecuaciones. Sigue la ruta del artículo guía (Semestre Económico, 2025) y la
  matriz del proyecto.
  > El autor exacto del artículo guía debe confirmarse: los portales oficiales (Semestre
  > Económico, SciELO, Dialnet) están bloqueados por la política de red de la sesión.

> Nota sobre las figuras oficiales: la política de red de esta sesión bloquea el acceso
> directo a los portales oficiales (ilo.org, inei.gob.pe, cepal.org devuelven 403 en la
> puerta de egreso), por lo que los gráficos oficiales se reprodujeron a partir de las
> figuras que ya obran en el proyecto de tesis (ILOSTAT e INEI). Para incorporar otros
> gráficos oficiales específicos, basta con adjuntar las imágenes y se insertan tal cual.

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
