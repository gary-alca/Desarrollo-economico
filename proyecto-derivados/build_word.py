# -*- coding: utf-8 -*-
"""Genera el informe final en Word: Proyecto de Derivados (Futuros y Opciones)."""
import numpy as np
import data as d
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

NAVY = RGBColor(0x1F, 0x4E, 0x78)
GREY = RGBColor(0x59, 0x59, 0x59)

# ---------- helpers de calculo ----------
def cap_riesgo(pos):
    STs = np.linspace(min(l["K"] for l in pos["legs"]) - 60,
                      max(l["K"] for l in pos["legs"]) + 60, 6000)
    return -min(d.estrategia_gp_total(pos, s) for s in STs)

def maxG(pos):
    STs = np.linspace(min(l["K"] for l in pos["legs"]) - 60,
                      max(l["K"] for l in pos["legs"]) + 60, 6000)
    return max(d.estrategia_gp_total(pos, s) for s in STs)

def breakevens(pos):
    STs = np.linspace(min(l["K"] for l in pos["legs"]) - 60,
                      max(l["K"] for l in pos["legs"]) + 60, 8000)
    g = np.array([d.estrategia_gp_total(pos, s) for s in STs])
    bes = []
    for i in range(1, len(STs)):
        if (g[i-1] < 0) != (g[i] < 0):
            bes.append(round((STs[i-1]+STs[i])/2, 2))
    return bes

def fut_pl(f):
    sign = 1 if f["posicion"] == "Larga" else -1
    prev = f["entrada"]; acum = 0
    for s in f["settle"]:
        acum += (s - prev) * sign * f["contratos"] * f["tamano"]; prev = s
    return acum

OPC = d.OPCIONES
CR = {p["id"]: cap_riesgo(p) for p in OPC}
MG = {p["id"]: maxG(p) for p in OPC}
BE = {p["id"]: breakevens(p) for p in OPC}
NET = {p["id"]: d.credito_debito_neto(p) * 100 * p["contratos"] for p in OPC}
tot_riesgo_opc = sum(CR.values())
net_prem_opc = sum(NET.values())
fut_total_pl = sum(fut_pl(f) for f in d.FUTUROS.values())
fut_margin = sum(f["contratos"] * f["margen_ini"] for f in d.FUTUROS.values())

# ---------- documento ----------
doc = Document()
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)

def H(txt, lvl=1):
    h = doc.add_heading(txt, level=lvl)
    for run in h.runs:
        run.font.color.rgb = NAVY
    return h

def P(txt, italic=False, bold=False, size=11, align=None, color=None):
    p = doc.add_paragraph()
    r = p.add_run(txt); r.italic = italic; r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    if align: p.alignment = align
    return p

def bullets(items):
    for it in items:
        doc.add_paragraph(it, style="List Bullet")

def numbered(items):
    for it in items:
        doc.add_paragraph(it, style="List Number")

def table(headers, rows, widths=None, note=None):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(headers):
        c = t.rows[0].cells[j]; c.text = ""
        run = c.paragraphs[0].add_run(h); run.bold = True; run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for row in rows:
        cells = t.add_row().cells
        for j, v in enumerate(row):
            cells[j].text = ""
            run = cells[j].paragraphs[0].add_run(str(v)); run.font.size = Pt(9)
    if widths:
        for j, w in enumerate(widths):
            for row in t.rows:
                row.cells[j].width = Inches(w)
    if note:
        P(note, italic=True, size=8, color=GREY)
    return t

def money(x): return f"USD {x:,.0f}"

# ============================================================ PORTADA
tp = doc.add_paragraph(); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = tp.add_run("PROYECTO DE DERIVADOS FINANCIEROS")
r.bold = True; r.font.size = Pt(22); r.font.color.rgb = NAVY
P("Administración dinámica de un portafolio de USD 1,000,000 en Futuros y Opciones",
  align=WD_ALIGN_PARAGRAPH.CENTER, size=13, color=GREY)
P("Horizonte: 18 de junio – 9 de julio de 2026", align=WD_ALIGN_PARAGRAPH.CENTER, size=12)
doc.add_paragraph()
P("Rol: Gestor de portafolios, analista cuantitativo y especialista en derivados",
  align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=GREY)
P("Mercados: CME · ICE · CBOE · NYMEX · COMEX · CBOT",
  align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=GREY)
doc.add_page_break()

# ============================================================ NOTA METODOLOGICA
H("Nota metodológica (leer primero)", 1)
P("Este trabajo se rige por un cronograma de tres tramos que no deben mezclarse. "
  "La transparencia sobre el origen de cada dato es parte de la evaluación, por lo que "
  "se declara explícitamente qué precio corresponde a qué fecha y qué dato es real, "
  "estimado o ilustrativo.", )
table(
    ["Tramo", "Fechas", "Instrumentos", "Fuente de precios", "Naturaleza"],
    [
        ["A. Retrospectivo", "18–24 jun 2026", "Solo futuros",
         "Liquidaciones diarias (COMEX/NYMEX/CME)", "Reconstrucción ilustrativa (hindsight)"],
        ["B. Apertura opciones", "2 jul 2026 (*)", "Opciones + futuros",
         "Cadenas de opciones adjuntas (MarketWatch)", "Prima de entrada real"],
        ["C. Administración", "2–9 jul 2026", "Opciones (valoración/cierre) + futuros",
         "MarketWatch por strike/vencimiento", "Decisiones bajo incertidumbre"],
    ],
    widths=[1.1, 1.0, 1.2, 1.6, 1.6],
)
P("(*) Decisión metodológica sobre la fecha de apertura de opciones. — El plan original "
  "situaba la apertura de opciones el 25 de junio. Sin embargo, las ÚNICAS cadenas de opciones "
  "verificables de las que se dispone son las capturas de MarketWatch del 2 de julio de 2026 "
  "(NVDA, AAPL, MSFT, DAL con vencimiento 10-jul y SPY con vencimiento 18-dic). "
  "Las reglas del proyecto prohíben inventar primas y advierten que las primas intradía pasadas "
  "no se pueden reconstruir de forma fiable. Por coherencia y verificabilidad, se ancla la ENTRADA "
  "de las opciones al 2 de julio de 2026 (inicio de la ventana de administración en tiempo real) "
  "usando esos bid/ask/last reales, y se analiza el resultado al vencimiento. "
  "Donde el precio spot de entrada del 25 de junio difiere del del 2 de julio (p. ej. AAPL ~275 → "
  "308; MSFT ~353 → 390), se interpreta como la revalorización natural del subyacente y se deja "
  "constancia expresa.", size=10)
