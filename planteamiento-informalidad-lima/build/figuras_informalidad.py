# -*- coding: utf-8 -*-
"""Generación de las 9 figuras del Planteamiento del Problema (300 dpi).

Tesis: "Factores socioeconómicos que influyen en la informalidad laboral en el
departamento de Lima en los años 2024-2025".

Todos los datos provienen de fuentes oficiales (OIT/ILOSTAT, INEI, CEPAL, CEPLAN)
con su cita correspondiente. No se han inventado datos: cuando una serie no está
disponible de forma continua, se grafican los puntos efectivamente documentados.
Estilo profesional y consistente, similar al de las notas metodológicas del MIDIS.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

# Paleta profesional y consistente
AZUL = "#1F4E79"      # azul oscuro (énfasis)
AZUL2 = "#2E75B6"     # azul medio
AZUL3 = "#9DC3E6"     # azul claro
NARANJA = "#C55A11"   # naranja (alerta / valores altos)
NARANJA2 = "#ED9B40"  # naranja claro
GRIS = "#7F7F7F"      # gris (referencia)
VERDE = "#548235"     # verde (valores bajos / Lima)
ROJO = "#9E2A2B"      # rojo oscuro

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "figure.dpi": 300,
})


def _save(fig, name):
    fig.tight_layout()
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("OK", name)
    return path


def _vlabels(ax, bars, fmt="{:.1f}", suffix="%", offset=0.012):
    ymax = max(b.get_height() for b in bars)
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + offset * ymax,
                fmt.format(b.get_height()) + suffix, ha="center", va="bottom",
                fontsize=9.5, fontweight="bold")


def _hlabels(ax, bars, fmt="{:.1f}", suffix="%", dx=0.6):
    for b in bars:
        ax.text(b.get_width() + dx, b.get_y() + b.get_height() / 2,
                fmt.format(b.get_width()) + suffix, va="center", ha="left",
                fontsize=9.5, fontweight="bold")


# ----------------------------------------------------------------------
# Figura 1. Empleo informal en el mundo según nivel de ingreso (OIT, 2024)
# ----------------------------------------------------------------------
def fig1_mundo_ingreso():
    cat = ["Países de\ningreso bajo", "Promedio\nmundial", "Países de\ningreso alto"]
    val = [88.0, 58.0, 13.0]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL2, VERDE], width=0.58)
    _vlabels(ax, bars)
    ax.set_title("Tasa de empleo informal en el mundo según nivel\nde ingreso de los países, 2024")
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig1_mundo_ingreso.png")


# ----------------------------------------------------------------------
# Figura 2. Informalidad laboral en América Latina por país (OIT, 2024)
# ----------------------------------------------------------------------
def fig2_america_latina():
    paises = ["Uruguay", "Chile", "Brasil", "Argentina", "México",
              "Colombia", "Perú", "Bolivia"]
    val = [22.0, 25.8, 37.2, 47.4, 53.1, 55.8, 73.6, 80.0]
    colors = [VERDE, VERDE, AZUL3, AZUL3, AZUL2, AZUL2, NARANJA, NARANJA]
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    bars = ax.barh(paises, val, color=colors, height=0.66)
    _hlabels(ax, bars)
    prom = 47.6
    ax.axvline(prom, color=GRIS, linestyle="--", linewidth=1.2)
    ax.annotate(f"Promedio regional: {prom:.1f}%",
                xy=(prom, 7.45), xytext=(prom - 2, 7.7),
                color=GRIS, fontsize=8.3, ha="right", va="bottom",
                fontweight="bold")
    ax.set_title("Tasa de informalidad laboral en países\nde América Latina, 2024")
    ax.set_xlabel("% de la población ocupada")
    ax.set_xlim(0, 92)
    ax.set_ylim(-0.6, 8.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.xaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig2_america_latina.png")


# ----------------------------------------------------------------------
# Figura 3. Evolución de la tasa de empleo informal en el Perú, 2011-2024
# ----------------------------------------------------------------------
def fig3_evolucion_peru():
    años = list(range(2011, 2025))
    tasa = [75.1, 74.3, 73.7, 72.8, 73.2, 72.0, 72.5, 72.4, 72.7,
            75.3, 76.8, 71.1, 71.1, 70.9]
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    ax.plot(años, tasa, marker="o", color=AZUL, linewidth=2.4, markersize=6)
    for x, y in zip(años, tasa):
        if x in (2011, 2019, 2020, 2021, 2022, 2024):
            ax.text(x, y + 0.55, f"{y:.1f}", ha="center", fontsize=8.6,
                    fontweight="bold", color=AZUL)
    # Sombra del repunte pandémico
    ax.axvspan(2019.7, 2021.3, color=NARANJA2, alpha=0.18)
    ax.text(2020.5, 78.0, "Pandemia\nCOVID-19", ha="center", fontsize=8.3,
            color=NARANJA, fontweight="bold")
    # Quiebre metodológico ENAHO -> EPEN
    ax.axvline(2021.5, color=GRIS, linestyle=":", linewidth=1.2)
    ax.text(2021.55, 70.0, "Cambio de fuente\nENAHO → EPEN", fontsize=7.6,
            color=GRIS, va="top")
    ax.set_title("Evolución de la tasa de empleo informal en el Perú, 2011-2024")
    ax.set_ylabel("% de la PEA ocupada")
    ax.set_xlabel("Año")
    ax.set_ylim(68, 80)
    ax.set_xticks(años)
    ax.set_xticklabels(años, rotation=45, fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig3_evolucion_peru.png")


# ----------------------------------------------------------------------
# Figura 4. Empleo informal en el Perú según rama de actividad (INEI, 2024)
# ----------------------------------------------------------------------
def fig4_sector():
    cat = ["Agricultura,\npesca y minería", "Construcción", "Comercio",
           "Manufactura", "Servicios"]
    val = [91.5, 76.9, 71.6, 63.6, 59.0]
    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL2, AZUL2, AZUL2, AZUL3], width=0.62)
    _vlabels(ax, bars)
    ax.axhline(70.9, color=GRIS, linestyle="--", linewidth=1.1)
    ax.text(4.45, 72.2, "Promedio\nnacional: 70,9%", fontsize=7.8, color=GRIS, ha="right")
    ax.set_title("Tasa de empleo informal en el Perú según\nrama de actividad económica, 2024")
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig4_sector.png")


# ----------------------------------------------------------------------
# Figura 5. Empleo informal en el Perú según nivel educativo (INEI, 2024)
# ----------------------------------------------------------------------
def fig5_educativo():
    cat = ["Primaria\no menos", "Secundaria", "Superior\nuniversitaria"]
    val = [94.6, 81.2, 37.9]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL2, VERDE], width=0.58)
    _vlabels(ax, bars)
    ax.set_title("Tasa de empleo informal en el Perú según\nnivel educativo alcanzado, 2024")
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig5_educativo.png")


# ----------------------------------------------------------------------
# Figura 6. Empleo informal en el Perú según tamaño de empresa (INEI, 2024)
# ----------------------------------------------------------------------
def fig6_tamano_empresa():
    cat = ["Pequeña empresa\n(1 a 10 trab.)", "Promedio\nnacional",
           "Gran empresa\n(51 y más trab.)"]
    val = [88.6, 70.9, 15.6]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL2, VERDE], width=0.58)
    _vlabels(ax, bars)
    ax.set_title("Tasa de empleo informal en el Perú según\ntamaño de empresa, 2024")
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig6_tamano_empresa.png")


# ----------------------------------------------------------------------
# Figura 7. Empleo informal en el Perú según grupos de edad (INEI, 2024)
# ----------------------------------------------------------------------
def fig7_edad():
    cat = ["14 a 24 años", "25 a 44 años", "45 y más años"]
    val = [85.4, 67.1, 71.2]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL3, AZUL2], width=0.55)
    _vlabels(ax, bars)
    ax.axhline(70.9, color=GRIS, linestyle="--", linewidth=1.1)
    ax.text(2.45, 72.2, "Promedio\nnacional: 70,9%", fontsize=7.8, color=GRIS, ha="right")
    ax.set_title("Tasa de empleo informal en el Perú según\ngrupos de edad, 2024")
    ax.set_ylabel("% de la población ocupada")
    ax.set_xlabel("Grupo de edad")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig7_edad.png")


# ----------------------------------------------------------------------
# Figura 8. Empleo informal según sexo y área de residencia (INEI, 2024)
# ----------------------------------------------------------------------
def fig8_sexo_area():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.2))
    # Panel a: sexo
    ax = axes[0]
    bars = ax.bar(["Hombres", "Mujeres"], [68.8, 73.1],
                  color=[AZUL2, NARANJA], width=0.5)
    _vlabels(ax, bars)
    ax.set_title("Según sexo", fontsize=11)
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    # Panel b: área
    ax = axes[1]
    bars = ax.bar(["Urbana", "Rural"], [65.1, 94.6],
                  color=[AZUL2, NARANJA], width=0.5)
    _vlabels(ax, bars)
    ax.set_title("Según área de residencia", fontsize=11)
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    fig.suptitle("Tasa de empleo informal en el Perú según sexo y área de residencia, 2024",
                 fontsize=11.5, fontweight="bold", y=1.02)
    return _save(fig, "fig8_sexo_area.png")


# ----------------------------------------------------------------------
# Figura 9. Lima frente a las principales ciudades del Perú (INEI, 2024)
# ----------------------------------------------------------------------
def fig9_lima_ciudades():
    ciudades = ["Lima\nMetropolitana", "Tumbes", "Promedio\nnacional",
                "Ayacucho", "Pucallpa", "Juliaca"]
    val = [54.8, 69.7, 70.9, 71.2, 73.0, 82.5]
    colors = [VERDE, AZUL3, GRIS, AZUL2, AZUL2, NARANJA]
    fig, ax = plt.subplots(figsize=(7.8, 4.5))
    bars = ax.barh(ciudades, val, color=colors, height=0.62)
    _hlabels(ax, bars)
    ax.set_title("Informalidad laboral de Lima frente a las\nprincipales ciudades del Perú, 2024")
    ax.set_xlabel("% de la población ocupada")
    ax.set_xlim(0, 95)
    ax.spines[["top", "right"]].set_visible(False)
    ax.xaxis.grid(True, linestyle=":", alpha=0.5)
    # Resaltar Lima
    ax.get_yticklabels()[0].set_fontweight("bold")
    ax.get_yticklabels()[0].set_color(VERDE)
    return _save(fig, "fig9_lima_ciudades.png")


def build_all():
    fig1_mundo_ingreso()
    fig2_america_latina()
    fig3_evolucion_peru()
    fig4_sector()
    fig5_educativo()
    fig6_tamano_empresa()
    fig7_edad()
    fig8_sexo_area()
    fig9_lima_ciudades()


if __name__ == "__main__":
    build_all()
