# -*- coding: utf-8 -*-
"""Capítulo III. Metodología de la Investigación (~25 páginas) en Word (.docx).

Tesis: "Factores socioeconómicos que influyen en la informalidad laboral en el
departamento de Lima en los años 2024-2025" (Escuela Profesional de Economía, UNMSM).

Se sigue la ruta metodológica del estudio guía publicado en la revista Semestre
Económico (UNAP, 2025) —nivel explicativo, diseño no experimental de corte
transversal, datos secundarios de la ENAHO (INEI) y modelo econométrico Logit/Probit—
y la matriz de consistencia metodológica del proyecto.

Formato: A4, Times New Roman 12, interlineado 1.5, justificado, márgenes 2.54 cm.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(__file__)
OUT = os.path.join(os.path.dirname(BASE), "Capitulo_III_Metodologia_Informalidad_Lima.docx")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
GRISTXT = RGBColor(0x40, 0x40, 0x40)

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
rpr = normal.element.get_or_add_rPr()
rfn = rpr.get_or_add_rFonts()
for k in ("w:ascii", "w:hAnsi", "w:cs"):
    rfn.set(qn(k), "Times New Roman")
pf = normal.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
pf.line_spacing = 1.5
pf.space_after = Pt(0)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

for sec in doc.sections:
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.54)
    sec.bottom_margin = Cm(2.54)
    sec.left_margin = Cm(2.54)
    sec.right_margin = Cm(2.54)


def _font(run, name="Times New Roman"):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    for k in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(k), name)


def h1(text, size=14):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = AZUL; _font(r)
    return p


def h2(text, size=13):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = AZUL; _font(r)
    return p


def h3(text, size=12):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text); r.bold = True; r.italic = True; r.font.size = Pt(size); r.font.color.rgb = AZUL; _font(r)
    return p


def para(text, after=6, indent=True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(after)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    for i, seg in enumerate(text.split("**")):
        r = p.add_run(seg); _font(r)
        if i % 2 == 1:
            r.bold = True
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(3)
    for i, seg in enumerate(text.split("**")):
        r = p.add_run(seg); _font(r)
        if i % 2 == 1:
            r.bold = True
    return p


def ecuacion(text, numero=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text); r.italic = True; r.font.size = Pt(12); _font(r)
    if numero:
        tab = p.add_run("\t\t(" + numero + ")"); tab.italic = False; _font(tab)
    return p


def _shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def tabla_titulo(numero, titulo):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"Tabla {numero}"); r.bold = True; r.font.size = Pt(11); _font(r)
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(4)
    r2 = p2.add_run(titulo); r2.italic = True; r2.font.size = Pt(11); _font(r2)


def tabla(headers, rows, nota=None, widths=None, fs=9.5):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    hdr = t.rows[0].cells
    for i, htext in enumerate(headers):
        _shade(hdr[i], "1F4E79")
        cp = hdr[i].paragraphs[0]; cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.paragraph_format.line_spacing = 1.0
        run = cp.add_run(htext); run.bold = True; run.font.size = Pt(fs); run.font.color.rgb = BLANCO; _font(run)
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            if ri % 2 == 1:
                _shade(cells[i], "EAF1F8")
            cp = cells[i].paragraphs[0]; cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            cp.paragraph_format.line_spacing = 1.0
            run = cp.add_run(val); run.font.size = Pt(fs); _font(run)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    if nota:
        np = doc.add_paragraph(); np.paragraph_format.space_after = Pt(8); np.paragraph_format.space_before = Pt(2)
        nr = np.add_run("Nota. " + nota); nr.font.size = Pt(9); nr.italic = True; nr.font.color.rgb = GRISTXT; _font(nr)


def referencia(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(1.25)
    p.paragraph_format.first_line_indent = Cm(-1.25)
    for i, seg in enumerate(text.split("//")):
        r = p.add_run(seg); _font(r)
        if i % 2 == 1:
            r.italic = True


# ======================================================================
# CAPÍTULO III
# ======================================================================
h1("Capítulo III. Metodología de la Investigación", size=15)
para(
    "El presente capítulo describe la estrategia metodológica adoptada para identificar y "
    "cuantificar el efecto de los factores socioeconómicos sobre la probabilidad de "
    "informalidad laboral en el departamento de Lima durante el periodo 2024-2025. La ruta "
    "metodológica replica, adaptándola al ámbito limeño, la aproximación empleada por la "
    "literatura econométrica reciente sobre los determinantes de la informalidad en el Perú, "
    "que combina datos secundarios de la Encuesta Nacional de Hogares (ENAHO) del Instituto "
    "Nacional de Estadística e Informática (INEI) con modelos de elección discreta de tipo "
    "Logit y Probit (Semestre Económico, 2025). El capítulo se organiza en diez secciones: "
    "tipo, enfoque y diseño de la investigación; población, muestra y unidad de análisis; "
    "operacionalización de las variables; fuentes y técnicas de recolección de datos; "
    "especificación del modelo econométrico; pruebas de validación y diagnóstico; "
    "procedimiento de análisis; y consideraciones éticas.")
para(
    "Como **antecedente metodológico de referencia** se toma el estudio de la revista "
    "Semestre Económico (2025), titulado «Determinantes de la informalidad laboral: un "
    "análisis para el Perú, 2019 y 2022», cuya ruta metodológica resulta directamente "
    "trasladable al presente trabajo. Dicho estudio adopta un nivel explicativo con diseño "
    "no experimental de corte transversal, emplea como fuente secundaria los microdatos de "
    "la ENAHO y estima un modelo econométrico Logit binomial para identificar los "
    "determinantes de la informalidad, alcanzando un ajuste predictivo elevado (área bajo "
    "la curva ROC de 0,934 y 0,933). Entre los determinantes significativos, el estudio "
    "identifica el nivel educativo, el ingreso, la edad, el sexo, el estado civil, el "
    "tamaño de empresa y el área de residencia, hallazgos que orientan la selección de "
    "variables y la especificación del modelo de la presente investigación, circunscrita al "
    "departamento de Lima y al periodo 2024-2025.")

# ----------------------------------------------------------------------
h1("3.1. Tipo de investigación")
para(
    "La presente investigación es de **tipo aplicada**, dado que su finalidad no es generar "
    "teoría nueva, sino utilizar el conocimiento económico existente para resolver un "
    "problema concreto y socialmente relevante del mercado de trabajo peruano: la elevada y "
    "persistente informalidad laboral en el departamento de Lima. El conocimiento derivado "
    "busca aportar evidencia empírica útil para el diseño de políticas públicas de "
    "formalización laboral orientadas a este territorio.")
para(
    "Desde el punto de vista del **enfoque**, la investigación es **cuantitativa**, puesto "
    "que el análisis se sustenta íntegramente en datos numéricos provenientes de una "
    "encuesta de hogares oficial, procesados mediante técnicas estadísticas y "
    "econométricas. El enfoque cuantitativo permite contrastar de manera objetiva las "
    "hipótesis planteadas a partir de la medición de variables y de la estimación de "
    "relaciones de probabilidad entre ellas (Hernández-Sampieri y Mendoza, 2018).")
para(
    "En cuanto al **nivel o alcance**, la investigación es **explicativa** (o "
    "correlacional-causal). El estudio no se limita a describir la magnitud de la "
    "informalidad ni a establecer asociaciones simples entre variables, sino que busca "
    "estimar la **dirección y la magnitud del efecto** que ejercen los factores "
    "socioeconómicos —el nivel de ingresos, el nivel educativo y los determinantes "
    "demográficos— sobre la probabilidad de que un trabajador se encuentre en condición de "
    "informalidad, controlando por el resto de características observables. Este nivel "
    "explicativo es coherente con la ruta metodológica del estudio de referencia, que "
    "adopta igualmente un nivel explicativo con datos de la ENAHO (Semestre Económico, "
    "2025).")
para(
    "Finalmente, por su finalidad temporal y su relación con la práctica, la investigación "
    "se inscribe en el paradigma **positivista** y emplea el método **hipotético-deductivo**: "
    "a partir de un marco teórico —las teorías dualista, de la segmentación del mercado "
    "laboral y del capital humano— se derivan hipótesis contrastables que se someten a "
    "prueba empírica mediante la estimación de un modelo econométrico. El paradigma "
    "positivista resulta pertinente porque el objeto de estudio —la condición de "
    "informalidad y sus determinantes— es susceptible de medición objetiva y de "
    "cuantificación, y porque el propósito de la investigación es explicar relaciones de "
    "causalidad probabilística entre variables observables, antes que interpretar "
    "significados subjetivos.")
para(
    "La elección de este tipo de investigación se justifica, además, por la naturaleza del "
    "problema y la disponibilidad de información. El estudio de los determinantes de la "
    "informalidad requiere trabajar con un gran número de observaciones individuales y con "
    "una variable de resultado de naturaleza cualitativa (formal/informal), condiciones "
    "que el enfoque cuantitativo y las técnicas econométricas de elección discreta "
    "satisfacen plenamente. La aproximación cualitativa, en cambio, no permitiría estimar "
    "la magnitud del efecto de cada factor ni generalizar los hallazgos a la población de "
    "trabajadores del departamento de Lima.")

# ----------------------------------------------------------------------
h1("3.2. Diseño de investigación")
para(
    "El diseño de la investigación es **no experimental, de corte transversal y de alcance "
    "explicativo o causal**. Es no experimental porque las variables de estudio no son "
    "manipuladas por el investigador, sino observadas tal como ocurren en la realidad a "
    "partir de los registros de una encuesta de hogares; el investigador no asigna "
    "tratamientos ni interviene sobre las condiciones laborales de los trabajadores "
    "(Hernández-Sampieri y Mendoza, 2018).")
para(
    "Es de **corte transversal** porque la información se recolecta y analiza para un "
    "momento o periodo determinado —los años 2024 y 2025— sin seguimiento longitudinal de "
    "los mismos individuos en el tiempo. La unidad de análisis se observa una sola vez, lo "
    "que resulta adecuado para los objetivos del estudio, centrados en identificar los "
    "factores asociados a la informalidad en una coyuntura específica y no en analizar su "
    "evolución dinámica.")
para(
    "Es de **alcance causal** porque, mediante la especificación de un modelo de elección "
    "binaria, se busca estimar el efecto parcial de cada factor socioeconómico sobre la "
    "probabilidad de informalidad, manteniendo constantes las demás variables. El diseño "
    "se complementa con la naturaleza de **fuente secundaria** de los datos: la "
    "investigación utiliza microdatos ya recolectados y procesados por el INEI a través de "
    "la ENAHO, lo que garantiza la representatividad estadística y la validez de la "
    "medición (INEI, 2025).")
h3("Esquema del diseño")
para(
    "El diseño puede esquematizarse como la observación, en un mismo corte temporal, de la "
    "variable dependiente dicotómica (condición de informalidad) y de un conjunto de "
    "variables explicativas socioeconómicas, sobre las cuales se estima una función de "
    "probabilidad. Formalmente, el diseño responde al esquema M → O(X, Y), donde M es la "
    "muestra de trabajadores de la PEA ocupada del departamento de Lima, X es el vector de "
    "factores socioeconómicos y Y es la condición de informalidad observada en el periodo "
    "2024-2025.")
h3("Ventajas y limitaciones del diseño transversal")
para(
    "El diseño transversal ofrece ventajas relevantes para los objetivos de la "
    "investigación. En primer lugar, permite trabajar con una muestra de gran tamaño y "
    "representativa de la población, lo que confiere potencia estadística a las pruebas de "
    "hipótesis y precisión a la estimación de los efectos. En segundo lugar, evita los "
    "problemas de atrición y de pérdida de seguimiento característicos de los diseños "
    "longitudinales. En tercer lugar, resulta económico y oportuno, al aprovechar "
    "información oficial ya recolectada y procesada.")
para(
    "No obstante, el diseño transversal presenta limitaciones que se reconocen "
    "explícitamente. Al observar a los individuos en un único momento, no permite "
    "establecer relaciones de causalidad en sentido estricto, sino asociaciones de "
    "probabilidad condicional interpretables como efectos parciales bajo el supuesto de "
    "exogeneidad de los regresores. Asimismo, no captura la dinámica temporal de la "
    "informalidad ni las transiciones de los trabajadores entre el sector formal y el "
    "informal. Estas limitaciones se mitigan controlando por un conjunto amplio de "
    "variables observables y se discuten en la sección de limitaciones metodológicas.",
    after=8)

# ----------------------------------------------------------------------
h1("3.3. Población y muestra")
h2("3.3.1. Población")
para(
    "La **población** objeto de estudio está constituida por toda la **población "
    "económicamente activa (PEA) ocupada del departamento de Lima** durante los años "
    "2024-2025; es decir, el conjunto de personas de 14 y más años de edad residentes en "
    "el departamento de Lima que, en el periodo de referencia, se encontraban ocupadas en "
    "alguna actividad económica, ya sea en condición de formalidad o de informalidad. De "
    "acuerdo con el INEI (2025), la PEA ocupada del departamento de Lima supera los cinco "
    "millones de trabajadores, lo que la convierte en el mayor mercado laboral del país y "
    "en un ámbito de especial relevancia para el estudio de la informalidad.")
para(
    "El mercado laboral del departamento de Lima se caracteriza por la concentración del "
    "empleo en los sectores de comercio y servicios, por una elevada presencia de "
    "micro y pequeñas empresas y por una marcada heterogeneidad en las condiciones de "
    "trabajo. A pesar de presentar una de las tasas de informalidad relativamente más bajas "
    "del país, el departamento de Lima alberga el mayor volumen absoluto de trabajadores "
    "informales, lo que justifica el análisis de los factores socioeconómicos que "
    "determinan la probabilidad de informalidad en este ámbito. La población así definida "
    "constituye el universo sobre el cual se realizan las inferencias estadísticas del "
    "estudio.")
h2("3.3.2. Muestra")
para(
    "La **muestra** está conformada por el subconjunto de registros de la ENAHO "
    "correspondientes a la PEA ocupada del departamento de Lima en los años 2024 y 2025. "
    "La ENAHO es una encuesta de carácter **probabilístico, de áreas, estratificada, "
    "multietápica e independiente en cada departamento**, cuyo marco muestral se construye "
    "a partir de la información cartográfica y de los Censos Nacionales de Población y "
    "Vivienda, así como del material estadístico de la actualización del Sistema de "
    "Focalización de Hogares (INEI, 2025). En consecuencia, la muestra empleada hereda las "
    "propiedades de representatividad y de inferencia estadística del diseño muestral "
    "oficial del INEI, y los resultados pueden expandirse a la población mediante los "
    "factores de ponderación correspondientes.")
para(
    "A partir del marco muestral nacional, se extrae la **submuestra de trabajadores "
    "ocupados del departamento de Lima**, a la que se aplican los siguientes criterios de "
    "inclusión y exclusión, en línea con la práctica de la literatura econométrica sobre "
    "informalidad (Semestre Económico, 2025):")
bullet("**Criterio de inclusión 1.** Personas pertenecientes a la PEA ocupada, es decir, "
       "que declararon haber trabajado al menos una hora en la semana de referencia o que, "
       "teniendo empleo, no trabajaron por razones circunstanciales.")
bullet("**Criterio de inclusión 2.** Personas de 14 y más años de edad, límite inferior "
       "de la edad de trabajar según la normativa nacional.")
bullet("**Criterio de inclusión 3.** Residentes habituales del departamento de Lima, "
       "identificados a través del código de ubicación geográfica (ubigeo) de la vivienda.")
bullet("**Criterio de exclusión.** Se excluyen los registros con información incompleta o "
       "inconsistente en las variables relevantes del modelo (condición de informalidad, "
       "ingreso, nivel educativo, edad, sexo y estado civil), así como la población "
       "económicamente inactiva y los desocupados.")
para(
    "El **tamaño muestral final** corresponde al número de observaciones válidas de la PEA "
    "ocupada de Lima que resultan tras la aplicación de los criterios anteriores sobre los "
    "módulos de empleo e ingresos (módulo 500) y las características de los miembros del "
    "hogar (módulo 200) de la ENAHO 2024 y 2025. Dado que la ENAHO es una encuesta con "
    "muestra anual superior a 36 mil viviendas a nivel nacional, la submuestra de Lima "
    "garantiza un número de observaciones suficiente para la estimación robusta de un "
    "modelo de elección binaria. Como referencia metodológica, el estudio guía trabajó con "
    "muestras nacionales de 64 954 y 61 181 personas para los años analizados (Semestre "
    "Económico, 2025).")
h3("Diseño muestral de la ENAHO")
para(
    "El diseño muestral de la ENAHO es **probabilístico**, de modo que cada unidad de la "
    "población tiene una probabilidad conocida y distinta de cero de ser seleccionada; "
    "**estratificado**, pues la población se divide en estratos socioeconómica y "
    "geográficamente homogéneos antes de la selección; **multietápico**, dado que la "
    "selección se realiza en etapas sucesivas; y **de áreas**, porque las unidades "
    "primarias de muestreo corresponden a conglomerados geográficos. En el ámbito urbano, "
    "la unidad primaria de muestreo es el conglomerado (aproximadamente 120 viviendas "
    "particulares) y la unidad secundaria es la vivienda particular; en el ámbito rural se "
    "consideran conglomerados y áreas de empadronamiento rural (INEI, 2025).")
para(
    "La condición probabilística del diseño implica que, para producir estimaciones "
    "representativas de la población, cada observación debe ponderarse por su **factor de "
    "expansión**, el cual recoge la probabilidad de selección de la unidad y los ajustes "
    "por no respuesta y por proyección de población. En consecuencia, tanto los "
    "estadísticos descriptivos como las estimaciones econométricas se calculan incorporando "
    "los factores de expansión y el diseño complejo de la muestra, a fin de obtener errores "
    "estándar correctos y resultados expandibles a la PEA ocupada del departamento de Lima.")
para(
    "Aunque la ENAHO proporciona una muestra probabilística cuyo tamaño es suficiente para "
    "la inferencia, a título ilustrativo el tamaño muestral mínimo requerido para estimar "
    "una proporción poblacional puede aproximarse mediante la expresión para poblaciones "
    "grandes:")
ecuacion("n = [Z²·p·(1 − p)] / e²", "3.1")
para(
    "donde n es el tamaño muestral, Z es el valor de la distribución normal estándar "
    "asociado al nivel de confianza (1,96 para el 95 %), p es la proporción esperada de "
    "informalidad (que puede fijarse en 0,5 para maximizar el tamaño) y e es el margen de "
    "error admisible. Con un nivel de confianza del 95 % y un margen de error del 2 %, el "
    "tamaño muestral mínimo resultaría de aproximadamente 2 401 observaciones, ampliamente "
    "superado por la submuestra de la PEA ocupada de Lima en la ENAHO, lo que confirma la "
    "suficiencia de la muestra para la estimación del modelo.")
h2("3.3.3. Unidad de análisis")
para(
    "La **unidad de análisis** es el **trabajador individual** perteneciente a la PEA "
    "ocupada del departamento de Lima en el periodo 2024-2025. Sobre cada individuo se "
    "observa su condición de informalidad laboral y el conjunto de características "
    "socioeconómicas y demográficas que constituyen las variables explicativas del modelo.")
h2("3.3.4. Ámbito de estudio")
para(
    "El **ámbito de estudio** es el **departamento de Lima**, ubicado en la costa central "
    "del Perú. Su elección obedece a su relevancia económica y demográfica: concentra "
    "alrededor de un tercio de la población nacional y aporta cerca de la mitad del "
    "producto bruto interno del país, además de albergar la mayor parte de la actividad "
    "empresarial formal, de la oferta de educación superior y de los servicios modernos "
    "(INEI, 2025). El departamento de Lima comprende tanto a Lima Metropolitana —área "
    "predominantemente urbana y de elevada densidad empresarial— como a las provincias de "
    "Lima, de carácter más rural y agrario, lo que configura un territorio heterogéneo en "
    "el que coexisten realidades laborales diversas.")
para(
    "Esta heterogeneidad interna hace del departamento de Lima un ámbito particularmente "
    "idóneo para el estudio de los determinantes individuales de la informalidad: a "
    "diferencia de las regiones predominantemente rurales, donde la informalidad se explica "
    "en gran medida por la estructura productiva agraria, en Lima la informalidad convive "
    "con un tejido económico moderno, de modo que sus determinantes deben buscarse en mayor "
    "medida en las características socioeconómicas de los trabajadores —ingreso, educación y "
    "atributos demográficos—, que son precisamente las variables del presente modelo.",
    after=8)

# ----------------------------------------------------------------------
h1("3.4. Operacionalización de las variables")
para(
    "El estudio considera una variable dependiente dicotómica (la condición de empleo "
    "informal), dos variables independientes asociadas directamente a las hipótesis "
    "principales (el nivel de ingresos y el nivel educativo) y un conjunto de variables de "
    "control de naturaleza demográfica (edad, sexo y estado civil). La operacionalización "
    "de cada variable se detalla a continuación y se sintetiza en la Tabla 1.")

h2("3.4.1. Variable dependiente: empleo informal")
para(
    "La variable dependiente es la **condición de empleo informal** del trabajador, "
    "definida conforme a los criterios de la Organización Internacional del Trabajo y del "
    "INEI: se considera informal al ocupado cuyo puesto de trabajo no se encuentra sujeto a "
    "la legislación laboral nacional y, por tanto, carece de protección social y de "
    "beneficios laborales (INEI, 2025). Operativamente, se construye como una **variable "
    "dicotómica (binaria)** que toma el valor de 1 cuando el trabajador es informal —no "
    "cuenta con un contrato laboral ni con acceso a la seguridad social— y el valor de 0 "
    "cuando es formal:")
ecuacion("Informalᵢ = 1  si el trabajador i es informal;   Informalᵢ = 0  si es formal", "3.2")

h2("3.4.2. Variables independientes")
para(
    "**a) Nivel de ingresos.** Recoge el nivel de ingreso laboral del trabajador. Siguiendo "
    "la matriz de consistencia del estudio, se operacionaliza como una variable dicotómica "
    "construida con relación a la **Remuneración Mínima Vital (RMV)**: toma el valor de 0 "
    "cuando el ingreso del trabajador es menor a la RMV y el valor de 1 cuando es mayor o "
    "igual a la RMV. Esta variable permite contrastar la hipótesis de que un mayor nivel de "
    "ingresos reduce la probabilidad de informalidad; por ello, se espera que su "
    "coeficiente presente **signo negativo**.")
para(
    "**b) Nivel educativo.** Mide el máximo nivel educativo alcanzado por el trabajador. Se "
    "operacionaliza como una variable **categórica** con cuatro niveles —primaria, "
    "secundaria, superior no universitaria y superior universitaria—, que en la estimación "
    "se introduce mediante variables dicotómicas (dummies), tomando la categoría de menor "
    "nivel como referencia. De acuerdo con la teoría del capital humano, se espera que a "
    "mayor nivel educativo disminuya la probabilidad de informalidad; por ello, el "
    "coeficiente esperado es de **signo negativo**.")
para(
    "En términos operativos, a partir de la variable categórica de nivel educativo se "
    "construyen tres variables dicotómicas —secundaria, superior no universitaria y "
    "superior universitaria—, dejando la categoría «primaria o menos» como **categoría de "
    "referencia (base)**. De este modo, cada coeficiente estimado mide el efecto de "
    "alcanzar el nivel educativo correspondiente respecto de contar únicamente con "
    "educación primaria, lo que permite una interpretación directa del gradiente educativo "
    "de la informalidad. La omisión de una categoría es necesaria para evitar la trampa de "
    "las variables dicotómicas (multicolinealidad perfecta).")

h2("3.4.3. Variables de control")
para(
    "Para aislar el efecto de las variables de interés y reducir el sesgo por variables "
    "omitidas, el modelo incorpora un conjunto de **variables de control** de carácter "
    "demográfico, que la literatura identifica como determinantes relevantes de la "
    "informalidad (Semestre Económico, 2025):")
bullet("**Edad.** Medida en número de años cumplidos. Para capturar la relación no lineal "
       "(en forma de U) entre edad e informalidad documentada por la evidencia, se incluye "
       "adicionalmente el término cuadrático de la edad (edad²).")
bullet("**Sexo (género).** Variable dicotómica que toma el valor de 0 para los hombres y "
       "de 1 para las mujeres.")
bullet("**Estado civil.** Variable dicotómica que toma el valor de 1 para las personas "
       "casadas y de 0 para las no casadas (convivientes, viudas, divorciadas, separadas y "
       "solteras).")
para(
    "La elección y el signo esperado de cada variable se fundamentan en el marco teórico. "
    "Conforme a la **teoría del capital humano** (Becker, 1964), una mayor inversión en "
    "educación incrementa la productividad del trabajador y su acceso a empleos formales, "
    "por lo que el nivel educativo debe asociarse negativamente con la informalidad. La "
    "**teoría de la segmentación del mercado laboral** (Doeringer y Piore, 1971) sostiene "
    "que las barreras de capital humano e ingreso impiden el tránsito hacia el sector "
    "formal, de modo que un mayor nivel de ingresos reduce la probabilidad de informalidad. "
    "Finalmente, la misma teoría reconoce que el acceso al empleo formal depende también de "
    "factores demográficos: se espera que las mujeres presenten mayor probabilidad de "
    "informalidad (signo positivo del sexo), que la edad describa una relación no lineal en "
    "forma de U y que el estado civil ejerza un efecto ambiguo, según predomine la mayor "
    "necesidad de estabilidad de ingresos de las personas casadas o su mayor dedicación al "
    "trabajo no remunerado del hogar.")

tabla_titulo("1", "Operacionalización de las variables del estudio")
tabla(
    ["Variable", "Tipo", "Indicador / medición", "Codificación", "Signo esp."],
    [["Empleo informal (dependiente)", "Dicotómica",
      "Condición de informalidad del puesto de trabajo", "1 = informal; 0 = formal", "—"],
     ["Nivel de ingresos (independiente)", "Dicotómica",
      "Ingreso laboral respecto de la RMV", "0 = menor a la RMV; 1 = mayor o igual a la RMV", "(−)"],
     ["Nivel educativo (independiente)", "Categórica",
      "Máximo nivel educativo alcanzado", "Primaria / secundaria / superior no univ. / superior univ.", "(−)"],
     ["Edad (control)", "Continua", "Años cumplidos (y edad²)", "Número de años", "(U)"],
     ["Sexo (control)", "Dicotómica", "Sexo del trabajador", "0 = hombre; 1 = mujer", "(+)"],
     ["Estado civil (control)", "Dicotómica", "Situación conyugal", "1 = casado; 0 = no casado", "(±)"]],
    nota="Elaboración propia a partir de la matriz de consistencia metodológica del proyecto "
         "y de la ENAHO (INEI, 2025). RMV = Remuneración Mínima Vital. El signo esperado se "
         "refiere al efecto sobre la probabilidad de informalidad.",
    widths=[3.4, 2.0, 4.0, 4.6, 1.6], fs=9)

h2("3.4.4. Definiciones conceptuales y operacionales")
para(
    "Para garantizar la precisión de la medición, se distinguen las definiciones "
    "conceptuales (el significado teórico de cada constructo) de las definiciones "
    "operacionales (la forma concreta en que se mide a partir de la ENAHO):")
para(
    "**Empleo informal.** Conceptualmente, es el conjunto de empleos que no están sujetos "
    "a la legislación laboral nacional ni al pago de impuestos sobre la renta, y que no "
    "otorgan protección social ni beneficios laborales (OIT, 2024; INEI, 2025). "
    "Operacionalmente, se mide como una variable dicotómica que identifica al trabajador "
    "informal por la ausencia de afiliación a un sistema de pensiones o de seguro de salud "
    "vinculado al empleo y por la inexistencia de un contrato laboral registrado.")
para(
    "**Sector informal.** Conceptualmente, comprende las unidades productivas de los "
    "hogares no constituidas en sociedad y no registradas ante la administración "
    "tributaria. Su distinción respecto del empleo informal es relevante, pues una persona "
    "puede tener un empleo informal dentro de una empresa del sector formal, y viceversa "
    "(INEI, 2025).")
para(
    "**Población económicamente activa (PEA) ocupada.** Conjunto de personas de 14 y más "
    "años que, en el periodo de referencia, participaron en la producción de bienes y "
    "servicios y se encontraban trabajando. **Remuneración Mínima Vital (RMV).** Ingreso "
    "mínimo legal que debe percibir un trabajador del régimen laboral de la actividad "
    "privada, utilizado en este estudio como umbral para clasificar el nivel de ingresos. "
    "**Nivel educativo.** Máximo grado de estudios alcanzado por la persona dentro del "
    "sistema educativo formal, agrupado en las categorías de la Tabla 1.")

# ----------------------------------------------------------------------
h1("3.5. Fuentes y técnicas de recolección de datos")
para(
    "La **fuente de información** es de carácter **secundario**: se emplean los microdatos "
    "de la **Encuesta Nacional de Hogares sobre Condiciones de Vida y Pobreza (ENAHO)** "
    "ejecutada por el INEI para los años 2024 y 2025, de acceso público a través del "
    "Sistema de Microdatos del INEI. La ENAHO constituye la principal fuente oficial para "
    "el estudio del empleo y la informalidad en el Perú, dado que recoge de manera "
    "estandarizada las características demográficas, educativas, laborales y de ingresos de "
    "los miembros del hogar (INEI, 2025).")
para(
    "La **técnica de recolección** es el **análisis documental** de fuentes estadísticas "
    "secundarias. A diferencia de la encuesta o la entrevista, esta técnica no genera datos "
    "nuevos, sino que examina de manera sistemática información previamente registrada y "
    "procesada por un organismo oficial. El procedimiento de construcción de la base de "
    "datos de trabajo comprende las siguientes etapas: (i) descarga de los módulos "
    "pertinentes de la ENAHO 2024 y 2025 —módulo 200 (características de los miembros del "
    "hogar), módulo 300 (educación) y módulo 500 (empleo e ingresos)—; (ii) fusión de los "
    "módulos mediante los identificadores de conglomerado, vivienda, hogar y persona; "
    "(iii) filtrado de la PEA ocupada residente en el departamento de Lima; (iv) "
    "construcción y recodificación de las variables del modelo según la Tabla 1; y "
    "(v) depuración de valores perdidos e inconsistentes.")
para(
    "El **instrumento**, en sentido estricto, es la **ficha de registro y sistematización "
    "de datos** en la cual se consolidan las variables operacionalizadas para cada unidad "
    "de análisis. La validez y la confiabilidad de la medición están garantizadas por el "
    "diseño metodológico de la ENAHO, instrumento oficial sometido a controles de calidad "
    "estadística por el INEI.")
para(
    "La Tabla 2 resume los módulos de la ENAHO empleados y las variables que de ellos se "
    "extraen para la construcción de la base de datos de trabajo.")
tabla_titulo("2", "Módulos de la ENAHO utilizados y variables extraídas")
tabla(
    ["Módulo ENAHO", "Contenido", "Variables del modelo"],
    [["Módulo 200 — Características de los miembros del hogar",
      "Edad, sexo, estado civil, relación de parentesco",
      "Edad, sexo, estado civil"],
     ["Módulo 300 — Educación",
      "Nivel educativo alcanzado, años de estudio",
      "Nivel educativo"],
     ["Módulo 500 — Empleo e ingresos",
      "Condición de actividad, categoría ocupacional, contrato, seguridad social, ingresos",
      "Empleo informal, nivel de ingresos"],
     ["Sumaria — Variables calculadas",
      "Ingreso y gasto del hogar, factores de expansión, ubigeo",
      "Factor de expansión, identificación de Lima"]],
    nota="Elaboración propia a partir de la documentación de la ENAHO (INEI, 2025). "
         "El ubigeo permite identificar a los residentes del departamento de Lima.",
    widths=[4.6, 5.4, 4.0], fs=9)

h2("3.5.1. Justificación de la fuente de datos")
para(
    "La ENAHO se elige como fuente principal por cuatro razones. Primero, es la encuesta "
    "oficial de mayor cobertura temática sobre las condiciones de empleo, educación e "
    "ingresos de los hogares peruanos, y constituye la base sobre la cual el INEI calcula "
    "los indicadores oficiales de informalidad. Segundo, su carácter probabilístico y su "
    "representatividad a nivel departamental permiten realizar inferencias válidas sobre la "
    "PEA ocupada del departamento de Lima. Tercero, su periodicidad anual y su continuidad "
    "metodológica facilitan el análisis para el periodo 2024-2025. Cuarto, el acceso "
    "público y gratuito a los microdatos garantiza la transparencia y la replicabilidad de "
    "la investigación.")
para(
    "La ENAHO se ejecuta de manera continua a lo largo del año, con una muestra anual "
    "superior a 36 mil viviendas a nivel nacional, distribuidas en los ámbitos urbano y "
    "rural de los veinticuatro departamentos y la Provincia Constitucional del Callao. Su "
    "marco muestral se actualiza a partir de los censos de población y vivienda, lo que "
    "asegura la cobertura adecuada del departamento de Lima, el más poblado del país.")
h2("3.5.2. Validez y confiabilidad")
para(
    "La **validez** de la medición se sustenta en que las variables se construyen a partir "
    "de los criterios oficiales del INEI y de la OIT para la medición de la informalidad, "
    "lo que asegura la validez de contenido y de constructo. La **confiabilidad** se "
    "garantiza por el riguroso proceso de diseño, capacitación, supervisión y control de "
    "calidad que el INEI aplica a la ENAHO, así como por la estandarización de los "
    "instrumentos a lo largo del tiempo. Al tratarse de una fuente secundaria oficial, no "
    "se requiere una prueba piloto ni el cálculo de coeficientes de confiabilidad como el "
    "alfa de Cronbach, propios de instrumentos elaborados por el investigador; la "
    "confiabilidad descansa en la solidez metodológica de la encuesta nacional (INEI, "
    "2025).")

# ----------------------------------------------------------------------
h1("3.6. Especificación del modelo econométrico")
para(
    "Dado que la variable dependiente es **dicotómica** —el trabajador es informal o no lo "
    "es—, la estimación por mínimos cuadrados ordinarios (MCO) resulta inadecuada. El "
    "análisis se realiza, por tanto, mediante **modelos de elección binaria de tipo Logit "
    "y Probit**, idóneos para modelar la probabilidad de ocurrencia de un evento "
    "dicotómico (Gujarati y Porter, 2010; Wooldridge, 2010).")

h2("3.6.1. Limitaciones del modelo de probabilidad lineal")
para(
    "Si la condición de informalidad se modelara mediante un modelo de probabilidad lineal "
    "estimado por MCO de la forma:")
ecuacion("Informalᵢ = β₀ + β₁X₁ᵢ + β₂X₂ᵢ + … + βₖXₖᵢ + uᵢ", "3.3")
para(
    "se incurriría en tres problemas conocidos: (i) las probabilidades predichas pueden "
    "situarse fuera del intervalo [0, 1], careciendo de sentido; (ii) el término de error "
    "es heterocedástico por construcción; y (iii) se impone una relación lineal entre los "
    "regresores y la probabilidad, supuesto poco plausible. Por ello, se recurre a modelos "
    "no lineales que restringen la probabilidad estimada al intervalo [0, 1] mediante una "
    "función de distribución acumulada (Maddala, 1983; Greene, 2012).")

h2("3.6.2. Modelos Logit y Probit")
para(
    "Los modelos Logit y Probit expresan la probabilidad de que el trabajador sea informal "
    "como una función no lineal de un índice latente Zᵢ = Xᵢ′β, donde Xᵢ es el vector de "
    "variables explicativas y β el vector de parámetros. En el **modelo Logit**, la "
    "probabilidad se modela mediante la función de distribución logística acumulada:")
ecuacion("P(Informalᵢ = 1 | Xᵢ) = Λ(Xᵢ′β) = e^(Xᵢ′β) / [1 + e^(Xᵢ′β)] = 1 / [1 + e^(−Xᵢ′β)]", "3.4")
para(
    "En el **modelo Probit**, la probabilidad se modela mediante la función de distribución "
    "normal estándar acumulada Φ(·):")
ecuacion("P(Informalᵢ = 1 | Xᵢ) = Φ(Xᵢ′β) = ∫_{−∞}^{Xᵢ′β} φ(z) dz", "3.5")
para(
    "Ambas funciones garantizan que la probabilidad estimada se mantenga acotada entre 0 y "
    "1 y que la relación entre los regresores y la probabilidad adopte la forma de una "
    "curva sigmoide. La diferencia entre ambos radica en la función de distribución "
    "supuesta para el término de error: logística en el Logit y normal en el Probit. En la "
    "práctica —y salvo en las colas de la distribución, donde la función logística asigna "
    "una probabilidad ligeramente mayor a los eventos extremos que la normal—, ambos "
    "modelos producen resultados muy similares en términos de signos y "
    "significancia, aunque el modelo Logit es predominante en los estudios de informalidad "
    "por la facilidad de interpretación de sus coeficientes en términos de **razón de "
    "momios (odds ratio)** (Semestre Económico, 2025).")
para(
    "Ambos modelos admiten una interpretación a partir de una **variable latente**. Sea "
    "Y*ᵢ una variable continua no observable que representa la propensión o utilidad neta de "
    "la informalidad para el trabajador i, determinada por Y*ᵢ = Xᵢ′β + uᵢ. El investigador "
    "no observa Y*ᵢ, sino únicamente su manifestación dicotómica, de modo que el trabajador "
    "es informal cuando su propensión supera un umbral, convencionalmente fijado en cero:")
ecuacion("Informalᵢ = 1 si Y*ᵢ > 0;   Informalᵢ = 0 si Y*ᵢ ≤ 0", "3.6")
para(
    "Bajo este enfoque, la probabilidad de informalidad es P(Informalᵢ = 1) = P(uᵢ > "
    "−Xᵢ′β) = F(Xᵢ′β), donde F(·) es la función de distribución acumulada del término de "
    "error. Si se supone que uᵢ sigue una distribución logística se obtiene el modelo "
    "Logit; si se supone normal estándar, el Probit. Esta derivación dota de fundamento "
    "teórico a la especificación y vincula el modelo con la teoría de la utilidad aleatoria "
    "de la elección discreta.")
h3("Supuestos del modelo")
para(
    "La estimación válida de los modelos de elección binaria descansa en los siguientes "
    "supuestos: (i) **correcta especificación** de la forma funcional de la probabilidad y "
    "de los regresores incluidos; (ii) **ausencia de multicolinealidad perfecta** entre las "
    "variables explicativas; (iii) **exogeneidad** de los regresores, es decir, "
    "independencia entre las variables explicativas y el término de error; (iv) "
    "**observaciones independientes**, garantizada por el diseño muestral; y (v) **tamaño "
    "muestral suficiente**, requerido por las propiedades asintóticas del estimador de "
    "máxima verosimilitud. El cumplimiento de estos supuestos se verifica mediante las "
    "pruebas de diagnóstico descritas en la sección 3.7.")

h2("3.6.3. Especificación empírica del modelo")
para(
    "El modelo econométrico que se estima para contrastar la hipótesis general, "
    "expresándolo a través del índice latente Zᵢ, adopta la siguiente forma:")
ecuacion("Zᵢ = β₀ + β₁Ingresoᵢ + β₂Educᵢ + β₃Edadᵢ + β₄Edadᵢ² + β₅Sexoᵢ + β₆EstCivilᵢ + uᵢ", "3.7")
para(
    "donde Informalᵢ es la condición de informalidad del trabajador i; Ingresoᵢ es la "
    "variable dicotómica de nivel de ingresos respecto de la RMV; Educᵢ representa el "
    "conjunto de variables dicotómicas de nivel educativo; Edadᵢ y Edadᵢ² son la edad y su "
    "término cuadrático; Sexoᵢ es la variable de género; EstCivilᵢ es el estado civil; y uᵢ "
    "es el término de error. Los parámetros β₁ a β₆ miden el efecto de cada factor sobre el "
    "índice latente de informalidad.")
para(
    "A partir de esta especificación general se derivan los modelos correspondientes a cada "
    "hipótesis específica. Para la **hipótesis específica 1**, el parámetro de interés es "
    "β₁, que mide el efecto del nivel de ingresos sobre la probabilidad de informalidad; la "
    "hipótesis se confirma si β₁ es **negativo y estadísticamente significativo**. Para la "
    "**hipótesis específica 2**, los parámetros de interés son los asociados al nivel "
    "educativo (β₂), que se espera sean **negativos y significativos**. Para la "
    "**hipótesis específica 3**, se evalúa la significancia conjunta e individual de los "
    "parámetros demográficos (β₃ a β₆) correspondientes a la edad, el sexo y el estado "
    "civil.")

h2("3.6.4. Estimación por máxima verosimilitud")
para(
    "A diferencia del modelo lineal, los modelos Logit y Probit se estiman por el método de "
    "**máxima verosimilitud (MV)**, que selecciona los valores de los parámetros que "
    "maximizan la probabilidad de observar la muestra efectivamente registrada. La función "
    "de log-verosimilitud del modelo, para una muestra de n trabajadores, es:")
ecuacion("ln L(β) = Σᵢ { Informalᵢ · ln[F(Xᵢ′β)] + (1 − Informalᵢ) · ln[1 − F(Xᵢ′β)] }", "3.8")
para(
    "donde F(·) es la función logística Λ(·) en el caso Logit o la normal estándar Φ(·) en "
    "el caso Probit. Los estimadores de máxima verosimilitud se obtienen mediante "
    "procedimientos iterativos de optimización numérica (por ejemplo, el algoritmo de "
    "Newton-Raphson) y son consistentes, asintóticamente eficientes y asintóticamente "
    "normales (Greene, 2012).")

h2("3.6.5. Efectos marginales y razón de momios")
para(
    "Una característica esencial de los modelos no lineales es que **los coeficientes "
    "estimados no se interpretan directamente como en el modelo lineal**: el coeficiente βⱼ "
    "indica únicamente el signo del efecto, pero no su magnitud sobre la probabilidad. Para "
    "cuantificar el efecto de cada variable sobre la probabilidad de informalidad se "
    "calculan los **efectos marginales**, que en el modelo Logit se expresan como:")
ecuacion("∂P(Informalᵢ = 1) / ∂Xⱼ = Λ(Xᵢ′β) · [1 − Λ(Xᵢ′β)] · βⱼ", "3.9")
para(
    "El efecto marginal mide el cambio en la probabilidad de ser informal ante un cambio "
    "unitario en la variable explicativa Xⱼ. Dado que este efecto depende del punto en que "
    "se evalúa, se reportan los **efectos marginales en la media** de las variables y los "
    "**efectos marginales promedio** de la muestra. Para las variables dicotómicas, el "
    "efecto marginal se calcula como la diferencia de probabilidad entre las categorías 1 "
    "y 0.")
para(
    "Complementariamente, en el modelo Logit se interpreta la **razón de momios (odds "
    "ratio)**, definida como el cociente entre la probabilidad de ser informal y la de no "
    "serlo:")
ecuacion("P(Informalᵢ = 1) / P(Informalᵢ = 0) = e^(Xᵢ′β)", "3.10")
para(
    "El exponencial de cada coeficiente, e^(βⱼ), expresa cuántas veces se modifica la razón "
    "de momios de informalidad ante un cambio unitario en la variable correspondiente, "
    "manteniendo constantes las demás. Un valor superior a la unidad indica que la variable "
    "aumenta la probabilidad relativa de informalidad, mientras que un valor inferior a la "
    "unidad indica que la reduce.")

para(
    "A modo ilustrativo, si el exponencial del coeficiente del nivel educativo superior "
    "universitario resultara, por ejemplo, igual a 0,35, ello significaría que la razón de "
    "momios de informalidad de un trabajador con educación universitaria equivale a 0,35 "
    "veces la de un trabajador con educación primaria, es decir, una reducción del 65 % en "
    "la razón de probabilidades de ser informal, manteniendo constantes las demás "
    "variables. De manera análoga, un efecto marginal de -0,30 indicaría que, en promedio, "
    "contar con educación universitaria reduce en 30 puntos porcentuales la probabilidad de "
    "informalidad respecto de la categoría de referencia. Esta forma de interpretación, en "
    "términos de efectos marginales y razones de momios, es la que se adopta en la "
    "presentación de los resultados.")

h2("3.6.6. Selección entre Logit y Probit")
para(
    "Dado que ambos modelos son apropiados para la variable dependiente dicotómica, se "
    "estiman las dos especificaciones y se selecciona la de mejor desempeño con base en los "
    "**criterios de información de Akaike (AIC) y Bayesiano (BIC)** —prefiriéndose el modelo "
    "con menores valores— y en la **capacidad predictiva** medida por el área bajo la curva "
    "ROC. El modelo Logit se adopta como especificación principal por la interpretabilidad "
    "de sus razones de momios, y el modelo Probit se estima como **prueba de robustez**, "
    "verificándose la coincidencia de signos, magnitudes y niveles de significancia entre "
    "ambos (Semestre Económico, 2025).")
para(
    "Los criterios de información se calculan como:")
ecuacion("AIC = −2·ln L + 2k          BIC = −2·ln L + k·ln(n)", "3.11")
para(
    "donde ln L es el valor de la log-verosimilitud del modelo estimado, k es el número de "
    "parámetros y n es el tamaño de la muestra. Ambos criterios penalizan la complejidad "
    "del modelo —el BIC de manera más estricta, al ponderar por el logaritmo del tamaño "
    "muestral—, de modo que, entre dos especificaciones con ajuste similar, se prefiere la "
    "más parsimoniosa. La concordancia de los resultados entre las especificaciones Logit y "
    "Probit constituye, además, una evidencia de la solidez de los hallazgos frente a la "
    "elección de la forma funcional.", after=8)

# ----------------------------------------------------------------------
h1("3.7. Pruebas de validación y diagnóstico del modelo")
para(
    "Con el fin de garantizar la validez de las estimaciones, se aplican pruebas de bondad "
    "de ajuste, de capacidad predictiva y de diagnóstico econométrico, sintetizadas en la "
    "Tabla 2.")

h2("3.7.1. Bondad de ajuste")
para(
    "La bondad de ajuste global del modelo se evalúa mediante el **pseudo-R² de McFadden**, "
    "definido a partir de la log-verosimilitud del modelo estimado (ln L_c) y la del modelo "
    "que solo incluye la constante (ln L_0):")
ecuacion("R²_McFadden = 1 − (ln L_c / ln L₀)", "3.12")
para(
    "Asimismo, la significancia conjunta de los parámetros se contrasta mediante la "
    "**prueba de razón de verosimilitud (LR)**, que sigue una distribución ji-cuadrada con "
    "tantos grados de libertad como restricciones evaluadas, y cuya hipótesis nula plantea "
    "que todos los coeficientes de pendiente son iguales a cero.")
para(
    "Conviene precisar que el pseudo-R² de McFadden no admite la misma interpretación que "
    "el coeficiente de determinación del modelo lineal: sus valores tienden a ser más "
    "bajos, y se considera que un valor situado entre 0,2 y 0,4 refleja un ajuste "
    "satisfactorio en modelos de elección discreta. Por ello, la evaluación de la bondad de "
    "ajuste no se sustenta en un único indicador, sino en la combinación del pseudo-R², la "
    "prueba de razón de verosimilitud, los criterios de información y, sobre todo, la "
    "capacidad predictiva del modelo.")

h2("3.7.2. Capacidad predictiva")
para(
    "La capacidad predictiva del modelo se evalúa mediante la **matriz de clasificación**, "
    "que contrasta los valores observados con los predichos a partir de un umbral de "
    "probabilidad (usualmente 0,5), y mediante el **área bajo la curva ROC (AUC)**, que "
    "resume la capacidad del modelo para discriminar entre trabajadores formales e "
    "informales. Un valor del AUC cercano a 1 indica un excelente poder de discriminación; "
    "como referencia, el estudio guía alcanzó valores de AUC de 0,934 y 0,933, indicativos "
    "de un ajuste predictivo muy satisfactorio (Semestre Económico, 2025).")
para(
    "La matriz de clasificación cruza las categorías observadas con las predichas y permite "
    "calcular indicadores de desempeño como la **sensibilidad** (proporción de informales "
    "correctamente clasificados), la **especificidad** (proporción de formales "
    "correctamente clasificados) y el **porcentaje global de aciertos**. Su estructura se "
    "presenta en la Tabla 4.")
tabla_titulo("3", "Estructura de la matriz de clasificación")
tabla(
    ["Observado \\ Predicho", "Informal (1)", "Formal (0)", "Total"],
    [["Informal (1)", "Verdaderos positivos (VP)", "Falsos negativos (FN)", "VP + FN"],
     ["Formal (0)", "Falsos positivos (FP)", "Verdaderos negativos (VN)", "FP + VN"],
     ["Total", "VP + FP", "FN + VN", "n"]],
    nota="Elaboración propia. Sensibilidad = VP/(VP+FN); especificidad = VN/(FP+VN); "
         "aciertos globales = (VP+VN)/n.",
    widths=[4.0, 4.0, 4.0, 2.0], fs=9)

h2("3.7.3. Multicolinealidad")
para(
    "Para descartar la presencia de multicolinealidad entre las variables explicativas se "
    "calcula el **factor de inflación de la varianza (VIF)**. Se considera que existe "
    "multicolinealidad moderada cuando el VIF supera el valor de 5 y grave cuando supera "
    "el valor de 10; en este último caso, se evalúa la transformación o eliminación de las "
    "variables afectadas.")

h2("3.7.4. Especificación y calibración")
para(
    "La correcta especificación del modelo se verifica mediante la **prueba de "
    "especificación de enlace (link test)** y la **prueba de bondad de ajuste de "
    "Hosmer-Lemeshow**, que contrasta la concordancia entre las frecuencias observadas y "
    "esperadas por grupos de probabilidad. El no rechazo de la hipótesis nula en esta "
    "última prueba indica que el modelo se encuentra correctamente calibrado. El "
    "estadístico de Hosmer-Lemeshow se define como:")
ecuacion("Ĥ = Σ_{g=1}^{G} [(O_g − E_g)² / (E_g · (1 − E_g/n_g))]", "3.13")
para(
    "donde G es el número de grupos (usualmente diez deciles de riesgo), O_g y E_g son las "
    "frecuencias observada y esperada de informales en el grupo g, y n_g es el número de "
    "observaciones del grupo. El estadístico se distribuye como una ji-cuadrada con G − 2 "
    "grados de libertad; un p-valor superior a 0,05 indica que no existe evidencia de mala "
    "calibración del modelo.")

tabla_titulo("4", "Pruebas de validación y diagnóstico econométrico")
tabla(
    ["Dimensión", "Prueba / estadístico", "Criterio de decisión"],
    [["Bondad de ajuste", "Pseudo-R² de McFadden; razón de verosimilitud (LR)",
      "Mayor pseudo-R²; rechazo de H₀ en la prueba LR (p < 0,05)"],
     ["Capacidad predictiva", "Matriz de clasificación; área bajo la curva ROC (AUC)",
      "Mayor porcentaje de aciertos; AUC cercano a 1"],
     ["Multicolinealidad", "Factor de inflación de la varianza (VIF)",
      "VIF < 5 (sin problema); VIF > 10 (multicolinealidad grave)"],
     ["Especificación", "Link test; prueba de Hosmer-Lemeshow",
      "No rechazo de H₀ (modelo bien especificado)"],
     ["Selección del modelo", "Criterios de información AIC y BIC",
      "Se prefiere el modelo con menores AIC y BIC"]],
    nota="Elaboración propia con base en Gujarati y Porter (2010), Greene (2012) y la ruta "
         "metodológica del estudio de referencia (Semestre Económico, 2025).",
    widths=[3.4, 5.6, 6.6], fs=9)

# ----------------------------------------------------------------------
h1("3.8. Procedimiento de análisis e interpretación de la información")
para(
    "El análisis de la información se estructura en tres niveles progresivos, ejecutados "
    "en un entorno estadístico especializado (Stata o R):")
para(
    "**a) Análisis descriptivo.** En una primera etapa se calculan las medidas de "
    "frecuencia y de tendencia central de las variables del modelo, tanto para el conjunto "
    "de la PEA ocupada de Lima como desagregadas por condición de formalidad. Se examina la "
    "distribución de la informalidad según el nivel de ingresos, el nivel educativo, la "
    "edad, el sexo y el estado civil, y se construyen tablas de contingencia que anticipan "
    "la dirección esperada de las asociaciones. La Tabla 5 detalla los estadísticos que se "
    "reportarán para cada variable según su naturaleza.")
tabla_titulo("5", "Plan de análisis descriptivo según tipo de variable")
tabla(
    ["Tipo de variable", "Variables", "Estadísticos a reportar"],
    [["Dicotómicas",
      "Empleo informal, nivel de ingresos, sexo, estado civil",
      "Frecuencias absolutas y relativas (%)"],
     ["Categóricas",
      "Nivel educativo",
      "Distribución porcentual por categoría"],
     ["Continuas",
      "Edad",
      "Media, mediana, desviación estándar, mínimo y máximo"],
     ["Cruces (bivariado)",
      "Informalidad por cada factor",
      "Tablas de contingencia y prueba ji-cuadrada"]],
    nota="Elaboración propia. Todos los estadísticos se calculan ponderando por el factor "
         "de expansión de la ENAHO.",
    widths=[3.4, 6.0, 5.6], fs=9)
para(
    "El análisis descriptivo cumple una doble función: caracterizar el perfil de la "
    "informalidad laboral en el departamento de Lima y verificar, de manera preliminar, la "
    "plausibilidad de las hipótesis antes de la estimación multivariada. Las pruebas de "
    "asociación bivariada (ji-cuadrada para variables categóricas) permiten contrastar la "
    "independencia entre la informalidad y cada factor socioeconómico.")
para(
    "**b) Análisis inferencial y estimación econométrica.** En una segunda etapa se estiman "
    "los modelos Logit y Probit por máxima verosimilitud, se calculan los efectos "
    "marginales y las razones de momios, y se contrastan las hipótesis a partir de la "
    "significancia estadística de los parámetros (a niveles de 1 %, 5 % y 10 %). Los "
    "resultados de la estimación se presentan en tablas que reportan, para cada variable, "
    "el coeficiente estimado, el error estándar, el estadístico z, el p-valor, el efecto "
    "marginal y la razón de momios, así como los estadísticos globales de ajuste del modelo "
    "(log-verosimilitud, pseudo-R², AIC, BIC y área bajo la curva ROC). Esta presentación "
    "estandarizada facilita la comparación entre las especificaciones Logit y Probit y la "
    "lectura de la magnitud económica de los efectos.")
para(
    "**c) Validación.** En una tercera etapa se aplican las pruebas de bondad de ajuste, de "
    "capacidad predictiva y de diagnóstico descritas en la sección 3.7, con el fin de "
    "garantizar la robustez de los resultados antes de su interpretación económica.")
h3("Procesamiento, software y reproducibilidad")
para(
    "El procesamiento de la información se realiza en un **paquete estadístico "
    "especializado** —Stata o R—, ampliamente utilizado en la investigación econométrica. "
    "En Stata, la estimación de los modelos de elección binaria se efectúa con los comandos "
    "logit y probit, los efectos marginales con margins, las razones de momios con la "
    "opción or y las pruebas de diagnóstico con estat gof, estat classification y "
    "lroc; en R, se emplean las funciones glm de la familia binomial y los paquetes "
    "margins, pROC y ResourceSelection. Dada la naturaleza compleja de la muestra de la "
    "ENAHO, las estimaciones incorporan el diseño muestral mediante la declaración de la "
    "encuesta (svyset en Stata o el paquete survey en R), de modo que los errores "
    "estándar reflejen la estratificación, el conglomerado y los factores de expansión.")
para(
    "Con el fin de garantizar la **reproducibilidad** del estudio, se documentan todos los "
    "pasos de construcción de la base de datos y de estimación en una sintaxis (do-file o "
    "script) ordenada y comentada, que permite replicar los resultados a partir de los "
    "microdatos públicos de la ENAHO. Asimismo, se conservan las versiones de las bases de "
    "datos y de los programas utilizados, en línea con las buenas prácticas de "
    "transparencia y de ciencia abierta.")
para(
    "La interpretación de los resultados se realiza en términos de los **efectos "
    "marginales** sobre la probabilidad de informalidad y de las **razones de momios**, "
    "vinculando los hallazgos empíricos con el marco teórico —las teorías dualista, de la "
    "segmentación del mercado laboral y del capital humano— y con la evidencia previa.",
    after=8)

# ----------------------------------------------------------------------
h1("3.9. Procedimiento de contraste de hipótesis")
para(
    "El contraste de las hipótesis se realiza a partir de la significancia estadística y "
    "del signo de los parámetros estimados, así como de los efectos marginales. Para cada "
    "coeficiente se calcula el estadístico z (cociente entre el coeficiente y su error "
    "estándar) y su p-valor asociado. La regla de decisión general consiste en **rechazar "
    "la hipótesis nula de no efecto** (H0: betaj = 0) cuando el p-valor es inferior al "
    "nivel de significancia establecido (1 %, 5 % o 10 %). La hipótesis de investigación se "
    "confirma cuando, además de ser significativo, el coeficiente presenta el signo "
    "predicho por la teoría.")
h3("Formulación estadística de las hipótesis")
para(
    "Cada hipótesis de investigación se traduce en un par de hipótesis estadísticas. Para "
    "la **hipótesis específica 1** (efecto del nivel de ingresos), se plantea:")
ecuacion("H0: β₁ = 0     vs.     H1: β₁ < 0", "3.14")
para(
    "donde el no rechazo de H0 implicaría ausencia de efecto del ingreso sobre la "
    "informalidad y el rechazo, con β₁ negativo, confirmaría la hipótesis de investigación. "
    "Para la **hipótesis específica 2** (efecto del nivel educativo), se contrasta la "
    "significancia conjunta de los coeficientes de las categorías educativas:")
ecuacion("H0: β₂ⱼ = 0 para todo j     vs.     H1: al menos un β₂ⱼ < 0", "3.15")
para(
    "Para la **hipótesis específica 3** (efecto de los factores demográficos), se evalúa la "
    "significancia conjunta de los parámetros de edad, sexo y estado civil mediante una "
    "prueba de Wald o de razón de verosimilitud:")
ecuacion("H0: β₃ = β₄ = β₅ = β₆ = 0     vs.     H1: al menos uno ≠ 0", "3.16")
para(
    "Finalmente, la **hipótesis general** se contrasta mediante la significancia conjunta "
    "del nivel de ingresos y del nivel educativo, verificando además que el modelo en su "
    "conjunto sea estadísticamente significativo a través de la prueba de razón de "
    "verosimilitud global.")
para(
    "De manera específica, la **hipótesis general** se contrasta verificando la "
    "significancia conjunta del nivel de ingresos y del nivel educativo mediante la prueba "
    "de razón de verosimilitud; la **hipótesis específica 1** se confirma si el coeficiente "
    "del nivel de ingresos es negativo y significativo; la **hipótesis específica 2**, si "
    "los coeficientes del nivel educativo son negativos y significativos; y la **hipótesis "
    "específica 3**, si los coeficientes de la edad, el sexo y el estado civil resultan "
    "estadísticamente significativos, individual o conjuntamente. La Tabla 6 sintetiza las "
    "reglas de decisión.")
tabla_titulo("6", "Reglas de decisión para el contraste de hipótesis")
tabla(
    ["Hipótesis", "Parámetro", "Criterio de confirmación"],
    [["H. general", "Ingreso y educación",
      "Significancia conjunta (LR) y signos negativos"],
     ["H. específica 1", "Nivel de ingresos",
      "Coeficiente negativo y significativo (p < 0,05)"],
     ["H. específica 2", "Nivel educativo",
      "Coeficientes negativos y significativos (p < 0,05)"],
     ["H. específica 3", "Edad, sexo y estado civil",
      "Coeficientes significativos, individual o conjuntamente"]],
    nota="Elaboración propia. Los signos esperados se sustentan en el marco teórico "
         "(capital humano y segmentación del mercado laboral).",
    widths=[3.0, 5.0, 6.0], fs=9)

# ----------------------------------------------------------------------
h1("3.10. Pruebas de robustez")
para(
    "Para asegurar que los resultados no dependen de decisiones de modelado específicas, se "
    "ejecutan diversas **pruebas de robustez**. En primer lugar, se contrasta la "
    "consistencia de los resultados entre las especificaciones Logit y Probit, verificando "
    "que los signos, las magnitudes relativas y los niveles de significancia de los efectos "
    "marginales se mantengan estables. En segundo lugar, se estiman especificaciones "
    "alternativas que incorporan progresivamente las variables de control, a fin de evaluar "
    "la sensibilidad de los coeficientes de interés a la inclusión de covariables.")
para(
    "En tercer lugar, se examina la estabilidad de los resultados ante definiciones "
    "alternativas de la variable dependiente, por ejemplo, la informalidad definida por la "
    "ausencia de seguridad social frente a la definición basada en la ausencia de contrato. "
    "En cuarto lugar, se estiman los modelos para cada año del periodo (2024 y 2025) por "
    "separado, con el objeto de comprobar la persistencia de los efectos a lo largo del "
    "periodo de estudio. La coincidencia de los resultados entre estas especificaciones "
    "reforzaría la validez interna de las conclusiones.")

# ----------------------------------------------------------------------
h1("3.11. Limitaciones metodológicas")
para(
    "La investigación reconoce explícitamente sus limitaciones. En primer lugar, el "
    "**carácter transversal** del diseño impide establecer causalidad en sentido estricto y "
    "captar las transiciones de los trabajadores entre el sector formal e informal; los "
    "efectos estimados deben interpretarse como asociaciones de probabilidad condicional "
    "bajo el supuesto de exogeneidad. En segundo lugar, al emplearse **datos secundarios**, "
    "el estudio se circunscribe a las variables disponibles en la ENAHO, lo que excluye "
    "determinantes potencialmente relevantes, como la calidad de la educación, las redes "
    "sociales o las preferencias individuales, y abre la posibilidad de un sesgo por "
    "variables omitidas.")
para(
    "En tercer lugar, la **operacionalización dicotómica** de algunas variables, como el "
    "nivel de ingresos respecto de la RMV, simplifica fenómenos continuos y puede ocultar "
    "no linealidades. En cuarto lugar, los resultados son **representativos del "
    "departamento de Lima** y del periodo 2024-2025, por lo que su generalización a otros "
    "ámbitos o periodos debe realizarse con cautela. Estas limitaciones no invalidan los "
    "hallazgos, pero delimitan su alcance y orientan futuras investigaciones, idealmente de "
    "carácter longitudinal o con datos de panel.", after=8)

# ----------------------------------------------------------------------
h1("3.12. Matriz de consistencia metodológica")
para(
    "La coherencia entre el problema, los objetivos, las hipótesis, las variables y la "
    "metodología se resume en la matriz de consistencia que se presenta en la Tabla 7.")
tabla_titulo("7", "Matriz de consistencia metodológica (síntesis)")
tabla(
    ["Problema", "Objetivo", "Hipótesis", "Variable", "Modelo"],
    [["¿Cuáles son los factores que determinan la informalidad laboral en Lima, 2024-2025?",
      "Determinar los factores que influyen en la informalidad laboral en Lima, 2024-2025.",
      "Los principales factores son el nivel de ingresos y el nivel educativo.",
      "Dep.: empleo informal", "Logit / Probit"],
     ["¿Cuál es el efecto del nivel de ingresos sobre la informalidad?",
      "Determinar el efecto del nivel de ingresos sobre la informalidad.",
      "El nivel de ingresos tiene un efecto negativo sobre la informalidad.",
      "Indep.: nivel de ingresos", "Logit / Probit"],
     ["¿Cuál es el efecto del nivel educativo sobre la informalidad?",
      "Determinar el efecto del nivel educativo sobre la informalidad.",
      "El nivel educativo tiene un efecto negativo sobre la informalidad.",
      "Indep.: nivel educativo", "Logit / Probit"],
     ["¿Cuál es el efecto de la edad, el género y el estado civil sobre la informalidad?",
      "Establecer el efecto de la edad, el género y el estado civil sobre la informalidad.",
      "La edad, el género y el estado civil influyen en la informalidad.",
      "Control: edad, sexo, estado civil", "Logit / Probit"]],
    nota="Elaboración propia a partir de la matriz de consistencia del proyecto. Todas las "
         "filas comparten el mismo tipo (aplicada, cuantitativa, explicativa), diseño (no "
         "experimental, transversal) y fuente de datos (ENAHO-INEI, 2024-2025).",
    widths=[3.3, 3.3, 3.3, 2.6, 2.1], fs=8.5)

# ----------------------------------------------------------------------
h1("3.13. Consideraciones éticas")
para(
    "La investigación se sujeta a los principios éticos de la investigación científica y a "
    "las normas de integridad académica de la Universidad Nacional Mayor de San Marcos. Al "
    "emplearse exclusivamente **datos secundarios, anonimizados y de acceso público** "
    "provenientes de la ENAHO, se garantiza la **confidencialidad y la protección de la "
    "identidad** de los informantes, pues los microdatos del INEI no permiten identificar a "
    "las personas ni a los hogares encuestados. Asimismo, se respeta la **propiedad "
    "intelectual** mediante la citación rigurosa de todas las fuentes en formato APA, y se "
    "asegura la **transparencia y replicabilidad** del estudio mediante la documentación "
    "detallada de los procedimientos de construcción de la base de datos y de estimación. "
    "La investigación no presenta conflictos de interés ni riesgos para los sujetos, dado "
    "su carácter no experimental y de fuente secundaria.")
para(
    "De manera complementaria, la investigación observa los principios de **integridad y "
    "honestidad científica**: los datos no se manipulan ni se seleccionan de manera "
    "tendenciosa, los resultados se reportan con independencia de que confirmen o refuten "
    "las hipótesis, y se evita toda forma de plagio mediante el reconocimiento explícito de "
    "las fuentes. Se respeta, asimismo, el principio de **beneficencia**, en la medida en "
    "que los hallazgos se orientan a aportar evidencia útil para el diseño de políticas de "
    "formalización laboral que beneficien a los trabajadores informales del departamento de "
    "Lima, y el principio de **justicia**, al analizar un fenómeno que afecta de manera "
    "desproporcionada a los grupos más vulnerables de la población.")
para(
    "Finalmente, el uso de los microdatos de la ENAHO se realiza conforme a las condiciones "
    "de uso establecidas por el INEI para la difusión de información estadística, que "
    "autorizan su empleo con fines académicos y de investigación, siempre que se cite "
    "adecuadamente la fuente y se preserve el carácter anónimo y agregado de la "
    "información.", after=8)

# ----------------------------------------------------------------------
h1("3.14. Síntesis metodológica")
para(
    "En síntesis, la presente investigación adopta un enfoque **cuantitativo**, de tipo "
    "**aplicado** y nivel **explicativo**, con un diseño **no experimental de corte "
    "transversal**. A partir de los microdatos de la ENAHO (INEI) correspondientes a la PEA "
    "ocupada del departamento de Lima en 2024-2025, se estima un **modelo de elección "
    "binaria (Logit, con Probit como prueba de robustez)** que cuantifica el efecto del "
    "nivel de ingresos, el nivel educativo y los factores demográficos —edad, sexo y estado "
    "civil— sobre la probabilidad de informalidad laboral. La interpretación se realiza "
    "mediante efectos marginales y razones de momios, y la validez de las estimaciones se "
    "sustenta en pruebas de bondad de ajuste, capacidad predictiva y diagnóstico "
    "econométrico. Esta estrategia, coherente con la matriz de consistencia del proyecto y "
    "con el antecedente metodológico de referencia (Semestre Económico, 2025), permite "
    "responder de manera rigurosa a las preguntas de investigación y contrastar las "
    "hipótesis planteadas, generando evidencia empírica actualizada y focalizada para el "
    "diseño de políticas de formalización laboral en el departamento de Lima.", after=8)

# ----------------------------------------------------------------------
h1("Referencias", size=13)
for r in [
    "Greene, W. H. (2012). //Econometric analysis// (7.ª ed.). Pearson.",
    "Gujarati, D. N., & Porter, D. C. (2010). //Econometría// (5.ª ed.). McGraw-Hill.",
    "Hernández-Sampieri, R., & Mendoza, C. P. (2018). //Metodología de la investigación: "
    "las rutas cuantitativa, cualitativa y mixta//. McGraw-Hill.",
    "Instituto Nacional de Estadística e Informática. (2025). //Producción y empleo "
    "informal en el Perú: Cuenta Satélite de la Economía Informal 2022-2024//. INEI.",
    "Instituto Nacional de Estadística e Informática. (2025). //Encuesta Nacional de "
    "Hogares sobre Condiciones de Vida y Pobreza (ENAHO): ficha técnica//. INEI.",
    "Maddala, G. S. (1983). //Limited-dependent and qualitative variables in econometrics//. "
    "Cambridge University Press.",
    "Wooldridge, J. M. (2010). //Econometric analysis of cross section and panel data// "
    "(2.ª ed.). MIT Press.",
    "Determinantes de la informalidad laboral: un análisis para el Perú, 2019 y 2022. "
    "(2025). //Semestre Económico//, 14(1). Universidad Nacional del Altiplano. "
    "http://www.scielo.org.pe/scielo.php?script=sci_arttext&pid=S2523-08402025000100006",
]:
    referencia(r)

doc.save(OUT)
print("Guardado:", OUT)