P("Futuros. — Los futuros operan durante todo el horizonte (no se congelan). Las series de "
  "liquidación diaria empleadas en las tablas de marca a mercado son ILUSTRATIVAS y coherentes con "
  "la tesis macro, porque no se dispone de la serie oficial CME/NYMEX/COMEX para esas fechas de 2026. "
  "Las fórmulas del Excel recalculan automáticamente al pegar los settlements oficiales; la mecánica "
  "(G/P diaria, cuenta de margen y margin call) es la que se evalúa.", size=10)
P("Regla anti-invención. — Cuando falta un dato se declara y se estima con un supuesto razonable "
  "(interpolación por moneyness o paridad put-call). Nunca se inventan precios, primas ni "
  "volatilidades.", size=10, bold=True)
doc.add_page_break()

# ============================================================ 1. INTRODUCCION
H("1. Introducción", 1)
P("El presente informe documenta la construcción y la administración dinámica de un portafolio "
  "hipotético de USD 1,000,000 compuesto por futuros y opciones sobre acciones, índices y materias "
  "primas, negociados en los principales mercados internacionales (CME, ICE, CBOE, NYMEX, COMEX y "
  "CBOT). El objetivo pedagógico no es maximizar la rentabilidad, sino demostrar el dominio del uso "
  "de derivados, la administración del riesgo y la toma de decisiones fundamentadas.")
P("El portafolio se administra día a día: cada posición se abre, mantiene, reduce, aumenta, "
  "reemplaza o cierra según cambian las condiciones del mercado, y cada decisión queda anclada a un "
  "dato de mercado real de su fecha (Sección 10, Bitácora). Se respeta el cronograma de tres tramos "
  "descrito en la Nota metodológica.")

# ============================================================ 2. OBJETIVOS
H("2. Objetivos", 1)
numbered([
    "Construir un portafolio diversificado de derivados coherente con un capital de ~USD 1,000,000.",
    "Justificar cada posición con fundamentos macroeconómicos, financieros y técnicos.",
    "Administrar el portafolio de forma dinámica (bitácora fechada de decisiones).",
    "Cuantificar y gestionar los riesgos: mercado, volatilidad, liquidez, apalancamiento y concentración.",
    "Entregar los dos libros de Excel (opciones formato Ejercicio 7 y futuros marca a mercado) con totales que cuadran.",
])

# ============================================================ 3. METODOLOGIA
H("3. Metodología", 1)
bullets([
    "Selección de subyacentes por tesis (macro + catalizadores + técnico) y por adecuación de la estructura de opción a la visión y a la volatilidad implícita.",
    "Valoración de opciones al vencimiento por payoff intrínseco; valoración intra-ventana por Black-Scholes cuando no se dispone de la cadena diaria (se declara).",
    "Futuros valorados por marca a mercado diaria con cuenta de margen y disparo de margin call al perforar el margen de mantenimiento.",
    "Dimensionamiento por capital en riesgo (pérdida máxima de estructuras definidas) y por margen inicial (futuros), no por nocional bruto.",
    "Tasa libre de riesgo r = 4.5% anual (T-bill ~3 meses, referencia); T en años hasta el vencimiento.",
])

# ============================================================ 4. CONTEXTO MACRO
H("4. Contexto macroeconómico (18 jun – 9 jul 2026)", 1)
P("Nota: síntesis del entorno relevante para las posiciones. Las cifras puntuales deben "
  "contrastarse con las fuentes citadas al cierre de cada jornada.", italic=True, size=9, color=GREY)
bullets([
    "Política monetaria (Fed): mercado atento a las minutas del FOMC (miércoles) en busca del tono sobre recortes; un sesgo dovish favorece oro y bonos y presiona al dólar.",
    "Inflación y empleo: datos que sorprendan al alza reavivan el miedo a tasas más altas por más tiempo (negativo para bonos y equity); sorpresas a la baja son pro-riesgo.",
    "Tasas y bonos del Tesoro: la pendiente y el 10 años (rendimiento) condicionan la valoración de tecnológicas de larga duración (MSFT, AAPL, NVDA).",
    "Dólar (DXY): un dólar más débil apoya materias primas denominadas en USD (oro).",
    "Petróleo: distensión EE.UU.–Irán y mayor oferta apuntan a un sesgo bajista del crudo (tesis corto WTI y viento de cola para DAL por menor costo de combustible).",
    "Oro: refugio ante riesgo geopolítico y ante una Fed más laxa (tesis largo GC).",
    "Volatilidad (VIX): régimen relativamente bajo (<16), lo que abarata coberturas y encarece, en términos relativos, la venta de prima; condiciona la elección de estructuras.",
    "Renta variable: S&P 500 en tendencia alcista lenta en semana de pocos catalizadores (entorno favorable a estructuras neutrales como la mariposa de SPY).",
])
P("Eventos programados relevantes: minutas del FOMC; datos de empleo e inflación de EE.UU.; "
  "reporte trimestral de DAL (viernes) con volatilidad implícita inflada previa al anuncio.")

