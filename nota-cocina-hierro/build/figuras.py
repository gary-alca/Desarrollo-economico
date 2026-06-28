# -*- coding: utf-8 -*-
"""Generación de figuras de la Nota Metodológica "Cocina con Hierro" (300 dpi).

Datos reales provenientes de fuentes oficiales (INEI-ENDES, MIDIS-JUNTOS) con sus
citas correspondientes. Cuando una serie completa no está disponible públicamente,
se grafican únicamente los puntos efectivamente documentados y se señala en la nota.
Las figuras conceptuales (árbol de problemas, teoría del cambio, diseño phase-in) y
la curva de poder son de elaboración propia con fines ilustrativos.
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
ROJO = "#9E2A2B"     # color institucional asociado a hierro/sangre
ROJO2 = "#C0504D"
VINO = "#7B1E22"
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


# ============================================================
# FIGURAS DE DATOS REALES
# ============================================================

def fig1_evolucion_anemia():
    """Evolución de la prevalencia de anemia 6-35 meses (ENDES/INEI).
    Solo años con cifra oficial consolidada localizada."""
    años = ["2019", "2021", "2023", "2024"]
    val = [40.1, 38.8, 43.1, 43.7]
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.plot(años, val, marker="o", color=ROJO, linewidth=2.6, markersize=9)
    for x, y in zip(años, val):
        ax.text(x, y + 0.6, f"{y}%", ha="center", fontsize=10, fontweight="bold", color=ROJO)
    ax.axhline(40, color=GRIS, linestyle="--", linewidth=1)
    ax.set_title("Prevalencia de anemia en niñas y niños de 6 a 35 meses, Perú")
    ax.set_ylabel("% de la población de 6 a 35 meses")
    ax.set_xlabel("Año (ENDES)")
    ax.set_ylim(30, 50)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.text(0.0, -0.22,
            "Nota: se grafican los años con cifra oficial consolidada bajo el punto de corte vigente hasta 2023.",
            transform=ax.transAxes, fontsize=8.0, color=GRIS)
    return _save(fig, "fig01_evolucion_anemia.png")


def fig2_urbano_rural():
    """Anemia por área de residencia, 2023 y 2024 (INEI-ENDES)."""
    grupos = ["Nacional", "Urbana", "Rural"]
    v2023 = [43.1, 40.2, 50.3]
    v2024 = [43.7, np.nan, 51.9]
    x = np.arange(len(grupos))
    w = 0.38
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    b1 = ax.bar(x - w / 2, v2023, w, label="2023", color=ROJO2)
    b2 = ax.bar(x + w / 2, [0 if np.isnan(v) else v for v in v2024], w,
                label="2024", color=VINO)
    for b, v in zip(b1, v2023):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.7, f"{v}", ha="center",
                fontsize=9, fontweight="bold")
    for b, v in zip(b2, v2024):
        if not np.isnan(v):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.7, f"{v}", ha="center",
                    fontsize=9, fontweight="bold")
    ax.set_title("Anemia en niñas y niños de 6 a 35 meses por área de residencia")
    ax.set_ylabel("% de la población de 6 a 35 meses")
    ax.set_xticks(x)
    ax.set_xticklabels(grupos)
    ax.set_ylim(0, 60)
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig02_urbano_rural.png")


def fig3_departamentos():
    """Departamentos con mayor prevalencia de anemia, 2023 (INEI-ENDES)."""
    dep = ["Puno", "Ucayali", "Madre de\nDios", "Loreto", "Pasco", "Nacional"]
    val = [70.4, 59.4, 58.3, 53.0, 52.0, 43.1]
    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    colors = [VINO, ROJO, ROJO, ROJO2, ROJO2, GRIS]
    bars = ax.bar(dep, val, color=colors, width=0.64)
    _barlabels(ax, bars, fmt="{:.1f}", suffix="%")
    ax.set_title("Departamentos con mayor prevalencia de anemia (6-35 meses), 2023")
    ax.set_ylabel("% de la población de 6 a 35 meses")
    ax.set_ylim(0, 80)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.text(0.0, -0.20,
            "Nota: Loreto y Pasco son valores referenciales del rango alto reportado; la línea gris marca el promedio nacional.",
            transform=ax.transAxes, fontsize=7.8, color=GRIS)
    return _save(fig, "fig03_departamentos.png")


def fig4_cobertura_juntos():
    """Hogares usuarios del Programa JUNTOS (MIDIS)."""
    años = ["2023", "2024*", "2026**"]
    val = [750, 830, 761]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = ax.bar(años, val, color=[AZUL3, AZUL2, AZUL], width=0.55)
    _barlabels(ax, bars, fmt="{:,.0f}")
    ax.set_title("Hogares afiliados al Programa Nacional JUNTOS (miles)")
    ax.set_ylabel("Miles de hogares")
    ax.set_xlabel("Año")
    ax.set_ylim(0, 1000)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.text(0.0, -0.24,
            "* Hogares afiliados reportados por el aplicativo institucional. ** Hogares con abono en la primera operación de pago.",
            transform=ax.transAxes, fontsize=7.8, color=GRIS)
    return _save(fig, "fig04_cobertura_juntos.png")


def fig5_curva_poder():
    """Curva de poder ilustrativa: MDE en g/dL vs número de conglomerados.
    Elaboración propia con la fórmula estándar de Hemming et al. para CRT."""
    k = np.arange(8, 41, 2)          # número de conglomerados por brazo
    m = 30                            # niños por conglomerado
    sigma = 1.3                       # DE de hemoglobina (g/dL), referencial
    icc = 0.05                        # coeficiente de correlación intraclase
    z_alpha = 1.96                    # alfa = 0.05 (dos colas)
    z_beta = 0.84                     # potencia 0.80
    deff = 1 + (m - 1) * icc          # efecto de diseño
    n_eff = (k * m) / deff            # tamaño efectivo por brazo
    mde = (z_alpha + z_beta) * sigma * np.sqrt(2.0 / n_eff)
    # ANCOVA: ajuste por línea de base con correlación rho reduce la varianza
    rho = 0.5
    mde_anc = mde * np.sqrt(1 - rho ** 2)
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(k, mde, marker="o", color=GRIS, linewidth=2.2, markersize=6,
            label="Diferencia de medias (sin ajuste)")
    ax.plot(k, mde_anc, marker="s", color=ROJO, linewidth=2.6, markersize=6,
            label="ANCOVA (ajuste por hemoglobina basal, ρ=0,5)")
    ax.axhline(0.45, color=AZUL, linestyle="--", linewidth=1.4)
    ax.text(40, 0.47, "Efecto objetivo: 0,45 g/dL", ha="right", fontsize=9,
            color=AZUL, fontweight="bold")
    ax.set_title("Efecto mínimo detectable según número de conglomerados por brazo")
    ax.set_ylabel("MDE en hemoglobina (g/dL)")
    ax.set_xlabel("Número de conglomerados por brazo (m = 30 niños; ICC = 0,05)")
    ax.set_ylim(0, 1.2)
    ax.legend(frameon=False, fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    return _save(fig, "fig05_curva_poder.png")


# ============================================================
# DIAGRAMAS CONCEPTUALES (elaboración propia)
# ============================================================

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


def fig6_arbol():
    """Árbol de problemas de la anemia infantil en hogares JUNTOS."""
    fig, ax = plt.subplots(figsize=(9.4, 6.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    # Consecuencias (arriba)
    ax.text(5, 6.85, "CONSECUENCIAS", ha="center", fontsize=11, fontweight="bold", color=NARANJA)
    _box(ax, 2.4, 6.05, 5.2, 0.6,
         "Pérdida de capital humano: menor desarrollo\ncognitivo, escolar y productivo en el largo plazo",
         NARANJA, ec=NARANJA, fontsize=8.0)
    _box(ax, 0.4, 4.95, 2.8, 0.78, "Retraso del\ndesarrollo cognitivo\ny psicomotor", "#E2A06B", ec=NARANJA, fontsize=7.9, fontcolor="black")
    _box(ax, 3.6, 4.95, 2.8, 0.78, "Mayor morbilidad\ne infecciones en\nla primera infancia", "#E2A06B", ec=NARANJA, fontsize=7.9, fontcolor="black")
    _box(ax, 6.8, 4.95, 2.8, 0.78, "Menor rendimiento\nescolar y logro\neducativo futuro", "#E2A06B", ec=NARANJA, fontsize=7.9, fontcolor="black")
    # Problema central
    _box(ax, 1.4, 3.55, 7.2, 0.85,
         "PROBLEMA CENTRAL\nAlta prevalencia de anemia infantil en niñas y niños de 6 a 35\nmeses de hogares usuarios del Programa JUNTOS",
         ROJO, ec=ROJO, fontsize=8.6)
    # Causas directas (abajo)
    _box(ax, 0.4, 2.05, 2.8, 0.82, "Alimentación\ncomplementaria pobre\nen hierro biodisponible", AZUL3, ec=AZUL2, fontsize=7.7, fontcolor="black")
    _box(ax, 3.6, 2.05, 2.8, 0.82, "Prácticas culinarias\ny de cuidado\ninadecuadas", AZUL3, ec=AZUL2, fontsize=7.7, fontcolor="black")
    _box(ax, 6.8, 2.05, 2.8, 0.82, "Baja adherencia a la\nsuplementación con\nhierro", AZUL3, ec=AZUL2, fontsize=7.7, fontcolor="black")
    ax.text(5, 1.45, "CAUSAS DIRECTAS", ha="center", fontsize=11, fontweight="bold", color=AZUL2)
    # Causas indirectas
    _box(ax, 0.4, 0.35, 9.2, 0.7,
         "CAUSAS INDIRECTAS: pobreza y restricción presupuestaria del hogar · desinformación nutricional · "
         "barreras de acceso a servicios de salud · agua y saneamiento deficientes",
         "#D9E1F2", ec=AZUL2, fontsize=7.8, fontcolor="black")
    # Flechas
    for cx in [1.8, 5.0, 8.2]:
        _arrow(ax, cx, 2.87, cx, 3.53, color=AZUL2)
    _arrow(ax, 2.6, 4.4, 1.8, 4.93, color=NARANJA)
    _arrow(ax, 5.0, 4.4, 5.0, 4.93, color=NARANJA)
    _arrow(ax, 7.4, 4.4, 8.2, 4.93, color=NARANJA)
    _arrow(ax, 5.0, 1.05, 5.0, 2.03, color=AZUL2)
    return _save(fig, "fig06_arbol.png")


def fig7_teoria_cambio():
    """Teoría del cambio del proyecto piloto Cocina con Hierro."""
    fig, ax = plt.subplots(figsize=(9.4, 5.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    cols = [
        ("INSUMOS", AZUL, [
            "Sesiones demostrativas\ny recetario con\nalimentos ricos en hierro",
            "Promotores y personal\nde salud capacitados",
            "Articulación con\nJUNTOS y MINSA"]),
        ("ACTIVIDADES", AZUL2, [
            "Sesiones demostrativas\nde cocina con hierro",
            "Consejería nutricional\ny refuerzo conductual",
            "Visitas de seguimiento\nal hogar"]),
        ("PRODUCTOS", VERDE, [
            "Madres con nuevos\nconocimientos y\nhabilidades culinarias",
            "Mayor frecuencia de\npreparaciones ricas\nen hierro",
            "Mejor adherencia a la\nsuplementación"]),
        ("RESULTADOS", ROJO, [
            "Corto plazo: mayor\ningesta de hierro\nbiodisponible",
            "Mediano plazo: aumento\nde la hemoglobina\ninfantil",
            "Largo plazo: reducción\nde la anemia y mejor\ncapital humano"]),
    ]
    x = 0.2
    w = 2.2
    for title, color, items in cols:
        ax.text(x + w / 2, 5.6, title, ha="center", fontsize=10.5, fontweight="bold", color=color)
        y = 4.3
        for it in items:
            _box(ax, x, y, w, 1.05, it, color, ec=color, fontsize=7.6)
            y -= 1.5
        x += 2.5
    for cx in [2.42, 4.92, 7.42]:
        _arrow(ax, cx, 2.9, cx + 0.32, 2.9, color=GRIS)
    ax.text(5.0, 0.12,
            "Supuestos: participación efectiva de las madres · disponibilidad local de alimentos ricos en hierro · "
            "continuidad de la suplementación del MINSA · ausencia de shocks externos.",
            ha="center", fontsize=7.8, style="italic", color=GRIS)
    return _save(fig, "fig07_teoria_cambio.png")


def fig8_diseno_phasein():
    """Diseño experimental aleatorizado por conglomerados con entrada escalonada."""
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(5, 5.7, "Aleatorización por conglomerados (establecimientos de salud / centros poblados)",
            ha="center", fontsize=10, fontweight="bold", color=AZUL)
    _box(ax, 3.6, 4.6, 2.8, 0.7, "Marco muestral de\nconglomerados elegibles", AZUL, ec=AZUL, fontsize=8.2)
    # Dos brazos
    _box(ax, 0.8, 3.0, 3.4, 0.9, "GRUPO DE TRATAMIENTO\nCocina con Hierro desde\nel inicio (Fase 1)", ROJO, ec=ROJO, fontsize=8.2)
    _box(ax, 5.8, 3.0, 3.4, 0.9, "GRUPO DE CONTROL\nEntrada diferida\n(Fase 2, phase-in)", GRIS, ec=GRIS, fontsize=8.2)
    _arrow(ax, 4.4, 4.55, 2.5, 3.95, color=AZUL2)
    _arrow(ax, 5.6, 4.55, 7.5, 3.95, color=AZUL2)
    # Línea de tiempo de medición
    _box(ax, 0.8, 1.7, 3.4, 0.7, "Línea de base → Tratamiento\n→ Línea de salida", "#F2DCDB", ec=ROJO, fontsize=7.9, fontcolor="black")
    _box(ax, 5.8, 1.7, 3.4, 0.7, "Línea de base → Espera\n→ Línea de salida → Tratamiento", "#EDEDED", ec=GRIS, fontsize=7.9, fontcolor="black")
    _arrow(ax, 2.5, 2.95, 2.5, 2.42, color=ROJO)
    _arrow(ax, 7.5, 2.95, 7.5, 2.42, color=GRIS)
    ax.text(5, 0.9,
            "La medición de impacto compara la hemoglobina al cierre de la Fase 1; el control recibe la intervención en la Fase 2.",
            ha="center", fontsize=8.2, style="italic", color=GRIS)
    return _save(fig, "fig08_diseno_phasein.png")


def build_all():
    paths = {
        "fig1": fig1_evolucion_anemia(),
        "fig2": fig2_urbano_rural(),
        "fig3": fig3_departamentos(),
        "fig4": fig4_cobertura_juntos(),
        "fig5": fig5_curva_poder(),
        "fig6": fig6_arbol(),
        "fig7": fig7_teoria_cambio(),
        "fig8": fig8_diseno_phasein(),
    }
    return paths


if __name__ == "__main__":
    p = build_all()
    for k, v in p.items():
        print(k, v)
