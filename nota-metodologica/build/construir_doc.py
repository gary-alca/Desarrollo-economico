# -*- coding: utf-8 -*-
"""Ensambla la Nota Metodológica completa (~20 páginas) en formato Word."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(__file__)
IMG = os.path.join(BASE, "img")
OUT = os.path.join(os.path.dirname(BASE), "Nota_Metodologica_Beca18.docx")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
AZUL2 = RGBColor(0x2E, 0x75, 0xB6)
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
    run.font.color.rgb = AZUL
    run.font.size = Pt(15)
    run.font.name = "Calibri"
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    return p


def h2(text):
    p = doc.add_heading(level=2)
    run = p.add_run(text)
    run.font.color.rgb = AZUL2
    run.font.size = Pt(12.5)
    run.font.name = "Calibri"
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    return p


def h3(text):
    p = doc.add_heading(level=3)
    run = p.add_run(text)
    run.font.color.rgb = AZUL2
    run.font.size = Pt(11.5)
    run.italic = True
    return p


def para(text, justify=True, after=6):
    p = doc.add_paragraph()
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(after)
    # negritas con **...**
    parts = text.split("**")
    for i, seg in enumerate(parts):
        run = p.add_run(seg)
        if i % 2 == 1:
            run.bold = True
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
    # Caption arriba
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(8)
    cap.paragraph_format.space_after = Pt(2)
    r = cap.add_run(f"Figura {numero}. ")
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = AZUL
    r2 = cap.add_run(titulo)
    r2.bold = True
    r2.font.size = Pt(10)
    # Imagen
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_after = Pt(2)
    pic.add_run().add_picture(os.path.join(IMG, img_name), width=Inches(width))
    # Fuente
    fp = doc.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.paragraph_format.space_after = Pt(4)
    fr = fp.add_run(f"Fuente: {fuente} Elaboración propia.")
    fr.font.size = Pt(8.5)
    fr.italic = True
    fr.font.color.rgb = GRISTXT
    # Interpretación
    if interpretacion:
        para(interpretacion)


def tabla_titulo(numero, titulo):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"Tabla {numero}. ")
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = AZUL
    r2 = p.add_run(titulo)
    r2.bold = True
    r2.font.size = Pt(10)


def tabla(headers, rows, nota="Elaboración propia.", widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    hdr = t.rows[0].cells
    for i, htext in enumerate(headers):
        _set_cell_bg(hdr[i], "1F4E79")
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
                _set_cell_bg(cells[i], "EAF1F8")
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
    r.font.color.rgb = AZUL
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("Fortalecimiento de competencias en Excel e Inteligencia "
                    "Artificial para la empleabilidad en el marco de Beca 18")
    r2.bold = True
    r2.font.size = Pt(15)
    r2.font.color.rgb = AZUL2
    doc.add_paragraph()
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rs = sub.add_run("Evaluación de impacto mediante diseño cuasi-experimental de "
                     "emparejamiento por puntaje de propensión (PSM)")
    rs.italic = True
    rs.font.size = Pt(12)
    for _ in range(6):
        doc.add_paragraph()
    for linea, val in [("Curso", "Desarrollo Económico"),
                       ("Tema", "Empleabilidad y competencias digitales en educación superior"),
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
        "Esta nota metodológica propone y diseña la evaluación de impacto de un programa de "
        "fortalecimiento de competencias digitales avanzadas —centrado en **Excel avanzado** y en el "
        "**manejo aplicado de Inteligencia Artificial (IA)** para la productividad laboral— dirigido a "
        "becarios de Beca 18 que cursan el último año de su carrera, con independencia del campo "
        "profesional. La intervención no reemplaza la formación de la carrera, sino que la complementa "
        "con herramientas transversales de empleabilidad demandadas por el mercado de trabajo "
        "contemporáneo.")
    para(
        "El diagnóstico documenta una paradoja persistente del mercado laboral peruano: pese a la "
        "expansión del acceso a la educación superior y al crecimiento sostenido de Beca 18, una "
        "proporción elevada de jóvenes y de egresados accede a empleos informales, subcalificados o de "
        "baja remuneración. La informalidad laboral nacional bordea el 71 % y alcanza el 85 % entre los "
        "jóvenes de 14 a 24 años (INEI, 2024). En paralelo, la demanda de competencias digitales y de "
        "IA crece de manera acelerada: el Foro Económico Mundial reporta que la formación en IA y "
        "analítica de datos figura entre las tres prioridades de capacitación de las empresas para el "
        "periodo 2023-2027 (World Economic Forum, 2023).")
    para(
        "Dado que no resulta ética ni administrativamente admisible negar por sorteo una formación "
        "complementaria a estudiantes que ya son beneficiarios de una beca del Estado, la evaluación "
        "adopta un **diseño cuasi-experimental de emparejamiento por puntaje de propensión (Propensity "
        "Score Matching, PSM)**. Los becarios se inscriben voluntariamente y, para cada participante, se "
        "construye un contrafactual a partir de un \"gemelo estadístico\" —mismo campo de carrera, "
        "institución comparable, edad y rendimiento académico— que no llevó el curso. El parámetro de "
        "interés es el efecto promedio del tratamiento sobre los tratados (ATT).")
    para(
        "El éxito del programa no se mide con un indicador binario de empleo, sino con **indicadores de "
        "calidad del empleo** evaluados a los 6 y 12 meses del egreso: tasa de inserción laboral formal, "
        "nivel de ingresos y velocidad de inserción. La estrategia de medición combina **registros "
        "administrativos** (cruce anonimizado con la Planilla Electrónica del MTPE y la SUNAT) con una "
        "**encuesta de seguimiento tipo panel** que captura el mecanismo de productividad (uso de IA y "
        "horas ahorradas). El documento incluye la teoría de cambio, el árbol de diagnóstico, el modelo "
        "econométrico, el cálculo de poder, el análisis de amenazas a la validez con sus mitigaciones y "
        "las consideraciones éticas, de preregistro y de protección de datos.")


# ============================================================
# 2. ANTECEDENTES Y DIAGNÓSTICO
# ============================================================
def antecedentes():
    h1("2. Antecedentes y diagnóstico")
    h2("2.1 Motivación")
    para(
        "El Perú atraviesa una transición tecnológica que redefine las competencias requeridas en el "
        "mercado de trabajo. La automatización de tareas rutinarias, la difusión de la analítica de datos "
        "y la irrupción de la IA generativa han elevado el valor de las habilidades digitales en "
        "prácticamente todas las ocupaciones, al tiempo que han depreciado el contenido de tareas "
        "manuales y administrativas (Acemoglu y Restrepo, 2019; World Bank, 2016). En este contexto, la "
        "empleabilidad de los egresados depende cada vez menos del título profesional aislado y cada vez "
        "más de la capacidad de movilizar herramientas digitales para resolver problemas y elevar la "
        "productividad.")
    para(
        "Beca 18, el principal programa de becas del Estado peruano, ha ampliado de manera significativa "
        "el acceso de jóvenes de alto rendimiento y bajos recursos a la educación superior. La cobertura "
        "ha crecido de cerca de 5 000 becas anuales en sus primeras convocatorias a más de 20 000 en "
        "2025, con un acumulado superior a 116 000 beneficiarios entre 2012 y 2025 (Pronabec, 2025). "
        "Este esfuerzo fiscal, sin embargo, no garantiza por sí solo una inserción laboral de calidad: el "
        "retorno de la inversión pública en becas se materializa únicamente cuando el egresado logra "
        "traducir su formación en un empleo formal y productivo.")
    figura("fig01_becas.png", "1",
           "Becas otorgadas por Beca 18 en convocatorias seleccionadas",
           "Programa Nacional de Becas y Crédito Educativo (Pronabec, 2025).",
           "El gráfico de barras —idóneo para comparar magnitudes discretas entre años— evidencia la "
           "expansión de la cobertura de Beca 18. Tras un periodo prolongado en torno a las 5 000 becas "
           "anuales, la convocatoria de 2024 duplicó la oferta (10 000) y la de 2025 la cuadruplicó "
           "(más de 20 000). Esta escala creciente tiene dos implicancias para la presente propuesta. "
           "Primero, amplía la población elegible para una intervención complementaria de competencias "
           "digitales y, con ello, el potencial de impacto agregado sobre la empleabilidad de los "
           "becarios. Segundo, vuelve más exigente la rendición de cuentas sobre los resultados "
           "laborales: a mayor inversión pública, mayor es la necesidad de evidencia rigurosa sobre la "
           "eficacia de las acciones formativas. La variable graficada corresponde al número de becas "
           "nuevas adjudicadas por convocatoria; los años se seleccionaron por disponibilidad de cifras "
           "oficiales consolidadas. La tendencia respalda la pertinencia de incorporar, sobre esta base "
           "creciente de beneficiarios, un componente de formación digital orientado a maximizar el "
           "retorno social de la beca.")
    para(
        "El sostenimiento de esta cobertura descansa en un presupuesto público considerable. El "
        "presupuesto institucional de Pronabec superó los S/ 1 000 millones en 2022 y, tras una "
        "contracción en 2023, se aprobó en torno a S/ 1 390 millones para 2026 (MEF, 2025). La magnitud "
        "del gasto refuerza el argumento de eficiencia: intervenciones de costo relativamente bajo, como "
        "la formación digital complementaria, pueden elevar de manera apreciable el retorno de la "
        "inversión ya comprometida en las becas.")
    figura("fig02_presupuesto.png", "2",
           "Presupuesto institucional de Pronabec (millones de soles)",
           "Ministerio de Economía y Finanzas (MEF, 2025) y Pronabec.",
           "El gráfico de barras compara el presupuesto institucional de Pronabec en años fiscales "
           "seleccionados. Se observa un nivel cercano a S/ 1 023 millones en 2022, una contracción a "
           "S/ 890 millones en 2023 y una recuperación hasta cerca de S/ 1 390 millones aprobados para "
           "2026. La variable corresponde al presupuesto institucional expresado en millones de soles "
           "corrientes. La elección del gráfico de barras se justifica por tratarse de valores discretos "
           "comparables entre periodos. La interpretación económica es relevante para la propuesta: el "
           "volumen y la volatilidad del presupuesto subrayan la importancia de demostrar, con "
           "evaluaciones de impacto creíbles, que cada sol invertido en formación complementaria genera "
           "mejoras medibles en la empleabilidad. En un escenario de restricción fiscal, las "
           "intervenciones de bajo costo y alto apalancamiento —como capacitar en Excel e IA a becarios "
           "que ya reciben financiamiento— resultan particularmente atractivas para la asignación "
           "eficiente de recursos públicos.")
    para(
        "La urgencia de fortalecer la empleabilidad se comprende mejor al examinar la calidad del "
        "empleo según el nivel educativo. Aunque la educación superior reduce la informalidad, no la "
        "elimina: cerca del 39 % de los ocupados con educación universitaria permanece en la "
        "informalidad (INEI, 2024). El problema no es solo acceder a un empleo, sino acceder a uno "
        "formal, calificado y acorde con la formación recibida.")
    figura("fig03_informal_nivel.png", "3",
           "Tasa de empleo informal según nivel educativo, 2023",
           "Instituto Nacional de Estadística e Informática (INEI, 2024).",
           "El gráfico de barras ordena la tasa de empleo informal de mayor a menor nivel educativo y "
           "es adecuado para visualizar el gradiente educativo de la formalidad. La variable es la "
           "proporción de ocupados con empleo informal en cada estrato. Se aprecia que la informalidad "
           "desciende de manera monotónica con la educación: desde niveles cercanos al 88 % entre "
           "quienes solo alcanzaron primaria hasta 39,2 % entre los universitarios. Dos lecturas "
           "interesan a la propuesta. Por un lado, la educación superior es un factor protector frente a "
           "la informalidad, lo que valida la inversión en becas. Por otro, el hecho de que casi cuatro "
           "de cada diez profesionales universitarios sigan en la informalidad revela que el título, por "
           "sí solo, es insuficiente para garantizar empleo de calidad. Las competencias digitales "
           "avanzadas operan precisamente sobre ese margen: pueden inclinar la probabilidad de inserción "
           "hacia el empleo formal y calificado, complementando el efecto del nivel educativo y "
           "reduciendo la brecha que el gráfico hace visible.")
    figura("fig04_juvenil.png", "4",
           "Indicadores del mercado laboral juvenil y profesional, 2023-2024",
           "Instituto Nacional de Estadística e Informática (INEI, 2024).",
           "El gráfico de barras reúne cuatro indicadores que perfilan la vulnerabilidad laboral juvenil "
           "y profesional. La informalidad alcanza el 85,3 % entre los jóvenes de 14 a 24 años, muy por "
           "encima del 71,1 % nacional; el subempleo afecta al 45,4 % de la población económicamente "
           "activa; y el desempleo entre universitarios (7,6 %) supera al de niveles educativos básicos. "
           "Este último dato es contraintuitivo y revelador: el mayor desempleo relativo de los "
           "profesionales sugiere fricciones de inserción y una posible desalineación entre la formación "
           "y la demanda efectiva del mercado. La variable de cada barra corresponde a la tasa "
           "respectiva expresada en porcentaje. La elección del gráfico de barras permite contrastar "
           "indicadores heterogéneos en una sola lectura. En conjunto, la figura sustenta el problema "
           "central de la propuesta: los jóvenes —incluidos los profesionales— enfrentan barreras de "
           "calidad del empleo que una formación digital orientada al mercado puede contribuir a "
           "atenuar, al elevar la pertinencia laboral del capital humano formado.")
    para(
        "Detrás de estas brechas laborales subyace una brecha digital estructural. El acceso y el uso de "
        "tecnologías digitales están desigualmente distribuidos entre ámbitos geográficos, lo que limita "
        "la acumulación temprana de competencias digitales en amplios segmentos de la población joven.")
    figura("fig05_brecha_digital.png", "5",
           "Hogares con acceso a internet según ámbito, 2023",
           "Instituto Nacional de Estadística e Informática (INEI, 2024).",
           "El gráfico de barras compara el acceso a internet entre hogares de Lima Metropolitana, resto "
           "urbano y área rural. La brecha es pronunciada: mientras en Lima el acceso supera el 80 % de "
           "los hogares, en el área rural apenas alcanza alrededor de un cuarto. La variable es el "
           "porcentaje de hogares con conexión a internet. El gráfico de barras es apropiado porque "
           "contrasta una misma magnitud entre categorías mutuamente excluyentes. La relevancia para la "
           "propuesta es doble. Primero, la desigualdad de acceso implica que muchos becarios de origen "
           "rural o de menores recursos llegan a la educación superior con una dotación digital previa "
           "más débil, lo que justifica una intervención que nivele competencias. Segundo, la brecha "
           "advierte sobre un riesgo de diseño: la formación debe contemplar el acceso a equipos y "
           "conectividad para no reproducir la desigualdad que pretende corregir. La nivelación de "
           "competencias digitales se vuelve así un instrumento de equidad, además de empleabilidad.")
    para(
        "Frente a estas brechas de oferta, la demanda de competencias digitales por parte de las "
        "empresas se intensifica. La evidencia prospectiva internacional señala que las habilidades "
        "tecnológicas y analíticas encabezan las prioridades de contratación y capacitación.")
    figura("fig06_demanda_wef.png", "6",
           "Habilidades en ascenso priorizadas por las empresas, 2023-2027",
           "World Economic Forum (2023), Future of Jobs Report.",
           "El gráfico de barras presenta la proporción de empresas que consideran en ascenso un "
           "conjunto de habilidades clave hacia 2027. El pensamiento analítico y creativo, la "
           "alfabetización tecnológica y las competencias en IA y big data figuran entre las más "
           "valoradas; en particular, la formación en IA y analítica de datos es priorizada por cerca "
           "del 42 % de las empresas encuestadas. La variable corresponde al porcentaje de firmas que "
           "reporta cada habilidad como creciente en importancia. El gráfico de barras facilita el "
           "ordenamiento por relevancia. Para la propuesta, la figura ofrece el sustento de demanda que "
           "complementa al diagnóstico de oferta: las competencias que el programa busca desarrollar "
           "—manejo avanzado de hojas de cálculo, automatización e IA generativa— coinciden con las que "
           "el mercado declara priorizar. Esta correspondencia entre lo que se enseñaría y lo que las "
           "empresas demandan es central para la teoría de cambio, pues hace plausible que la formación "
           "se traduzca en mejores resultados de inserción y remuneración.")
    figura("fig07_uso_digital.png", "7",
           "Población que usa internet según grupo de edad, 2023",
           "Instituto Nacional de Estadística e Informática (INEI, 2024).",
           "El gráfico de líneas muestra el uso de internet por grupo de edad y es idóneo para "
           "representar un perfil etario continuo. El uso alcanza su máximo entre los jóvenes de 19 a 24 "
           "años (en torno al 92 %) y decrece en las edades mayores. La variable es el porcentaje de la "
           "población de cada grupo que usa internet. Aunque los jóvenes son nativos digitales en cuanto "
           "a conectividad y consumo, este uso intensivo es mayoritariamente recreativo y comunicacional, "
           "no productivo ni profesional. Allí radica una distinción crucial para la propuesta: usar "
           "redes sociales o mensajería no equivale a dominar Excel avanzado, automatización o ingeniería "
           "de prompts. La figura matiza, por tanto, el supuesto de que la juventud ya posee las "
           "competencias digitales que el mercado demanda. El programa apunta precisamente a transformar "
           "la familiaridad digital general en competencias digitales aplicadas y certificables, "
           "cerrando la brecha entre el uso cotidiano y el uso productivo de la tecnología.")
    para(
        "El argumento económico de fondo es el retorno salarial de las competencias digitales. La "
        "evidencia internacional documenta de manera consistente una prima salarial asociada al uso "
        "intensivo de herramientas digitales en el puesto de trabajo, que se amplía conforme aumenta la "
        "sofisticación del uso (OECD, 2019).")
    figura("fig08_retorno_salarial.png", "8",
           "Ingreso laboral relativo según intensidad de uso de competencias digitales",
           "Organización para la Cooperación y el Desarrollo Económicos (OECD, 2019).",
           "El gráfico de barras representa, mediante un índice con base 100 para los trabajadores sin "
           "uso digital, el ingreso laboral relativo según la intensidad de uso de competencias "
           "digitales. La progresión es clara: el uso básico de ofimática se asocia a ingresos "
           "superiores en torno al 18 %, el uso intermedio orientado al análisis de datos alrededor del "
           "42 %, y el uso avanzado —automatización e IA— a primas cercanas al 70 % respecto de la "
           "línea base. La variable es el índice de ingreso relativo. El gráfico de barras es adecuado "
           "para mostrar una gradiente comparativa. Estas cifras, de carácter referencial y construidas "
           "a partir de la literatura sobre retornos a las competencias digitales, ilustran el mecanismo "
           "salarial que articula la teoría de cambio: a mayor sofisticación digital, mayor "
           "productividad y, por tanto, mayor remuneración esperada. La hipótesis central de la "
           "evaluación —que los becarios capacitados acceden a puestos mejor pagados, como analistas— se "
           "apoya conceptualmente en esta relación, que el diseño cuasi-experimental permitirá "
           "contrastar empíricamente en el contexto peruano.")
    figura("fig09_comparacion.png", "9",
           "Población con competencias digitales al menos básicas, comparación internacional",
           "Organización para la Cooperación y el Desarrollo Económicos (OECD, 2023).",
           "El gráfico de barras compara la proporción de población adulta con competencias digitales al "
           "menos básicas entre el promedio de la OCDE y un conjunto de países de la región. El Perú "
           "(alrededor del 31 %) se ubica por debajo del promedio de la OCDE (cerca del 56 %) y de pares "
           "regionales como Chile. La variable es el porcentaje de adultos con competencias digitales "
           "básicas. El gráfico de barras permite el contraste internacional directo. Estas cifras, de "
           "carácter referencial, dimensionan la brecha que enfrenta el país y refuerzan la justificación "
           "de la intervención: existe un margen amplio para elevar el nivel de competencias digitales "
           "de la fuerza laboral peruana. Focalizar esta nivelación en becarios de Beca 18 —jóvenes de "
           "alto rendimiento y con trayectoria educativa— constituye una estrategia costo-efectiva, pues "
           "actúa sobre un capital humano con elevada capacidad de aprovechamiento y de difusión "
           "posterior de las competencias adquiridas en sus entornos laborales.")
    para(
        "En síntesis, el diagnóstico articula una oferta de competencias digitales insuficiente y "
        "desigual con una demanda creciente y bien remunerada de esas mismas competencias. Beca 18 "
        "ofrece una plataforma idónea para una intervención complementaria que cierre esa brecha, "
        "siempre que su eficacia se sustente en evidencia rigurosa, objeto de la presente nota.")
    # Tabla 1: síntesis de indicadores de contexto
    tabla_titulo("1", "Indicadores de contexto del diagnóstico")
    tabla(
        ["Indicador", "Valor", "Fuente"],
        [["Acumulado de beneficiarios de Beca 18 (2012-2025)", "≈ 116 217", "Pronabec (2025)"],
         ["Presupuesto institucional de Pronabec (2026, aprobado)", "≈ S/ 1 390 millones", "MEF (2025)"],
         ["Informalidad laboral nacional (2023)", "71,1 %", "INEI (2024)"],
         ["Informalidad laboral juvenil (14-24 años)", "85,3 %", "INEI (2024)"],
         ["Empleo informal entre universitarios", "39,2 %", "INEI (2024)"],
         ["Subempleo nacional (abr. 2023 - mar. 2024)", "45,4 %", "INEI (2024)"],
         ["Empresas que priorizan formación en IA y big data", "≈ 42 %", "WEF (2023)"]],
        nota="Elaboración propia a partir de fuentes oficiales.",
        widths=[8.5, 3.5, 4.0])

    # 2.2 Evidencia
    h2("2.2 Evidencia")
    para(
        "La literatura de evaluación de impacto sobre programas de capacitación laboral juvenil ofrece "
        "lecciones directamente aplicables al diseño propuesto. Lejos de constituir un listado, esta "
        "revisión interesa por el contraste entre objetivos, metodologías, resultados y limitaciones, y "
        "por su relación con la presente intervención.")
    para(
        "La evidencia experimental latinoamericana es particularmente informativa. Attanasio, Kugler y "
        "Meghir (2011) evaluaron mediante un ensayo aleatorizado el programa Jóvenes en Acción en "
        "Colombia y encontraron efectos positivos y significativos sobre el empleo formal y los ingresos, "
        "especialmente en mujeres. Card et al. (2011), en un RCT del programa Juventud y Empleo de "
        "República Dominicana, hallaron impactos modestos sobre el empleo pero mejoras en la formalidad y "
        "en habilidades socioemocionales, lo que advierte que los efectos sobre la cantidad de empleo "
        "pueden ser menores que los efectos sobre su calidad. En el Perú, las evaluaciones de PROJoven "
        "(Ñopo, Robles y Saavedra, 2008; Díaz y Rosas-Shady, 2016) documentaron incrementos en empleo "
        "formal e ingresos, con heterogeneidad por sexo y por calidad del componente formativo. Estas "
        "evaluaciones inspiran directamente la elección de indicadores de calidad del empleo —y no de "
        "mera ocupación— adoptada en la sección 4.")
    para(
        "La síntesis global más influyente, el meta-análisis de Card, Kluve y Weber (2018) sobre más de "
        "200 evaluaciones de programas activos del mercado laboral, concluye que los efectos tienden a "
        "ser pequeños o nulos en el corto plazo pero crecen apreciablemente en el mediano y largo plazo, "
        "y que los programas con fuerte componente de formación de capital humano —como el aquí "
        "propuesto— muestran mejores resultados diferidos. Esta evidencia fundamenta la decisión de "
        "medir resultados a los 6 y 12 meses del egreso y de no concluir prematuramente sobre la eficacia "
        "a partir de impactos inmediatos.")
    figura("fig10_programas.png", "10",
           "Programas de capacitación laboral con impacto positivo significativo",
           "Card, Kluve y Weber (2018), meta-análisis de programas activos del mercado laboral.",
           "El gráfico de barras representa la proporción de evaluaciones que reportan un impacto "
           "positivo y significativo según el horizonte temporal de medición. La proporción asciende "
           "desde alrededor del 21 % en el corto plazo (menos de un año) hasta cerca del 52 % en el "
           "largo plazo (dos a tres años). La variable es el porcentaje de evaluaciones con efecto "
           "positivo significativo. El gráfico de barras permite visualizar la progresión temporal del "
           "efecto. La implicancia metodológica es decisiva para la presente propuesta: los programas de "
           "capacitación, y en particular los intensivos en formación de capital humano, despliegan sus "
           "efectos con rezago, a medida que los participantes encuentran empleos acordes con sus nuevas "
           "competencias. Concluir sobre la eficacia a partir de mediciones inmediatas conduciría a "
           "subestimar el impacto. Por ello, el diseño de evaluación contempla mediciones a los 6 y 12 "
           "meses del egreso, ventana coherente con la maduración de los efectos documentada en la "
           "literatura internacional.")
    # Tabla 2: revisión crítica de evidencia
    tabla_titulo("2", "Revisión crítica de la evidencia seleccionada")
    tabla(
        ["Estudio", "Intervención y método", "Muestra y resultados", "Relación con la propuesta"],
        [["Attanasio, Kugler y Meghir (2011)",
          "Jóvenes en Acción (Colombia); RCT",
          "Jóvenes vulnerables; ↑ empleo formal e ingresos, mayor efecto en mujeres",
          "Sustenta el uso de RCT/cuasi-experimentos y el foco en formalidad"],
         ["Card et al. (2011)",
          "Juventud y Empleo (Rep. Dominicana); RCT",
          "Efecto modesto en empleo; mejora en formalidad y habilidades socioemocionales",
          "Justifica medir calidad del empleo, no solo ocupación"],
         ["Ñopo, Robles y Saavedra (2008); Díaz y Rosas-Shady (2016)",
          "PROJoven (Perú); cuasi-experimental y de seguimiento",
          "↑ empleo formal e ingresos; heterogeneidad por sexo",
          "Antecedente nacional directo; inspira indicadores y fuentes"],
         ["Card, Kluve y Weber (2018)",
          "Meta-análisis de programas activos; +200 evaluaciones",
          "Efectos crecientes en el mediano/largo plazo; mejores en formación",
          "Fundamenta la medición a 6 y 12 meses"]],
        nota="Elaboración propia con base en la literatura citada.",
        widths=[3.6, 4.0, 4.6, 3.8])

    # 2.3 Árbol de diagnóstico
    h2("2.3 Árbol de diagnóstico")
    para(
        "El problema central que motiva la intervención es la **brecha de competencias digitales "
        "avanzadas en los becarios de Beca 18**, que limita su empleabilidad pese a contar con formación "
        "superior. El árbol de diagnóstico organiza las causas que originan el problema y los efectos que "
        "de él se derivan, ofreciendo la base lógica para la teoría de cambio.")
    figura("fig12_arbol.png", "11",
           "Árbol de diagnóstico del problema central",
           "Análisis del equipo evaluador.",
           "El diagrama de árbol —apropiado para representar relaciones causa-efecto jerárquicas— sitúa "
           "en el centro el problema y despliega hacia abajo sus causas y hacia arriba sus efectos. Entre "
           "las causas directas se identifican una oferta formativa centrada en los contenidos de la "
           "carrera y sin componente digital, la escasa exposición de los estudiantes a herramientas de "
           "productividad e IA, y la desconexión entre la formación impartida y la demanda efectiva del "
           "mercado laboral. Estas causas generan, como efectos, una inserción laboral informal y de baja "
           "calidad, ingresos por debajo del potencial profesional y una menor productividad y "
           "competitividad del egresado; en conjunto, configuran el efecto final de baja empleabilidad y "
           "subempleo profesional. La lógica del árbol orienta el diseño de la intervención: al actuar "
           "sobre las causas mediante una formación digital pertinente y vinculada al mercado, se busca "
           "revertir la cadena de efectos. Esta estructura causal se traduce, en la sección siguiente, en "
           "una teoría de cambio que explicita cómo los insumos y actividades del programa conducen a los "
           "resultados de empleabilidad esperados.")
    tabla_titulo("3", "Causas y efectos del problema central")
    tabla(
        ["Dimensión", "Elementos"],
        [["Causas directas",
          "Oferta formativa sin componente digital; escasa exposición a herramientas de productividad e IA; desconexión formación-mercado"],
         ["Causas indirectas",
          "Brecha digital de origen socioeconómico; rezago de la oferta educativa frente al cambio tecnológico"],
         ["Efectos directos",
          "Inserción informal y de baja calidad; ingresos por debajo del potencial; menor productividad"],
         ["Efecto final",
          "Baja empleabilidad y subempleo profesional del egresado de Beca 18"]],
        nota="Elaboración propia.",
        widths=[4.0, 12.0])


# ============================================================
# 3. PROPUESTA DE INTERVENCIÓN
# ============================================================
def propuesta():
    h1("3. Propuesta de intervención")
    h2("3.1 Descripción de la propuesta")
    para(
        "La intervención consiste en un **programa intensivo y voluntario de formación en competencias "
        "digitales avanzadas**, dirigido a becarios de Beca 18 que cursan el último año de su carrera, "
        "con independencia del campo profesional. Su objetivo es elevar la empleabilidad y la calidad de "
        "la inserción laboral mediante el dominio aplicado de Excel avanzado y de herramientas de IA "
        "orientadas a la productividad. El programa **complementa, no reemplaza**, la formación de la "
        "carrera.")
    para(
        "El programa tiene una duración aproximada de 16 semanas, organizadas en dos componentes "
        "técnicos —Excel avanzado e IA aplicada— y un componente de empleabilidad. Las sesiones combinan "
        "teoría y práctica supervisada, con proyectos auditables en vivo (diseño de macros, "
        "automatización de flujos e ingeniería de prompts). Al finalizar, el becario obtiene una "
        "**certificación** verificable, acompañamiento de **mentores**, acceso a una **bolsa laboral** "
        "vinculada a empresas y **seguimiento** de su trayectoria de inserción.")
    tabla_titulo("4", "Componentes y malla del programa")
    tabla(
        ["Componente", "Contenidos", "Duración", "Producto"],
        [["Excel avanzado",
          "Funciones avanzadas, tablas dinámicas, Power Query, macros y automatización (VBA)",
          "6 semanas",
          "Modelo de automatización funcional"],
         ["IA aplicada a la productividad",
          "IA generativa, ingeniería de prompts, asistentes, análisis y visualización de datos",
          "6 semanas",
          "Flujo de trabajo asistido por IA"],
         ["Empleabilidad",
          "Portafolio profesional, LinkedIn, simulación de pruebas técnicas, mentoría",
          "4 semanas",
          "Portafolio y vinculación laboral"]],
        nota="Elaboración propia.",
        widths=[3.5, 7.0, 2.2, 3.3])

    h2("3.2 Teoría de cambio")
    para(
        "La teoría de cambio articula la cadena causal que vincula los insumos del programa con los "
        "resultados de empleabilidad. Los **insumos** (plataforma y contenidos, docentes y mentores, "
        "datos administrativos y convenios) habilitan las **actividades** formativas (sesiones de Excel, "
        "talleres de IA, mentoría y bolsa laboral), que generan **productos** (becarios certificados, "
        "portafolios y proyectos auditables, vinculación con empresas). Estos productos producen "
        "**resultados** escalonados: en el corto plazo, el dominio de competencias digitales; en el "
        "mediano plazo, la inserción laboral formal y mejores ingresos; y en el largo plazo, una mayor "
        "empleabilidad y productividad sostenidas.")
    para(
        "La cadena descansa en supuestos verificables —demanda sostenida de competencias digitales, "
        "participación efectiva de los becarios y calidad de los datos administrativos— y enfrenta "
        "riesgos —deserción, contaminación entre participantes y desalineación de la oferta formativa— "
        "que se gestionan en el diseño de evaluación (sección 4). El Anexo 3 presenta la teoría de "
        "cambio en notación Mermaid para su reproducción.")
    figura("fig11_teoria_cambio.png", "12",
           "Teoría de cambio del programa",
           "Diseño del equipo evaluador.",
           "El diagrama de flujo —idóneo para representar una cadena de resultados— ordena de izquierda "
           "a derecha los insumos, las actividades, los productos y los resultados del programa, "
           "explicitando la lógica causal de la intervención. La lectura horizontal muestra cómo los "
           "recursos se transforman progresivamente en competencias y, luego, en resultados de "
           "empleabilidad de creciente alcance temporal. La columna de resultados distingue tres "
           "horizontes —corto, mediano y largo plazo— en correspondencia con la evidencia sobre la "
           "maduración diferida de los efectos de los programas de capacitación (Card, Kluve y Weber, "
           "2018). La franja inferior de supuestos recuerda que la cadena causal solo opera bajo "
           "condiciones habilitantes: una demanda de mercado que valore las competencias formadas, una "
           "participación efectiva de los becarios y la disponibilidad de datos administrativos "
           "confiables para la medición. Esta representación cumple una doble función: comunica la lógica "
           "del programa a los actores institucionales y fija los nodos de la cadena que la evaluación de "
           "impacto deberá medir, garantizando la correspondencia entre el diseño de la intervención y "
           "su estrategia de evaluación.")
    tabla_titulo("5", "Matriz de la teoría de cambio")
    tabla(
        ["Eslabón", "Elementos"],
        [["Insumos", "Plataforma y contenidos; docentes y mentores; datos Pronabec; convenios MTPE/SUNAT"],
         ["Actividades", "Sesiones de Excel avanzado; taller de IA y automatización; mentoría y bolsa laboral"],
         ["Productos", "Becarios certificados; portafolio y proyectos auditables; vinculación con empresas"],
         ["Resultados de corto plazo", "Dominio de competencias digitales aplicadas"],
         ["Resultados de mediano plazo", "Inserción laboral formal; mayores ingresos; menor tiempo de inserción"],
         ["Resultados de largo plazo", "Empleabilidad y productividad sostenidas"],
         ["Supuestos", "Demanda sostenida de competencias; participación efectiva; calidad de datos"],
         ["Riesgos", "Deserción; contaminación entre participantes; desalineación de la oferta"]],
        nota="Elaboración propia.",
        widths=[4.5, 11.5])

    h2("3.3 Actores involucrados")
    para(
        "La implementación articula a actores públicos, académicos y privados, cada uno con un rol, una "
        "responsabilidad y distintos niveles de influencia e interés en los resultados de la "
        "intervención.")
    tabla_titulo("6", "Matriz de actores involucrados")
    tabla(
        ["Actor", "Rol y responsabilidad", "Influencia", "Interés"],
        [["Pronabec", "Financiamiento, focalización y datos de becarios", "Alta", "Alto"],
         ["Universidades e institutos", "Articulación curricular y soporte logístico", "Media", "Alto"],
         ["Empresas tecnológicas", "Contenidos, prácticas y demanda laboral", "Media", "Alto"],
         ["MTPE / SUNAT", "Registros administrativos para la medición", "Alta", "Medio"],
         ["BID / Banco Mundial", "Asistencia técnica y financiamiento de la evaluación", "Media", "Medio"],
         ["Ministerio de Educación", "Rectoría de política educativa", "Alta", "Alto"],
         ["Docentes y mentores", "Ejecución formativa y acompañamiento", "Media", "Alto"],
         ["Beneficiarios (becarios)", "Participación y aprovechamiento del programa", "Baja", "Alto"]],
        nota="Elaboración propia.",
        widths=[3.8, 7.2, 2.5, 2.5])


# ============================================================
# 4. DISEÑO DE EVALUACIÓN
# ============================================================
def diseno():
    h1("4. Diseño de evaluación")
    h2("4.1 Preguntas de investigación e hipótesis")
    para(
        "La evaluación busca responder a la pregunta general: ¿la participación voluntaria de becarios "
        "de Beca 18 en el último año de su carrera en un programa de formación en Excel avanzado y "
        "manejo aplicado de IA incrementa la calidad de su inserción en el mercado laboral durante el "
        "primer año posterior al egreso?")
    para(
        "A diferencia de un experimento aleatorizado, en esta intervención los becarios deciden "
        "inscribirse libremente. La estrategia de identificación descansa, por tanto, en la construcción "
        "de un contrafactual creíble por medios estadísticos: el resultado laboral que habrían obtenido "
        "los becarios capacitados de no haber llevado el curso, aproximado mediante un grupo de "
        "comparación de características observables equivalentes, bajo el supuesto de selección sobre "
        "observables (Rosenbaum y Rubin, 1983; Heckman, Ichimura y Todd, 1997; Caliendo y Kopeinig, "
        "2008).")
    para("De la pregunta general se derivan cuatro hipótesis específicas:")
    bullet("**H1 (resultado principal):** los participantes presentan una tasa de inserción laboral "
           "formal significativamente mayor que la del grupo de comparación, a los 6 y 12 meses del egreso.")
    bullet("**H2:** los participantes perciben un ingreso laboral mensual bruto inicial significativamente "
           "mayor, asociado al acceso a puestos de mayor calificación.")
    bullet("**H3:** los participantes registran una menor velocidad de inserción (menos meses hasta el "
           "primer empleo profesional calificado).")
    bullet("**H4 (mecanismo):** los participantes reportan un uso más intensivo de IA generativa y un "
           "mayor ahorro de tiempo operativo, canal de productividad que vincula la formación con la "
           "mejora del empleo.")
    para(
        "Se designa **ex ante** H1 como resultado primario, único sobre el cual se sustentará la "
        "conclusión principal de eficacia, y se clasifican H2, H3 y H4 como secundarios, con corrección "
        "por comparaciones múltiples (procedimiento de Romano y Wolf). Esta jerarquización se fijará en "
        "el plan de análisis preregistrado (sección 4.5).")
    tabla_titulo("7", "Variables de la evaluación")
    tabla(
        ["Tipo", "Variables"],
        [["Resultado (finales)", "Inserción laboral formal (binaria); ingreso mensual bruto (S/); velocidad de inserción (meses)"],
         ["Intermedias (mecanismo)", "Uso de IA en tareas; horas semanales ahorradas; prueba técnica de Excel/IA en la entrevista"],
         ["Control (emparejamiento)", "Carrera y área; institución; edad; sexo; región; promedio ponderado; orden de mérito; modalidad; ciclo de egreso"]],
        nota="Elaboración propia.",
        widths=[4.0, 12.0])

    h2("4.2 Estrategia y diseño de evaluación")
    h3("a. Justificación del diseño cuasi-experimental")
    para(
        "A diferencia de evaluaciones con vacantes limitadas —en las que la sobredemanda permite asignar "
        "el acceso por sorteo—, en el marco de Beca 18 **no resulta ética ni administrativamente "
        "admisible negar por sorteo** una formación complementaria a estudiantes que ya son "
        "beneficiarios de una beca del Estado. Por ello, la metodología idónea es un **diseño "
        "cuasi-experimental de emparejamiento por puntaje de propensión (PSM)**.")
    para(
        "Los becarios se inscriben de forma voluntaria. Para cada participante, se busca en las bases de "
        "Pronabec un \"gemelo estadístico\" —mismo campo de carrera, institución comparable, edad y "
        "rendimiento académico— que no llevó el curso. Formalmente, se estima el puntaje de propensión "
        "e(X) = Pr(D = 1 | X) mediante un modelo logístico y se emparejan tratados y no tratados con "
        "puntajes próximos (Rosenbaum y Rubin, 1983). El parámetro de interés es el efecto promedio del "
        "tratamiento sobre los tratados:")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ATT = E[ Y(1) − Y(0) | D = 1 ]")
    r.italic = True
    r.font.size = Pt(11)
    para(
        "La identificación descansa en dos supuestos: **independencia condicional** (ausencia de "
        "confusores no observados relevantes dado X) y **soporte común** (existencia de comparables para "
        "cada tratado), este último verificado restringiendo el análisis a la región de traslape "
        "(Caliendo y Kopeinig, 2008).")
    h3("b. Procedimiento de emparejamiento y estratificación")
    para(
        "El emparejamiento se realiza **estratificado por áreas de carrera** (salud con salud, "
        "ingeniería con ingeniería, ciencias sociales con ciencias sociales), de modo que cada tratado "
        "se compara con controles de su mismo campo. Esto reconoce que las oportunidades y los niveles "
        "salariales difieren entre profesiones y, a la vez, sostiene que las competencias en Excel e IA "
        "son transversales a cualquier campo. Como algoritmo principal se emplea el vecino más cercano "
        "con caliper de 0,2 desviaciones estándar; como robustez, kernel e IPW. Se exige que el sesgo "
        "estandarizado de cada covariable se reduzca por debajo del 5 % tras el emparejamiento "
        "(Rosenbaum y Rubin, 1985).")
    h3("c. Resultados, indicadores y fuentes de datos")
    para(
        "Siguiendo la rigurosidad de las evaluaciones de capacitación laboral en el Perro, el éxito no "
        "se mide con un binario de \"trabaja o no\", sino con **indicadores de calidad del empleo** a "
        "los 6 y 12 meses del egreso, combinando registros administrativos (cobertura censal, sin sesgo "
        "de declaración) y una encuesta panel (variables de productividad no registradas).".replace("Perro", "Perú"))
    tabla_titulo("8", "Indicadores, definición y fuentes de datos")
    tabla(
        ["Nivel", "Indicador", "Definición operativa", "Fuente"],
        [["Principal (H1)", "Inserción laboral formal", "Empleo con contrato y derechos en planilla", "Planilla Electrónica (MTPE)/SUNAT; 6 y 12 meses"],
         ["Secundario (H2)", "Ingreso laboral mensual", "Remuneración bruta inicial (S/)", "Planilla Electrónica (MTPE)/SUNAT"],
         ["Secundario (H3)", "Velocidad de inserción", "Meses hasta el primer empleo calificado", "Planilla Electrónica y encuesta"],
         ["Mecanismo (H4)", "Uso de IA y ahorro de tiempo", "Uso de IA; horas ahorradas; prueba técnica", "Encuesta de seguimiento (panel)"]],
        nota="Elaboración propia. El acceso a registros se realiza mediante convenios con datos anonimizados.",
        widths=[2.6, 3.2, 5.2, 5.0])
    para(
        "La estrategia mixta articula, por un lado, el **cruce anonimizado por DNI con la Planilla "
        "Electrónica del MTPE y la SUNAT** —insumo principal de H1, con datos objetivos de formalidad y "
        "salario— y, por otro, una **encuesta panel** aplicada a tratados y controles en idénticas "
        "ventanas, que indaga: ¿le tomaron prueba técnica de Excel o IA en la entrevista?, ¿usa IA "
        "generativa para automatizar tareas?, ¿cuántas horas semanales ahorra gracias a estas "
        "herramientas? (mecanismo, H4).")
    h3("d. Especificación econométrica")
    para(
        "Sobre la muestra emparejada se estima una regresión que controla por las covariables de "
        "emparejamiento (estimador **doblemente robusto**; Imbens y Wooldridge, 2009):")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Yᵢ = α + β·Dᵢ + Xᵢ′δ + μₐ + εᵢ")
    r.italic = True
    r.font.size = Pt(11)
    para(
        "donde Yᵢ es el resultado laboral del becario i; Dᵢ vale 1 si participó y 0 si es comparación; "
        "Xᵢ son las covariables observables; μₐ son efectos fijos por área de carrera; y εᵢ es el error. "
        "El coeficiente de interés β recoge el efecto causal promedio sobre los participantes (ATT). Los "
        "errores estándar se estiman de forma robusta y se ajustan para reflejar que el puntaje de "
        "propensión es estimado (Abadie e Imbens, 2016). Para resultados binarios se reportan el modelo "
        "lineal de probabilidad y la estimación logística; se verifica la consistencia de los efectos "
        "marginales. Como análisis de heterogeneidad se estima el efecto según área de carrera, sexo, "
        "región y rendimiento previo.")

    h2("4.3 Cálculo de poder y muestra propuesta")
    para(
        "El tamaño de muestra se determina mediante un cálculo de poder para detectar el efecto sobre el "
        "resultado primario (inserción laboral formal), según la formulación estándar del efecto mínimo "
        "detectable (Bloom, 1995), ajustado por la pérdida de eficiencia propia del PSM (descarte de "
        "unidades fuera del soporte común y emparejamiento con reposición). Como tasa base se adopta una "
        "probabilidad de inserción formal en torno al 45 % para egresados jóvenes, consistente con los "
        "niveles de informalidad documentados (INEI, 2024). Se busca detectar un efecto mínimo "
        "detectable de 10 puntos porcentuales (de 45 % a 55 %), con α = 0,05 y potencia de 0,80.")
    tabla_titulo("9", "Parámetros del cálculo de poder")
    tabla(
        ["Parámetro", "Valor propuesto"],
        [["Tasa base de inserción laboral formal", "45 %"],
         ["Efecto mínimo detectable (MDE)", "10 puntos porcentuales"],
         ["Nivel de significancia (α)", "0,05"],
         ["Potencia estadística (1 − β)", "0,80"],
         ["Razón de emparejamiento (control : tratado)", "1 : 1"],
         ["Ajuste por pérdida de eficiencia del PSM", "≈ 1,3"],
         ["Tamaño de muestra por grupo (analítico)", "≈ 390"],
         ["Tamaño de muestra total", "≈ 780"]],
        nota="Elaboración propia con base en Bloom (1995). Cifras orientativas sujetas a refinamiento por simulación.",
        widths=[9.0, 7.0])
    para(
        "El cálculo es sensible a la tasa base y a la calidad del emparejamiento. Se recomienda una "
        "sobremuestra de seguridad del 15 %-20 % frente a la deserción esperada en la encuesta y refinar "
        "el cálculo por simulación una vez disponibles estimaciones administrativas de las tasas de "
        "inserción y de la distribución del puntaje de propensión.")

    h2("4.4 Amenazas a la validez y estrategias de mitigación")
    para(
        "**Sesgo de selección por motivación (no observables).** El grupo que llevó el curso podría ser "
        "intrínsecamente más motivado. Se mitiga incorporando al modelo de propensión variables proxy "
        "—**promedio ponderado histórico** y **orden de mérito**— y aplicando un **análisis de "
        "sensibilidad de Rosenbaum** (Rosenbaum bounds) que cuantifica cuán fuerte debería ser un "
        "confusor no observado para invalidar las conclusiones (Rosenbaum, 2002; DiPrete y Gangl, 2004).")
    para(
        "**Contaminación (spillover).** Podría argumentarse que los participantes transmiten los "
        "contenidos por mensajería. El programa evalúa el **desarrollo de una competencia técnica "
        "auditable en vivo** (macros, ingeniería de prompts, automatización), que no se adquiere "
        "reenviando un archivo. Además, el grupo de comparación se conforma preferentemente con becarios "
        "de instituciones distintas y se incluye un ítem de verificación de exposición.")
    para(
        "**Relevancia por carrera.** El emparejamiento estratificado por área responde a la objeción de "
        "que ciertas profesiones \"no usan\" Excel o IA: el efecto se estima dentro de la profesión, y "
        "la evidencia respalda la transversalidad de estas competencias (World Bank, 2016; OECD, 2019).")
    para(
        "**Deserción y sesgo de medición.** Se prioriza el resultado primario sobre fuentes "
        "administrativas (cobertura censal, baja atrición), con pruebas de atrición diferencial y cotas "
        "de Lee. El autorreporte se atenúa con preguntas conductuales verificables y triangulación "
        "encuesta-registro. **Efectos Hawthorne y John Henry** se atenúan con resultados no reactivos "
        "(administrativos) y comunicación neutra del seguimiento.")
    tabla_titulo("10", "Principales amenazas a la validez y estrategias de mitigación")
    tabla(
        ["Amenaza", "Estrategia de mitigación"],
        [["Sesgo de selección (no observables)", "Proxies de motivación; análisis de sensibilidad de Rosenbaum"],
         ["Contaminación (spillover)", "Competencia auditable; comparación entre instituciones distintas; ítem de verificación"],
         ["Relevancia por carrera", "Emparejamiento estratificado por área; efectos fijos por área"],
         ["Deserción (attrition)", "Resultado primario administrativo; pruebas de atrición; cotas de Lee"],
         ["Sesgo de medición", "Preguntas conductuales verificables; triangulación encuesta-registro"],
         ["Efectos Hawthorne y John Henry", "Resultados no reactivos; comunicación neutra del seguimiento"],
         ["Soporte común insuficiente", "Restricción a la región de traslape; verificación de balance"]],
        nota="Elaboración propia.",
        widths=[5.5, 10.5])

    h2("4.5 Consideraciones éticas, preregistro y datos")
    para(
        "El diseño respeta los principios éticos de la evaluación de impacto. Ningún becario es privado "
        "del curso por sorteo: el acceso es voluntario y abierto, lo que preserva la equidad propia de "
        "Beca 18. La construcción del grupo de comparación se realiza ex post a partir de registros "
        "existentes, sin alterar prestaciones. El estudio requiere **consentimiento informado** en la "
        "encuesta y aprobación de un comité de ética. El cruce de registros (Pronabec, MTPE, SUNAT) se "
        "efectúa bajo convenios con **anonimización** y seudonimización por DNI, conforme a la Ley de "
        "Protección de Datos Personales.")
    para(
        "Se elaborará y depositará un **plan de análisis preregistrado** que fije el resultado primario, "
        "las hipótesis secundarias, las dimensiones de heterogeneidad y las especificaciones "
        "econométricas, incluido el algoritmo de emparejamiento, reduciendo los grados de libertad del "
        "investigador (Casey, Glennerster y Miguel, 2012). En el marco de la **ciencia abierta**, el "
        "código y los datos anonimizados se depositarán en un repositorio público al concluir la "
        "evaluación. Finalmente, se incorporará un análisis de **costo-efectividad** que compare el "
        "costo por inserción formal adicional con el de intervenciones alternativas (Card, Kluve y "
        "Weber, 2018).")


# ============================================================
# 5. CALENDARIO
# ============================================================
def calendario():
    h1("5. Calendario de actividades")
    para(
        "El cronograma contempla un horizonte aproximado de tres años, desde el diseño hasta la difusión "
        "de resultados, con mediciones de impacto a los 6 y 12 meses del egreso de la cohorte tratada.")
    tabla_titulo("11", "Calendario de actividades (tipo Gantt)")
    tabla(
        ["Fase", "Actividad", "Responsable", "Periodo"],
        [["1", "Diseño final, convenios y preregistro", "Pronabec / Equipo evaluador", "Meses 1-3"],
         ["2", "Identificación de becarios y línea de base", "Equipo evaluador", "Meses 3-5"],
         ["3", "Ejecución del programa (16 semanas)", "Docentes y mentores", "Meses 5-9"],
         ["4", "Egreso y construcción del grupo de comparación (PSM)", "Equipo evaluador", "Meses 9-11"],
         ["5", "Seguimiento a 6 meses (registros + encuesta)", "Equipo evaluador / MTPE", "Meses 15-17"],
         ["6", "Seguimiento a 12 meses (registros + encuesta)", "Equipo evaluador / MTPE", "Meses 21-23"],
         ["7", "Estimación de impacto y costo-efectividad", "Equipo evaluador", "Meses 23-27"],
         ["8", "Difusión de resultados y repositorio abierto", "Pronabec / Equipo evaluador", "Meses 27-30"]],
        nota="Elaboración propia. Los periodos son referenciales y se ajustarán al calendario académico.",
        widths=[1.5, 7.5, 4.5, 2.5])


# ============================================================
# 6. REFERENCIAS
# ============================================================
def referencias():
    h1("6. Referencias")
    refs = [
        "Abadie, A. e Imbens, G. W. (2016). Matching on the estimated propensity score. Econometrica, 84(2), 781-807.",
        "Acemoglu, D. y Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. Journal of Economic Perspectives, 33(2), 3-30.",
        "Attanasio, O., Kugler, A. y Meghir, C. (2011). Subsidizing vocational training for disadvantaged youth in Colombia: Evidence from a randomized trial. American Economic Journal: Applied Economics, 3(3), 188-220.",
        "Bloom, H. S. (1995). Minimum detectable effects: A simple way to report the statistical power of experimental designs. Evaluation Review, 19(5), 547-556.",
        "Caliendo, M. y Kopeinig, S. (2008). Some practical guidance for the implementation of propensity score matching. Journal of Economic Surveys, 22(1), 31-72.",
        "Card, D., Ibarrarán, P., Regalia, F., Rosas-Shady, D. y Soares, Y. (2011). The labor market impacts of youth training in the Dominican Republic. Journal of Labor Economics, 29(2), 267-300.",
        "Card, D., Kluve, J. y Weber, A. (2018). What works? A meta-analysis of recent active labor market program evaluations. Journal of the European Economic Association, 16(3), 894-931.",
        "Casey, K., Glennerster, R. y Miguel, E. (2012). Reshaping institutions: Evidence on aid impacts using a preanalysis plan. The Quarterly Journal of Economics, 127(4), 1755-1812.",
        "Díaz, J. J. y Rosas-Shady, D. (2016). Impact evaluation of the job youth training program Projoven. Banco Interamericano de Desarrollo.",
        "DiPrete, T. A. y Gangl, M. (2004). Assessing bias in the estimation of causal effects: Rosenbaum bounds on matching estimators. Sociological Methodology, 34(1), 271-310.",
        "Gertler, P. J., Martinez, S., Premand, P., Rawlings, L. B. y Vermeersch, C. M. J. (2016). Impact evaluation in practice (2.ª ed.). Banco Mundial.",
        "Heckman, J. J., Ichimura, H. y Todd, P. E. (1997). Matching as an econometric evaluation estimator: Evidence from evaluating a job training programme. The Review of Economic Studies, 64(4), 605-654.",
        "Heckman, J. J., Ichimura, H. y Todd, P. (1998). Matching as an econometric evaluation estimator. The Review of Economic Studies, 65(2), 261-294.",
        "Imbens, G. W. y Wooldridge, J. M. (2009). Recent developments in the econometrics of program evaluation. Journal of Economic Literature, 47(1), 5-86.",
        "Instituto Nacional de Estadística e Informática [INEI]. (2024). Comportamiento de los indicadores de mercado laboral a nivel nacional. INEI.",
        "Ministerio de Economía y Finanzas [MEF]. (2025). Ley de Presupuesto del Sector Público para el Año Fiscal 2026. MEF.",
        "Ñopo, H., Robles, M. y Saavedra, J. (2008). Occupational training to reduce gender segregation: The impacts of ProJoven. Banco Interamericano de Desarrollo.",
        "Organización para la Cooperación y el Desarrollo Económicos [OECD]. (2019). OECD skills outlook 2019: Thriving in a digital world. OECD Publishing.",
        "Organización para la Cooperación y el Desarrollo Económicos [OECD]. (2023). OECD skills outlook 2023. OECD Publishing.",
        "Programa Nacional de Becas y Crédito Educativo [Pronabec]. (2025). Estadísticas de Beca 18. Ministerio de Educación.",
        "Rosenbaum, P. R. (2002). Observational studies (2.ª ed.). Springer.",
        "Rosenbaum, P. R. y Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. Biometrika, 70(1), 41-55.",
        "Rosenbaum, P. R. y Rubin, D. B. (1985). Constructing a control group using multivariate matched sampling methods that incorporate the propensity score. The American Statistician, 39(1), 33-38.",
        "World Bank. (2016). World development report 2016: Digital dividends. World Bank.",
        "World Economic Forum [WEF]. (2023). The future of jobs report 2023. World Economic Forum.",
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
    h2("Anexo 1. Instrumento de seguimiento (encuesta panel)")
    para("Módulo aplicado a tratados y controles a los 6 y 12 meses del egreso. Preguntas seleccionadas:")
    for q in [
        "¿Se encuentra actualmente trabajando? (Sí/No). En caso afirmativo, ¿bajo qué modalidad de contrato?",
        "¿Su empleo está registrado en planilla? ¿Cuenta con beneficios de ley?",
        "¿Cuál es su remuneración bruta mensual actual (en soles)?",
        "¿Cuántos meses transcurrieron entre su egreso y su primer empleo profesional?",
        "¿Le tomaron una prueba técnica de Excel o de IA en la entrevista de selección? (Sí/No)",
        "¿Utiliza IA generativa para automatizar tareas en su puesto? (Nunca/A veces/Frecuentemente)",
        "¿Cuántas horas a la semana estima que ahorra gracias a estas herramientas?",
    ]:
        bullet(q)
    h2("Anexo 2. Matriz de operacionalización de variables")
    tabla(
        ["Variable", "Definición", "Indicador", "Instrumento"],
        [["Inserción laboral formal", "Empleo con contrato y derechos", "Registro en planilla (binario)", "Planilla Electrónica (MTPE)"],
         ["Ingreso laboral", "Remuneración bruta mensual", "Soles por mes", "Planilla / encuesta"],
         ["Velocidad de inserción", "Tiempo hasta el primer empleo calificado", "Número de meses", "Planilla / encuesta"],
         ["Uso de IA", "Intensidad de uso de IA en tareas", "Escala de frecuencia", "Encuesta panel"],
         ["Ahorro de tiempo", "Tiempo liberado por automatización", "Horas semanales", "Encuesta panel"]],
        nota="Elaboración propia.",
        widths=[3.5, 4.5, 4.0, 4.0])
    h2("Anexo 3. Teoría de cambio en notación Mermaid")
    mermaid = (
        "flowchart LR\n"
        "  subgraph Insumos\n"
        "    I1[Plataforma y contenidos Excel + IA]\n"
        "    I2[Docentes y mentores]\n"
        "    I3[Datos Pronabec y convenios MTPE/SUNAT]\n"
        "  end\n"
        "  subgraph Actividades\n"
        "    A1[Sesiones de Excel avanzado]\n"
        "    A2[Taller de IA y automatizacion]\n"
        "    A3[Mentoria y bolsa laboral]\n"
        "  end\n"
        "  subgraph Productos\n"
        "    P1[Becarios certificados]\n"
        "    P2[Portafolio y proyectos auditables]\n"
        "    P3[Vinculacion con empresas]\n"
        "  end\n"
        "  subgraph Resultados\n"
        "    R1[Corto plazo: competencias digitales]\n"
        "    R2[Mediano plazo: insercion formal e ingresos]\n"
        "    R3[Largo plazo: empleabilidad y productividad]\n"
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