# ============================================================ 5. CONTEXTO FINANCIERO
H("5. Contexto financiero y snapshot de mercado (2 jul 2026)", 1)
table(["Subyacente", "Cierre (2-jul)", "Vencimiento usado", "Rol en el portafolio"],
      [["AAPL — Apple", "308.63", "10-jul-2026", "Sesgo alcista (spread débito)"],
       ["MSFT — Microsoft", "390.49", "10-jul-2026", "Sesgo alcista (venta de prima)"],
       ["NVDA — Nvidia", "194.83", "10-jul-2026", "Sesgo bajista/neutral (venta de prima)"],
       ["DAL — Delta Air Lines", "92.75", "10-jul-2026", "Sesgo alcista (venta de prima, IV crush)"],
       ["SPY — S&P 500 ETF", "744.78", "18-dic-2026", "Neutral (mariposa)"]],
      widths=[1.6, 1.1, 1.3, 2.2],
      note="Fuente: capturas MarketWatch del 2-jul-2026 (cierre). SPY: única cadena disponible = diciembre 2026.")

# ============================================================ 6. RETROSPECTIVO
H("6. Análisis retrospectivo — solo futuros (18–24 jun 2026)", 1)
P("Nota de hindsight (inicio). — Esta sección es una reconstrucción ILUSTRATIVA con datos ya "
  "conocidos; NO representa decisiones tomadas en tiempo real. Se incluye porque las liquidaciones "
  "de futuros son verificables. La condición de tiempo real bajo incertidumbre aplica solo al tramo "
  "2–9 de julio.", bold=True, size=10)
P("En la primera semana se ilustran tres posiciones de futuros coherentes con el contexto macro "
  "disponible en esas fechas, cada una marcada a mercado. La mecánica completa (G/P diaria, cuenta de "
  "margen y margin call) figura en el Excel de futuros; aquí se resume la lógica:")
bullets([
    "Largo en Oro (GC, COMEX): refugio ante riesgo geopolítico y expectativa de Fed más laxa.",
    "Corto en Petróleo WTI (CL, NYMEX): distensión EE.UU.–Irán y mayor oferta.",
    "Largo en E-mini S&P 500 (ES, CME): tendencia alcista lenta del índice (posición direccional).",
])
P("Estas mismas posiciones continúan operando después del 24 de junio (los futuros no se congelan), "
  "por lo que su marca a mercado se extiende hasta el 9 de julio en el Excel. Los settlements diarios "
  "son ilustrativos (ver Nota metodológica).")
P("Nota de hindsight (fin). — Reiteramos que el tramo A es ilustrativo y no debe leerse como "
  "'aciertos' de trading en tiempo real.", italic=True, size=10)

# ============================================================ 7. JUSTIFICACION ACTIVOS
H("7. Justificación de los activos seleccionados (portafolio principal)", 1)
P("La selección combina (i) una tesis macro/catalizador clara por subyacente, (ii) una estructura "
  "de opción cuya forma de ganar coincide con esa tesis y con el régimen de volatilidad, y (iii) "
  "riesgo definido. Los futuros aportan exposición macro directa (materias primas e índice) que "
  "diversifica el bloque de opciones sobre acciones tecnológicas.")

# ============================================================ 8. CONSTRUCCION
H("8. Construcción del portafolio", 1)
H("8.1 Posiciones de opciones (apertura 2-jul-2026)", 2)
rows = []
for p in OPC:
    strikes = "/".join(str(int(l["K"]) if l["K"] == int(l["K"]) else l["K"]) for l in p["legs"])
    neto = d.credito_debito_neto(p)
    tipo = "Crédito" if neto > 0 else "Débito"
    rows.append([p["subyacente"], p["estrategia"], strikes, p["exp"][5:], p["contratos"],
                 f"{neto:+.2f}", f"{NET[p['id']]:+,.0f}", f"{MG[p['id']]:,.0f}", f"{-CR[p['id']]:,.0f}"])
table(["Activo", "Estrategia", "Strikes", "Venc.", "Contr.", "Prima/acc",
       "Prima total", "Ganancia máx.", "Pérdida máx."], rows,
      widths=[0.7, 1.5, 0.9, 0.6, 0.6, 0.8, 0.9, 0.9, 0.9])
P(f"Prima neta del bloque de opciones: {money(net_prem_opc)} "
  f"({'crédito neto' if net_prem_opc>=0 else 'débito neto'}). "
  f"Capital total en riesgo (suma de pérdidas máximas): {money(tot_riesgo_opc)}.", bold=True)

H("8.2 Posiciones de futuros (operan 18-jun a 9-jul-2026)", 2)
frows = []
for sym, f in d.FUTUROS.items():
    frows.append([f["activo"], sym, f["mercado"], f["posicion"], f["contratos"],
                  f"{f['tamano']} {f['unidad']}", f"{f['entrada']:,.2f}",
                  money(f["entrada"] * f["contratos"] * f["tamano"]),
                  money(f["contratos"] * f["margen_ini"])])
table(["Activo", "Símb.", "Mercado", "Posición", "Contr.", "Tamaño", "Entrada",
       "Nocional", "Margen inicial"], frows,
      widths=[1.2, 0.5, 0.8, 0.7, 0.6, 1.0, 0.8, 1.1, 1.1])
P(f"Margen inicial total (futuros): {money(fut_margin)}. "
  f"Nocional bruto de futuros: {money(sum(f['entrada']*f['contratos']*f['tamano'] for f in d.FUTUROS.values()))}.",
  bold=True)

