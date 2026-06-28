# -*- coding: utf-8 -*-
"""Ensambla la Nota Metodológica "Cocina con Hierro" (~17 páginas) en Word.

Evaluación de impacto experimental (ensayo aleatorizado por conglomerados con
entrada escalonada; estimador principal ANCOVA; IV/2SLS ante incumplimiento) del
proyecto piloto orientado a reducir la anemia infantil en hogares JUNTOS.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(__file__)
IMG = os.path.join(BASE, "img")
OUT = os.path.join(os.path.dirname(BASE), "Nota_Metodologica_Cocina_con_Hierro.docx")

ROJO = RGBColor(0x9E, 0x2A, 0x2B)
ROJO2 = RGBColor(0xC0, 0x50, 0x4D)
AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRISTXT = RGBColor(0x59, 0x59, 0x59)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

doc = Document()

# --- Estilos base ---
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)
normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
normal.paragraph_format.line_spacing = 1.15
normal.paragraph_format.space_after = Pt(6)

for sec in doc.sections:
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)
    sec.left_margin = Cm(2.8)
    sec.right_margin = Cm(2.8)


def _set_cell_bg(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def h1(text):
    p = doc.add_heading(level=1)
    run = p.add_run(text)
    run.font.color.rgb = ROJO
    run.font.size = Pt(15)
    run.font.name = "Calibri"
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    return p


def h2(text):
    p = doc.add_heading(level=2)
    run = p.add_run(text)
    run.font.color.rgb = ROJO2
    run.font.size = Pt(12.5)
    run.font.name = "Calibri"
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    return p


def h3(text):
    p = doc.add_heading(level=3)
    run = p.add_run(text)
    run.font.color.rgb = ROJO2
    run.font.size = Pt(11.5)
    run.italic = True
    return p


def para(text, justify=True, after=6):
    p = doc.add_paragraph()
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(after)
    parts = text.split("**")
    for i, seg in enumerate(parts):
        run = p.add_run(seg)
        if i % 2 == 1:
            run.bold = True
    return p


def ecuacion(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(11.5)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(3)
    parts = text.split("**")
    for i, seg in enumerate(parts):
        run = p.add_run(seg)
        if i % 2 == 1:
            run.bold = True
    return p


def figura(img_name, numero, titulo, fuente, interpretacion, width=5.9):
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(8)
    cap.paragraph_format.space_after = Pt(2)
    r = cap.add_run(f"Figura {numero}. ")
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = ROJO
    r2 = cap.add_run(titulo)
    r2.bold = True
    r2.font.size = Pt(10)
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_after = Pt(2)
    pic.add_run().add_picture(os.path.join(IMG, img_name), width=Inches(width))
    fp = doc.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.paragraph_format.space_after = Pt(4)
    fr = fp.add_run(f"Fuente: {fuente}")
    fr.font.size = Pt(8.5)
    fr.italic = True
    fr.font.color.rgb = GRISTXT
    if interpretacion:
        para(interpretacion)


def tabla_titulo(numero, titulo):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"Tabla {numero}. ")
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = ROJO
    r2 = p.add_run(titulo)
    r2.bold = True
    r2.font.size = Pt(10)


def tabla(headers, rows, nota="Elaboración propia.", widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    hdr = t.rows[0].cells
    for i, htext in enumerate(headers):
        _set_cell_bg(hdr[i], "9E2A2B")
        cp = hdr[i].paragraphs[0]
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = cp.add_run(htext)
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = BLANCO
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            if ri % 2 == 1:
                _set_cell_bg(cells[i], "F6E7E7")
            cp = cells[i].paragraphs[0]
            cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = cp.add_run(val)
            run.font.size = Pt(9)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    np = doc.add_paragraph()
    np.paragraph_format.space_after = Pt(8)
    nr = np.add_run(f"Nota. {nota}")
    nr.font.size = Pt(8.5)
    nr.italic = True
    nr.font.color.rgb = GRISTXT


# ============================================================
# PORTADA
# ============================================================
def portada():
    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("NOTA METODOLÓGICA")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = ROJO
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("Proyecto piloto «Cocina con Hierro» para fortalecer la "
                    "alimentación complementaria y reducir la anemia infantil en "
                    "hogares usuarios del Programa Nacional JUNTOS")
    r2.bold = True
    r2.font.size = Pt(15)
    r2.font.color.rgb = ROJO2
    doc.add_paragraph()
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rs = sub.add_run("Diseño para la evaluación de impacto mediante ensayo "
                     "aleatorizado por conglomerados con entrada escalonada "
                     "(estimador ANCOVA; variables instrumentales ante incumplimiento)")
    rs.italic = True
    rs.font.size = Pt(12)
    for _ in range(6):
        doc.add_paragraph()
    for linea, val in [("Curso", "Desarrollo Económico"),
                       ("Tema", "Evaluación de impacto de programas sociales y nutrición infantil"),
                       ("Nivel", "Posgrado / Evaluación de impacto"),
                       ("Versión", "1.0"),
                       ("Lima, Perú", "2026")]:
        pl = doc.add_paragraph()
        pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rl = pl.add_run(f"{linea}: ")
        rl.bold = True
        rl.font.size = Pt(11)
        pl.add_run(val).font.size = Pt(11)
    doc.add_page_break()


# ============================================================
# 1. RESUMEN EJECUTIVO
# ============================================================
def resumen():
    h1("1. Resumen ejecutivo")
    para(
        "La presente nota metodológica diseña la estrategia para estimar el impacto causal del proyecto "
        "piloto **«Cocina con Hierro»**, una intervención de educación alimentaria y cambio de "
        "comportamiento dirigida a las madres de niñas y niños de 6 a 35 meses pertenecientes a hogares "
        "usuarios del **Programa Nacional de Apoyo Directo a los Más Pobres (JUNTOS)**. La intervención "
        "consiste en sesiones demostrativas de preparación de alimentos ricos en hierro biodisponible, "
        "consejería nutricional y refuerzo conductual, y se concibe como complemento de la "
        "suplementación con hierro que el sector salud ya provee, no como su sustituto.")
    para(
        "El diagnóstico documenta que la anemia en niñas y niños de 6 a 35 meses constituye un problema "
        "de salud pública persistente en el Perú: tras un periodo de descenso, la prevalencia nacional "
        "se elevó a **43,1 % en 2023 y 43,7 % en 2024** (INEI, 2024, 2025), con brechas marcadas en el "
        "área rural (51,9 % en 2024) y en departamentos como Puno (70,4 %). Dado que JUNTOS concentra su "
        "atención en hogares pobres del ámbito rural —precisamente donde la anemia es más prevalente—, "
        "este programa ofrece una plataforma idónea para una intervención nutricional complementaria de "
        "bajo costo, siempre que su eficacia se sustente en evidencia experimental rigurosa.")
    para(
        "La evaluación adopta un **ensayo controlado aleatorizado por conglomerados** (cluster RCT), en "
        "el que la asignación al tratamiento se realiza a nivel de establecimiento de salud o centro "
        "poblado y no de hogar individual, a fin de reflejar la naturaleza comunitaria de la "
        "intervención y de contener la contaminación entre grupos. Por consideraciones éticas y "
        "operativas, se emplea un **diseño de entrada escalonada (phase-in)**: el grupo de control "
        "recibe la intervención en una fase posterior, lo que preserva la equidad sin comprometer la "
        "identificación del efecto causal en la primera fase. La variable de resultado primaria es la "
        "**concentración de hemoglobina** (g/dL), ajustada por altitud, medida en línea de base y en "
        "línea de salida.")
    para(
        "La estrategia de estimación principal es un modelo de **análisis de covarianza (ANCOVA)**, que "
        "regresa la hemoglobina final sobre la asignación al tratamiento controlando por la hemoglobina "
        "basal; esta especificación maximiza la potencia estadística cuando la autocorrelación del "
        "resultado es moderada (McKenzie, 2012). Ante un eventual **incumplimiento del tratamiento** "
        "(participación parcial de las madres asignadas), se complementa con una estimación de "
        "**variables instrumentales por mínimos cuadrados en dos etapas (2SLS)**, empleando la "
        "asignación aleatoria como instrumento de la participación efectiva, lo que identifica el efecto "
        "local del tratamiento sobre los cumplidores (LATE; Imbens y Angrist, 1994; Angrist, Imbens y "
        "Rubin, 1996). El documento desarrolla la teoría del cambio, el árbol de diagnóstico, el cálculo "
        "de poder, el análisis de amenazas a la validez con sus estrategias de mitigación, y las "
        "consideraciones éticas, de preregistro y de manejo de datos que sustentan una eventual "
        "implementación del estudio.")


# ============================================================
# 2. ANTECEDENTES Y DIAGNÓSTICO
# ============================================================
def antecedentes():
    h1("2. Antecedentes y diagnóstico")
    h2("2.1 Motivación")
    para(
        "La política social peruana ha situado la reducción de la anemia infantil entre sus prioridades "
        "sanitarias. El **Plan Nacional para la Reducción y Control de la Anemia Materno Infantil y la "
        "Desnutrición Crónica Infantil 2017-2021** y el posterior **Plan Multisectorial de Lucha contra "
        "la Anemia** establecieron metas explícitas de reducción de la prevalencia y articularon la "
        "respuesta de los sectores de salud, desarrollo social y saneamiento (MINSA, 2017). En esa "
        "arquitectura, el Programa Nacional JUNTOS ocupa un lugar estratégico: como programa de "
        "transferencias monetarias condicionadas, vincula el apoyo económico a los hogares pobres con el "
        "cumplimiento de corresponsabilidades en salud y educación, entre ellas los controles de "
        "crecimiento y desarrollo (CRED) de la primera infancia.")
    para(
        "El Programa JUNTOS atiende a una población amplia y crecientemente focalizada en los hogares más "
        "pobres del país. Hacia 2023 superó los 750 000 hogares usuarios y, según reportes "
        "institucionales recientes, la operación de pago alcanzó a más de 760 000 hogares en condición "
        "de pobreza y pobreza extrema (MIDIS-JUNTOS, 2024, 2026). Esta cobertura, concentrada en el "
        "ámbito rural y andino-amazónico, coincide territorialmente con las zonas de mayor prevalencia "
        "de anemia, lo que confiere a JUNTOS una capacidad de focalización difícilmente replicable por "
        "otros canales de política.")
    figura("fig04_cobertura_juntos.png", "1",
           "Hogares afiliados al Programa Nacional JUNTOS (miles)",
           "MIDIS-JUNTOS (2024, 2026). Elaboración propia.",
           "El gráfico de barras —idóneo para comparar magnitudes discretas entre periodos— evidencia la "
           "escala del Programa JUNTOS, que se ubica en torno a 750 000-830 000 hogares usuarios en los "
           "años recientes. La magnitud de la cobertura tiene dos implicancias para la presente "
           "propuesta. Primero, JUNTOS ofrece una plataforma operativa y un registro de beneficiarios "
           "que permite focalizar una intervención nutricional en los hogares con niñas y niños menores "
           "de 36 meses, población objetivo de la lucha contra la anemia. Segundo, la concentración del "
           "programa en hogares pobres del ámbito rural —donde la anemia es más prevalente— maximiza el "
           "potencial de impacto de una intervención complementaria de bajo costo unitario. La cifra de "
           "2026 corresponde a los hogares con abono en la primera operación de pago del año; las de "
           "años previos, a los hogares afiliados reportados por la institución.")
    para(
        "Pese a la prioridad de política y a la cobertura de los programas sociales, la anemia infantil "
        "se mantiene en niveles elevados y, tras un descenso parcial en la segunda mitad de la década "
        "pasada, ha vuelto a aumentar. Según la Encuesta Demográfica y de Salud Familiar (ENDES) del "
        "INEI, la prevalencia en niñas y niños de 6 a 35 meses pasó de 40,1 % en 2019 a 38,8 % en 2021 "
        "y se elevó a **43,1 % en 2023 y 43,7 % en 2024** (INEI, 2024, 2025). El retroceso reciente "
        "revela que las estrategias vigentes —centradas en la suplementación con hierro— no han bastado "
        "por sí solas para sostener la reducción de la anemia.")
    figura("fig01_evolucion_anemia.png", "2",
           "Prevalencia de anemia en niñas y niños de 6 a 35 meses, Perú",
           "Instituto Nacional de Estadística e Informática (INEI, 2024, 2025), ENDES. Elaboración propia.",
           "El gráfico de líneas —apropiado para representar la evolución temporal de una serie— muestra "
           "que la prevalencia de anemia descendió hasta 38,8 % en 2021 pero revirtió su tendencia y "
           "alcanzó 43,7 % en 2024, retornando por encima del umbral del 40 %. La variable corresponde "
           "al porcentaje de la población de 6 a 35 meses con hemoglobina por debajo del punto de corte. "
           "Se grafican únicamente los años con cifra oficial consolidada bajo el punto de corte vigente "
           "hasta 2023; en 2024 el MINSA adoptó nuevos umbrales de la OMS, por lo que las series no son "
           "estrictamente comparables (Resolución Ministerial N.º 251-2024-MINSA). La persistencia y el "
           "repunte recientes sustentan la pertinencia de reforzar el componente educativo y conductual "
           "de la respuesta, más allá de la provisión de suplementos.")
    para(
        "La anemia, además, está desigualmente distribuida. En 2023 afectó al 50,3 % de los niños del "
        "área rural frente al 40,2 % del área urbana, y en 2024 la prevalencia rural se elevó a 51,9 % "
        "(INEI, 2024, 2025). A nivel departamental, la incidencia es máxima en Puno (70,4 %), Ucayali "
        "(59,4 %) y Madre de Dios (58,3 %). Esta concentración territorial refuerza la lógica de "
        "intervenir a través de JUNTOS, cuya presencia es justamente más densa en los ámbitos de mayor "
        "prevalencia.")
    figura("fig02_urbano_rural.png", "3",
           "Anemia en niñas y niños de 6 a 35 meses por área de residencia",
           "Instituto Nacional de Estadística e Informática (INEI, 2024, 2025), ENDES. Elaboración propia.",
           "El gráfico de barras agrupadas contrasta la prevalencia de anemia entre el ámbito nacional, "
           "urbano y rural en 2023 y 2024. La brecha urbano-rural es persistente y se amplió: mientras "
           "el ámbito urbano se mantuvo en torno al 40 %, el rural superó el 50 % y se elevó a 51,9 % en "
           "2024. La variable es el porcentaje de niñas y niños de 6 a 35 meses con anemia. La elección "
           "del gráfico de barras se justifica por tratarse de categorías mutuamente excluyentes "
           "comparables entre dos años. La lectura es directa para el diseño: el problema se concentra "
           "donde JUNTOS opera, lo que aumenta la pertinencia y el potencial de impacto de una "
           "intervención focalizada en hogares rurales pobres.")
    figura("fig03_departamentos.png", "4",
           "Departamentos con mayor prevalencia de anemia (6-35 meses), 2023",
           "Instituto Nacional de Estadística e Informática (INEI, 2024), ENDES. Elaboración propia.",
           "El gráfico de barras ordena de mayor a menor la prevalencia de anemia en los departamentos "
           "más afectados, contrastándolos con el promedio nacional (línea gris). Puno alcanza el 70,4 %, "
           "más de 27 puntos por encima del promedio del país. La variable es el porcentaje de niñas y "
           "niños de 6 a 35 meses con anemia por departamento. La marcada heterogeneidad territorial "
           "tiene una implicancia metodológica relevante para la presente propuesta: dado que la "
           "prevalencia y sus determinantes varían entre regiones, el diseño de evaluación contempla la "
           "**estratificación geográfica** de la aleatorización, de modo que el balance entre los grupos "
           "de tratamiento y control se preserve dentro de cada estrato y la inferencia no se vea "
           "confundida por diferencias regionales estructurales.")
    para(
        "Las estrategias actuales presentan limitaciones reconocidas. La suplementación con hierro, "
        "pilar de la respuesta sanitaria, enfrenta una baja adherencia: efectos secundarios "
        "gastrointestinales, percepciones negativas sobre el suplemento y barreras de acceso reducen su "
        "consumo efectivo (WHO, 2016; Pasricha et al., 2021). A ello se suma que la alimentación "
        "complementaria de las niñas y niños suele ser pobre en hierro biodisponible: predominan dietas "
        "basadas en cereales y tubérculos, con escaso aporte de hierro hemínico de origen animal "
        "(vísceras, sangrecita, pescado), pese a su disponibilidad local y bajo costo. La evidencia "
        "señala que la sola entrega de insumos no modifica de manera sostenida las prácticas de "
        "alimentación, y que se requieren componentes educativos y de cambio de comportamiento para "
        "traducir el conocimiento en prácticas culinarias efectivas (Bhutta et al., 2013).")
    para(
        "De esta secuencia —prioridad de política, plataforma de JUNTOS, persistencia de la anemia y "
        "limitaciones de las estrategias actuales— surge la necesidad de **fortalecer el componente "
        "educativo y conductual** de la intervención nutricional. El proyecto piloto «Cocina con Hierro» "
        "responde a esa necesidad: busca dotar a las madres de conocimientos y habilidades culinarias "
        "concretas para incorporar hierro biodisponible en la dieta diaria de sus hijos, aprovechando "
        "los alimentos disponibles en su entorno. La presente nota define la metodología que permitiría "
        "estimar, con rigor causal, si esa estrategia logra elevar la hemoglobina infantil.")
    tabla_titulo("1", "Indicadores de contexto del diagnóstico")
    tabla(
        ["Indicador", "Valor", "Fuente"],
        [["Anemia en niñas y niños de 6 a 35 meses (2023)", "43,1 %", "INEI (2024)"],
         ["Anemia en niñas y niños de 6 a 35 meses (2024)", "43,7 %", "INEI (2025)"],
         ["Anemia en el área rural (2024)", "51,9 %", "INEI (2025)"],
         ["Anemia en el área urbana (2023)", "40,2 %", "INEI (2024)"],
         ["Departamento con mayor prevalencia: Puno (2023)", "70,4 %", "INEI (2024)"],
         ["Hogares usuarios del Programa JUNTOS (2024)", "≈ 830 000", "MIDIS-JUNTOS (2024)"],
         ["Hogares con abono (primera operación 2026)", "760 736", "MIDIS-JUNTOS (2026)"]],
        nota="Elaboración propia a partir de fuentes oficiales. Las cifras de 2024 corresponden al punto de "
             "corte vigente hasta ese año; el cambio metodológico del MINSA (R. M. N.º 251-2024) altera la comparabilidad.",
        widths=[8.5, 3.5, 4.0])

    h2("2.2 Evidencia")
    para(
        "La literatura ofrece evidencia experimental y cuasi-experimental directamente pertinente para "
        "el diseño propuesto. Esta revisión se organiza en tres niveles —internacional, latinoamericano "
        "y peruano— y privilegia los estudios con asignación aleatoria y los que midieron resultados "
        "biológicos (hemoglobina, estado del hierro) y no solo conocimientos o prácticas autorreportadas.")
    para(
        "**Evidencia internacional.** La serie de The Lancet sobre nutrición materno-infantil "
        "sistematizó las intervenciones con mayor respaldo causal y concluyó que la combinación de "
        "suplementación, fortificación y **educación nutricional para mejorar la alimentación "
        "complementaria** figura entre las acciones costo-efectivas para reducir la carga de la "
        "desnutrición y la anemia (Black et al., 2013; Bhutta et al., 2013). Las revisiones sistemáticas "
        "de la Colaboración Cochrane muestran que los micronutrientes en polvo reducen la anemia en la "
        "primera infancia, pero advierten que su efectividad depende críticamente de la adherencia, lo "
        "que justifica acompañar la provisión de insumos con componentes de consejería y cambio de "
        "comportamiento (De-Regil et al., 2013). La guía de la OMS sobre suplementación diaria con hierro "
        "en lactantes y niños recoge esta misma lógica integral (WHO, 2016).")
    para(
        "**Evidencia latinoamericana.** Los programas de transferencias monetarias condicionadas han "
        "sido evaluados experimentalmente con resultados en salud y nutrición infantil. La evaluación "
        "del programa Oportunidades de México documentó efectos positivos sobre el desarrollo y la "
        "reducción de la anemia en la primera infancia, asociados al componente de salud y a las "
        "transferencias (Fernald, Gertler y Neufeld, 2008). Esta evidencia respalda la hipótesis de que "
        "la plataforma de un programa de transferencias condicionadas, como JUNTOS, puede potenciar el "
        "efecto de una intervención nutricional, a la vez que advierte que la transferencia por sí sola "
        "rinde efectos limitados sobre la anemia si no se acompaña de acciones específicas.")
    para(
        "**Evidencia peruana.** El antecedente metodológico más relevante es el ensayo aleatorizado por "
        "conglomerados de Penny et al. (2005), publicado en The Lancet, que evaluó una intervención de "
        "educación nutricional entregada a través de los servicios de salud en el Perú y halló mejoras "
        "significativas en las prácticas de alimentación y en el crecimiento infantil. Este estudio "
        "demuestra la viabilidad y la validez de un diseño experimental por conglomerados centrado en el "
        "cambio de comportamiento, y constituye el referente directo del presente piloto. En el plano "
        "de las transferencias, las evaluaciones de JUNTOS (Perova y Vakis, 2012; Sánchez y Jaramillo, "
        "2012) encontraron efectos sobre el uso de servicios de salud y resultados nutricionales, con "
        "magnitudes que dependen de la intensidad y duración de la exposición al programa. En conjunto, "
        "la evidencia sugiere que un componente educativo-culinario bien diseñado, articulado a JUNTOS y "
        "al sector salud, es una vía plausible para incidir sobre la anemia, y que su eficacia debe "
        "establecerse mediante un diseño experimental que aísle el efecto causal.")
    tabla_titulo("2", "Revisión crítica de la evidencia seleccionada")
    tabla(
        ["Estudio", "País / método", "Resultados", "Relación con la propuesta"],
        [["Penny et al. (2005), The Lancet",
          "Perú; ensayo aleatorizado por conglomerados",
          "Mejora de prácticas de alimentación y del crecimiento infantil",
          "Referente directo del diseño por conglomerados y del componente educativo"],
         ["Fernald, Gertler y Neufeld (2008), The Lancet",
          "México; evaluación experimental de Oportunidades",
          "Reducción de anemia y mejora del desarrollo en la primera infancia",
          "Sustenta el uso de la plataforma de transferencias condicionadas"],
         ["De-Regil et al. (2013), Cochrane",
          "Revisión sistemática; micronutrientes en polvo",
          "Reducen anemia, pero la efectividad depende de la adherencia",
          "Justifica el componente de consejería y cambio de comportamiento"],
         ["Bhutta et al. (2013), The Lancet",
          "Revisión global de intervenciones nutricionales",
          "La educación para la alimentación complementaria es costo-efectiva",
          "Fundamenta la teoría del cambio del piloto"],
         ["Perova y Vakis (2012)",
          "Perú; evaluación de JUNTOS",
          "Efectos sobre uso de servicios de salud y nutrición según exposición",
          "Contextualiza el potencial y los límites de JUNTOS frente a la anemia"]],
        nota="Elaboración propia con base en la literatura citada.",
        widths=[3.6, 3.6, 4.4, 4.4])

    h2("2.3 Árbol de diagnóstico")
    para(
        "El problema central que motiva la intervención es la **alta prevalencia de anemia en niñas y "
        "niños de 6 a 35 meses de hogares usuarios del Programa JUNTOS**. El árbol de diagnóstico "
        "ordena las causas que originan el problema y las consecuencias que de él se derivan, "
        "ofreciendo la base lógica para la teoría del cambio.")
    figura("fig06_arbol.png", "5",
           "Árbol de diagnóstico del problema central",
           "Elaboración propia.",
           "El diagrama de árbol —apropiado para representar relaciones causa-efecto jerárquicas— sitúa "
           "en el centro el problema y despliega hacia abajo sus causas y hacia arriba sus consecuencias. "
           "Entre las **causas directas** se identifican una alimentación complementaria pobre en hierro "
           "biodisponible, prácticas culinarias y de cuidado inadecuadas, y una baja adherencia a la "
           "suplementación con hierro. Estas causas se sustentan, a su vez, en **causas indirectas** de "
           "carácter estructural: la pobreza y la restricción presupuestaria del hogar, la desinformación "
           "nutricional, las barreras de acceso a los servicios de salud y las deficiencias de agua y "
           "saneamiento. Las **consecuencias** de la anemia operan sobre el capital humano: retraso del "
           "desarrollo cognitivo y psicomotor, mayor morbilidad e infecciones en la primera infancia, y "
           "menor rendimiento escolar y logro educativo futuro, que en conjunto se traducen en una "
           "pérdida de productividad de largo plazo. La intervención «Cocina con Hierro» actúa "
           "principalmente sobre las dos primeras causas directas —la calidad de la alimentación "
           "complementaria y las prácticas culinarias— y, de manera complementaria, sobre la adherencia "
           "a la suplementación, a través de la consejería.")
    tabla_titulo("3", "Causas y consecuencias del problema central")
    tabla(
        ["Dimensión", "Elementos"],
        [["Causas directas",
          "Alimentación complementaria pobre en hierro biodisponible; prácticas culinarias y de cuidado inadecuadas; baja adherencia a la suplementación con hierro"],
         ["Causas indirectas",
          "Pobreza y restricción presupuestaria; desinformación nutricional; barreras de acceso a servicios de salud; agua y saneamiento deficientes"],
         ["Consecuencias directas",
          "Retraso del desarrollo cognitivo y psicomotor; mayor morbilidad; menor rendimiento escolar futuro"],
         ["Consecuencia final",
          "Pérdida de capital humano y de productividad en el largo plazo"]],
        nota="Elaboración propia.",
        widths=[4.0, 12.0])


# ============================================================
# 3. PROPUESTA DE INTERVENCIÓN
# ============================================================
def propuesta():
    h1("3. Propuesta de intervención")
    h2("3.1 Descripción de la propuesta")
    para(
        "«Cocina con Hierro» es un **programa de educación alimentaria y cambio de comportamiento de "
        "base comunitaria**, dirigido a las madres o cuidadoras principales de niñas y niños de 6 a 35 "
        "meses de hogares usuarios de JUNTOS. Su objetivo es incrementar el consumo de hierro "
        "biodisponible en la alimentación complementaria mediante el desarrollo de habilidades "
        "culinarias prácticas, la consejería nutricional personalizada y el refuerzo conductual "
        "sostenido. El programa **complementa**, y no reemplaza, la entrega de suplementos de hierro y "
        "los controles CRED a cargo del MINSA.")
    para(
        "El componente central son las **sesiones demostrativas de cocina**, en las que un personal "
        "capacitado (nutricionista o promotor de salud) prepara, junto con las madres, recetas a base "
        "de alimentos locales ricos en hierro hemínico —sangrecita, hígado y otras vísceras, bazo, "
        "pescado— combinados con potenciadores de la absorción (alimentos ricos en vitamina C) y con "
        "orientación sobre los inhibidores que conviene evitar (infusiones y lácteos junto a la comida "
        "principal). Cada sesión articula demostración, práctica guiada, degustación y entrega de un "
        "**recetario ilustrado** adaptado a la disponibilidad y al presupuesto del hogar.")
    para(
        "El protocolo de la intervención se detalla en la Tabla 4. El programa contempla **doce sesiones "
        "demostrativas** de aproximadamente 90 minutos, con **frecuencia quincenal** a lo largo de seis "
        "meses, organizadas en grupos de 10 a 15 madres por establecimiento de salud o centro poblado. "
        "Entre sesiones, **promotores comunitarios** realizan visitas domiciliarias de seguimiento para "
        "reforzar las prácticas, resolver dudas y apoyar la adherencia a la suplementación. La "
        "elegibilidad se define por la condición de hogar usuario de JUNTOS con al menos una niña o niño "
        "de 6 a 35 meses al inicio de la línea de base. La implementación se apoya en la "
        "infraestructura de los establecimientos de salud y en el padrón de JUNTOS para la convocatoria "
        "y el seguimiento.")
    tabla_titulo("4", "Protocolo de la intervención «Cocina con Hierro»")
    tabla(
        ["Componente", "Descripción", "Dosis"],
        [["Sesiones demostrativas de cocina",
          "Preparación práctica de recetas con hierro hemínico y potenciadores de absorción; degustación",
          "12 sesiones de ≈ 90 min, frecuencia quincenal (6 meses)"],
         ["Consejería nutricional",
          "Orientación personalizada sobre alimentación complementaria y adherencia a la suplementación",
          "Integrada a cada sesión y a las visitas"],
         ["Visitas domiciliarias de seguimiento",
          "Refuerzo conductual en el hogar a cargo de promotores comunitarios",
          "Al menos 1 visita entre sesiones"],
         ["Materiales",
          "Recetario ilustrado, insumos para la demostración, material de consejería",
          "Entrega por hogar participante"],
         ["Elegibilidad",
          "Hogar usuario de JUNTOS con niña/niño de 6 a 35 meses al inicio",
          "Verificada con el padrón de JUNTOS"]],
        nota="Elaboración propia.",
        widths=[3.8, 8.2, 4.0])

    h2("3.2 Teoría del cambio")
    para(
        "La teoría del cambio articula la cadena causal que vincula los insumos del programa con la "
        "reducción de la anemia, y explicita el mecanismo por el cual se espera que opere cada vínculo. "
        "No se limita a encadenar etapas: justifica, con base en la evidencia, por qué cada eslabón "
        "produce el siguiente.")
    para(
        "Los **insumos** (sesiones demostrativas, recetario, personal de salud y promotores capacitados, "
        "articulación con JUNTOS y MINSA) habilitan las **actividades** formativas y de seguimiento "
        "(sesiones de cocina, consejería y visitas domiciliarias). El **primer vínculo causal** sostiene "
        "que la práctica guiada y la degustación, a diferencia de la mera transmisión de información, "
        "generan **conocimientos y habilidades culinarias** efectivos: la teoría del aprendizaje "
        "experiencial y la evidencia de Penny et al. (2005) indican que el cambio de prácticas requiere "
        "demostración y ensayo, no solo mensajes. El **segundo vínculo** plantea que esas habilidades, "
        "reforzadas en el hogar, elevan la **frecuencia de preparaciones ricas en hierro** y mejoran la "
        "adherencia a la suplementación; el seguimiento domiciliario es el mecanismo que convierte el "
        "conocimiento en hábito sostenido (Bhutta et al., 2013). El **tercer vínculo** afirma que una "
        "mayor ingesta de hierro biodisponible incrementa la **absorción y los depósitos de hierro** y, "
        "por esa vía fisiológica, eleva la **concentración de hemoglobina** (Pasricha et al., 2021). El "
        "**cuarto vínculo** conecta el aumento de la hemoglobina con la **reducción de la anemia** y, en "
        "el largo plazo, con mejores resultados de desarrollo cognitivo y de capital humano (Black "
        "et al., 2013).")
    figura("fig07_teoria_cambio.png", "6",
           "Teoría del cambio del proyecto piloto «Cocina con Hierro»",
           "Elaboración propia.",
           "El diagrama de flujo —idóneo para representar una cadena de resultados— ordena de izquierda "
           "a derecha los insumos, las actividades, los productos y los resultados del programa, "
           "distinguiendo tres horizontes temporales en la columna de resultados: corto plazo (mayor "
           "ingesta de hierro biodisponible), mediano plazo (aumento de la hemoglobina infantil) y largo "
           "plazo (reducción de la anemia y mejora del capital humano). La franja inferior de supuestos "
           "recuerda que la cadena causal solo opera bajo condiciones habilitantes: participación "
           "efectiva de las madres, disponibilidad local de alimentos ricos en hierro, continuidad de la "
           "suplementación del MINSA y ausencia de shocks externos. Esta representación cumple una doble "
           "función: comunica la lógica del programa a los actores institucionales y fija los nodos de la "
           "cadena que la evaluación deberá medir —en particular, la hemoglobina como resultado primario "
           "y las prácticas alimentarias como mecanismo intermedio—, garantizando la correspondencia "
           "entre el diseño de la intervención y su estrategia de evaluación.")
    tabla_titulo("5", "Matriz de la teoría del cambio")
    tabla(
        ["Eslabón", "Elementos"],
        [["Insumos", "Sesiones y recetario; personal de salud y promotores; articulación JUNTOS-MINSA"],
         ["Actividades", "Sesiones demostrativas de cocina; consejería nutricional; visitas domiciliarias"],
         ["Productos", "Madres con nuevas habilidades culinarias; mayor frecuencia de preparaciones ricas en hierro; mejor adherencia"],
         ["Resultado de corto plazo", "Mayor ingesta de hierro biodisponible en la alimentación complementaria"],
         ["Resultado de mediano plazo", "Aumento de la concentración de hemoglobina infantil"],
         ["Resultado de largo plazo", "Reducción de la prevalencia de anemia; mejor desarrollo y capital humano"],
         ["Supuestos", "Participación efectiva; disponibilidad local de alimentos; continuidad de la suplementación"]],
        nota="Elaboración propia.",
        widths=[4.5, 11.5])

    h2("3.3 Actores involucrados")
    para(
        "La implementación articula a actores del sector social, de salud, comunitarios y académicos, "
        "cada uno con funciones y responsabilidades definidas, así como con distintos niveles de "
        "influencia e interés en los resultados de la intervención.")
    tabla_titulo("6", "Matriz de actores involucrados")
    tabla(
        ["Actor", "Función y responsabilidad", "Influencia", "Interés"],
        [["MIDIS", "Rectoría de la política social; financiamiento y conducción del piloto", "Alta", "Alto"],
         ["Programa JUNTOS", "Focalización, padrón de usuarios y convocatoria de hogares", "Alta", "Alto"],
         ["MINSA", "Rectoría sanitaria; suplementación y controles CRED", "Alta", "Alto"],
         ["Establecimientos de salud", "Sede de las sesiones; personal nutricional y registro de hemoglobina", "Media", "Alto"],
         ["Promotores comunitarios", "Sesiones demostrativas y visitas de seguimiento", "Media", "Alto"],
         ["Madres y cuidadoras", "Participación y adopción de prácticas en el hogar", "Baja", "Alto"],
         ["Equipo evaluador", "Diseño, aleatorización, medición y estimación de impacto", "Alta", "Alto"],
         ["Instituciones académicas y cooperación (BM, BID)", "Asistencia técnica, validación y financiamiento de la evaluación", "Media", "Medio"]],
        nota="Elaboración propia.",
        widths=[3.8, 7.2, 2.5, 2.5])


# ============================================================
# 4. DISEÑO DE EVALUACIÓN  (~40 % del contenido)
# ============================================================
def diseno():
    h1("4. Diseño de evaluación")
    para(
        "Esta sección constituye el núcleo de la nota metodológica. Define la estrategia que permitiría "
        "identificar el efecto causal de «Cocina con Hierro» sobre la hemoglobina infantil, con un nivel "
        "de detalle suficiente para sustentar la replicación del estudio. Se desarrollan las preguntas e "
        "hipótesis, la estrategia experimental por conglomerados con entrada escalonada, el modelo "
        "econométrico (ANCOVA como estimador principal y variables instrumentales ante incumplimiento), "
        "el cálculo de poder, el análisis de amenazas a la validez y las consideraciones éticas, de "
        "preregistro y de datos.")

    h2("4.1 Preguntas de investigación e hipótesis")
    para(
        "La **pregunta principal** de investigación es: ¿el proyecto piloto «Cocina con Hierro» "
        "incrementa la concentración de hemoglobina de las niñas y niños de 6 a 35 meses de hogares "
        "usuarios de JUNTOS, respecto del nivel que habrían alcanzado en ausencia de la intervención? "
        "De ella se derivan **preguntas secundarias**: ¿reduce la intervención la probabilidad de "
        "padecer anemia?; ¿mejora las prácticas de alimentación complementaria y la adherencia a la "
        "suplementación (mecanismos intermedios)?; ¿es el efecto heterogéneo según la severidad inicial "
        "de la anemia, la edad del niño o el ámbito geográfico?")
    para(
        "A diferencia de un diseño observacional, el experimento aleatorizado garantiza por construcción "
        "la equivalencia esperada entre los grupos de tratamiento y control, de modo que la diferencia "
        "de resultados al cierre puede interpretarse causalmente (Duflo, Glennerster y Kremer, 2007; "
        "Gertler et al., 2016). Las hipótesis se formulan en consecuencia.")
    para("**Hipótesis sustantivas:**")
    bullet("**H1 (principal):** la intervención incrementa la concentración promedio de hemoglobina de "
           "las niñas y niños tratados respecto del grupo de control, medida en la línea de salida.")
    bullet("**H2:** la intervención reduce la prevalencia de anemia (probabilidad de hemoglobina por "
           "debajo del punto de corte ajustado por altitud) en el grupo tratado.")
    bullet("**H3 (mecanismo):** la intervención aumenta la frecuencia de consumo de alimentos ricos en "
           "hierro y la adherencia a la suplementación, canales que vinculan la formación con la mejora "
           "de la hemoglobina.")
    para("**Hipótesis econométricas:** sobre el coeficiente de tratamiento β del modelo ANCOVA,")
    bullet("**H0:** β = 0 (la intervención no tiene efecto sobre la hemoglobina);")
    bullet("**H1:** β > 0 (la intervención eleva la hemoglobina).")
    para(
        "La **variable dependiente** principal es la concentración de hemoglobina (g/dL) ajustada por "
        "altitud, medida en la línea de salida; como resultado secundario se define la condición binaria "
        "de anemia. La **variable independiente de interés** es la asignación aleatoria al tratamiento a "
        "nivel de conglomerado. Se incluyen como covariables la hemoglobina basal, la edad y el sexo del "
        "niño, y características del hogar. Se designa **ex ante** H1 (hemoglobina) como resultado "
        "primario, único sobre el cual se sustentará la conclusión principal de eficacia; los resultados "
        "secundarios y los análisis de heterogeneidad incorporarán correcciones por comparaciones "
        "múltiples (procedimiento de Romano y Wolf, 2005), conforme al plan de análisis preregistrado "
        "(sección 4.5).")
    tabla_titulo("7", "Variables de la evaluación")
    tabla(
        ["Tipo", "Variables"],
        [["Resultado primario", "Concentración de hemoglobina (g/dL) ajustada por altitud, en línea de salida"],
         ["Resultado secundario", "Anemia (binaria, según punto de corte ajustado por altitud)"],
         ["Mecanismo (intermedias)", "Frecuencia de consumo de alimentos ricos en hierro; adherencia a la suplementación; conocimientos maternos"],
         ["Tratamiento", "Asignación aleatoria del conglomerado a «Cocina con Hierro» (binaria)"],
         ["Covariables / control", "Hemoglobina basal; edad y sexo del niño; educación materna; tamaño del hogar; estrato geográfico"]],
        nota="Elaboración propia.",
        widths=[4.2, 11.8])

    h2("4.2 Estrategia y diseño de evaluación")
    h3("a. Ensayo aleatorizado por conglomerados")
    para(
        "La evaluación adopta un **ensayo controlado aleatorizado por conglomerados** (cluster RCT), en "
        "el que la unidad de aleatorización es el **conglomerado** —el establecimiento de salud y su "
        "ámbito de influencia, o el centro poblado— y no el hogar individual. Tres razones justifican "
        "este nivel de asignación. Primero, la **naturaleza comunitaria** de la intervención: las "
        "sesiones demostrativas son grupales y se ofrecen a la comunidad, por lo que no es viable "
        "asignar tratamiento a unos hogares y negarlo a sus vecinos dentro del mismo establecimiento. "
        "Segundo, el **control de la contaminación**: si tratados y controles convivieran en la misma "
        "localidad, el intercambio de recetas y prácticas entre madres difundiría la intervención hacia "
        "el grupo de control y sesgaría a la baja el efecto estimado; aleatorizar por conglomerado "
        "confina la difusión dentro de las unidades tratadas. Tercero, la **factibilidad operativa y "
        "ética**, pues la asignación comunitaria es más transparente y aceptable para los actores "
        "locales. La **unidad de análisis**, en cambio, es la niña o el niño de 6 a 35 meses, nivel al "
        "que se mide el resultado de hemoglobina.")
    para(
        "La aleatorización se realiza de forma **estratificada** por ámbito geográfico (departamento o "
        "red de salud) y, dentro de cada estrato, por el tamaño del conglomerado, a fin de asegurar el "
        "balance de los grupos en presencia de la marcada heterogeneidad territorial documentada en el "
        "diagnóstico (Bruhn y McKenzie, 2009). Cuando el número de conglomerados sea reducido, se "
        "recurrirá al **emparejamiento por pares** (pair-matching) dentro de cada estrato antes de "
        "aleatorizar, lo que mejora el balance y la precisión.")
    h3("b. Diseño de entrada escalonada (phase-in) y cronograma de asignación")
    para(
        "Por razones éticas —no privar indefinidamente del programa a hogares pobres elegibles— y "
        "operativas —escalonar la carga logística—, se adopta un **diseño de entrada escalonada "
        "(phase-in)**: todos los conglomerados reciben finalmente la intervención, pero el momento de "
        "ingreso se asigna al azar. En la **Fase 1**, el grupo de tratamiento recibe «Cocina con Hierro» "
        "mientras el grupo de control permanece en lista de espera y mantiene la oferta estándar del "
        "Estado (suplementación y CRED). La **estimación de impacto** compara la hemoglobina de ambos "
        "grupos al cierre de la Fase 1, cuando solo el grupo de tratamiento ha sido expuesto. En la "
        "**Fase 2**, el grupo de control recibe la intervención, lo que preserva la equidad. Este diseño "
        "es de uso extendido en evaluaciones de política social y conserva la validez interna del "
        "experimento en la primera fase (Duflo et al., 2007; Hemming et al., 2015).")
    figura("fig08_diseno_phasein.png", "7",
           "Diseño experimental por conglomerados con entrada escalonada (phase-in)",
           "Elaboración propia.",
           "El diagrama representa el flujo de la asignación. A partir de un marco muestral de "
           "conglomerados elegibles, la aleatorización estratificada distribuye las unidades en dos "
           "brazos. El grupo de tratamiento recibe «Cocina con Hierro» en la Fase 1 (línea de base, "
           "intervención y línea de salida), mientras el grupo de control permanece en espera con la "
           "oferta estándar y recibe la intervención recién en la Fase 2. La comparación de impacto se "
           "realiza al cierre de la Fase 1, momento en que la única diferencia sistemática entre los "
           "grupos es la exposición a la intervención, lo que sustenta la interpretación causal del "
           "contraste. El escalonamiento resuelve la objeción ética de negar el programa y, a la vez, "
           "permite estimar el efecto de corto plazo sin contaminación entre brazos.")
    h3("c. Proceso de randomización, seguimiento y medición")
    para(
        "El **proceso de randomización** se ejecutará mediante un algoritmo reproducible con semilla "
        "fijada y documentada, a partir del listado de conglomerados elegibles y de las variables de "
        "estratificación, antes de iniciar cualquier actividad de la intervención. Se verificará el "
        "**balance de covariables** en la línea de base mediante pruebas de diferencia de medias por "
        "conglomerado y se reportará la tabla de balance, conforme a las buenas prácticas de los ensayos "
        "de campo (Bruhn y McKenzie, 2009; Athey e Imbens, 2017). El **seguimiento** comprende el "
        "registro de asistencia a las sesiones, las visitas domiciliarias y un sistema de monitoreo de "
        "la implementación (fidelidad del tratamiento). La **medición de resultados** se realiza en dos "
        "momentos —línea de base y línea de salida— con el mismo protocolo: la hemoglobina se determina "
        "por punción capilar con hemoglobinómetro calibrado, con control de calidad, y se **ajusta por "
        "altitud** según los procedimientos oficiales, dado que la población objetivo reside "
        "mayoritariamente en zonas altoandinas. Los mecanismos intermedios (prácticas de alimentación, "
        "adherencia, conocimientos) se miden mediante un cuestionario aplicado a la madre. Este "
        "protocolo —semilla de aleatorización, estratos, instrumentos y procedimientos de medición— se "
        "documentará con detalle suficiente para permitir la **replicación** del estudio.")

    h3("d. Modelo econométrico principal: ANCOVA")
    para(
        "La estrategia de estimación principal es un modelo de **análisis de covarianza (ANCOVA)**, que "
        "regresa la hemoglobina en la línea de salida sobre la asignación al tratamiento, controlando "
        "por la hemoglobina basal:")
    ecuacion("Hᵢⱼ,₁ = α + β·Tⱼ + γ·Hᵢⱼ,₀ + Xᵢⱼ′δ + uⱼ + εᵢⱼ")
    para(
        "donde Hᵢⱼ,₁ es la hemoglobina del niño i del conglomerado j en la línea de salida; Tⱼ es la "
        "asignación aleatoria al tratamiento del conglomerado j (1 = tratamiento, 0 = control); Hᵢⱼ,₀ es "
        "la hemoglobina basal; Xᵢⱼ es un vector de covariables (edad y sexo del niño, características del "
        "hogar y efectos fijos de estrato); uⱼ es el componente de error a nivel de conglomerado; y εᵢⱼ "
        "es el error idiosincrásico. El **coeficiente de interés es β**, que recoge el efecto promedio "
        "del tratamiento (intención de tratar, ITT) sobre la hemoglobina.")
    para(
        "La elección de ANCOVA frente a la simple diferencia de medias o a la estimación en diferencias "
        "(diferencias-en-diferencias) responde a un argumento de **eficiencia estadística**: cuando la "
        "autocorrelación del resultado entre líneas de base y de salida es moderada —como es típico en "
        "la hemoglobina—, controlar por el valor basal reduce sustancialmente la varianza residual y, "
        "por tanto, el tamaño de muestra requerido para una potencia dada (McKenzie, 2012). La "
        "**identificación** del efecto causal descansa en la aleatorización: al asignarse Tⱼ al azar, es "
        "independiente de los resultados potenciales y de las covariables, de modo que β es un estimador "
        "insesgado del efecto del tratamiento. La inferencia debe reconocer la estructura de "
        "conglomerados: los **errores estándar se agrupan (cluster) a nivel de conglomerado**, pues las "
        "observaciones de niños de un mismo establecimiento no son independientes; con pocos "
        "conglomerados se emplearán correcciones de muestra finita o inferencia por aleatorización "
        "(randomization inference) (Cameron y Miller, 2015).")

    h3("e. Variables instrumentales (2SLS) ante incumplimiento del tratamiento")
    para(
        "El modelo ANCOVA estima el efecto de **intención de tratar** (ITT): el efecto de ser asignado "
        "al programa, con independencia de la participación efectiva. Sin embargo, es previsible cierto "
        "**incumplimiento**: algunas madres asignadas al tratamiento no asistirán a las sesiones o lo "
        "harán parcialmente. En ese caso, el ITT subestima el efecto sobre quienes efectivamente "
        "participan. Para recuperar el **efecto del tratamiento sobre el tratado**, se complementa la "
        "estimación con **variables instrumentales por mínimos cuadrados en dos etapas (2SLS)**, "
        "empleando la asignación aleatoria Tⱼ como **instrumento** de la participación efectiva Dᵢⱼ:")
    ecuacion("1.ª etapa:  Dᵢⱼ = π₀ + π₁·Tⱼ + Xᵢⱼ′θ + νᵢⱼ")
    ecuacion("2.ª etapa:  Hᵢⱼ,₁ = α + βₗ·D̂ᵢⱼ + γ·Hᵢⱼ,₀ + Xᵢⱼ′δ + ωᵢⱼ")
    para(
        "El estimador βₗ identifica el **efecto local promedio del tratamiento (LATE)** sobre los "
        "**cumplidores** —las madres que participan si y solo si son asignadas— bajo cuatro supuestos "
        "(Imbens y Angrist, 1994; Angrist, Imbens y Rubin, 1996): (i) **relevancia**, el instrumento "
        "predice la participación (π₁ ≠ 0), verificable con el estadístico F de la primera etapa; (ii) "
        "**independencia**, garantizada por la aleatorización; (iii) **restricción de exclusión**, la "
        "asignación afecta la hemoglobina únicamente a través de la participación y no por otras vías; y "
        "(iv) **monotonicidad**, ausencia de «desafiadores» (madres que participarían solo si no son "
        "asignadas). La **ventaja** del enfoque es que aprovecha la aleatorización para obtener un efecto "
        "causal de la participación, no contaminado por la autoselección; su **limitación** es que el "
        "LATE se circunscribe a los cumplidores y no necesariamente coincide con el efecto promedio "
        "poblacional. Por ello, y conforme a la práctica de las evaluaciones rigurosas, **el ITT (ANCOVA) "
        "se reporta como resultado principal** y la estimación por IV se presenta como complemento "
        "interpretativo ante incumplimiento, no como modelo central.")

    h3("f. Interpretación de los coeficientes")
    para(
        "El coeficiente β se expresa en las unidades del resultado. Por ejemplo, un valor de **β = 0,45** "
        "indica que la intervención eleva, en promedio, la concentración de hemoglobina de las niñas y "
        "niños tratados en **0,45 g/dL** respecto del grupo de control, manteniendo constante la "
        "hemoglobina basal. La interpretación debe atender tres dimensiones. La **significancia "
        "estadística** se evalúa con el valor p y el **intervalo de confianza al 95 %**: si el intervalo "
        "—por ejemplo, [0,18; 0,72] g/dL— excluye el cero, se rechaza H0 y se concluye que el efecto es "
        "estadísticamente distinto de cero. La **precisión** se lee en la amplitud del intervalo. Y la "
        "**relevancia práctica** exige contrastar la magnitud con un referente clínico y de política: "
        "un incremento de 0,45 g/dL puede bastar para desplazar a una fracción apreciable de niños por "
        "encima del punto de corte de anemia, lo que se cuantifica de forma directa con el resultado "
        "secundario binario (H2). En la estimación por IV, el coeficiente βₗ se interpreta de manera "
        "análoga, pero referido al efecto sobre los cumplidores. La nota subraya que la significancia "
        "estadística no equivale por sí sola a relevancia de política: ambas deben informarse de forma "
        "conjunta.")

    h2("4.3 Cálculo de poder y muestra propuesta")
    para(
        "El tamaño de la muestra se determina mediante un **cálculo de poder** para detectar el efecto "
        "sobre el resultado primario (hemoglobina). En un diseño por conglomerados, el cálculo difiere "
        "del de un experimento individual porque las observaciones dentro de un mismo conglomerado están "
        "correlacionadas. Los parámetros relevantes son: la **potencia** (1 − β), probabilidad de "
        "detectar un efecto verdadero, fijada en 0,80; el **nivel de significancia** (α = 0,05, dos "
        "colas); el **tamaño de efecto esperado**, o efecto mínimo detectable (MDE), fijado en **0,45 "
        "g/dL** sobre la base de la evidencia de intervenciones nutricionales; el **coeficiente de "
        "correlación intraclase (ICC)**, que mide qué fracción de la varianza total se sitúa entre "
        "conglomerados (se asume un valor conservador de 0,05); la **desviación estándar** de la "
        "hemoglobina (≈ 1,3 g/dL); el número de **niños por conglomerado** (m); y el número de "
        "**conglomerados** por brazo (k).")
    para(
        "La correlación intraclase eleva el tamaño requerido a través del **efecto de diseño**, "
        "DEFF = 1 + (m − 1)·ICC. En sentido contrario, el ajuste por la hemoglobina basal del modelo "
        "ANCOVA reduce la varianza residual en un factor (1 − ρ²), donde ρ es la correlación entre las "
        "mediciones de línea de base y de salida (McKenzie, 2012). La Figura 8 ilustra cómo el MDE "
        "disminuye conforme aumenta el número de conglomerados, y cómo el ajuste ANCOVA desplaza la "
        "curva hacia abajo, permitiendo detectar el efecto objetivo con menos conglomerados.")
    figura("fig05_curva_poder.png", "8",
           "Efecto mínimo detectable según número de conglomerados por brazo",
           "Elaboración propia, fórmula estándar de potencia para ensayos por conglomerados.",
           "El gráfico de líneas —idóneo para representar una relación funcional continua— muestra el "
           "efecto mínimo detectable (en g/dL de hemoglobina) en función del número de conglomerados por "
           "brazo, fijados 30 niños por conglomerado y un ICC de 0,05. La curva gris corresponde a la "
           "diferencia simple de medias y la roja al estimador ANCOVA con ajuste por la hemoglobina basal "
           "(ρ = 0,5), que reduce el MDE para cualquier número de conglomerados. La línea azul marca el "
           "efecto objetivo de 0,45 g/dL: su intersección con la curva ANCOVA indica que se requieren "
           "aproximadamente **20 conglomerados por brazo** (40 en total) para detectar ese efecto con una "
           "potencia del 80 %. Estas cifras son ilustrativas y deben refinarse mediante simulación una "
           "vez disponibles estimaciones empíricas del ICC y de la correlación basal-salida en la "
           "población objetivo.")
    tabla_titulo("8", "Parámetros del cálculo de poder")
    tabla(
        ["Parámetro", "Valor propuesto"],
        [["Efecto mínimo detectable (MDE)", "0,45 g/dL de hemoglobina"],
         ["Desviación estándar de la hemoglobina", "≈ 1,3 g/dL"],
         ["Nivel de significancia (α)", "0,05 (dos colas)"],
         ["Potencia estadística (1 − β)", "0,80"],
         ["Coeficiente de correlación intraclase (ICC)", "0,05"],
         ["Correlación basal-salida (ρ, ganancia ANCOVA)", "≈ 0,5"],
         ["Niños por conglomerado (m)", "≈ 30"],
         ["Conglomerados por brazo (k)", "≈ 20"],
         ["Conglomerados totales", "≈ 40"],
         ["Tamaño de muestra analítico (niños)", "≈ 1 200"]],
        nota="Elaboración propia con base en la fórmula estándar de potencia para ensayos por conglomerados "
             "y en McKenzie (2012). Cifras orientativas sujetas a refinamiento por simulación y a una "
             "sobremuestra del 15 %-20 % por deserción.",
        widths=[9.0, 7.0])
    para(
        "El cálculo es sensible al ICC y a la correlación basal-salida: un ICC mayor o una correlación "
        "menor elevan el número de conglomerados requerido. Por ello se recomienda contemplar una "
        "**sobremuestra de seguridad del 15 %-20 %** frente a la deserción esperada entre líneas, y "
        "refinar el cálculo mediante **simulación** una vez se disponga de estimaciones empíricas de "
        "estos parámetros en la población objetivo.")

    h2("4.4 Amenazas a la validez y estrategias de mitigación")
    para(
        "El diseño experimental enfrenta amenazas a la validez interna y externa que es preciso "
        "anticipar y mitigar de manera explícita.")
    para(
        "**Sesgo de selección.** La aleatorización elimina el sesgo de selección en la asignación; no "
        "obstante, podría reintroducirse si el cumplimiento de la elegibilidad o la conformación de los "
        "conglomerados respondiera a criterios no aleatorios. Se mitiga fijando la elegibilidad y la "
        "aleatorización **antes** de la intervención y verificando el balance de covariables en la línea "
        "de base.")
    para(
        "**Contaminación y spillovers.** El intercambio de recetas entre madres de tratamiento y control "
        "difundiría la intervención hacia el grupo de control. La aleatorización **por conglomerados** es "
        "la principal defensa, pues separa geográficamente los brazos; se refuerza priorizando "
        "conglomerados con baja interacción entre sí y midiendo la exposición del control a contenidos "
        "del programa para detectar contaminación efectiva.")
    para(
        "**Atrición (deserción).** La pérdida diferencial de niños entre líneas —por migración o "
        "rechazo— sesga el estimador si se correlaciona con los resultados. Se mitiga con un seguimiento "
        "intensivo, pruebas de **atrición diferencial** entre brazos y, de ser necesario, **cotas de "
        "Lee** para acotar el sesgo. El **incumplimiento** se aborda con la estrategia de IV descrita en "
        "la sección 4.2.e, preservando el ITT como resultado principal.")
    para(
        "**Efecto Hawthorne y efecto John Henry.** Las madres tratadas podrían modificar su conducta por "
        "saberse observadas (Hawthorne), y las del control podrían esforzarse de manera compensatoria "
        "(John Henry). Ambos se atenúan con una **comunicación neutra** del seguimiento, con la medición "
        "objetiva de la hemoglobina —resultado no fácilmente manipulable— y con el diseño phase-in, que "
        "ofrece al control la perspectiva de recibir el programa y reduce su incentivo a comportamientos "
        "compensatorios. La **mortalidad experimental** (atrición severa) se monitorea como parte del "
        "seguimiento.")
    para(
        "**Equilibrio entre grupos.** Se reportará la tabla de balance de la línea de base; ante "
        "desbalances residuales en covariables relevantes, el control por dichas covariables en el "
        "modelo ANCOVA corrige la estimación. La **validez externa** se favorece seleccionando "
        "conglomerados representativos de los ámbitos de mayor prevalencia y documentando el contexto de "
        "implementación.")
    tabla_titulo("9", "Principales amenazas a la validez y estrategias de mitigación")
    tabla(
        ["Amenaza", "Estrategia de mitigación"],
        [["Sesgo de selección", "Aleatorización y elegibilidad fijadas ex ante; verificación de balance"],
         ["Contaminación / spillovers", "Aleatorización por conglomerados; medición de exposición del control"],
         ["Atrición diferencial", "Seguimiento intensivo; pruebas de atrición; cotas de Lee"],
         ["Incumplimiento del tratamiento", "Estimación por variables instrumentales (LATE); ITT como principal"],
         ["Efecto Hawthorne / John Henry", "Comunicación neutra; resultado objetivo (hemoglobina); diseño phase-in"],
         ["Desbalance entre grupos", "Estratificación; control por covariables en ANCOVA"],
         ["Validez externa", "Selección de conglomerados representativos; documentación del contexto"]],
        nota="Elaboración propia.",
        widths=[5.5, 10.5])

    h2("4.5 Consideraciones éticas, preregistro y datos")
    para(
        "El estudio se rige por los principios éticos de la investigación con seres humanos y, en "
        "particular, con **menores de edad**. Requiere la aprobación de un **comité de ética** y el "
        "**consentimiento informado** de las madres o cuidadoras, tanto para la participación en la "
        "intervención como para la toma de muestras de hemoglobina del niño. El diseño **phase-in** "
        "responde a la exigencia ética de no privar de manera permanente a hogares pobres elegibles: el "
        "grupo de control recibe la intervención en la Fase 2. Durante toda la evaluación se mantiene la "
        "oferta estándar del Estado (suplementación y CRED) para ambos grupos, de modo que ningún niño "
        "queda desprovisto de la atención sanitaria a la que tiene derecho.")
    para(
        "La **confidencialidad** se garantiza mediante la seudonimización de los registros y el "
        "tratamiento de los datos conforme a la Ley de Protección de Datos Personales; el equipo "
        "evaluador no accede a identidades nominales. Con el fin de reforzar la credibilidad y la "
        "transparencia, se elaborará y depositará un **plan de análisis preregistrado** en un registro "
        "público (por ejemplo, el AEA RCT Registry), en el que se fijarán con anticipación el resultado "
        "primario, las hipótesis secundarias, las dimensiones de heterogeneidad y las especificaciones "
        "econométricas, incluido el manejo del incumplimiento y de las comparaciones múltiples; el "
        "preregistro reduce los grados de libertad del investigador y el riesgo de búsqueda selectiva de "
        "resultados (Casey, Glennerster y Miguel, 2012).")
    para(
        "El **plan de manejo de datos** contempla la documentación de instrumentos, la trazabilidad de "
        "la base y la **reproducibilidad** del análisis: en el marco de la ciencia abierta, el código de "
        "estimación y la **base de datos anonimizada** se depositarán en un repositorio público al "
        "concluir la evaluación, junto con un cuaderno de análisis que permita replicar los resultados. "
        "Se incorporará, además, un análisis de **costo-efectividad** que compare el costo por punto de "
        "hemoglobina ganado —o por caso de anemia evitado— con el de intervenciones alternativas, de "
        "modo que los resultados sean directamente útiles para la decisión de escalar el piloto.")


# ============================================================
# 5. CALENDARIO
# ============================================================
def calendario():
    h1("5. Calendario de actividades")
    para(
        "El cronograma contempla un horizonte aproximado de **dos años y medio**, desde la planificación "
        "hasta la difusión de resultados, e integra el diseño phase-in: la línea de salida de la Fase 1 "
        "—momento de la estimación de impacto— se mide al cabo de seis meses de intervención, tras lo "
        "cual el grupo de control ingresa al programa.")
    tabla_titulo("10", "Calendario de actividades (tipo Gantt)")
    tabla(
        ["Fase", "Actividad", "Responsable", "Periodo"],
        [["1", "Planificación, convenios y preregistro del protocolo", "MIDIS / Equipo evaluador", "Meses 1-3"],
         ["2", "Selección y aleatorización estratificada de conglomerados", "Equipo evaluador", "Meses 3-4"],
         ["3", "Línea de base (hemoglobina y cuestionario)", "Equipo evaluador / EE. SS.", "Meses 4-5"],
         ["4", "Implementación Fase 1 (12 sesiones, 6 meses)", "Promotores / MINSA", "Meses 5-11"],
         ["5", "Seguimiento y monitoreo de fidelidad", "Equipo evaluador", "Meses 5-11"],
         ["6", "Línea de salida Fase 1 (medición de impacto)", "Equipo evaluador / EE. SS.", "Meses 11-12"],
         ["7", "Procesamiento de datos y estimación econométrica", "Equipo evaluador", "Meses 12-16"],
         ["8", "Implementación Fase 2 (entrada del grupo de control)", "Promotores / MINSA", "Meses 12-18"],
         ["9", "Análisis de costo-efectividad y reportes", "Equipo evaluador", "Meses 16-20"],
         ["10", "Difusión de resultados y repositorio abierto", "MIDIS / Equipo evaluador", "Meses 20-24"]],
        nota="Elaboración propia. Los periodos son referenciales y se ajustarán al calendario operativo.",
        widths=[1.3, 7.7, 4.5, 2.5])


# ============================================================
# 6. REFERENCIAS
# ============================================================
def referencias():
    h1("6. Referencias")
    refs = [
        "Angrist, J. D., Imbens, G. W. y Rubin, D. B. (1996). Identification of causal effects using instrumental variables. Journal of the American Statistical Association, 91(434), 444-455.",
        "Athey, S. e Imbens, G. W. (2017). The econometrics of randomized experiments. En A. V. Banerjee y E. Duflo (Eds.), Handbook of Economic Field Experiments (Vol. 1, pp. 73-140). North-Holland.",
        "Bhutta, Z. A., Das, J. K., Rizvi, A., Gaffey, M. F., Walker, N., Horton, S., Webb, P., Lartey, A. y Black, R. E. (2013). Evidence-based interventions for improvement of maternal and child nutrition: What can be done and at what cost? The Lancet, 382(9890), 452-477.",
        "Black, R. E., Victora, C. G., Walker, S. P., Bhutta, Z. A., Christian, P., de Onis, M., Ezzati, M., Grantham-McGregor, S., Katz, J., Martorell, R. y Uauy, R. (2013). Maternal and child undernutrition and overweight in low-income and middle-income countries. The Lancet, 382(9890), 427-451.",
        "Bruhn, M. y McKenzie, D. (2009). In pursuit of balance: Randomization in practice in development field experiments. American Economic Journal: Applied Economics, 1(4), 200-232.",
        "Cameron, A. C. y Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. Journal of Human Resources, 50(2), 317-372.",
        "Casey, K., Glennerster, R. y Miguel, E. (2012). Reshaping institutions: Evidence on aid impacts using a preanalysis plan. The Quarterly Journal of Economics, 127(4), 1755-1812.",
        "De-Regil, L. M., Suchdev, P. S., Vist, G. E., Walleser, S. y Peña-Rosas, J. P. (2013). Home fortification of foods with multiple micronutrient powders for health and nutrition in children under two years of age. Cochrane Database of Systematic Reviews, (4), CD008959.",
        "Duflo, E., Glennerster, R. y Kremer, M. (2007). Using randomization in development economics research: A toolkit. En T. P. Schultz y J. A. Strauss (Eds.), Handbook of Development Economics (Vol. 4, pp. 3895-3962). North-Holland.",
        "Fernald, L. C. H., Gertler, P. J. y Neufeld, L. M. (2008). Role of cash in conditional cash transfer programmes for child health, growth, and development: An analysis of Mexico's Oportunidades. The Lancet, 371(9615), 828-837.",
        "Gertler, P. J., Martinez, S., Premand, P., Rawlings, L. B. y Vermeersch, C. M. J. (2016). Impact evaluation in practice (2.ª ed.). Banco Mundial.",
        "Glennerster, R. y Takavarasha, K. (2013). Running randomized evaluations: A practical guide. Princeton University Press.",
        "Hemming, K., Haines, T. P., Chilton, P. J., Girling, A. J. y Lilford, R. J. (2015). The stepped wedge cluster randomised trial: Rationale, design, analysis, and reporting. BMJ, 350, h391.",
        "Imbens, G. W. y Angrist, J. D. (1994). Identification and estimation of local average treatment effects. Econometrica, 62(2), 467-475.",
        "Instituto Nacional de Estadística e Informática [INEI]. (2024). Perú: Indicadores de resultados de los programas presupuestales, ENDES 2023. INEI.",
        "Instituto Nacional de Estadística e Informática [INEI]. (2025). Perú: Indicadores de resultados de los programas presupuestales, ENDES 2024. INEI.",
        "McKenzie, D. (2012). Beyond baseline and follow-up: The case for more T in experiments. Journal of Development Economics, 99(2), 210-221.",
        "Ministerio de Desarrollo e Inclusión Social [MIDIS]. (2024). Programa Nacional de Apoyo Directo a los Más Pobres - JUNTOS: Información institucional. MIDIS.",
        "Ministerio de Salud [MINSA]. (2017). Plan Nacional para la Reducción y Control de la Anemia Materno Infantil y la Desnutrición Crónica Infantil en el Perú: 2017-2021. MINSA.",
        "Pasricha, S.-R., Tye-Din, J., Muckenthaler, M. U. y Swinkels, D. W. (2021). Iron deficiency. The Lancet, 397(10270), 233-248.",
        "Penny, M. E., Creed-Kanashiro, H. M., Robert, R. C., Narro, M. R., Caulfield, L. E. y Black, R. E. (2005). Effectiveness of an educational intervention delivered through the health services to reduce growth faltering: A cluster-randomised controlled trial. The Lancet, 365(9474), 1863-1872.",
        "Perova, E. y Vakis, R. (2012). 5 years in Juntos: New evidence on the program's short and long-term impacts. Economía, 35(69), 53-82.",
        "Romano, J. P. y Wolf, M. (2005). Stepwise multiple testing as formalized data snooping. Econometrica, 73(4), 1237-1282.",
        "Sánchez, A. y Jaramillo, M. (2012). Impacto del programa Juntos sobre la nutrición temprana. Revista Estudios Económicos, (23), 53-66. Banco Central de Reserva del Perú.",
        "World Health Organization [WHO]. (2016). Guideline: Daily iron supplementation in infants and children. World Health Organization.",
    ]
    for r in sorted(refs):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.first_line_indent = Cm(-1)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(r)
        run.font.size = Pt(10)


# ============================================================
# 7. ANEXOS
# ============================================================
def anexos():
    h1("7. Anexos")
    h2("Anexo 1. Instrumento de medición (línea de base y de salida)")
    para("Variables registradas para cada niña o niño de 6 a 35 meses y su madre o cuidadora:")
    for q in [
        "Concentración de hemoglobina (g/dL) por punción capilar, ajustada por altitud.",
        "Edad (en meses) y sexo del niño; antecedente de bajo peso al nacer.",
        "Frecuencia semanal de consumo de alimentos ricos en hierro (sangrecita, hígado, pescado).",
        "Adherencia a la suplementación con hierro (días de consumo en la última semana).",
        "Conocimientos maternos sobre alimentación rica en hierro (escala).",
        "Educación de la madre, tamaño del hogar, acceso a agua segura y saneamiento.",
        "Asistencia a las sesiones demostrativas y a las visitas domiciliarias (fidelidad).",
    ]:
        bullet(q)
    h2("Anexo 2. Matriz de operacionalización de variables")
    tabla(
        ["Variable", "Definición", "Indicador", "Instrumento"],
        [["Hemoglobina", "Concentración en sangre ajustada por altitud", "g/dL", "Hemoglobinómetro (línea base y salida)"],
         ["Anemia", "Hemoglobina bajo el punto de corte", "Binaria (sí/no)", "Hemoglobinómetro"],
         ["Consumo de hierro", "Frecuencia de alimentos ricos en hierro", "Veces por semana", "Cuestionario a la madre"],
         ["Adherencia", "Consumo del suplemento de hierro", "Días en la última semana", "Cuestionario / registro"],
         ["Participación", "Asistencia efectiva a la intervención", "N.º de sesiones (0-12)", "Registro de asistencia"]],
        nota="Elaboración propia.",
        widths=[3.2, 4.6, 4.0, 4.2])
    h2("Anexo 3. Teoría del cambio en notación Mermaid")
    mermaid = (
        "flowchart LR\n"
        "  subgraph Insumos\n"
        "    I1[Sesiones demostrativas y recetario]\n"
        "    I2[Personal de salud y promotores]\n"
        "    I3[Articulacion JUNTOS y MINSA]\n"
        "  end\n"
        "  subgraph Actividades\n"
        "    A1[Sesiones de cocina con hierro]\n"
        "    A2[Consejeria nutricional]\n"
        "    A3[Visitas domiciliarias]\n"
        "  end\n"
        "  subgraph Productos\n"
        "    P1[Madres con nuevas habilidades]\n"
        "    P2[Mas preparaciones ricas en hierro]\n"
        "    P3[Mejor adherencia a suplementacion]\n"
        "  end\n"
        "  subgraph Resultados\n"
        "    R1[Corto plazo: mayor ingesta de hierro]\n"
        "    R2[Mediano plazo: mayor hemoglobina]\n"
        "    R3[Largo plazo: menos anemia, mejor capital humano]\n"
        "  end\n"
        "  Insumos --> Actividades --> Productos --> Resultados\n"
    )
    p = doc.add_paragraph()
    run = p.add_run(mermaid)
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    p.paragraph_format.left_indent = Cm(0.5)


# ============================================================
# BUILD
# ============================================================
portada()
resumen()
antecedentes()
propuesta()
diseno()
calendario()
referencias()
anexos()

# Pie de página con numeración
section = doc.sections[0]
footer = section.footer
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = fp.add_run()
fldChar1 = OxmlElement("w:fldChar"); fldChar1.set(qn("w:fldCharType"), "begin")
instrText = OxmlElement("w:instrText"); instrText.set(qn("xml:space"), "preserve"); instrText.text = "PAGE"
fldChar2 = OxmlElement("w:fldChar"); fldChar2.set(qn("w:fldCharType"), "end")
run._r.append(fldChar1); run._r.append(instrText); run._r.append(fldChar2)
run.font.size = Pt(9)

doc.save(OUT)
print("Documento generado:", OUT)
print("Párrafos:", len(doc.paragraphs), "| Tablas:", len(doc.tables))
