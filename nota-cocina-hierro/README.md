# Nota Metodológica — Proyecto piloto «Cocina con Hierro» (JUNTOS)

Nota metodológica para la **evaluación de impacto** del proyecto piloto «Cocina con
Hierro», orientado a fortalecer la alimentación complementaria y reducir la anemia
infantil en niñas y niños de 6 a 35 meses de hogares usuarios del **Programa Nacional
JUNTOS**.

El diseño es un **ensayo controlado aleatorizado por conglomerados con entrada
escalonada (phase-in)**; el estimador principal es **ANCOVA** (hemoglobina final
controlando por la basal) y, ante incumplimiento del tratamiento, se complementa con
**variables instrumentales por 2SLS** (efecto local sobre los cumplidores, LATE).

El estilo y la estructura siguen las notas metodológicas oficiales del MIDIS para
evaluaciones de impacto. Todas las cifras del diagnóstico provienen de fuentes
oficiales (INEI-ENDES, MIDIS-JUNTOS, MINSA) y las referencias son reales (formato APA 7).

## Estructura

1. Resumen ejecutivo
2. Antecedentes y diagnóstico (motivación, evidencia, árbol de diagnóstico)
3. Propuesta de intervención (descripción, teoría del cambio, actores)
4. Diseño de evaluación (preguntas e hipótesis, estrategia experimental, modelo
   econométrico ANCOVA + IV, cálculo de poder, amenazas a la validez, ética/preregistro)
5. Calendario de actividades
6. Referencias
7. Anexos

## Reproducción

```bash
pip install python-docx matplotlib numpy
cd build
python figuras.py        # genera las figuras en build/img/ (datos oficiales)
python construir_doc.py  # ensambla Nota_Metodologica_Cocina_con_Hierro.docx
```

El documento `Nota_Metodologica_Cocina_con_Hierro.docx` es autocontenido (incrusta las
figuras). Las imágenes en `build/img/` son artefactos regenerables y no se versionan.