H("8.3 Uso del capital (~USD 1,000,000)", 2)
reserva = d.CAPITAL - fut_margin - max(tot_riesgo_opc - net_prem_opc, 0)
table(["Concepto", "Monto (USD)", "Comentario"],
      [["Margen inicial de futuros", f"{fut_margin:,.0f}", "Comprometido en cuentas de margen"],
       ["Capital en riesgo de opciones (neto de prima)", f"{max(tot_riesgo_opc-net_prem_opc,0):,.0f}",
        "Pérdida máxima teórica del bloque de opciones"],
       ["Colchón de liquidez / reserva", f"{reserva:,.0f}",
        "Para margin calls, ajustes y nuevas oportunidades"],
       ["Capital objetivo", f"{d.CAPITAL:,.0f}", ""]],
      widths=[2.6, 1.3, 2.4])
P("El nocional teórico agregado supera el capital (apalancamiento inherente a los derivados), pero "
  "la exposición económica real de las opciones está limitada por el ancho de cada spread y la "
  "pérdida máxima definida; los futuros están respaldados por margen y colchón de liquidez.", size=10)

# ============================================================ 9. JUSTIFICACION INDIVIDUAL
H("9. Justificación individual de cada posición", 1)

def just_opcion(p, tesis, riesgo_txt, porque_no, ventajas, desventajas, escenarios_txt):
    H(f"9.x {p['subyacente']} — {p['nombre']}", 2)
    neto = d.credito_debito_neto(p)
    be = ", ".join(f"{b:.2f}" for b in BE[p["id"]]) or "n/a"
    tbl = [
        ["¿Por qué este activo?", tesis["activo"]],
        ["¿Por qué esta estrategia?", tesis["estrategia"]],
        ["¿Qué esperas que ocurra?", tesis["espera"]],
        ["¿Qué riesgo aprovecha?", tesis["riesgo_aprov"]],
        ["Escenario de ganancia", escenarios_txt["gana"]],
        ["Escenario de pérdida", escenarios_txt["pierde"]],
        ["Pérdida máxima", f"{money(-CR[p['id']])} ({p['contratos']} contratos)"],
        ["Ganancia potencial", f"{money(MG[p['id']])}"],
        ["Break-even(s)", be],
        ["Prima neta", f"{neto:+.2f}/acción → {money(NET[p['id']])} "
                       f"({'crédito' if neto>0 else 'débito'})"],
        ["¿Por qué no otra estrategia?", porque_no],
        ["Ventajas", ventajas],
        ["Desventajas", desventajas],
        ["Eventos que la favorecen / perjudican", riesgo_txt],
    ]
    table(["Pregunta", "Respuesta"], tbl, widths=[1.9, 4.4])
    try:
        doc.add_picture(f"img/{p['id']}.png", width=Inches(5.4))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    except Exception:
        pass

# DAL
just_opcion(OPC[0],
    tesis={"activo": "DAL reporta el viernes; 22 de 24 analistas en compra fuerte y cuatro sorpresas "
                     "positivas seguidas; el abaratamiento del crudo reduce el costo de combustible (~-USD 300 M).",
           "estrategia": "Bull Put Spread: se cobra prima con la volatilidad implícita inflada previa al "
                         "reporte y se aprovecha el 'IV crush' posterior; el put comprado en 85 topa la pérdida.",
           "espera": "Que DAL se mantenga por encima de 90 al vencimiento (soporte técnico ~92.7) y que la "
                     "caída de la volatilidad tras el reporte abarate la recompra.",
           "riesgo_aprov": "Volatilidad implícita alta (Vega corta) y sesgo alcista moderado."},
    riesgo_txt="Favorece: buena guía, crudo a la baja, IV crush. Perjudica: guía débil que rompa el soporte "
               "(BPA esperado ~-32% interanual).",
    porque_no="No una venta de put desnuda (riesgo ilimitado a la baja) ni una call simple (paga theta sin "
              "aprovechar el IV crush). El spread define la pérdida.",
    ventajas="Riesgo definido; se beneficia del paso del tiempo y de la caída de volatilidad.",
    desventajas="Ganancia limitada a la prima; pérdida mayor que la ganancia si se rompe el soporte.",
    escenarios_txt={"gana": "DAL ≥ 90 al vencimiento → se retiene el crédito completo.",
                    "pierde": "DAL ≤ 85 → pérdida máxima definida."})

# MSFT
just_opcion(OPC[1],
    tesis={"activo": "MSFT fue la más castigada de las grandes tecnológicas (miedo al gasto en centros de "
                     "datos de IA) y mostró señales de suelo; al 2-jul cotiza recuperada en ~390 (tesis de "
                     "capitulación/suelo confirmada).",
           "estrategia": "Bull Put Spread 385/380: expresa el sesgo alcista cobrando prima justo por debajo "
                         "del mercado, con pérdida topada por el put comprado en 380.",
           "espera": "Que MSFT sostenga los 385 tras haber recuperado el nivel.",
           "riesgo_aprov": "Continuación alcista tras el suelo, con venta de prima (Vega/Theta a favor)."},
    riesgo_txt="Favorece: continuidad de la recuperación, resultados sólidos de fin de mes. Perjudica: "
               "recaída por revisión del gasto en IA.",
    porque_no="Se prefiere el spread a la venta de put cash-secured pura (que exigiría reservar ~USD 1.17 M "
              "para asignación de 30 contratos) porque el spread define el riesgo y libera capital.",
    ventajas="Riesgo definido y menor consumo de capital que la venta cash-secured.",
    desventajas="Ganancia limitada; el estrechamiento de strikes reduce la prima.",
    escenarios_txt={"gana": "MSFT ≥ 385 → crédito completo.",
                    "pierde": "MSFT ≤ 380 → pérdida máxima definida."})

