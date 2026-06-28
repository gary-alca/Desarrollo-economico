# -*- coding: utf-8 -*-
"""Apartado 1.1 Planteamiento del Problema (~6 páginas) en Word (.docx).

Versión con GRÁFICOS OFICIALES tomados tal cual de fuentes oficiales (ILOSTAT/OIT
e INEI). Las figuras NO son de elaboración propia: se reproducen directamente de
las publicaciones oficiales (las mismas que ya obran en el proyecto de tesis).

Formato: Times New Roman 12, interlineado 1.5, texto justificado, márgenes 2.54 cm.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn

BASE = os.path.dirname(__file__)
IMG = os.path.join(os.path.dirname(BASE), "oficial_img")
OUT = os.path.join(os.path.dirname(BASE),
                   "1.1_Planteamiento_del_Problema_6pag_graficos_oficiales.docx")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRISTXT = RGBColor(0x40, 0x40, 0x40)

doc = Document()

normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
rpr = normal.element.get_or_add_rPr()
rf = rpr.get_or_add_rFonts()
rf.set(qn("w:ascii"), "Times New Roman")
rf.set(qn("w:hAnsi"), "Times New Roman")
rf.set(qn("w:cs"), "Times New Roman")
pf = normal.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
pf.line_spacing = 1.5
pf.space_after = Pt(0)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

for sec in doc.sections:
    sec.page_width = Cm(21.0)     # A4
    sec.page_height = Cm(29.7)    # A4
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
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = AZUL
    _font(r)
    return p


def para(text, indent=True, after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(after)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    for i, seg in enumerate(text.split("**")):
        r = p.add_run(seg)
        _font(r)
        if i % 2 == 1:
            r.bold = True
    return p


def figura(img_name, numero, titulo, fuente, width=5.4):
    cap = doc.add_paragraph()
    cap.paragraph_format.space_before = Pt(8)
    cap.paragraph_format.space_after = Pt(0)
    r = cap.add_run(f"Figura {numero}")
    r.bold = True
    r.font.size = Pt(11)
    _font(r)
    tit = doc.add_paragraph()
    tit.paragraph_format.space_after = Pt(3)
    rt = tit.add_run(titulo)
    rt.italic = True
    rt.font.size = Pt(11)
    _font(rt)
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_after = Pt(2)
    pic.add_run().add_picture(os.path.join(IMG, img_name), width=Inches(width))
    fp = doc.add_paragraph()
    fp.paragraph_format.space_after = Pt(8)
    rn = fp.add_run("Nota. ")
    rn.italic = True
    rn.font.size = Pt(10)
    _font(rn)
    rfu = fp.add_run(fuente)
    rfu.font.size = Pt(10)
    rfu.font.color.rgb = GRISTXT
    _font(rfu)


def referencia(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Cm(1.25)
    p.paragraph_format.first_line_indent = Cm(-1.25)
    for i, seg in enumerate(text.split("//")):
        r = p.add_run(seg)
        _font(r)
        if i % 2 == 1:
            r.italic = True


# ======================================================================
heading("1.1. Planteamiento del problema", size=14)

para(
    "La informalidad laboral constituye uno de los rasgos más persistentes y "
    "estructurales del mundo del trabajo contemporáneo. En términos conceptuales, el "
    "empleo informal comprende el conjunto de relaciones laborales que, total o "
    "parcialmente, escapan a la cobertura efectiva de la legislación laboral y de la "
    "protección social, de modo que los trabajadores carecen de seguridad social, "
    "aportes previsionales, estabilidad contractual y beneficios laborales básicos "
    "(Organización Internacional del Trabajo [OIT], 2024a). Conviene distinguir, además, "
    "entre el «sector informal» —referido a las unidades productivas no registradas— y "
    "el «empleo informal» —referido a las condiciones del puesto de trabajo, que pueden "
    "presentarse incluso dentro de empresas formales—, distinción metodológica que el "
    "Instituto Nacional de Estadística e Informática (INEI) recoge para medir el "
    "fenómeno en el Perú y que se sintetiza en la Figura 1.")

figura(
    "oficial_inei_esquema.png", "1",
    "Esquema conceptual de la informalidad laboral (sector y empleo)",
    "Tomado del Instituto Nacional de Estadística e Informática (INEI, 2019).",
    width=4.0)

para(
    "El estudio sistemático de la informalidad se remonta a la noción de «sector "
    "informal» propuesta por Hart (1973) y ha dado lugar a tres grandes lecturas "
    "teóricas que aún estructuran el debate: la estructuralista, que la entiende como "
    "resultado de la insuficiente capacidad de absorción del sector moderno; la "
    "legalista o institucionalista, que la atribuye a los costos regulatorios y "
    "tributarios de la formalidad (De Soto, 1986); y la que la concibe, en parte, como "
    "una decisión voluntaria de trabajadores y microempresarios que ponderan costos y "
    "beneficios de formalizarse (Maloney, 2004). Esta diversidad de enfoques anticipa "
    "que la informalidad no obedece a una causa única, sino a una constelación de "
    "factores socioeconómicos cuya identificación constituye el objeto de la presente "
    "investigación.")

# --- Mundo ---
para(
    "A escala mundial, la magnitud del fenómeno es considerable. Según la OIT (2024a), "
    "alrededor del 58 % de la población ocupada mundial —cerca de 2.000 millones de "
    "personas— se desempeña en condiciones de informalidad, proporción que se ha "
    "mantenido relativamente estable en las últimas dos décadas pese al crecimiento "
    "económico global. Este promedio agregado, no obstante, oculta una marcada "
    "heterogeneidad asociada al nivel de desarrollo: mientras que en las economías de "
    "ingreso alto la informalidad afecta a apenas el 13 % de los ocupados, en las de "
    "ingreso bajo alcanza cerca del 88 % de la fuerza de trabajo (OIT, 2024a). Esta "
    "relación inversa entre informalidad y nivel de ingreso, ilustrada por la "
    "trayectoria mundial de la Figura 2, constituye uno de los hechos estilizados más "
    "robustos de la economía del desarrollo: la informalidad es, a la vez, causa y "
    "manifestación del subdesarrollo (La Porta y Shleifer, 2014).")

figura(
    "oficial_ilostat_mundial_2004_2022.png", "2",
    "Tasa de empleo informal en el mundo, 2004-2022 (%)",
    "Tomado de ILOSTAT, Organización Internacional del Trabajo (OIT, 2023).",
    width=5.2)

# --- América Latina ---
para(
    "En América Latina y el Caribe, la informalidad es un rasgo estructural del mercado "
    "de trabajo y un determinante central de la desigualdad. Hacia 2024, alrededor del "
    "47,6 % de la población ocupada de la región se encontraba en empleo informal (OIT, "
    "2024b); sin embargo, la mayor parte de los nuevos empleos creados en el último "
    "ciclo han sido informales y se concentran en los hogares de menores ingresos, "
    "perpetuando trampas de pobreza y vulnerabilidad (Comisión Económica para América "
    "Latina y el Caribe [CEPAL], 2023). La evidencia regional muestra de manera "
    "consistente que la probabilidad de ser informal aumenta con el menor nivel "
    "educativo, en las mujeres, en los jóvenes y los adultos mayores, en las zonas "
    "rurales y entre los trabajadores "
    "de microempresas (CEPAL, 2023). Dentro de este panorama, el Perú figura "
    "sistemáticamente entre los países con mayores tasas de informalidad de la región, "
    "lo que confiere especial relevancia al análisis de sus determinantes.")

# --- Perú ---
para(
    "En el Perú, la informalidad laboral representa el desafío estructural más "
    "persistente del mercado de trabajo. Según el INEI (2025), en 2024 el 70,9 % de la "
    "población económicamente activa ocupada se desempeñaba en un empleo informal; de "
    "este total, el 55,7 % correspondía a empleo informal dentro del sector informal y "
    "el 15,2 % fuera de él, mientras que solo el 29,1 % accedía a un empleo formal "
    "(Figura 3). En otras palabras, siete de cada diez trabajadores peruanos laboran sin "
    "acceso a seguridad social, gratificaciones, compensación por tiempo de servicios ni "
    "aportes previsionales.")

figura(
    "oficial_inei_peru_2024.png", "3",
    "Perú: PEA ocupada por condición de empleo formal e informal, 2024",
    "Tomado del Instituto Nacional de Estadística e Informática (INEI, 2025), "
    "Encuesta Permanente de Empleo Nacional.",
    width=4.3)

para(
    "La trayectoria histórica del indicador revela una notable rigidez estructural: la "
    "informalidad descendió solo marginalmente entre 2011 (75,1 %) y 2019 (72,7 %), se "
    "elevó abruptamente durante la pandemia de COVID-19 —hasta 76,8 % en 2021— y, pese a "
    "la recuperación posterior, se mantiene en niveles incompatibles con el nivel de "
    "ingreso del país (INEI, 2025; CEPLAN, 2024). Esta persistencia se vincula a las "
    "características de la estructura productiva: Chacaltana (2016) y Loayza (2008) "
    "sostienen que la informalidad combina la escasez de empleo formal en una economía "
    "de baja productividad con débiles capacidades estatales de fiscalización y un marco "
    "regulatorio costoso. La dimensión sectorial es elocuente: la informalidad alcanza "
    "el 91,5 % en la agricultura, pesca y minería y se mantiene por encima del 59 % "
    "incluso en los servicios (INEI, 2025). La meta nacional de reducir la informalidad "
    "al 60 % hacia 2030 (CEPLAN, 2024) luce, a la luz de esta trayectoria, difícil de "
    "alcanzar sin intervenciones focalizadas, lo que justifica investigar con precisión "
    "los factores socioeconómicos que la sostienen.")

para(
    "Las consecuencias de la informalidad se proyectan tanto sobre los trabajadores "
    "como sobre el conjunto de la economía. En el plano individual, los trabajadores "
    "informales carecen de protección social, enfrentan mayor inestabilidad de ingresos "
    "y disponen de escaso acceso a la capacitación y al crédito formal. En el plano "
    "agregado, la informalidad erosiona la base tributaria del Estado y deprime la "
    "productividad media, pues las unidades informales permanecen pequeñas y "
    "descapitalizadas; la evidencia comparada muestra que en economías más formales, "
    "como Chile, la productividad por trabajador casi duplica la peruana (Loayza, 2008; "
    "Ulyssea, 2020). Ante la falta de empleo formal, amplios segmentos de la PEA "
    "recurren a ocupaciones eventuales de subsistencia —los «cachuelos»—, que rara vez "
    "ofrecen estabilidad ni desarrollo profesional.")

# --- Factores socioeconómicos ---
para(
    "Más allá de los condicionantes estructurales, la literatura ha identificado un "
    "conjunto de **factores socioeconómicos de orden individual** que determinan la "
    "probabilidad de informalidad. El primero y más robusto es el **nivel educativo**. "
    "Desde la teoría del capital humano, la inversión en educación eleva la "
    "productividad del individuo y su acceso a empleos formales mejor remunerados "
    "(Becker, 1964). En el Perú esta relación es nítida y monotónica: la informalidad "
    "afecta al 94,6 % de los ocupados con primaria o menos, al 81,2 % de quienes "
    "completaron secundaria y al 37,9 % de quienes cuentan con educación superior "
    "universitaria (INEI, 2025), una brecha cercana a 57 puntos porcentuales entre los "
    "extremos.")

para(
    "El **nivel de ingresos** y el **tamaño de la empresa** configuran un segundo bloque "
    "de determinantes, estrechamente ligados entre sí. Las unidades de menor tamaño "
    "—microempresas y autoempleos— carecen del capital y la escala necesarios para "
    "asumir los costos de la formalización y para ofrecer remuneraciones competitivas: "
    "en las empresas de 1 a 10 trabajadores la informalidad alcanza el 88,6 %, frente a "
    "solo el 15,6 % en las de 51 o más (INEI, 2025; Ulyssea, 2020). A ello se suman las "
    "**características demográficas**. La edad mantiene una relación no lineal con la "
    "informalidad —máxima entre los jóvenes de 14 a 24 años (85,4 %), mínima en las "
    "edades centrales y nuevamente creciente entre los adultos mayores—; las mujeres "
    "registran tasas superiores a las de los hombres (73,1 % frente a 68,8 %), por la "
    "segregación ocupacional y la carga del trabajo de cuidado; y la informalidad es muy "
    "superior en el ámbito rural (94,6 %) respecto del urbano (65,1 %) (INEI, 2025; "
    "CEPAL, 2023). El estado civil, por su parte, también incide en la decisión de "
    "informalidad: la literatura reporta que las personas con pareja o con "
    "responsabilidades de jefatura del hogar presentan patrones de inserción laboral "
    "diferenciados, asociados a una mayor necesidad de estabilidad de ingresos, por lo "
    "que constituye un control demográfico pertinente. Estos hallazgos sustentan la "
    "inclusión del nivel de ingresos, el nivel educativo y los determinantes "
    "demográficos —edad, sexo y estado civil— como variables explicativas centrales del "
    "presente estudio.")

# --- Lima ---
para(
    "El **departamento de Lima** constituye el principal mercado laboral del país: "
    "concentra alrededor de un tercio de la población nacional y aporta cerca de la "
    "mitad del producto bruto interno, además de albergar la mayor densidad de empresas "
    "formales, instituciones de educación superior y servicios modernos. Coherentemente, "
    "Lima Metropolitana exhibe una de las tasas de informalidad más bajas del país "
    "—en torno al 54,8 %, frente al 70,9 % nacional y al 82,5 % de ciudades como Juliaca "
    "(INEI, 2025)—. Sin embargo, esta lectura agregada encierra una paradoja decisiva "
    "para la investigación: aun siendo la región con menor tasa relativa, el "
    "departamento de Lima alberga el **mayor volumen absoluto de trabajadores "
    "informales** del país, dado que concentra la mayor parte de la población ocupada "
    "nacional. A ello se suma que, según el INEI (2025), Lima y Callao figuraron entre "
    "las ciudades donde la informalidad aumentó respecto de 2023, lo que sugiere un "
    "posible estancamiento del proceso de formalización en la capital. Además, el "
    "departamento comprende tanto la metrópoli moderna como provincias de carácter "
    "rural, donde la "
    "informalidad es mucho mayor, de modo que el promedio departamental enmascara "
    "realidades laborales profundamente desiguales.")

# --- Vacíos / importancia / pertinencia / cierre ---
para(
    "La revisión de la literatura revela **vacíos de conocimiento** que justifican el "
    "estudio. Buena parte de las investigaciones nacionales emplea datos previos a la "
    "pandemia (Tello, 2014; Tenorio, 2020) y no captura las transformaciones del mercado "
    "de trabajo en la fase de normalización 2024-2025; la mayoría aborda la informalidad "
    "a escala agregada o se centra en otras regiones, siendo escasos los estudios que "
    "analizan específicamente el departamento de Lima con la información más reciente de "
    "la Encuesta Permanente de Empleo Nacional; y una parte de la literatura privilegia "
    "el enfoque empresarial de formalización de las MYPE por sobre el enfoque del "
    "trabajador, dejando insuficientemente explorada la interacción simultánea entre "
    "ingreso, educación y características demográficas en la determinación individual de "
    "la informalidad.")

para(
    "La relevancia del problema es, a la vez, **económica y social**. En el plano "
    "social, la informalidad priva a millones de trabajadores limeños de protección "
    "frente a la enfermedad, la vejez y el desempleo, y reproduce ciclos "
    "intergeneracionales de pobreza (Perry et al., 2007; CEPAL, 2023). En el plano "
    "económico, deprime la productividad agregada, restringe la recaudación tributaria y "
    "limita la inclusión financiera (Loayza, 2008; Ulyssea, 2020). Dado que Lima "
    "concentra la mayor parte de la actividad económica nacional, las mejoras en la "
    "formalización de su mercado laboral tendrían efectos amplificados sobre el "
    "crecimiento, la equidad y las finanzas públicas del conjunto del país.")

para(
    "La elección de Lima y del periodo **2024-2025** obedece a razones científicas y de "
    "oportunidad: Lima es el mercado laboral más grande y diverso, donde la informalidad "
    "no puede atribuirse principalmente a la ruralidad sino a factores socioeconómicos "
    "individuales; el periodo corresponde a la fase de normalización pospandemia, en la "
    "que la informalidad se mantiene elevada e incluso repuntó en la capital; y, por "
    "primera vez de manera consolidada, se dispone de la información de la Encuesta "
    "Permanente de Empleo Nacional, que permite un análisis más preciso y actualizado. "
    "En particular, la disponibilidad de microdatos individuales habilita la estimación "
    "de modelos de elección discreta —como los modelos logit y probit— que cuantifican "
    "el efecto marginal de cada factor socioeconómico sobre la probabilidad de "
    "informalidad, controlando por las demás características del trabajador. "
    "En síntesis, la informalidad laboral es un fenómeno estructural, global y "
    "persistente que en el departamento de Lima —pese a presentar las tasas relativas "
    "más bajas del país— afecta a la mayoría de los trabajadores y al mayor volumen "
    "absoluto de población ocupada del territorio nacional, asociado de manera robusta "
    "al nivel de ingresos, el nivel educativo y las características demográficas. "
    "Comprender la magnitud y la dirección del efecto de estos factores en el contexto "
    "limeño de 2024-2025 resulta indispensable para orientar políticas públicas "
    "eficaces, lo que conduce a la formulación del problema de investigación.")

# --- Referencias (en página aparte) ---
doc.add_page_break()
heading("Referencias", size=13)
refs = [
    "Becker, G. S. (1964). //Human capital: A theoretical and empirical analysis//. "
    "Columbia University Press.",
    "Centro Nacional de Planeamiento Estratégico. (2024). //Persistencia de la "
    "informalidad laboral y del empleo vulnerable//. Observatorio Nacional de "
    "Prospectiva.",
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
    "Saavedra-Chanduvi, J. (2007). //Informality: Exit and exclusion//. Banco Mundial.",
    "Tello, M. D. (2014). //¿Es la informalidad laboral una decisión voluntaria en el "
    "Perú?// Consorcio de Investigación Económica y Social.",
    "Tenorio, D. (2020). El empleo informal en el Perú: una breve caracterización "
    "2007-2018. //Pensamiento Crítico//, 25(1), 51-75. "
    "https://doi.org/10.15381/pc.v25i1.18477",
    "Ulyssea, G. (2020). Informality: Causes and consequences for development. //Annual "
    "Review of Economics//, 12, 525-546.",
]
for r in refs:
    referencia(r)

doc.save(OUT)
print("Guardado:", OUT)
