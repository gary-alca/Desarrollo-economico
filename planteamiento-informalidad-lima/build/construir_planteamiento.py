# -*- coding: utf-8 -*-
"""Ensambla el apartado 1.1 Planteamiento del Problema en formato Word (.docx).

Tesis: "Factores socioeconómicos que influyen en la informalidad laboral en el
departamento de Lima en los años 2024-2025" (Escuela Profesional de Economía,
Universidad Nacional Mayor de San Marcos).

Formato exigido: Times New Roman 12, interlineado 1.5, texto justificado,
márgenes 2.54 cm, figuras insertadas y referencias en APA 7.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(__file__)
IMG = os.path.join(BASE, "img")
OUT = os.path.join(os.path.dirname(BASE), "1.1_Planteamiento_del_Problema_Informalidad_Lima.docx")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRISTXT = RGBColor(0x40, 0x40, 0x40)

doc = Document()

# --- Estilo base: Times New Roman 12, interlineado 1.5, justificado ---
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
rpr = normal.element.get_or_add_rPr()
rfonts = rpr.get_or_add_rFonts()
rfonts.set(qn("w:ascii"), "Times New Roman")
rfonts.set(qn("w:hAnsi"), "Times New Roman")
rfonts.set(qn("w:cs"), "Times New Roman")
pf = normal.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
pf.line_spacing = 1.5
pf.space_after = Pt(0)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Márgenes 2.54 cm (1 pulgada) en todos los lados
for sec in doc.sections:
    sec.top_margin = Cm(2.54)
    sec.bottom_margin = Cm(2.54)
    sec.left_margin = Cm(2.54)
    sec.right_margin = Cm(2.54)


def _font(run, name="Times New Roman"):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    rf.set(qn("w:ascii"), name)
    rf.set(qn("w:hAnsi"), name)
    rf.set(qn("w:cs"), name)


def heading(text, size=14):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = AZUL
    _font(r)
    return p


def subheading(text, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = AZUL
    _font(r)
    return p


def para(text, first_line_indent=True, space_after=6, justify=True):
    """Párrafo con sangría de primera línea (estilo tesis). **negrita** soportada."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(space_after)
    if first_line_indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    parts = text.split("**")
    for i, seg in enumerate(parts):
        r = p.add_run(seg)
        _font(r)
        if i % 2 == 1:
            r.bold = True
    return p


def figura(img_name, numero, titulo, fuente, ficha, interpretacion, width=5.7):
    # Caption: "Figura X" en una línea y el título en la siguiente (APA 7)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    cap.paragraph_format.space_before = Pt(10)
    cap.paragraph_format.space_after = Pt(0)
    r = cap.add_run(f"Figura {numero}")
    r.bold = True
    r.font.size = Pt(11)
    _font(r)
    tit = doc.add_paragraph()
    tit.alignment = WD_ALIGN_PARAGRAPH.LEFT
    tit.paragraph_format.space_after = Pt(4)
    rt = tit.add_run(titulo)
    rt.italic = True
    rt.font.size = Pt(11)
    _font(rt)
    # Imagen centrada
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_before = Pt(2)
    pic.paragraph_format.space_after = Pt(2)
    pic.add_run().add_picture(os.path.join(IMG, img_name), width=Inches(width))
    # Nota / Fuente (APA 7)
    fp = doc.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    fp.paragraph_format.space_after = Pt(2)
    rn = fp.add_run("Nota. ")
    rn.italic = True
    rn.font.size = Pt(10)
    _font(rn)
    rf = fp.add_run(f"Elaboración propia a partir de datos de {fuente}")
    rf.font.size = Pt(10)
    _font(rf)
    # Ficha técnica del gráfico
    fc = doc.add_paragraph()
    fc.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    fc.paragraph_format.space_after = Pt(4)
    rfc = fc.add_run(ficha)
    rfc.font.size = Pt(10)
    rfc.font.color.rgb = GRISTXT
    _font(rfc)
    # Interpretación académica
    para(interpretacion, first_line_indent=True, space_after=8)