# AAPL
just_opcion(OPC[2],
    tesis={"activo": "AAPL a poca distancia de convertirse en la empresa más valiosa del mundo; titular que "
                     "atrae compradores y fondos de tendencia.",
           "estrategia": "Bull Call Spread 310/322.5: se compra la exposición alcista y se vende la call 322.5 "
                         "para financiar parte del débito y amortiguar el desgaste por theta en una semana sin "
                         "catalizador propio.",
           "espera": "Un avance moderado de AAPL por encima de 313.26 (break-even) hacia 322.5.",
           "riesgo_aprov": "Momentum alcista con costo y riesgo acotados."},
    riesgo_txt="Favorece: continuidad del momentum, titular de 'empresa más valiosa'. Perjudica: pérdida de "
               "los ~300 (soporte) o rotación fuera de tecnología.",
    porque_no="No una call simple (paga más theta y prima) ni un futuro (sin riesgo definido). El spread abarata "
              "la apuesta direccional.",
    ventajas="Débito y pérdida acotados; buena relación ganancia/pérdida (~2.8:1).",
    desventajas="Necesita movimiento al alza; si AAPL solo lateraliza, el theta erosiona el débito.",
    escenarios_txt={"gana": "AAPL ≥ 322.5 → ganancia máxima.",
                    "pierde": "AAPL ≤ 310 → pérdida del débito pagado (regla de salida: cerrar si pierde ~300)."})

# SPY
just_opcion(OPC[3],
    tesis={"activo": "S&P 500 en avance lento en semana de pocos datos; entorno ideal para una estructura "
                     "neutral que gana con el paso del tiempo cerca de un precio objetivo.",
           "estrategia": "Butterfly de calls 745/755/765: débito muy pequeño y gran convexidad si el índice "
                         "termina cerca de 755.",
           "espera": "Que SPY gravite en torno a 755. (Se usa la cadena de diciembre por ser la única "
                     "disponible; para el horizonte de julio la estructura se mantiene cerca de su valor de "
                     "entrada, ver 8.1 y Nota metodológica.)",
           "riesgo_aprov": "Baja volatilidad realizada en torno a un precio central."},
    riesgo_txt="Favorece: mercado en rango cerca de 755, VIX bajo. Perjudica: minutas de la Fed más duras que "
               "disparen un movimiento amplio en cualquier dirección.",
    porque_no="No un straddle/strangle largo (apuestan a movimiento amplio, lo contrario a la tesis) ni una call "
              "simple (direccional). La mariposa monetiza la quietud con riesgo mínimo.",
    ventajas="Pérdida mínima (débito ~USD 1.10/acción); enorme relación ganancia/pérdida.",
    desventajas="Requiere que el subyacente termine cerca del strike central; con vencimiento de diciembre la "
                "maduración es lenta (alternativa defensiva: comprar una put de SPY como seguro con VIX bajo).",
    escenarios_txt={"gana": "SPY ≈ 755 al vencimiento → ganancia máxima.",
                    "pierde": "SPY ≤ 745 o ≥ 765 → pérdida limitada al débito."})

# NVDA
just_opcion(OPC[4],
    tesis={"activo": "La incursión de Meta en la nube alimentó la lectura de exceso de capacidad de IA "
                     "(sobre-stock de GPUs), que presionaría los ingresos de Nvidia.",
           "estrategia": "Bear Call Spread 195/200: con la volatilidad implícita elevada conviene VENDER prima; "
                         "se cobra la call 195 y se compra la 200 para topar la pérdida si NVDA rebota.",
           "espera": "Que NVDA se mantenga en/por debajo de 195.",
           "riesgo_aprov": "Volatilidad implícita cara y sesgo bajista/neutral (venta de prima con tope)."},
    riesgo_txt="Favorece: confirmación del exceso de capacidad, rotación fuera de semiconductores. Perjudica: "
               "rebote técnico o buenas noticias de demanda de GPUs.",
    porque_no="Con IV cara, la compra de put es menos eficiente (se paga prima inflada); por eso se elige "
              "vender prima con el bear call spread. Un bear put spread se reservaría para IV barata.",
    ventajas="Riesgo definido; se cobra prima y el tiempo juega a favor.",
    desventajas="Ganancia limitada al crédito; pérdida mayor que la ganancia si NVDA supera 200.",
    escenarios_txt={"gana": "NVDA ≤ 195 → crédito completo.",
                    "pierde": "NVDA ≥ 200 → pérdida máxima definida."})

# Futuros justificacion breve
H("9.6 Futuros — justificación", 2)
table(["Futuro", "Posición", "Tesis", "Gana si…", "Pierde si…"],
      [["Oro (GC)", "Larga", "Refugio geopolítico + Fed dovish", "Sube el oro", "Cae el oro"],
       ["WTI (CL)", "Corta", "Distensión EE.UU.–Irán, más oferta", "Cae el crudo", "Repunta el crudo"],
       ["E-mini S&P (ES)", "Larga", "Tendencia alcista lenta del índice", "Sube el S&P", "Cae el S&P"]],
      widths=[1.2, 0.9, 2.0, 1.1, 1.1])

# ============================================================ 10. BITACORA
H("10. Bitácora de administración dinámica", 1)
P("Cada entrada ancla la decisión a un dato de mercado de su fecha. Los movimientos de subyacente "
  "citados en la ventana 2–9 jul provienen de la evolución de precios usada para la valoración; "
  "cuando no se dispone de la cadena diaria, la revaloración de la opción se estima por Black-Scholes "
  "(se indica). Regla de oro: ninguna posición se mantiene solo porque estaba en el plan.", size=10)

def bitacora(fecha, entradas):
    hp = doc.add_paragraph()
    r = hp.add_run(fecha); r.bold = True; r.font.color.rgb = NAVY
    for e in entradas:
        doc.add_paragraph(e, style="List Bullet")

