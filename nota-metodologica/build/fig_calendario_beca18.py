# -*- coding: utf-8 -*-
"""Calendario tipo Gantt para la intervención de Beca 18 (Excel + IA, diseño PSM)."""
import os
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

NAVY = "#1F3864"
NAVY2 = "#2E5A88"
BAR_BLUE = "#2F6FAB"
BAR_GREEN = "#7CB342"
BAR_LBLUE = "#9DC3E6"
GRID = "#C9D2DC"
ROWALT = "#F2F5F9"

# ---- Meses (30 meses: Jul 2026 - Dic 2028) ----
month_abbr = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]
seq = []
y, m = 2026, 7  # arranca Jul 2026
for i in range(30):
    seq.append((y, m))
    m += 1
    if m > 12:
        m = 1
        y += 1
NMON = len(seq)
years = {}
for idx, (yy, mm) in enumerate(seq):
    years.setdefault(yy, []).append(idx + 1)  # columnas 1..30

COLORS = {"blue": BAR_BLUE, "green": BAR_GREEN, "lblue": BAR_LBLUE}

phases = [
    ("FASE 1", "Diseño y preparación", [
        ("Diseño final del programa y convenios interinstitucionales", "Pronabec / MINEDU / MTPE", "Coordinación y financiamiento", (1, 3), "blue"),
        ("Desarrollo de plataforma y contenidos (Excel + IA)", "Equipo técnico", "Macros, automatización, IA", (1, 4), "blue"),
        ("Preregistro del plan de análisis", "Equipo evaluador", "Fija H1 como resultado primario", (2, 4), "blue"),
    ]),
    ("FASE 2", "Convocatoria y línea de base", [
        ("Convocatoria e inscripción voluntaria de becarios", "Pronabec", "Participación libre y abierta", (4, 5), "blue"),
        ("Levantamiento de línea de base (encuesta)", "Equipo evaluador", "Incluye módulo de mecanismo (H4)", (4, 6), "blue"),
    ]),
    ("FASE 3", "Ejecución del programa", [
        ("Ejecución del programa (16 semanas)", "Docentes / mentores", "Excel, IA y empleabilidad", (5, 9), "blue"),
        ("Mentoría y bolsa laboral", "Equipo / Empresas", "Vinculación con empresas", (7, 10), "blue"),
        ("Egreso de la cohorte tratada", "Pronabec / IES", "Hito de cierre del curso", (11, 11), "green"),
    ]),
    ("FASE 4", "Emparejamiento y seguimiento", [
        ("Construcción del grupo de comparación (PSM)", "Equipo evaluador", "Gemelo estadístico por área", (11, 13), "blue"),
        ("Cruce de registros administrativos (Planilla MTPE / SUNAT)", "Equipo / MTPE", "Datos anonimizados por DNI", (12, 24), "green"),
        ("Seguimiento a 6 meses (registros + encuesta)", "Equipo evaluador", "Resultado principal (H1)", (16, 18), "blue"),
        ("Seguimiento a 12 meses (registros + encuesta)", "Equipo evaluador", "Resultado principal (H1)", (22, 24), "blue"),
    ]),
    ("FASE 5", "Análisis y difusión", [
        ("Estimación de impacto (ATT) y costo-efectividad", "Equipo evaluador", "Estimador doblemente robusto", (24, 28), "blue"),
        ("Informe final, difusión y repositorio abierto", "Pronabec / Equipo", "Ciencia abierta", (28, 30), "lblue"),
    ]),
]

# ---- Geometría ----
X_FASE = (0.0, 0.55)
X_ACT = (0.55, 4.7)
X_RESP = (4.7, 6.5)
X_NOTAS = (6.5, 8.4)
GX0 = 8.4
WCOL = 0.30
GX1 = GX0 + NMON * WCOL
RH = 0.62
HEAD = 3  # filas de encabezado

nrows = HEAD + sum(1 + len(a) for _, _, a in phases)
TOTAL_H = nrows * RH

fig, ax = plt.subplots(figsize=(16.2, 0.46 * nrows + 1.2))
ax.set_xlim(-0.05, GX1 + 0.05)
ax.set_ylim(0, TOTAL_H)
ax.invert_yaxis()
ax.axis("off")


def ytop(r):
    return r * RH


def cell(x0, x1, r0, r1, fc, ec=None, lw=0.5):
    ax.add_patch(Rectangle((x0, ytop(r0)), x1 - x0, (r1 - r0) * RH,
                           facecolor=fc, edgecolor=ec, linewidth=lw, zorder=1))


def txt(x, r, s, **kw):
    ax.text(x, ytop(r) + RH / 2, s, va="center", zorder=4, **kw)


# ===== Encabezado superior =====
# Banda izquierda (títulos de columnas) en navy, filas 0-2
cell(0, GX0, 0, 3, NAVY)
for (x0, x1), name in [(X_FASE, "Fase"), (X_ACT, "Actividad"),
                       (X_RESP, "Responsable"), (X_NOTAS, "Notas")]:
    ax.text((x0 + x1) / 2, ytop(2) + RH / 2, name, va="center", ha="center",
            color="white", fontsize=8.5, fontweight="bold", zorder=4)

