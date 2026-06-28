# -*- coding: utf-8 -*-
"""Recreación en español de 'Top 10 skills of 2023' (World Economic Forum)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

# Colores por tipo de habilidad (según la versión original del WEF)
COG = "#5FC2B0"     # Habilidades cognitivas (verde azulado claro)
SELF = "#1C6FB0"    # Autoeficacia (azul)
MGMT = "#86BBE3"    # Habilidades de gestión (azul claro)
TECH = "#A98BC4"    # Habilidades tecnológicas (morado)
OTHERS = "#1A8A70"  # Trabajo con otros (verde)

FONDO = "#F4F4F2"
TXT = "#1a1a1a"
GRISL = "#cfd6da"

items = [
    (1, "Pensamiento analítico", COG, "bars"),
    (2, "Pensamiento creativo", COG, "gear"),
    (3, "Resiliencia, flexibilidad y agilidad", SELF, "bolt"),
    (4, "Motivación y autoconocimiento", SELF, "lens"),
    (5, "Curiosidad y aprendizaje permanente", SELF, "lensq"),
    (6, "Alfabetización tecnológica", TECH, "chip"),
    (7, "Fiabilidad y atención al detalle", SELF, "clip"),
    (8, "Empatía y escucha activa", OTHERS, "heart"),
    (9, "Liderazgo e influencia social", OTHERS, "star"),
    (10, "Control de calidad", MGMT, "quality"),
]


def draw_icon(ax, key, cx, cy, R):
    s = R * 0.62
    wc = "white"
    lw = 1.8
    gpt = R * 72  # radio del círculo en puntos
    if key == "bars":
        for i, h in enumerate([0.55, 1.0, 1.45]):
            ax.add_patch(Rectangle((cx - 0.78 * s + i * 0.55 * s, cy - 0.75 * s),
                                   0.34 * s, h * s, color=wc))
    elif key == "gear":
        ax.add_patch(Circle((cx, cy), 0.85 * s, fill=False, ec=wc, lw=lw))
        for ang in range(0, 360, 45):
            a = np.radians(ang)
            ax.add_patch(Rectangle((cx + 0.85 * s * np.cos(a) - 0.14 * s,
                                    cy + 0.85 * s * np.sin(a) - 0.14 * s),
                                   0.28 * s, 0.28 * s, color=wc))
        ax.add_patch(Circle((cx, cy), 0.34 * s, fill=False, ec=wc, lw=lw))
    elif key == "bolt":
        pts = [(0.18, 1.0), (-0.55, 0.05), (0.02, 0.08), (-0.18, -1.0),
               (0.55, 0.0), (0.0, -0.03)]
        ax.add_patch(Polygon([(cx + p[0] * s, cy + p[1] * s) for p in pts],
                             closed=True, color=wc))
    elif key in ("lens", "lensq"):
        ax.add_patch(Circle((cx - 0.18 * s, cy + 0.22 * s), 0.62 * s, fill=False, ec=wc, lw=lw + 0.4))
        ax.plot([cx + 0.26 * s, cx + 0.78 * s], [cy - 0.22 * s, cy - 0.74 * s],
                color=wc, lw=lw + 1.4, solid_capstyle="round")
        if key == "lensq":
            ax.text(cx - 0.18 * s, cy + 0.18 * s, "?", color=wc, ha="center",
                    va="center", fontsize=gpt * 0.5, fontweight="bold")
    elif key == "chip":
        ax.add_patch(FancyBboxPatch((cx - 0.58 * s, cy - 0.58 * s), 1.16 * s, 1.16 * s,
                                    boxstyle="round,pad=0.0,rounding_size=0.08",
                                    fill=False, ec=wc, lw=lw))
        ax.add_patch(Rectangle((cx - 0.24 * s, cy - 0.24 * s), 0.48 * s, 0.48 * s,
                               fill=False, ec=wc, lw=lw))
        for d in (-0.32, 0.0, 0.32):
            ax.plot([cx + d * s, cx + d * s], [cy + 0.58 * s, cy + 0.86 * s], color=wc, lw=lw)
            ax.plot([cx + d * s, cx + d * s], [cy - 0.58 * s, cy - 0.86 * s], color=wc, lw=lw)
            ax.plot([cx + 0.58 * s, cx + 0.86 * s], [cy + d * s, cy + d * s], color=wc, lw=lw)
            ax.plot([cx - 0.58 * s, cx - 0.86 * s], [cy + d * s, cy + d * s], color=wc, lw=lw)
    elif key == "clip":
        ax.add_patch(FancyBboxPatch((cx - 0.5 * s, cy - 0.82 * s), 1.0 * s, 1.55 * s,
                                    boxstyle="round,pad=0.0,rounding_size=0.06",
                                    fill=False, ec=wc, lw=lw))
        for yy in (0.38, 0.05):
            ax.plot([cx - 0.28 * s, cx + 0.28 * s], [cy + yy * s, cy + yy * s], color=wc, lw=lw)
        ax.plot([cx - 0.3 * s, cx - 0.08 * s, cx + 0.36 * s],
                [cy - 0.4 * s, cy - 0.6 * s, cy - 0.15 * s], color=wc, lw=lw + 0.6,
                solid_capstyle="round", solid_joinstyle="round")
    elif key == "heart":
        ax.text(cx, cy - 0.02 * s, "♥", color=wc, ha="center", va="center",
                fontsize=gpt * 0.95)
    elif key == "star":
        ax.plot([cx], [cy], marker="*", color=wc, markersize=gpt * 1.4, linestyle="none")
    elif key == "quality":
        ax.add_patch(FancyBboxPatch((cx - 0.5 * s, cy - 0.78 * s), 1.0 * s, 1.5 * s,
                                    boxstyle="round,pad=0.0,rounding_size=0.06",
                                    fill=False, ec=wc, lw=lw))
        ax.plot([cx - 0.28 * s, cx - 0.04 * s, cx + 0.4 * s],
                [cy + 0.02 * s, cy - 0.22 * s, cy + 0.42 * s], color=wc, lw=lw + 0.8,
                solid_capstyle="round", solid_joinstyle="round")


fig, ax = plt.subplots(figsize=(14.3, 7.5))
fig.patch.set_facecolor(FONDO)
ax.set_facecolor(FONDO)
ax.set_xlim(0, 14.3)
ax.set_ylim(-1.15, 7.6)
ax.set_aspect("equal")
ax.axis("off")

# Título
ax.text(0.55, 7.0, "Las 10 habilidades más importantes de 2023",
        fontsize=18, fontweight="bold", color=TXT, va="center")

# Logo WEF (texto)
ax.text(14.0, 7.05, "WORLD\nECONOMIC\nFORUM", fontsize=11, fontweight="bold",
        color="#16263a", ha="right", va="center", linespacing=1.05)

R = 0.30
rows_y = [5.5, 4.5, 3.5, 2.5, 1.5]
col_cx = {"L": 1.30, "R": 7.80}
col_num = {"L": 0.92, "R": 7.42}
col_tx = {"L": 1.72, "R": 8.28}
DIV = 6.95

for idx, (num, texto, color, icon) in enumerate(items):
    col = "L" if idx < 5 else "R"
    row = idx % 5
    cy = rows_y[row]
    cx = col_cx[col]
    ax.text(col_num[col], cy, f"{num}.", fontsize=14, color=TXT, ha="right", va="center")
    ax.add_patch(Circle((cx, cy), R, color=color, zorder=2))
    draw_icon(ax, icon, cx, cy, R)
    ax.text(col_tx[col], cy, texto, fontsize=11, color=TXT, va="center", fontweight="bold")
    if row < 4:
        xa = col_num[col] - 0.32
        xb = (DIV - 0.1 if col == "L" else 13.95)
        ax.plot([xa, xb], [cy - 0.5, cy - 0.5], color=GRISL, lw=0.8, zorder=1)

# Divisor vertical central
ax.plot([DIV, DIV], [1.0, 5.95], color=GRISL, lw=0.9)
ax.text(0, 0, "", color=FONDO)  # ancla

# Leyenda
ax.text(0.55, 0.62, "Tipo de habilidad", fontsize=12.5, fontweight="bold", color=TXT, va="center")
leg = [("Habilidades cognitivas", COG), ("Autoeficacia", SELF),
       ("Habilidades de gestión", MGMT), ("Habilidades tecnológicas", TECH),
       ("Trabajo con otros", OTHERS)]
x = 0.58
for label, color in leg:
    ax.add_patch(Rectangle((x, 0.02 - 0.12), 0.24, 0.24, color=color))
    ax.text(x + 0.34, 0.02, label, fontsize=11.5, color=TXT, va="center")
    x += 0.34 + 0.16 + len(label) * 0.118

# Fuente y nota
ax.plot([0.55, 13.95], [-0.45, -0.45], color=GRISL, lw=0.8)
ax.text(0.55, -0.66, "Fuente", fontsize=9, color="#666", va="center")
ax.text(0.55, -0.9, "Foro Económico Mundial, Informe sobre el Futuro del Empleo 2023.",
        fontsize=9, color="#333", va="center")
ax.text(8.1, -0.66, "Nota", fontsize=9, color="#666", va="center")
ax.text(8.1, -0.9, "Habilidades consideradas de mayor importancia\npara los trabajadores al momento de la encuesta.",
        fontsize=9, color="#333", va="top", linespacing=1.2)

path = os.path.join(OUT, "top10_habilidades_wef_es.png")
fig.savefig(path, dpi=220, bbox_inches="tight", facecolor=FONDO, pad_inches=0.25)
plt.close(fig)
print(path)