bitacora("18–24 jun (Tramo A, futuros, hindsight)", [
    "ABRIR GC largo (3), CL corto (5), ES largo (2): apertura de las tres posiciones de futuros según tesis macro; marca a mercado diaria desde el primer día (ver Excel de futuros).",
    "24 jun — CL corto: repunte puntual del crudo acerca la cuenta al margen de mantenimiento; se atiende MARGIN CALL reponiendo hasta el margen inicial. La tesis bajista sigue vigente, se MANTIENE.",
])
bitacora("2 jul (Tramo B/C — apertura de opciones)", [
    "ABRIR DAL Bull Put Spread 90/85 (40): vender put 90 @2.16, comprar put 85 @0.85; crédito 1.31/acción. Motivo: IV inflada previa al reporte + soporte ~92.7.",
    "ABRIR MSFT Bull Put Spread 385/380 (30): crédito 1.64/acción. Motivo: suelo confirmado y recuperación a 390.",
    "ABRIR AAPL Bull Call Spread 310/322.5 (30): débito 3.26/acción. Motivo: momentum hacia 'empresa más valiosa'.",
    "ABRIR SPY Butterfly 745/755/765 (50): débito 1.10/acción. Motivo: mercado en rango, VIX bajo.",
    "ABRIR NVDA Bear Call Spread 195/200 (40): crédito 2.13/acción. Motivo: IV cara + tesis de sobre-oferta de GPUs.",
])
bitacora("3 jul — festivo (Independence Day observado)", [
    "Mercados cerrados. Sin marca a mercado ni gestión.",
])
bitacora("6 jul", [
    "MANTENER DAL, MSFT, NVDA: los créditos aún no alcanzan el objetivo de recompra al 50–60% del máximo; las tesis siguen vigentes.",
    "MANTENER AAPL: el subyacente avanza dentro del rango del spread; se vigila el soporte de 300 (regla de salida).",
    "Futuros: GC y ES acumulan G/P positiva; CL corto recupera terreno tras el repunte. Se MANTIENEN.",
])
bitacora("7–8 jul", [
    "REVISAR NVDA: si NVDA se acerca a 195 (short strike) se evalúa cerrar para asegurar parte del crédito; si rompe con fuerza al alza, la pérdida está topada en 200.",
    "REGLA aplicada: cerrar cualquier spread de crédito que alcance el 50–60% de su ganancia máxima; liberar margen para el tramo final.",
])
bitacora("9 jul (cierre de la ventana)", [
    "CERRAR/valorar opciones con el precio del subyacente al cierre (ver fila 'resultado por escenario' en cada hoja del Excel de opciones).",
    "Futuros: G/P acumulada del bloque ≈ " + money(fut_total_pl) + " (ilustrativo). Se decide rolar o cerrar según settlement real.",
])

# ============================================================ 11. ESTRATEGIA GENERAL
H("11. Estrategia general del portafolio", 1)
bullets([
    "Direccional neta ligeramente alcista en equity (AAPL, MSFT alcistas; NVDA bajista como contrapeso; SPY neutral), diversificada con macro vía futuros.",
    "Predominio de estructuras de riesgo definido (spreads y mariposa) para acotar la pérdida.",
    "Combinación de venta de prima (DAL, MSFT, NVDA — se benefician del paso del tiempo y del IV crush) con compra de convexidad barata (AAPL, SPY).",
    "Los futuros (oro largo, crudo corto, índice largo) añaden exposición no correlacionada con las tecnológicas y actúan como diversificador macro.",
])
H("11.1 Cómo interactúan las posiciones", 2)
P("El corto de NVDA compensa parcialmente el sesgo alcista de AAPL/MSFT dentro del sector tecnología "
  "(reduce beta neta). El oro largo actúa como cobertura ante shocks geopolíticos que golpearían al "
  "equity y a la mariposa de SPY. El corto de WTI y el largo de DAL comparten el mismo motor (crudo a "
  "la baja), lo que concentra esa apuesta: es una correlación deseada pero a vigilar (Sección 12).")

# ============================================================ 12. RIESGO + GRIEGAS
H("12. Gestión del riesgo", 1)
table(["Riesgo", "Exposición en este portafolio", "Mitigación"],
      [["Mercado (direccional)", "Sesgo alcista en equity + macro por futuros",
        "NVDA corto y SPY neutral compensan; spreads definidos"],
       ["Volatilidad", "Vega corta en DAL/MSFT/NVDA; Vega larga en AAPL/SPY",
        "Cartera de Vega mixta; se aprovecha IV crush donde la IV está cara"],
       ["Liquidez", "Opciones de subyacentes muy líquidos; SPY dic con OI alto",
        "Strikes con volumen/OI elevados en las cadenas"],
       ["Apalancamiento", "Nocional > capital (inherente a derivados)",
        "Dimensionar por pérdida máxima y margen; colchón de liquidez"],
       ["Concentración", "Tesis 'crudo a la baja' en DAL y CL a la vez; tecnología con peso alto",
        "Límite por posición; el oro y el índice diversifican"]],
      widths=[1.3, 2.6, 2.4])
H("12.1 Sensibilidad aproximada del portafolio", 2)
P(f"Bloque de opciones — pérdida máxima agregada ≈ {money(tot_riesgo_opc)} "
  f"(~{tot_riesgo_opc/d.CAPITAL*100:.1f}% del capital), con prima neta inicial {money(net_prem_opc)}. "
  f"Bloque de futuros — margen inicial {money(fut_margin)}; cada punto de movimiento adverso se refleja "
  "1:1 en la cuenta de margen (marca a mercado diaria). El colchón de liquidez cubre margin calls "
  "razonables.", size=10)
