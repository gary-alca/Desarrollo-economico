# -*- coding: utf-8 -*-
"""Genera diagramas de payoff (PNG) para incrustar en el Word."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import data as d

os.makedirs("img", exist_ok=True)
BLUE = "#1F4E78"; GREEN = "#2E7D32"; RED = "#C0392B"

def chart_payoff(pos):
    tick = pos["subyacente"]; spot = d.SPOT[tick]
    Ks = [l["K"] for l in pos["legs"]]
    lo, hi = min(Ks), max(Ks)
    span = max(hi - lo, spot * 0.06)
    ST = np.linspace(lo - span * 1.4 - 2, hi + span * 1.4 + 2, 500)
    gp = np.array([d.estrategia_gp_total(pos, s) for s in ST])
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=130)
    ax.axhline(0, color="#888", lw=0.8)
    ax.plot(ST, gp, color=BLUE, lw=2.2)
    ax.fill_between(ST, gp, 0, where=gp >= 0, color=GREEN, alpha=0.18)
    ax.fill_between(ST, gp, 0, where=gp < 0, color=RED, alpha=0.18)
    ax.axvline(spot, color="#E67E22", ls="--", lw=1.2, label=f"Spot {spot:.2f}")
    for K in Ks:
        ax.axvline(K, color="#999", ls=":", lw=0.9)
    ax.set_title(f"{tick} — {pos['nombre']}  (G/P al vencimiento)", fontsize=10, color=BLUE, weight="bold")
    ax.set_xlabel("Precio del subyacente al vencimiento (ST)", fontsize=8)
    ax.set_ylabel("G/P total (USD)", fontsize=8)
    ax.tick_params(labelsize=7)
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.15)
    fig.tight_layout()
    p = f"img/{pos['id']}.png"
    fig.savefig(p); plt.close(fig)
    return p

def chart_futuros():
    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=130)
    labels = [f[1] + " " + f[0][5:] for f in d.FECHAS_FUT]
    for sym, f in d.FUTUROS.items():
        sign = 1 if f["posicion"] == "Larga" else -1
        prev = f["entrada"]; acum = []; run = 0
        for s in f["settle"]:
            run += (s - prev) * sign * f["contratos"] * f["tamano"]; prev = s
            acum.append(run)
        ax.plot(range(len(acum)), acum, marker="o", ms=3, lw=1.8,
                label=f"{f['activo']} ({f['posicion']})")
    ax.axhline(0, color="#888", lw=0.8)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=6)
    ax.set_title("Futuros — G/P acumulada por marca a mercado (ilustrativo)",
                 fontsize=10, color=BLUE, weight="bold")
    ax.set_ylabel("G/P acumulada (USD)", fontsize=8)
    ax.tick_params(axis="y", labelsize=7)
    ax.legend(fontsize=7); ax.grid(alpha=0.15)
    fig.tight_layout()
    p = "img/futuros_pl.png"; fig.savefig(p); plt.close(fig)
    return p

if __name__ == "__main__":
    for pos in d.OPCIONES:
        print(chart_payoff(pos))
    print(chart_futuros())