def referencia(text):
    """Referencia APA 7 con sangría francesa."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.left_indent = Cm(1.25)
    p.paragraph_format.first_line_indent = Cm(-1.25)
    # cursiva con //...//
    parts = text.split("//")
    for i, seg in enumerate(parts):
        r = p.add_run(seg)
        _font(r)
        if i % 2 == 1:
            r.italic = True
    return p


# ======================================================================
# 1.1 PLANTEAMIENTO DEL PROBLEMA
# ======================================================================
heading("1.1. Planteamiento del problema", size=14)

# ---------------------------------------------------------------
# Contextualización mundial
# ---------------------------------------------------------------
para(
    "La informalidad laboral constituye uno de los rasgos más persistentes y "
    "estructurales del mundo del trabajo contemporáneo y, lejos de ser una anomalía "
    "transitoria de las economías en desarrollo, se ha consolidado como una forma "
    "predominante de organización del empleo a escala global. En términos conceptuales, "
    "el empleo informal comprende el conjunto de relaciones laborales que, total o "
    "parcialmente, escapan a la cobertura efectiva de la legislación laboral y de la "
    "protección social, de modo que los trabajadores carecen de seguridad social, "
    "aportes previsionales, estabilidad contractual y beneficios laborales básicos "
    "(Organización Internacional del Trabajo [OIT], 2024a). El estudio sistemático del "
    "fenómeno se remonta a la noción de «sector informal» acuñada por Hart (1973) a "
    "partir de sus observaciones sobre las oportunidades de ingreso urbano en Ghana, y "
    "desde entonces ha dado lugar a tres grandes lecturas teóricas que aún estructuran "
    "el debate: la perspectiva estructuralista, que entiende la informalidad como "
    "resultado de la insuficiente capacidad de absorción del sector moderno; la "
    "perspectiva legalista o institucionalista, que la atribuye a los costos "
    "regulatorios y tributarios de la formalidad (De Soto, 1986); y la perspectiva "
    "que la concibe, en parte, como una decisión voluntaria de trabajadores y "
    "microempresarios que ponderan costos y beneficios de formalizarse (Maloney, 2004). "
    "Esta diversidad de enfoques anticipa que la informalidad no obedece a una causa "
    "única, sino a una constelación de factores socioeconómicos cuya identificación es "
    "precisamente el objeto de la presente investigación.")

para(
    "La magnitud del fenómeno a escala planetaria es considerable. De acuerdo con la "
    "OIT (2024a), alrededor del 58 % de la población ocupada mundial —cerca de 2.000 "
    "millones de personas— se desempeña en condiciones de informalidad, proporción que "
    "se ha mantenido relativamente estable en las últimas dos décadas pese al "
    "crecimiento económico global. Sin embargo, este promedio agregado oculta una "
    "marcada heterogeneidad asociada al nivel de desarrollo de los países: mientras que "
    "en las economías de ingreso alto la informalidad afecta a apenas el 13 % de los "
    "ocupados, en las economías de ingreso bajo alcanza cerca del 88 % de la fuerza de "
    "trabajo (OIT, 2024a). Esta relación inversa entre informalidad y nivel de ingreso "
    "constituye uno de los hechos estilizados más robustos de la economía del "
    "desarrollo y sugiere que la informalidad es, simultáneamente, causa y "
    "manifestación del subdesarrollo (La Porta y Shleifer, 2014). La Figura 1 ilustra "
    "esta gradiente con datos de la OIT para 2024.")

figura(
    "fig1_mundo_ingreso.png", "1",
    "Tasa de empleo informal en el mundo según nivel de ingreso de los países, 2024",
    "la Organización Internacional del Trabajo (OIT, 2024a).",
    "Tipo de gráfico: barras verticales. Variable: tasa de empleo informal "
    "(% de la población ocupada). Justificación: el gráfico de barras es idóneo para "
    "comparar la magnitud de una misma variable entre categorías discretas y "
    "mutuamente excluyentes, lo que evidencia con claridad la gradiente de ingreso.",
    "La figura compara la tasa de empleo informal entre los países de ingreso bajo, el "
    "promedio mundial y los países de ingreso alto en 2024. El contraste es elocuente: "
    "la informalidad afecta a cerca del 88 % de los ocupados en las economías más "
    "pobres, frente a apenas el 13 % en las de mayor ingreso, una brecha de 75 puntos "
    "porcentuales. El promedio mundial (58 %) se ubica mucho más cerca del extremo "
    "superior, lo que revela que la mayoría de la fuerza de trabajo del planeta reside "
    "en economías de ingreso bajo y medio donde la informalidad es la norma. Desde la "
    "teoría del desarrollo, este patrón respalda la hipótesis de que la informalidad "
    "expresa la baja productividad agregada y la débil capacidad institucional de las "
    "economías en desarrollo, antes que una mera evasión regulatoria (La Porta y "
    "Shleifer, 2014; Ulyssea, 2020). La implicancia económica es directa: reducir la "
    "informalidad no se logra solo con fiscalización, sino elevando la productividad y "
    "la calidad del entramado empresarial. Para la presente investigación, la figura "
    "sitúa al Perú —economía de ingreso medio-alto con informalidad cercana al 71 %— "
    "en una posición anómala respecto de su nivel de ingreso, lo que vuelve "
    "imprescindible indagar los factores socioeconómicos que sostienen esa brecha.")

# ---------------------------------------------------------------
# América Latina
# ---------------------------------------------------------------
para(
    "En América Latina y el Caribe, la informalidad constituye un rasgo estructural del "
    "mercado de trabajo y un determinante central de la desigualdad regional. Hacia "
    "2024, alrededor del 47,6 % de la población ocupada de la región se encontraba en "
    "empleo informal (OIT, 2024b), proporción que, aunque inferior al promedio mundial, "
    "convive con niveles muy elevados de heterogeneidad estructural: la mayor parte de "
    "los nuevos empleos creados en el último ciclo de crecimiento han sido informales, "
    "y la informalidad se concentra en los hogares de menores ingresos, perpetuando "
    "trampas de pobreza y vulnerabilidad (Comisión Económica para América Latina y el "
    "Caribe [CEPAL], 2023). La evidencia regional muestra de manera consistente que la "
    "probabilidad de ser informal aumenta con el menor nivel educativo, en las mujeres "
    "—especialmente cuando existen dependientes en el hogar—, en los jóvenes y los "
    "adultos mayores, en las zonas rurales y entre los trabajadores de microempresas "
    "(CEPAL, 2023). La Figura 2 presenta la posición comparada de los principales "
    "países de la región.")

figura(
    "fig2_america_latina.png", "2",
    "Tasa de informalidad laboral en países de América Latina, 2024",
    "la Organización Internacional del Trabajo (OIT, 2024b).",
    "Tipo de gráfico: barras horizontales ordenadas. Variable: tasa de informalidad "
    "laboral (% de la población ocupada). Justificación: las barras horizontales "
    "ordenadas facilitan la lectura de un ordenamiento (ranking) entre países y la "
    "comparación de cada caso con el promedio regional señalado por la línea de "
    "referencia.",
    "La figura ordena a ocho países latinoamericanos según su tasa de informalidad "
    "laboral en 2024 y los contrasta con el promedio regional (47,6 %). Se observa una "
    "amplia dispersión: en un extremo, Bolivia (80,0 %) y el Perú (73,6 %) registran "
    "las mayores tasas, muy por encima del promedio; en el otro, Chile (25,8 %) y "
    "Uruguay (22,0 %) exhiben niveles propios de economías más formalizadas. El Perú "
    "aparece como el segundo país más informal de la muestra, lo que confirma la "
    "gravedad relativa del fenómeno en el contexto nacional. La heterogeneidad "
    "observada se asocia a diferencias en la estructura productiva, la institucionalidad "
    "laboral y los niveles de productividad de cada país (CEPAL, 2023; Maloney, 2004). "
    "Cabe precisar que las cifras comparativas de la OIT pueden diferir de las "
    "estimaciones nacionales por diferencias metodológicas; el Instituto Nacional de "
    "Estadística e Informática reporta para el Perú una tasa de 70,9 % en 2024 (INEI, "
    "2025). En cualquier caso, la posición del país entre los más informales de la "
    "región otorga relevancia y urgencia al estudio de sus determinantes "
    "socioeconómicos, particularmente en su principal mercado laboral, el departamento "
    "de Lima.")

# ---------------------------------------------------------------
# Perú
# ---------------------------------------------------------------
para(
    "En el Perú, la informalidad laboral representa el desafío estructural más "
    "persistente del mercado de trabajo. Según el INEI (2025), en 2024 el 70,9 % de la "
    "población económicamente activa ocupada se desempeñaba en un empleo informal; de "
    "este total, el 55,7 % correspondía a empleo informal dentro del sector informal y "
    "el 15,2 % a empleo informal fuera de él, mientras que solo el 29,1 % accedía a un "
    "empleo formal. En otras palabras, siete de cada diez trabajadores peruanos laboran "
    "sin acceso a seguridad social, gratificaciones, compensación por tiempo de "
    "servicios ni aportes previsionales. Más aún, la trayectoria histórica del "
    "indicador revela una notable rigidez estructural: la informalidad descendió solo "
    "marginalmente entre 2011 y 2019, se elevó abruptamente durante la pandemia de "
    "COVID-19 y, pese a la recuperación posterior, se mantiene en niveles incompatibles "
    "con el nivel de ingreso del país. La Figura 3 documenta esta evolución.")

figura(
    "fig3_evolucion_peru.png", "3",
    "Evolución de la tasa de empleo informal en el Perú, 2011-2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025) y el Centro "
    "Nacional de Planeamiento Estratégico (CEPLAN, 2024).",
    "Tipo de gráfico: serie de tiempo (líneas). Variable: tasa de empleo informal "
    "(% de la PEA ocupada). Justificación: el gráfico de líneas es el más adecuado "
    "para representar la evolución de una variable continua a lo largo del tiempo y "
    "permite visualizar tendencias, puntos de inflexión y el quiebre metodológico de "
    "la fuente.",
    "La figura traza la tasa de empleo informal del Perú entre 2011 y 2024. Tras un "
    "descenso lento y modesto —de 75,1 % en 2011 a 72,7 % en 2019—, la pandemia de "
    "COVID-19 provocó un repunte abrupto que llevó el indicador a 75,3 % en 2020 y a "
    "76,8 % en 2021, evidenciando la extrema fragilidad de las condiciones laborales de "
    "la mayoría de los trabajadores. A partir de 2022 se observa una contracción hasta "
    "el 70,9 % de 2024; no obstante, parte de esta caída coincide con el cambio de "
    "fuente estadística (de la ENAHO a la Encuesta Permanente de Empleo Nacional), por "
    "lo que la comparación intertemporal debe interpretarse con cautela. La lectura de "
    "fondo es la persistencia estructural: en catorce años, la informalidad apenas se "
    "redujo en torno a cuatro puntos porcentuales y nunca descendió del 70 %. Esta "
    "inercia confirma que el fenómeno no responde a fluctuaciones cíclicas sino a "
    "determinantes profundos de la estructura productiva y del capital humano "
    "(Chacaltana, 2016; Loayza, 2008). La meta nacional de reducir la informalidad al "
    "60 % hacia 2030 (CEPLAN, 2024) luce, a la luz de esta trayectoria, difícil de "
    "alcanzar sin intervenciones focalizadas, lo que justifica investigar con precisión "
    "los factores que la sostienen.")

para(
    "La persistencia de la informalidad en el Perú se encuentra estrechamente vinculada "
    "a las características de su estructura productiva. Chacaltana (2016) sostiene que la "
    "informalidad responde, en gran medida, a la escasez de empleo formal generada por "
    "una economía orientada a la explotación de recursos naturales y a actividades de "
    "baja productividad, con limitada capacidad de absorción de mano de obra "
    "calificada. En la misma línea, Loayza (2008) subraya que la informalidad combina "
    "una baja productividad de las unidades económicas con débiles capacidades estatales "
    "de fiscalización y un marco regulatorio costoso, de modo que amplios segmentos de "
    "la fuerza laboral quedan atrapados en empleos de subsistencia. Esta naturaleza "
    "estructural se manifiesta con nitidez en la dimensión sectorial del fenómeno, como "
    "muestra la Figura 4.")

figura(
    "fig4_sector.png", "4",
    "Tasa de empleo informal en el Perú según rama de actividad económica, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras verticales. Variable: tasa de empleo informal "
    "(% de la población ocupada) por rama de actividad. Justificación: el gráfico de "
    "barras permite comparar la incidencia de la informalidad entre sectores "
    "económicos y contrastarla con el promedio nacional (línea de referencia).",
    "La figura ordena la tasa de empleo informal por rama de actividad económica en "
    "2024. El sector primario —agricultura, pesca y minería— concentra la mayor "
    "informalidad (91,5 %), seguido por la construcción (76,9 %) y el comercio "
    "(71,6 %), mientras que la manufactura (63,6 %) y los servicios (59,0 %) registran "
    "los niveles más bajos, aunque todavía elevados. Esta jerarquía sectorial refleja "
    "la segmentación estructural del mercado laboral peruano y la coexistencia de "
    "economías modernas y tradicionales dentro de un mismo territorio: las actividades "
    "intensivas en capital y con mayor productividad tienden a la formalización, "
    "mientras que aquellas de baja productividad y pequeña escala reproducen la "
    "informalidad (La Porta y Shleifer, 2014). La implicancia económica es relevante "
    "para el estudio de Lima, cuya estructura productiva está dominada por el comercio "
    "y los servicios; aun en las ramas comparativamente más formalizadas, la "
    "informalidad supera el 59 %, lo que anticipa que en la capital el fenómeno no se "
    "explica únicamente por la composición sectorial, sino también por las "
    "características socioeconómicas de los trabajadores. La figura sustenta así la "
    "necesidad de un análisis a nivel individual de los determinantes de la "
    "informalidad.")

para(
    "Las consecuencias de la informalidad laboral son múltiples y se proyectan tanto "
    "sobre los trabajadores como sobre el conjunto de la economía. En el plano "
    "individual, los trabajadores informales carecen de protección social, enfrentan "
    "mayor inestabilidad de ingresos, disponen de escasas oportunidades de capacitación "
    "y crecimiento profesional, y encuentran dificultades para acceder al crédito "
    "formal. En el plano agregado, la informalidad erosiona la base tributaria del "
    "Estado, limita la cobertura de la seguridad social y deprime la productividad "
    "promedio de la economía, pues las unidades informales permanecen pequeñas, "
    "descapitalizadas e incapaces de aprovechar economías de escala (Loayza, 2008; "
    "Perry et al., 2007; Ulyssea, 2020). La evidencia comparada es ilustrativa: en "
    "economías de mayor formalidad, como Chile, la productividad media por trabajador "
    "duplica la peruana, en parte porque la formalidad facilita el acceso a "
    "financiamiento, tecnología y capacitación. La informalidad constituye, por tanto, "
    "no solo un problema de derechos laborales, sino un freno estructural al desarrollo "
    "económico nacional.")

# ---------------------------------------------------------------
# Factores socioeconómicos
# ---------------------------------------------------------------
subheading("Principales factores socioeconómicos asociados a la informalidad laboral")

para(
    "Más allá de los condicionantes estructurales y sectoriales, la literatura "
    "económica ha identificado un conjunto de factores socioeconómicos de orden "
    "individual que determinan la probabilidad de que un trabajador se inserte en el "
    "empleo informal. Entre ellos destacan el nivel educativo, el nivel de ingresos, el "
    "tamaño de la unidad productiva y las características demográficas —edad, sexo y "
    "estado civil— (CEPAL, 2023; Tenorio, 2020). El primero y más robusto de estos "
    "determinantes es la educación. Desde la teoría del capital humano, la inversión en "
    "educación incrementa la productividad de los individuos y, con ella, su acceso a "
    "empleos formales mejor remunerados (Becker, 1964); de manera complementaria, la "
    "teoría de la segmentación sostiene que las barreras de capital humano impiden el "
    "libre tránsito entre el sector informal y el formal, de modo que quienes poseen "
    "menor escolaridad tienden a permanecer atrapados en empleos informales. La Figura "
    "5 evidencia con claridad este gradiente educativo en el Perú.")

figura(
    "fig5_educativo.png", "5",
    "Tasa de empleo informal en el Perú según nivel educativo alcanzado, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras verticales. Variable: tasa de empleo informal "
    "(% de la población ocupada) según nivel educativo. Justificación: el gráfico de "
    "barras hace visible la relación monotónica decreciente entre escolaridad e "
    "informalidad, central para la hipótesis del estudio.",
    "La figura muestra que la informalidad laboral disminuye de manera marcada y "
    "monotónica conforme aumenta el nivel educativo. Entre los trabajadores que solo "
    "alcanzaron educación primaria o menos, la informalidad llega al 94,6 %; desciende "
    "al 81,2 % entre quienes completaron la secundaria y se reduce al 37,9 % entre "
    "quienes cuentan con educación superior universitaria, una brecha de casi 57 puntos "
    "porcentuales entre los extremos. Este patrón constituye evidencia empírica directa "
    "de la teoría del capital humano (Becker, 1964): la educación opera como el "
    "principal mecanismo de acceso al empleo formal, al elevar la productividad del "
    "trabajador y su atractivo para empresas formales, fiscalizadas y más productivas. "
    "No obstante, el hecho de que casi cuatro de cada diez profesionales universitarios "
    "permanezcan en la informalidad advierte que la credencial educativa, por sí sola, "
    "no garantiza la formalización, y que operan factores adicionales —demográficos, "
    "sectoriales e institucionales—. Para la presente investigación, centrada en el "
    "departamento de Lima, donde se concentra la mayor oferta de educación superior del "
    "país, el nivel educativo se postula como una de las variables explicativas "
    "centrales del modelo, con un efecto esperado negativo sobre la probabilidad de "
    "informalidad.")

para(
    "Estrechamente ligados al nivel educativo se encuentran el nivel de ingresos y el "
    "tamaño de la empresa, dimensiones que reflejan la segmentación del aparato "
    "productivo. Las unidades de menor tamaño, típicamente microempresas y "
    "autoempleos, carecen del capital y la escala necesarios para asumir los costos de "
    "la formalización y para ofrecer remuneraciones competitivas, de modo que "
    "concentran la mayor parte del empleo informal y de los bajos ingresos (Ulyssea, "
    "2020). La Figura 6 cuantifica esta relación para el caso peruano.")

figura(
    "fig6_tamano_empresa.png", "6",
    "Tasa de empleo informal en el Perú según tamaño de empresa, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras verticales. Variable: tasa de empleo informal "
    "(% de la población ocupada) según tamaño del establecimiento. Justificación: el "
    "gráfico de barras evidencia el fuerte contraste de informalidad entre pequeñas y "
    "grandes empresas, vinculado al nivel de ingresos.",
    "La figura contrasta la informalidad laboral según el tamaño de la empresa en 2024. "
    "En las pequeñas empresas de 1 a 10 trabajadores —donde predominan los bajos "
    "ingresos y la escasa capitalización— la informalidad alcanza el 88,6 %, mientras "
    "que en las grandes empresas de 51 o más trabajadores desciende al 15,6 %, una "
    "brecha de 73 puntos porcentuales respecto del promedio nacional de 70,9 %. Esta "
    "asociación revela que el tamaño de la unidad productiva, y el nivel de ingresos "
    "que de él se deriva, constituyen determinantes de primer orden de la "
    "informalidad: las grandes empresas disponen de capital, productividad y capacidad "
    "administrativa para cumplir con las obligaciones laborales y tributarias, en tanto "
    "que las microempresas operan en los márgenes de la subsistencia (La Porta y "
    "Shleifer, 2014; Ulyssea, 2020). La implicancia para el estudio es doble. Por un "
    "lado, sustenta la inclusión del nivel de ingresos como variable explicativa "
    "central, con efecto negativo esperado sobre la informalidad. Por otro, advierte "
    "que en el departamento de Lima —donde se concentra el grueso de la microempresa "
    "nacional— la estructura empresarial de baja escala constituye un canal relevante "
    "de reproducción de la informalidad, que el análisis econométrico deberá considerar.")

para(
    "Las características demográficas configuran un tercer bloque de determinantes "
    "socioeconómicos. La edad presenta una relación no lineal con la informalidad: es "
    "máxima entre los jóvenes que recién ingresan al mercado de trabajo, disminuye en "
    "las edades centrales de mayor experiencia y vuelve a elevarse entre los adultos "
    "mayores, configurando un perfil en forma de «U» (CEPAL, 2023). La Figura 7 "
    "documenta este patrón etario para el Perú.")

figura(
    "fig7_edad.png", "7",
    "Tasa de empleo informal en el Perú según grupos de edad, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras verticales. Variable: tasa de empleo informal "
    "(% de la población ocupada) por grupo de edad. Justificación: el gráfico de "
    "barras permite apreciar el perfil no lineal (en forma de U) de la informalidad a "
    "lo largo del ciclo de vida laboral.",
    "La figura revela que la informalidad laboral varía de manera no lineal a lo largo "
    "del ciclo de vida. El grupo de 14 a 24 años presenta la tasa más alta (85,4 %), "
    "muy por encima del promedio nacional, lo que refleja las dificultades de los "
    "jóvenes para acceder a un primer empleo formal en ausencia de experiencia y "
    "credenciales consolidadas. La informalidad desciende a su mínimo entre los 25 y 44 "
    "años (67,1 %), etapa de mayor acumulación de capital humano y experiencia, y "
    "vuelve a elevarse a 71,2 % entre los trabajadores de 45 y más años, en parte por "
    "la salida del empleo asalariado formal hacia el autoempleo. Este perfil en «U» es "
    "consistente con la evidencia latinoamericana (CEPAL, 2023) y confirma que la edad "
    "constituye un determinante demográfico relevante de la informalidad. Para la "
    "investigación, la elevada informalidad juvenil resulta especialmente significativa "
    "en el departamento de Lima, donde reside la mayor concentración de población joven "
    "y de instituciones de educación superior del país; comprender por qué los jóvenes "
    "limeños, pese a su mayor escolaridad relativa, enfrentan tasas tan altas de "
    "informalidad es uno de los interrogantes que motivan el estudio de los factores "
    "demográficos junto con el nivel educativo y el ingreso.")

para(
    "Finalmente, el sexo y el área de residencia completan el cuadro de determinantes. "
    "Las mujeres registran sistemáticamente mayores tasas de informalidad que los "
    "hombres, brecha que la literatura atribuye a la segregación ocupacional, a la "
    "carga desproporcionada del trabajo de cuidado no remunerado y a su mayor "
    "concentración en actividades de baja productividad (CEPAL, 2023). A su vez, la "
    "informalidad es notablemente más alta en el ámbito rural que en el urbano, lo que "
    "introduce una dimensión territorial decisiva para comprender las diferencias entre "
    "regiones. La Figura 8 cuantifica ambas brechas.")

figura(
    "fig8_sexo_area.png", "8",
    "Tasa de empleo informal en el Perú según sexo y área de residencia, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras verticales en dos paneles. Variables: tasa de empleo "
    "informal (% de la población ocupada) según sexo y según área de residencia. "
    "Justificación: la presentación en paneles permite comparar simultáneamente dos "
    "brechas —de género y territorial— sin mezclar categorías heterogéneas.",
    "La figura presenta dos brechas relevantes de la informalidad laboral en 2024. En "
    "el panel de sexo, las mujeres ocupadas registran una tasa de informalidad de "
    "73,1 %, frente al 68,8 % de los hombres, una diferencia de 4,3 puntos "
    "porcentuales que evidencia la mayor vulnerabilidad laboral femenina, asociada a la "
    "segregación ocupacional y a la carga del trabajo de cuidado (CEPAL, 2023). En el "
    "panel territorial, la brecha es mucho más pronunciada: la informalidad alcanza el "
    "94,6 % en el área rural frente al 65,1 % en el área urbana, una diferencia de 29,5 "
    "puntos que refleja el limitado acceso a empleo formal en amplias zonas del país. "
    "Esta dimensión territorial es crucial para la presente investigación, pues "
    "explica buena parte de las diferencias entre regiones y posiciona al departamento "
    "de Lima —predominantemente urbano— en el extremo de menor informalidad relativa. "
    "Al mismo tiempo, el hallazgo de que el sexo mantiene un efecto diferenciado aun en "
    "contextos urbanos justifica su inclusión como variable demográfica del modelo, "
    "junto con la edad y el estado civil, para analizar los determinantes de la "
    "informalidad en la capital.")

# ---------------------------------------------------------------
# Situación específica del departamento de Lima
# ---------------------------------------------------------------
subheading("La informalidad laboral en el departamento de Lima")

para(
    "El departamento de Lima constituye el principal mercado laboral del Perú y, por su "
    "peso demográfico y económico, un caso de estudio de especial relevancia. Concentra "
    "alrededor de un tercio de la población nacional y aporta cerca de la mitad del "
    "producto bruto interno del país, además de albergar la mayor densidad de empresas "
    "formales, instituciones de educación superior y servicios modernos. Coherentemente "
    "con su carácter urbano y su estructura productiva diversificada, Lima exhibe una "
    "de las tasas de informalidad más bajas del país: en Lima Metropolitana la "
    "informalidad bordea el 54,8 %, muy por debajo del promedio nacional de 70,9 % y de "
    "ciudades como Juliaca (82,5 %) o Pucallpa (73,0 %) (INEI, 2025). La Figura 9 sitúa "
    "a Lima en el contexto interregional.")

figura(
    "fig9_lima_ciudades.png", "9",
    "Informalidad laboral de Lima frente a las principales ciudades del Perú, 2024",
    "el Instituto Nacional de Estadística e Informática (INEI, 2025).",
    "Tipo de gráfico: barras horizontales ordenadas con caso de interés resaltado. "
    "Variable: tasa de empleo informal (% de la población ocupada) por ciudad. "
    "Justificación: las barras horizontales ordenadas permiten ubicar a Lima dentro "
    "del ranking nacional y dimensionar su distancia respecto del promedio y de las "
    "ciudades más informales.",
    "La figura compara la informalidad laboral de Lima Metropolitana con la de las "
    "ciudades de mayor informalidad del país y con el promedio nacional en 2024. Lima "
    "registra la tasa más baja del conjunto (54,8 %), unos 16 puntos porcentuales por "
    "debajo del promedio nacional (70,9 %) y casi 28 puntos por debajo de Juliaca "
    "(82,5 %), la ciudad más informal. Esta posición relativa favorable se explica por "
    "el carácter urbano de la capital, su mayor productividad, su elevada dotación de "
    "capital humano y la concentración de la actividad empresarial formal. Sin embargo, "
    "esta lectura agregada encierra una paradoja de enorme relevancia para la "
    "investigación: aun siendo la región con menor tasa relativa, el departamento de "
    "Lima alberga el mayor volumen absoluto de trabajadores informales del país, dado "
    "que concentra a la tercera parte de la población ocupada nacional. Es decir, detrás "
    "de la tasa más baja se oculta el mayor número de personas en condición de "
    "informalidad. A ello se suma que, según el INEI (2025), Lima y Callao figuraron "
    "entre las ciudades donde la informalidad aumentó respecto de 2023, lo que sugiere "
    "un posible estancamiento o reversión del proceso de formalización en la capital. "
    "Estos elementos vuelven imperativo analizar los factores que la sostienen.")

para(
    "La aparente ventaja de Lima encierra, además, una considerable heterogeneidad "
    "interna. El departamento comprende tanto la metrópoli —con su mercado laboral "
    "moderno— como las provincias de Lima, de carácter más rural y agrario, donde la "
    "informalidad alcanza niveles muy superiores. Esta dualidad interna implica que el "
    "promedio departamental enmascara realidades laborales profundamente desiguales, "
    "que solo un análisis de los determinantes socioeconómicos a nivel individual puede "
    "desentrañar. Comprender por qué, dentro de un mismo territorio dotado de las "
    "mejores condiciones relativas del país, una proporción mayoritaria de trabajadores "
    "permanece en la informalidad constituye precisamente el problema que esta "
    "investigación busca abordar.")

# ---------------------------------------------------------------
# Vacíos de conocimiento
# ---------------------------------------------------------------
subheading("Vacíos de conocimiento en la literatura")

para(
    "La revisión de la literatura revela vacíos de conocimiento que justifican la "
    "presente investigación. En primer lugar, buena parte de los estudios empíricos "
    "sobre los determinantes de la informalidad laboral en el Perú se concentra en "
    "periodos previos a la pandemia o emplea datos hasta 2019 (Tello, 2014; Tenorio, "
    "2020), de modo que no capturan las transformaciones estructurales del mercado de "
    "trabajo posteriores a la crisis del COVID-19 ni la nueva configuración de "
    "factores socioeconómicos en el periodo de normalización 2024-2025. En segundo "
    "lugar, la mayoría de las investigaciones nacionales aborda la informalidad a "
    "escala agregada o se focaliza en otras regiones y ciudades del país, mientras que "
    "son escasos los estudios que analizan específicamente el departamento de Lima "
    "—pese a su peso económico y demográfico determinante— con la información más "
    "reciente de la Encuesta Permanente de Empleo Nacional. En tercer lugar, una parte "
    "de la literatura previa privilegia el enfoque empresarial (formalización de las "
    "MYPE) por sobre el enfoque del trabajador, dejando insuficientemente explorada la "
    "interacción simultánea entre nivel de ingresos, nivel educativo y características "
    "demográficas —edad, sexo y estado civil— en la determinación de la probabilidad "
    "individual de informalidad. La presente investigación busca cubrir estos vacíos al "
    "estimar, con datos actualizados y a nivel del departamento de Lima, el efecto de "
    "dichos factores sobre la informalidad laboral durante 2024-2025.")

# ---------------------------------------------------------------
# Importancia económica y social
# ---------------------------------------------------------------
subheading("Importancia económica y social del problema")

para(
    "La relevancia de estudiar los factores socioeconómicos de la informalidad laboral "
    "en Lima trasciende lo académico y se proyecta sobre el bienestar de la población y "
    "la sostenibilidad del desarrollo. En el plano social, la informalidad priva a "
    "millones de trabajadores limeños de protección frente a la enfermedad, la vejez y "
    "el desempleo, los expone a la volatilidad de ingresos y reproduce ciclos "
    "intergeneracionales de pobreza y vulnerabilidad (Perry et al., 2007; CEPAL, 2023). "
    "En el plano económico, la informalidad deprime la productividad agregada, restringe "
    "la recaudación tributaria necesaria para financiar bienes públicos —educación, "
    "salud, infraestructura— y limita la profundización financiera, en la medida en que "
    "las unidades informales permanecen excluidas del crédito formal (Loayza, 2008; "
    "Ulyssea, 2020). Dado que Lima concentra la mayor parte de la actividad económica "
    "nacional, las mejoras en la formalización de su mercado laboral tendrían efectos "
    "amplificados sobre el crecimiento, la equidad y las finanzas públicas del conjunto "
    "del país. Identificar con precisión los factores que determinan la informalidad es, "
    "por tanto, un insumo indispensable para el diseño de políticas públicas eficaces y "
    "focalizadas.")

# ---------------------------------------------------------------
# Justificación de estudiar Lima 2024-2025
# ---------------------------------------------------------------
subheading("Pertinencia de estudiar el departamento de Lima durante 2024-2025")

para(
    "La elección del departamento de Lima y del periodo 2024-2025 obedece a razones "
    "científicas y de oportunidad analítica. Primero, Lima constituye el mercado "
    "laboral más grande, diverso y económicamente determinante del país, lo que lo "
    "convierte en un escenario privilegiado para examinar los determinantes de la "
    "informalidad en un contexto urbano y moderno, donde el fenómeno no puede atribuirse "
    "principalmente a la ruralidad o al rezago productivo, sino a factores "
    "socioeconómicos individuales. Segundo, el periodo 2024-2025 corresponde a la fase "
    "de normalización posterior a la pandemia, una coyuntura en la que el mercado "
    "laboral ha recuperado su dinámica pero la informalidad se mantiene en niveles "
    "elevados e incluso ha repuntado en la capital (INEI, 2025), lo que plantea "
    "interrogantes urgentes sobre la persistencia del fenómeno. Tercero, este periodo "
    "ofrece, por primera vez de manera consolidada, la información de la Encuesta "
    "Permanente de Empleo Nacional, que permite un análisis más preciso y actualizado "
    "de los factores socioeconómicos. Finalmente, el estudio resulta pertinente en el "
    "marco de la meta nacional de reducir la informalidad al 60 % hacia 2030 (CEPLAN, "
    "2024): generar evidencia empírica reciente y focalizada sobre Lima contribuye "
    "directamente a orientar las políticas necesarias para alcanzar dicho objetivo.")

# ---------------------------------------------------------------
# Cierre conduciendo a la formulación
# ---------------------------------------------------------------
para(
    "En síntesis, la informalidad laboral es un fenómeno estructural, global y "
    "persistente que en el Perú adquiere una magnitud particularmente elevada para su "
    "nivel de ingreso, y que en el departamento de Lima —pese a presentar las tasas "
    "relativas más bajas del país— afecta a la mayoría de los trabajadores y al mayor "
    "volumen absoluto de población ocupada del territorio nacional. La evidencia "
    "revisada muestra que esta informalidad se asocia de manera robusta con un conjunto "
    "de factores socioeconómicos —el nivel de ingresos, el nivel educativo y las "
    "características demográficas como la edad, el sexo y el estado civil—, cuya "
    "incidencia conjunta y actualizada en el contexto limeño de 2024-2025 no ha sido "
    "suficientemente investigada. Comprender la magnitud y la dirección del efecto de "
    "estos factores resulta indispensable para diseñar políticas públicas orientadas a "
    "reducir la informalidad y a construir un mercado laboral más inclusivo y "
    "productivo. A partir de esta problemática, la presente investigación se propone "
    "responder a la siguiente interrogante de investigación, que da lugar a la "
    "formulación del problema.")

# ======================================================================
# REFERENCIAS
# ======================================================================
heading("Referencias", size=13)

refs = [
    "Becker, G. S. (1964). //Human capital: A theoretical and empirical analysis, with "
    "special reference to education//. Columbia University Press.",

    "Centro Nacional de Planeamiento Estratégico. (2024). //Persistencia de la "
    "informalidad laboral y del empleo vulnerable//. Observatorio Nacional de "
    "Prospectiva. https://observatorio.ceplan.gob.pe/ficha/t29",

    "Chacaltana, J. (2016). Perú, 2002-2012: crecimiento, cambio estructural y "
    "formalización. //Revista CEPAL//, (119), 47-68.",

    "Comisión Económica para América Latina y el Caribe. (2023). //Informalidad laboral "
    "en América Latina: propuesta metodológica para su identificación a nivel "
    "subnacional//. CEPAL.",

    "De Soto, H. (1986). //El otro sendero: la revolución informal//. Editorial El "
    "Barranco.",

    "Hart, K. (1973). Informal income opportunities and urban employment in Ghana. "
    "//The Journal of Modern African Studies//, 11(1), 61-89. "
    "https://doi.org/10.1017/S0022278X00008089",

    "Instituto Nacional de Estadística e Informática. (2025). //Producción y empleo "
    "informal en el Perú: Cuenta Satélite de la Economía Informal 2022-2024//. INEI.",

    "La Porta, R., & Shleifer, A. (2014). Informality and development. //Journal of "
    "Economic Perspectives//, 28(3), 109-126. https://doi.org/10.1257/jep.28.3.109",

    "Loayza, N. (2008). Causas y consecuencias de la informalidad en el Perú. //Revista "
    "Estudios Económicos//, (15), 43-64. Banco Central de Reserva del Perú.",

    "Maloney, W. F. (2004). Informality revisited. //World Development//, 32(7), "
    "1159-1178. https://doi.org/10.1016/j.worlddev.2004.01.008",

    "Organización Internacional del Trabajo. (2024a). //Perspectivas sociales y del "
    "empleo en el mundo: Tendencias 2024//. OIT.",

    "Organización Internacional del Trabajo. (2024b). //Panorama Laboral 2024 de "
    "América Latina y el Caribe//. OIT.",

    "Perry, G. E., Maloney, W. F., Arias, O. S., Fajnzylber, P., Mason, A. D., & "
    "Saavedra-Chanduvi, J. (2007). //Informality: Exit and exclusion//. Banco Mundial. "
    "https://doi.org/10.1596/978-0-8213-7092-6",

    "Sandoval Betancour, G. (2014). La informalidad laboral: causas generales. "
    "//Equidad y Desarrollo//, (22), 9-45.",

    "Tello, M. D. (2014). //¿Es la informalidad laboral una decisión voluntaria en el "
    "Perú?// Consorcio de Investigación Económica y Social.",

    "Tenorio, D. (2020). El empleo informal en el Perú: una breve caracterización "
    "2007-2018. //Pensamiento Crítico//, 25(1), 51-75. "
    "https://doi.org/10.15381/pc.v25i1.18477",

    "Ulyssea, G. (2020). Informality: Causes and consequences for development. //Annual "
    "Review of Economics//, 12, 525-546. "
    "https://doi.org/10.1146/annurev-economics-082119-121914",
]
for r in refs:
    referencia(r)

doc.save(OUT)
print("Documento guardado en:", OUT)