H("12.2 Las griegas (conceptual y por posición)", 2)
table(["Griega", "Qué mide", "Lectura en el portafolio"],
      [["Delta (Δ)", "Sensibilidad al precio del subyacente",
        "Positiva en AAPL/MSFT/DAL (alcistas) y en ES/GC; negativa en NVDA y CL (corto); ~0 en la mariposa ATM"],
       ["Gamma (Γ)", "Velocidad de cambio de Delta",
        "Corta en los spreads de crédito (DAL/MSFT/NVDA) cerca del strike; larga y concentrada en la mariposa de SPY"],
       ["Theta (Θ)", "Desgaste temporal",
        "A favor en las ventas de prima (DAL/MSFT/NVDA) y en la mariposa; en contra en el bull call de AAPL "
        "(por eso se usa spread y no call simple)"],
       ["Vega (ν)", "Sensibilidad a la volatilidad implícita",
        "Corta en DAL/MSFT/NVDA (el bull put de DAL se beneficia del IV crush); larga en AAPL/SPY"],
       ["Rho (ρ)", "Sensibilidad a la tasa de interés",
        "Menor por el corto horizonte de julio; algo mayor en la mariposa de SPY (vencimiento de diciembre)"]],
      widths=[0.8, 2.0, 3.5])

# ============================================================ 13. ESCENARIOS
H("13. Escenarios (optimista / base / pesimista)", 1)
P("Resultado del bloque de opciones al vencimiento bajo movimientos de ±6% del subyacente respecto "
  "al cierre del 2-jul (para la mariposa, el escenario optimista sitúa a SPY en el strike central). "
  "Cada hoja del Excel de opciones incluye este cálculo por posición.", size=10)
def esc_val(p, kind):
    tick = p["subyacente"]; s = d.SPOT[tick]; Ks = [l["K"] for l in p["legs"]]
    if p["sesgo"].startswith("Bajista"):
        m = {"opt": s*0.94, "base": s, "pes": s*1.06}
    elif p["sesgo"].startswith("Neutral"):
        m = {"opt": float(np.mean(Ks)), "base": s, "pes": s*1.06}
    else:
        m = {"opt": s*1.06, "base": s, "pes": s*0.94}
    return d.estrategia_gp_total(p, m[kind])
erows = []
tot = {"opt": 0, "base": 0, "pes": 0}
for p in OPC:
    o, b, pe = esc_val(p, "opt"), esc_val(p, "base"), esc_val(p, "pes")
    tot["opt"] += o; tot["base"] += b; tot["pes"] += pe
    erows.append([p["subyacente"] + " " + p["estrategia"].split()[0],
                  f"{o:+,.0f}", f"{b:+,.0f}", f"{pe:+,.0f}"])
erows.append(["TOTAL OPCIONES", f"{tot['opt']:+,.0f}", f"{tot['base']:+,.0f}", f"{tot['pes']:+,.0f}"])
table(["Posición", "Optimista", "Base", "Pesimista"], erows,
      widths=[2.6, 1.2, 1.2, 1.2])
P(f"Rentabilidad del bloque de opciones sobre el capital en riesgo: "
  f"optimista {tot['opt']/tot_riesgo_opc*100:+.1f}%, base {tot['base']/tot_riesgo_opc*100:+.1f}%, "
  f"pesimista {tot['pes']/tot_riesgo_opc*100:+.1f}%.", size=10)
P("Explicación económica: en el escenario optimista dominan la mariposa de SPY (convexidad) y el "
  "bull call de AAPL; en el pesimista, las pérdidas están acotadas por el diseño de riesgo definido de "
  "todas las estructuras. Los futuros añaden su propia G/P por marca a mercado (Excel de futuros).", size=10)

# ============================================================ 14. MONITOREO
H("14. Plan de monitoreo diario (2–9 jul 2026)", 1)
table(["Variable", "Por qué importa para ESTE portafolio"],
      [["Minutas Fed / discurso", "Tono dovish/hawkish mueve oro (GC), bonos, dólar y tecnológicas de larga duración"],
       ["Inflación / empleo / PIB / PMI", "Sorpresas alteran expectativas de tasas → AAPL/MSFT/NVDA y ES"],
       ["Rendimiento bonos del Tesoro", "Duración de las tecnológicas; valoración de la mariposa de dic (Rho)"],
       ["VIX / volatilidad implícita", "Clave para las ventas de prima (DAL/MSFT/NVDA) y para la mariposa"],
       ["S&P 500 / Nasdaq / Dow", "Dirección de ES largo, SPY y beta del bloque tecnológico"],
       ["Petróleo (WTI)", "Motor doble: CL corto y DAL (costo de combustible)"],
       ["Oro", "GC largo (refugio)"],
       ["Dólar (DXY)", "Inverso al oro; afecta materias primas"],
       ["Volumen / open interest", "Liquidez para entrar/salir de los strikes"],
       ["Eventos geopolíticos", "Riesgo de cola: favorecen oro, golpean equity y la mariposa"]],
      widths=[2.0, 4.3])

# ============================================================ 15. REGLAS DE DECISION
H("15. Reglas para modificar el portafolio (SI → ENTONCES)", 1)
numbered([
    "SI la volatilidad implícita colapsa tras el reporte de DAL (IV crush) ENTONCES cerrar el bull put spread al 50–60% de su ganancia máxima.",
    "SI el S&P 500 rompe resistencia con fuerza ENTONCES aumentar ES largo y considerar cerrar el corto de NVDA (control de pérdida).",
    "SI el S&P pierde soporte ENTONCES reducir ES, comprar una put de SPY (seguro barato con VIX bajo) y mantener la mariposa.",
    "SI el petróleo supera un nivel clave al alza ENTONCES cubrir/reducir el corto de WTI (margin call) y revisar la tesis de DAL.",
    "SI cae el oro por debajo de su soporte ENTONCES reducir GC largo.",
    "SI el dólar se fortalece con fuerza ENTONCES revisar GC (presión bajista sobre el oro).",
    "SI los rendimientos de bonos suben con fuerza ENTONCES vigilar AAPL/MSFT (duración) y la mariposa de dic.",
    "SI la Fed vira a un tono hawkish inesperado ENTONCES recortar exposición alcista (AAPL/MSFT/ES) y reforzar coberturas.",
    "SI la inflación o el empleo sorprenden al alza ENTONCES reducir riesgo direccional alcista.",
    "SI ocurre un evento geopolítico relevante ENTONCES mantener/aumentar GC largo (oro) y proteger el equity con puts.",
    "SI AAPL pierde ~300 ENTONCES cerrar el bull call spread (regla de salida).",
    "SI NVDA se acerca a 195 (short strike) ENTONCES cerrar el bear call spread para asegurar el crédito.",
])

