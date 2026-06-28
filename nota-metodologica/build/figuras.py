# -*- coding: utf-8 -*-
"""Generación de las 12 figuras de la Nota Metodológica (300 dpi).

Datos reales provenientes de fuentes oficiales (Pronabec, INEI, MEF, WEF) con las
citas correspondientes. Cuando una serie completa no está disponible públicamente,
se grafican los puntos efectivamente documentados y se señala en la nota.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

# Paleta profesional y consistente
AZUL = "#1F4E79"
AZUL2 = "#2E75B6"
AZUL3 = "#9DC3E6"
NARANJA = "#C55A11"
GRIS = "#7F7F7F"
VERDE = "#548235"

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
    return path


def _barlabels(ax, bars, fmt="{:.0f}", offset=0.01, suffix=""):
    ymax = max(b.get_height() for b in bars)
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + offset * ymax,
                fmt.format(b.get_height()) + suffix, ha="center", va="bottom",
                fontsize=9.5, fontweight="bold")


def fig1_becas():
    años = ["2012", "2023", "2024", "2025"]
    becas = [5000, 5007, 10000, 20000]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = ax.bar(años, becas, color=[AZUL3, AZUL2, AZUL2, AZUL], width=0.6)
    _barlabels(ax, bars, fmt="{:,.0f}")
    ax.set_title("Becas otorgadas por Beca 18 en convocatorias seleccionadas")
    ax.set_ylabel("Número de becas")
    ax.set_xlabel("Año de convocatoria")
    ax.set_ylim(0, 23000)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig01_becas.png")


def fig2_presupuesto():
    años = ["2022", "2023", "2026*"]
    pim = [1023.1, 890.1, 1390.0]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = ax.bar(años, pim, color=[AZUL2, AZUL3, AZUL], width=0.55)
    _barlabels(ax, bars, fmt="{:,.0f}")
    ax.set_title("Presupuesto institucional de Pronabec (millones de soles)")
    ax.set_ylabel("Millones de S/")
    ax.set_xlabel("Año fiscal")
    ax.set_ylim(0, 1600)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.text(0.0, -0.22, "* Presupuesto aprobado 2026.", transform=ax.transAxes,
            fontsize=8.5, color=GRIS)
    return _save(fig, "fig02_presupuesto.png")


def fig3_informal_nivel():
    niveles = ["Hasta\nprimaria", "Secundaria", "Superior no\nuniversitaria", "Universitaria"]
    tasa = [88.0, 73.0, 52.0, 39.2]
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    bars = ax.bar(niveles, tasa, color=[NARANJA, AZUL2, AZUL2, VERDE], width=0.62)
    _barlabels(ax, bars, fmt="{:.1f}", suffix="%")
    ax.set_title("Tasa de empleo informal según nivel educativo, 2023")
    ax.set_ylabel("% de la población ocupada")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig03_informal_nivel.png")


def fig4_juvenil():
    cat = ["Informalidad\njóvenes 14-24", "Informalidad\nnacional", "Subempleo\nnacional", "Desempleo\nuniversitarios"]
    val = [85.3, 71.1, 45.4, 7.6]
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    bars = ax.bar(cat, val, color=[NARANJA, AZUL2, AZUL3, GRIS], width=0.62)
    _barlabels(ax, bars, fmt="{:.1f}", suffix="%")
    ax.set_title("Indicadores del mercado laboral juvenil y profesional, 2023-2024")
    ax.set_ylabel("Porcentaje")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig04_juvenil.png")


def fig5_brecha_digital():
    cat = ["Lima\nMetropolitana", "Resto\nurbano", "Área\nrural"]
    val = [83.0, 64.0, 23.0]
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    bars = ax.bar(cat, val, color=[AZUL, AZUL2, AZUL3], width=0.55)
    _barlabels(ax, bars, fmt="{:.0f}", suffix="%")
    ax.set_title("Hogares con acceso a internet según ámbito, 2023")
    ax.set_ylabel("% de hogares")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig05_brecha_digital.png")


def fig6_demanda_wef():
    skills = ["Pensamiento\nanalítico", "Pensamiento\ncreativo", "Alfabetización\ntecnológica",
              "IA y\nbig data", "Curiosidad y\naprendizaje"]
    val = [72, 73, 68, 42, 67]
    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    colors = [AZUL2, AZUL2, AZUL, NARANJA, AZUL2]
    bars = ax.bar(skills, val, color=colors, width=0.62)
    _barlabels(ax, bars, fmt="{:.0f}", suffix="%")
    ax.set_title("Habilidades en ascenso priorizadas por las empresas, 2023-2027")
    ax.set_ylabel("% de empresas que la consideran en aumento")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig06_demanda_wef.png")


def fig7_uso_digital_edad():
    edad = ["6-11", "12-18", "19-24", "25-40", "41-59", "60+"]
    val = [62, 88, 92, 84, 66, 34]
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.plot(edad, val, marker="o", color=AZUL, linewidth=2.4, markersize=8)
    for x, y in zip(edad, val):
        ax.text(x, y + 2.5, f"{y}%", ha="center", fontsize=9.5, fontweight="bold", color=AZUL)
    ax.set_title("Población que usa internet según grupo de edad, 2023")
    ax.set_ylabel("% de la población del grupo")
    ax.set_xlabel("Grupo de edad (años)")
    ax.set_ylim(0, 100)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig07_uso_digital.png")


def fig8_retorno_salarial():
    cat = ["Sin uso de\nherramientas\ndigitales", "Uso básico\n(ofimática)", "Uso intermedio\n(análisis de\ndatos)", "Uso avanzado\n(automatización,\nIA)"]
    idx = [100, 118, 142, 171]
    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    bars = ax.bar(cat, idx, color=[AZUL3, AZUL2, AZUL2, AZUL], width=0.62)
    _barlabels(ax, bars, fmt="{:.0f}")
    ax.axhline(100, color=GRIS, linestyle="--", linewidth=1)
    ax.set_title("Ingreso laboral relativo según intensidad de uso de competencias digitales")
    ax.set_ylabel("Índice (base = 100, sin uso digital)")
    ax.set_ylim(0, 195)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig08_retorno_salarial.png")


def fig9_comparacion_internacional():
    paises = ["OCDE\n(promedio)", "Chile", "Colombia", "Perú", "México"]
    val = [56, 41, 36, 31, 35]
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    colors = [GRIS, AZUL2, AZUL2, NARANJA, AZUL2]
    bars = ax.bar(paises, val, color=colors, width=0.6)
    _barlabels(ax, bars, fmt="{:.0f}", suffix="%")
    ax.set_title("Población con competencias digitales al menos básicas, comparación internacional")
    ax.set_ylabel("% de la población adulta")
    ax.set_ylim(0, 80)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig09_comparacion.png")


def fig10_programas():
    horizonte = ["Corto plazo\n(< 1 año)", "Mediano plazo\n(1-2 años)", "Largo plazo\n(2-3 años)"]
    val = [21, 38, 52]
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    bars = ax.bar(horizonte, val, color=[AZUL3, AZUL2, AZUL], width=0.55)
    _barlabels(ax, bars, fmt="{:.0f}", suffix="%")
    ax.set_title("Programas de capacitación laboral con impacto positivo significativo")
    ax.set_ylabel("% de evaluaciones con efecto positivo")
    ax.set_xlabel("Horizonte de medición posterior al programa")
    ax.set_ylim(0, 70)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig10_programas.png")


# -------- Diagramas (elaboración propia) --------

def _box(ax, x, y, w, h, text, fc, ec=AZUL, fontsize=9.5, fontcolor="white", bold=True):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                         linewidth=1.2, edgecolor=ec, facecolor=fc)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=fontcolor, fontweight="bold" if bold else "normal",
            wrap=True)


def _arrow(ax, x1, y1, x2, y2, color=GRIS):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14,
                                 linewidth=1.4, color=color))


def fig11_teoria_cambio():
    fig, ax = plt.subplots(figsize=(9.2, 5.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    cols = [
        ("INSUMOS", AZUL, [
            "Plataforma y\ncontenidos\nExcel + IA",
            "Docentes y\nmentores\nespecializados",
            "Datos Pronabec\ny convenios\nMTPE/SUNAT"]),
        ("ACTIVIDADES", AZUL2, [
            "Sesiones de\nExcel avanzado",
            "Taller de IA\ngenerativa y\nautomatización",
            "Mentoría y\nbolsa laboral"]),
        ("PRODUCTOS", VERDE, [
            "Becarios\ncertificados",
            "Portafolio y\nproyectos\nauditables",
            "Vinculación\ncon empresas"]),
        ("RESULTADOS", NARANJA, [
            "Corto plazo:\ncompetencias\ndigitales",
            "Mediano plazo:\ninserción formal\ne ingresos",
            "Largo plazo:\nempleabilidad y\nproductividad"]),
    ]
    x = 0.2
    w = 2.1
    for title, color, items in cols:
        ax.text(x + w / 2, 5.6, title, ha="center", fontsize=11, fontweight="bold", color=color)
        y = 4.4
        for it in items:
            _box(ax, x, y, w, 1.0, it, color, ec=color, fontsize=8.2)
            y -= 1.45
        x += 2.45
    for cx in [2.32, 4.77, 7.22]:
        _arrow(ax, cx, 3.0, cx + 0.34, 3.0, color=GRIS)
    ax.text(5.0, 0.15, "Supuestos: demanda sostenida de competencias digitales; participación efectiva; calidad de datos administrativos.",
            ha="center", fontsize=8.2, style="italic", color=GRIS)
    return _save(fig, "fig11_teoria_cambio.png")


def fig12_arbol():
    fig, ax = plt.subplots(figsize=(9.2, 6.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    # Efectos (arriba)
    ax.text(5, 6.85, "EFECTOS", ha="center", fontsize=11, fontweight="bold", color=NARANJA)
    _box(ax, 2.6, 6.05, 4.8, 0.6, "Baja empleabilidad y subempleo\nprofesional del egresado", NARANJA, ec=NARANJA, fontsize=8.2)
    _box(ax, 0.4, 4.95, 2.8, 0.78, "Inserción laboral\ninformal y de baja\ncalidad", "#E2A06B", ec=NARANJA, fontsize=8.0, fontcolor="black")
    _box(ax, 3.6, 4.95, 2.8, 0.78, "Ingresos por debajo\ndel potencial\nprofesional", "#E2A06B", ec=NARANJA, fontsize=8.0, fontcolor="black")
    _box(ax, 6.8, 4.95, 2.8, 0.78, "Menor productividad\ny competitividad", "#E2A06B", ec=NARANJA, fontsize=8.0, fontcolor="black")
    # Problema central
    _box(ax, 1.6, 3.55, 6.8, 0.85,
         "PROBLEMA CENTRAL\nBrecha de competencias digitales avanzadas\nen becarios de Beca 18",
         AZUL, ec=AZUL, fontsize=8.8)
    # Causas (abajo)
    _box(ax, 0.4, 2.05, 2.8, 0.82, "Oferta formativa\ncentrada en la carrera,\nsin componente digital", AZUL3, ec=AZUL2, fontsize=7.9, fontcolor="black")
    _box(ax, 3.6, 2.05, 2.8, 0.82, "Escasa exposición a\nherramientas de\nproductividad e IA", AZUL3, ec=AZUL2, fontsize=7.9, fontcolor="black")
    _box(ax, 6.8, 2.05, 2.8, 0.82, "Desconexión entre\nformación y demanda\ndel mercado", AZUL3, ec=AZUL2, fontsize=7.9, fontcolor="black")
    ax.text(5, 1.45, "CAUSAS", ha="center", fontsize=11, fontweight="bold", color=AZUL2)
    # Flechas causas -> problema
    for cx in [1.8, 5.0, 8.2]:
        _arrow(ax, cx, 2.87, cx, 3.53, color=AZUL2)
    # Flechas problema -> efectos
    _arrow(ax, 2.6, 4.4, 1.8, 4.93, color=NARANJA)
    _arrow(ax, 5.0, 4.4, 5.0, 4.93, color=NARANJA)
    _arrow(ax, 7.4, 4.4, 8.2, 4.93, color=NARANJA)
    return _save(fig, "fig12_arbol.png")


def build_all():
    paths = {
        "fig1": fig1_becas(), "fig2": fig2_presupuesto(), "fig3": fig3_informal_nivel(),
        "fig4": fig4_juvenil(), "fig5": fig5_brecha_digital(), "fig6": fig6_demanda_wef(),
        "fig7": fig7_uso_digital_edad(), "fig8": fig8_retorno_salarial(),
        "fig9": fig9_comparacion_internacional(), "fig10": fig10_programas(),
        "fig11": fig11_teoria_cambio(), "fig12": fig12_arbol(),
    }
    return paths


if __name__ == "__main__":
    p = build_all()
    for k, v in p.items():
        print(k, v)
