# -*- coding: utf-8 -*-
"""Recreación en alta resolución del gráfico de tasa de culminación por quintil."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

años = list(range(2012, 2022))

# Series por quintil (valores anclados a las etiquetas 2012, 2016 y 2021)
q5 = [34.6, 35.5, 36.0, 36.3, 37.0, 38.4, 40.5, 42.0, 40.6, 37.3]
q4 = [25.6, 26.1, 24.8, 24.4, 27.7, 25.9, 28.1, 30.0, 29.5, 25.0]
q3 = [18.7, 18.4, 17.0, 16.2, 16.9, 17.7, 18.0, 20.2, 17.8, 18.5]
q2 = [12.0, 11.5, 11.4, 11.5, 11.9, 12.5, 13.2, 14.0, 14.3, 15.2]
q1 = [5.3, 5.6, 5.5, 5.2, 5.6, 6.2, 7.0, 7.2, 11.5, 8.2]

COL = {
    "q1": "#1F4E79",   # 1° Quintil - azul oscuro
    "q2": "#E84B9C",   # 2° Quintil - rosado
    "q3": "#F4A81D",   # 3° Quintil - naranja
    "q4": "#3FA34D",   # 4° Quintil - verde
    "q5": "#3C9FE0",   # 5° Quintil - celeste
}
CI = "#CFE3F3"  # banda de confianza celeste claro

# Semiancho del intervalo de confianza (se ensancha en los extremos)
def ci_halfwidth(n):
    base = [1.6, 1.3, 1.2, 1.2, 1.3, 1.5, 1.8, 2.1, 2.4, 2.6]
    return base[:n]

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
})

fig, ax = plt.subplots(figsize=(9.4, 5.8))

series = [("q1", q1, "1° Quintil"), ("q2", q2, "2° Quintil"),
          ("q3", q3, "3° Quintil"), ("q4", q4, "4° Quintil"),
          ("q5", q5, "5° Quintil")]

# Bandas de confianza
hw = ci_halfwidth(len(años))
for key, vals, _ in series:
    lo = [v - h for v, h in zip(vals, hw)]
    hi = [v + h for v, h in zip(vals, hw)]
    ax.fill_between(años, lo, hi, color=CI, alpha=0.85, linewidth=0, zorder=1)

# Líneas y marcadores
for key, vals, _ in series:
    ax.plot(años, vals, color=COL[key], linewidth=2.4, zorder=3,
            marker="o", markersize=6, markerfacecolor=COL[key],
            markeredgecolor="white", markeredgewidth=0.8)

# Etiquetas de valores (2012, 2016, 2021)
def etiqueta(x, y, texto, color, dx=0, dy=1.4, ha="center"):
    ax.annotate(texto, (x, y), xytext=(x + dx, y + dy), ha=ha, va="bottom",
                fontsize=10.5, fontweight="bold", color="#2b2b2b", zorder=5)

lab = {
    "q5": [(2012, 34.6, "34.6%**", 0.05, 1.4, "center"), (2016, 37.0, "37%**", 0, 1.5, "center"), (2021, 37.3, "37.3%**", 0.22, 1.3, "left")],
    "q4": [(2012, 25.6, "25.6%**", 0.05, 1.3, "center"), (2016, 27.7, "27.7%**", 0, 1.5, "center"), (2021, 25.0, "25%**", 0.22, 1.2, "left")],
    "q3": [(2012, 18.7, "18.7%**", 0.05, 1.3, "center"), (2016, 16.9, "16.9%**", 0, 1.4, "center"), (2021, 18.5, "18.5%**", 0.22, 1.2, "left")],
    "q2": [(2012, 12.0, "12%**", 0.05, 1.3, "center"), (2016, 11.9, "11.9%**", 0, 1.4, "center"), (2021, 15.2, "15.2%**", 0.22, 0.9, "left")],
    "q1": [(2012, 5.3, "5.3%**", 0.05, 1.3, "center"), (2016, 5.6, "5.6%**", 0, 1.3, "center"), (2021, 8.2, "8.2%**", 0.22, 1.0, "left")],
}
for key, items in lab.items():
    for x, y, t, dx, dy, ha in items:
        etiqueta(x, y, t, COL[key], dx, dy, ha)

# Ejes
ax.set_xlabel("Año", fontsize=11.5)
ax.set_ylabel("Tasa de culminación (%)", fontsize=11.5)
ax.set_xlim(2011.6, 2021.8)
ax.set_ylim(0, 46)
ax.set_xticks(años)
ax.set_yticks([15, 30, 45])
ax.set_yticklabels(["15%", "30%", "45%"])
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color("#9a9a9a")
ax.tick_params(colors="#4a4a4a")
ax.yaxis.grid(True, color="#e9e9e9", linewidth=0.8)
ax.set_axisbelow(True)

# Leyenda
handles = [Patch(facecolor=CI, edgecolor="none", label="Intervalo de\nConfianza (95%)")]
for key, _, name in series:
    handles.append(Line2D([0], [0], color=COL[key], marker="o", markersize=6,
                          markeredgecolor="white", linewidth=2.4, label=name))
leg = ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.12),
                ncol=6, frameon=False, fontsize=9.5, handlelength=1.6,
                columnspacing=1.4)

fig.tight_layout()
path = os.path.join(OUT, "tasa_culminacion_quintil.png")
fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(path)