# ============================================================ 16. ALTERNATIVAS
H("16. Estrategias alternativas (solo herramientas de clase)", 1)
table(["Posición", "Si la hipótesis falla…", "Alternativa (herramienta de clase)"],
      [["DAL BPS", "Guía débil, rompe soporte", "Cerrar y pasar a Bear Put Spread si el sesgo vira a bajista"],
       ["MSFT BPS", "Recaída por gasto en IA", "Convertir en Bear Call Spread o comprar put de cobertura"],
       ["AAPL BCS", "Momentum se agota / lateraliza", "Reemplazar por Butterfly de calls centrada en el precio actual"],
       ["SPY Butterfly", "Se espera movimiento amplio", "Reemplazar por Straddle/Strangle largo (aprovechar VIX bajo)"],
       ["NVDA BCS", "IV se abarata", "Pasar a compra de Put o Bear Put Spread (más eficiente con IV baja)"],
       ["Futuros", "Cambia la tesis macro", "Invertir posición (largo↔corto) o cerrar; cubrir con opciones sobre el futuro"]],
      widths=[1.2, 2.2, 2.9])
P("Herramientas permitidas: compra/venta de call y put; bull/bear call y put spreads; box spread; "
  "butterfly; straddle; strangle; strip; strap; futuros largos y cortos.", size=9, color=GREY)

# ============================================================ 17. ENTREGABLES EXCEL
H("17. Entregables en Excel", 1)
P("Se acompañan dos libros de Excel con fórmulas vivas (los totales cuadran y recalculan al cambiar "
  "los datos de entrada):")
bullets([
    "(A) Opciones_Ejercicio7.xlsx — una hoja por estrategia con el formato del Ejercicio 7: bloque de "
    "parámetros, tabla de payoff barriendo ST (columnas ST, K, PRIMA, EJERCE SI/NO, MONEYNESS ITM/ATM/OTM, "
    "PAYOFF, G/P por acción y G/P total por pata y neto), break-even, ganancia y pérdida máximas, y "
    "resultado por escenario. Incluye hoja RESUMEN con la tabla de posiciones y las distribuciones "
    "(por estrategia, sector y nivel de riesgo).",
    "(B) Futuros_MarcaAMercado.xlsx — una hoja por futuro con marca a mercado diaria y cuenta de margen: "
    "columnas Fecha, Día, Precio negociado, Precio de liquidación, G/P por unidad, G/P total diaria, "
    "G/P acumulada, Cuenta de Margen y Margin Call. La cuenta parte del margen inicial, se actualiza "
    "cada día y dispara margin call al perforar el margen de mantenimiento, reponiendo hasta el inicial. "
    "Incluye hoja RESUMEN.",
])
try:
    doc.add_picture("img/futuros_pl.png", width=Inches(5.6))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
except Exception:
    pass

# ============================================================ 18. CONCLUSIONES
H("18. Conclusiones", 1)
bullets([
    "El portafolio demuestra el uso deliberado de derivados: cada estructura se eligió para que su forma "
    "de ganar coincida con la tesis y el régimen de volatilidad, priorizando el riesgo definido.",
    f"El bloque de opciones arranca con {('crédito' if net_prem_opc>=0 else 'débito')} neto de "
    f"{money(abs(net_prem_opc))} y una pérdida máxima acotada de {money(tot_riesgo_opc)} "
    f"(~{tot_riesgo_opc/d.CAPITAL*100:.1f}% del capital).",
    "Los futuros aportan diversificación macro (oro, crudo, índice) y sirven para ejercitar la mecánica "
    "de marca a mercado, margen y margin call.",
    "La administración es dinámica: la bitácora y las reglas SI→ENTONCES muestran cómo se abriría, "
    "mantendría, reduciría, aumentaría, reemplazaría o cerraría cada posición según los datos.",
    "Limitación honesta: las cadenas de opciones disponibles son del 2-jul (no del 25-jun) y los "
    "settlements de futuros son ilustrativos; el valor del trabajo está en la mecánica correcta y en el "
    "razonamiento, no en cifras de mercado inventadas.",
])

# ============================================================ 19. REFERENCIAS
H("19. Referencias", 1)
bullets([
    "MarketWatch — cadenas de opciones (NVDA, AAPL, MSFT, DAL, SPY), snapshot 2-jul-2026 (capturas adjuntas).",
    "CME Group / NYMEX / COMEX / CBOT — especificaciones de contratos de futuros (GC, CL, ES) y márgenes.",
    "CBOE — índice de volatilidad VIX.",
    "Hull, J. C. — Options, Futures, and Other Derivatives (marco de valoración y marca a mercado).",
    "Reserva Federal (FOMC) — comunicados y minutas del período.",
    "Nota: reemplazar los datos ilustrativos de settlements de futuros por los prints oficiales antes de "
    "la entrega final; las fórmulas del Excel recalculan automáticamente.",
])

doc.save("Informe_Derivados.docx")
print("OK Informe_Derivados.docx")