# Fila de años
for yy, cols in years.items():
    a, b = cols[0], cols[-1]
    x0 = GX0 + (a - 1) * WCOL
    x1 = GX0 + b * WCOL
    cell(x0, x1, 0, 1, NAVY, ec="white", lw=0.8)
    ax.text((x0 + x1) / 2, ytop(0) + RH / 2, str(yy), va="center", ha="center",
            color="white", fontsize=9, fontweight="bold", zorder=4)

# Fila de número de mes y de nombre de mes
for i, (yy, mm) in enumerate(seq):
    x0 = GX0 + i * WCOL
    cell(x0, x0 + WCOL, 1, 2, NAVY2, ec="white", lw=0.5)
    cell(x0, x0 + WCOL, 2, 3, NAVY, ec="white", lw=0.5)
    ax.text(x0 + WCOL / 2, ytop(1) + RH / 2, str(i + 1), va="center", ha="center",
            color="white", fontsize=6.2, zorder=4)
    ax.text(x0 + WCOL / 2, ytop(2) + RH / 2, month_abbr[mm - 1], va="center", ha="center",
            color="white", fontsize=5.8, zorder=4)

# ===== Filas de contenido =====
r = HEAD
for fase, subt, acts in phases:
    # fila de fase (navy, ancho completo)
    cell(0, GX1, r, r + 1, NAVY)
    ax.text(X_FASE[0] + 0.08, ytop(r) + RH / 2, f"{fase}  ·  {subt}", va="center", ha="left",
            color="white", fontsize=8, fontweight="bold", zorder=4)
    r += 1
    for j, (act, resp, nota, (a, b), color) in enumerate(acts):
        # fondo alterno
        if j % 2 == 1:
            cell(0, GX0, r, r + 1, ROWALT)
        # grilla de meses (fondo)
        for i in range(NMON):
            x0 = GX0 + i * WCOL
            cell(x0, x0 + WCOL, r, r + 1, "white", ec=GRID, lw=0.4)
        # textos
        ax.text(X_ACT[0] + 0.12, ytop(r) + RH / 2, textwrap.fill(act, 40),
                va="center", ha="left", fontsize=6.6, zorder=4, color="#1a1a1a")
        ax.text(X_RESP[0] + 0.08, ytop(r) + RH / 2, textwrap.fill(resp, 18),
                va="center", ha="left", fontsize=6.3, zorder=4, color="#333")
        ax.text(X_NOTAS[0] + 0.08, ytop(r) + RH / 2, textwrap.fill(nota, 22),
                va="center", ha="left", fontsize=6.0, zorder=4, color="#555", style="italic")
        # barra Gantt
        bx0 = GX0 + (a - 1) * WCOL
        bw = (b - a + 1) * WCOL
        ax.add_patch(Rectangle((bx0 + 0.03, ytop(r) + 0.12), bw - 0.06, RH - 0.24,
                               facecolor=COLORS[color], edgecolor="white", linewidth=0.5, zorder=3))
        r += 1

# Líneas divisorias de columnas izquierdas
for xb in [X_FASE[1], X_ACT[1], X_RESP[1], X_NOTAS[1]]:
    ax.plot([xb, xb], [0, TOTAL_H], color="white", lw=0.8, zorder=2)
# Separadores de año (verticales gruesos)
for yy, cols in list(years.items())[1:]:
    xb = GX0 + (cols[0] - 1) * WCOL
    ax.plot([xb, xb], [ytop(HEAD), TOTAL_H], color="#8aa0b8", lw=0.9, zorder=2)

# ===== Título y leyenda =====
ax.text((0 + GX1) / 2, -0.9, "Tabla 5. Calendario de actividades para la intervención propuesta "
        "«Fortalecimiento de competencias en Excel e IA – Beca 18»",
        ha="center", va="center", fontsize=12.5, fontweight="bold", color="#1a1a1a")

leg_y = TOTAL_H + 0.5
items = [("Actividad principal", BAR_BLUE),
         ("Ventana de registros administrativos / hito", BAR_GREEN),
         ("Difusión de resultados", BAR_LBLUE)]
lx = 0.1
ax.text(lx, leg_y, "Leyenda:", va="center", fontsize=8.5, fontweight="bold")
lx += 1.2
for label, color in items:
    ax.add_patch(Rectangle((lx, leg_y - 0.18), 0.45, 0.36, facecolor=color, edgecolor="white"))
    ax.text(lx + 0.6, leg_y, label, va="center", fontsize=8)
    lx += 0.6 + len(label) * 0.115 + 0.6

ax.set_ylim(leg_y + 0.6, -1.3)  # deja espacio para título arriba y leyenda abajo

path = os.path.join(OUT, "calendario_beca18.png")
fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.2)
plt.close(fig)
print(path)
