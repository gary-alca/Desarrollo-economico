# -*- coding: utf-8 -*-
"""
Datos maestros del proyecto de derivados (portafolio USD 1,000,000).
Todos los precios de OPCIONES provienen de las capturas reales de MarketWatch
(snapshot 2 de julio de 2026). Los settlements de FUTUROS estan marcados como
ILUSTRATIVOS (ver nota metodologica) porque no se dispone de la serie oficial
CME/NYMEX/COMEX para esas fechas; las formulas del Excel recalculan solo con
pegar los prints reales.
"""

import math
from scipy.stats import norm

# ----------------------------------------------------------------------------
# 1. SNAPSHOT DE MERCADO (2-jul-2026, cierre) -- fuente: capturas MarketWatch
# ----------------------------------------------------------------------------
SPOT = {
    "AAPL": 308.63,
    "MSFT": 390.49,
    "NVDA": 194.83,
    "DAL":  92.75,
    "SPY":  744.78,   # cadena de diciembre 2026 (unica SPY disponible)
}

# Vencimientos
EXP = {
    "AAPL": "2026-07-10",
    "MSFT": "2026-07-10",
    "NVDA": "2026-07-10",
    "DAL":  "2026-07-10",
    "SPY":  "2026-12-18",
}

# ----------------------------------------------------------------------------
# 2. POSICIONES DE OPCIONES (entrada = snapshot real 2-jul-2026)
#    Cada 'leg': tipo(call/put), lado(long/short), K, prima (por accion)
#    prima tomada del BID (si vendemos) o ASK/mid (si compramos) de la captura.
# ----------------------------------------------------------------------------
OPCIONES = [
    {
        "id": "DAL_BPS",
        "subyacente": "DAL",
        "nombre": "Bull Put Spread 90/85",
        "estrategia": "Bull Put Spread",
        "sesgo": "Alcista / neutral",
        "contratos": 40,
        "exp": "2026-07-10",
        "legs": [
            {"tipo": "put", "lado": "short", "K": 90.0, "prima": 2.16},  # vendemos, mid bid/ask 2.01/2.32
            {"tipo": "put", "lado": "long",  "K": 85.0, "prima": 0.85},  # compramos, mid 0.73/0.97
        ],
        "confianza": "Alta",
        "riesgo_nivel": "Bajo (definido)",
        "sector": "Aerolineas / Consumo ciclico",
    },
    {
        "id": "MSFT_BPS",
        "subyacente": "MSFT",
        "nombre": "Bull Put Spread 385/380",
        "estrategia": "Bull Put Spread",
        "sesgo": "Alcista",
        "contratos": 30,
        "exp": "2026-07-10",
        "legs": [
            {"tipo": "put", "lado": "short", "K": 385.0, "prima": 5.13},
            {"tipo": "put", "lado": "long",  "K": 380.0, "prima": 3.49},
        ],
        "confianza": "Media-alta",
        "riesgo_nivel": "Bajo (definido)",
        "sector": "Tecnologia (Software/IA)",
    },
    {
        "id": "AAPL_BCS",
        "subyacente": "AAPL",
        "nombre": "Bull Call Spread 310/322.5",
        "estrategia": "Bull Call Spread",
        "sesgo": "Alcista",
        "contratos": 30,
        "exp": "2026-07-10",
        "legs": [
            {"tipo": "call", "lado": "long",  "K": 310.0, "prima": 3.95},
            {"tipo": "call", "lado": "short", "K": 322.5, "prima": 0.69},
        ],
        "confianza": "Media",
        "riesgo_nivel": "Medio (debito definido)",
        "sector": "Tecnologia (Hardware)",
    },
    {
        "id": "SPY_FLY",
        "subyacente": "SPY",
        "nombre": "Butterfly Calls 745/755/765 (Dic)",
        "estrategia": "Butterfly Spread (calls)",
        "sesgo": "Neutral (rango)",
        "contratos": 50,
        "exp": "2026-12-18",
        "legs": [
            {"tipo": "call", "lado": "long",  "K": 745.0, "prima": 38.60},
            {"tipo": "call", "lado": "short", "K": 755.0, "prima": 32.42, "mult": 2},
            {"tipo": "call", "lado": "long",  "K": 765.0, "prima": 27.34},
        ],
        "confianza": "Media",
        "riesgo_nivel": "Bajo (debito muy pequeno)",
        "sector": "Indice amplio (S&P 500)",
    },
    {
        "id": "NVDA_BCS",
        "subyacente": "NVDA",
        "nombre": "Bear Call Spread 195/200",
        "estrategia": "Bear Call Spread",
        "sesgo": "Bajista / neutral",
        "contratos": 40,
        "exp": "2026-07-10",
        "legs": [
            {"tipo": "call", "lado": "short", "K": 195.0, "prima": 4.05},
            {"tipo": "call", "lado": "long",  "K": 200.0, "prima": 1.92},
        ],
        "confianza": "Media (a evaluar por IV)",
        "riesgo_nivel": "Bajo (definido)",
        "sector": "Tecnologia (Semiconductores)",
    },
]

MULT = 100  # acciones por contrato

# ----------------------------------------------------------------------------
# 3. FUTUROS -- parametros. Settlements ILUSTRATIVOS (ver nota metodologica).
#    Fechas habiles 18-jun a 9-jul-2026 (excl. 19-jun Juneteenth, 3-jul feriado).
# ----------------------------------------------------------------------------
FECHAS_FUT = [
    ("2026-06-18", "Jue"), ("2026-06-22", "Lun"), ("2026-06-23", "Mar"),
    ("2026-06-24", "Mie"), ("2026-06-25", "Jue"), ("2026-06-26", "Vie"),
    ("2026-06-29", "Lun"), ("2026-06-30", "Mar"), ("2026-07-01", "Mie"),
    ("2026-07-02", "Jue"), ("2026-07-06", "Lun"), ("2026-07-07", "Mar"),
    ("2026-07-08", "Mie"), ("2026-07-09", "Jue"),
]

# Series de liquidacion ILUSTRATIVAS coherentes con la tesis macro:
# Oro sube (refugio geopolitico), WTI baja (distension EE.UU.-Iran),
# ES sube (grind alcista). Incluye un dia adverso para ilustrar Margin Call.
FUTUROS = {
    "GC": {
        "activo": "Oro", "simbolo": "GC", "mercado": "COMEX",
        "posicion": "Larga", "contratos": 3, "tamano": 100, "unidad": "oz",
        "margen_ini": 12100.0, "margen_mant": 11000.0,  # por contrato
        "entrada": 3300.0,
        # settlement diario ilustrativo
        "settle": [3300.0, 3288.0, 3305.0, 3322.0, 3341.0, 3355.0, 3348.0,
                   3362.0, 3379.0, 3395.0, 3410.0, 3402.0, 3418.0, 3433.0],
        "tesis": "Refugio ante riesgo geopolitico y sesgo dovish de la Fed.",
    },
    "CL": {
        "activo": "Petroleo WTI", "simbolo": "CL", "mercado": "NYMEX",
        "posicion": "Corta", "contratos": 5, "tamano": 1000, "unidad": "bbl",
        "margen_ini": 6050.0, "margen_mant": 5500.0,
        "entrada": 68.40,
        # baja tendencial pero con un repunte (dia adverso -> margin call corto)
        "settle": [68.40, 67.10, 66.20, 68.90, 70.30, 69.10, 67.80,
                   66.50, 65.40, 64.20, 63.10, 63.80, 62.40, 61.30],
        "tesis": "Distension EE.UU.-Iran y mayor oferta -> presion bajista del crudo.",
    },
    "ES": {
        "activo": "E-mini S&P 500", "simbolo": "ES", "mercado": "CME",
        "posicion": "Larga", "contratos": 2, "tamano": 50, "unidad": "pts indice",
        "margen_ini": 18500.0, "margen_mant": 16800.0,
        "entrada": 7395.0,
        "settle": [7395.0, 7360.0, 7402.0, 7430.0, 7455.0, 7448.0, 7470.0,
                   7495.0, 7480.0, 7448.0, 7502.0, 7525.0, 7540.0, 7561.0],
        "tesis": "Mercado que sube despacio en semana de pocos catalizadores.",
    },
}

CAPITAL = 1_000_000.0

# ----------------------------------------------------------------------------
# Utilidades de payoff y Black-Scholes
# ----------------------------------------------------------------------------
def leg_payoff(leg, ST):
    """Payoff intrinseco por accion (sin prima) segun lado/tipo."""
    K = leg["K"]
    if leg["tipo"] == "call":
        intr = max(ST - K, 0.0)
    else:
        intr = max(K - ST, 0.0)
    sign = 1.0 if leg["lado"] == "long" else -1.0
    return sign * intr

def leg_gp_share(leg, ST):
    """Ganancia/perdida por accion incluyendo prima."""
    mult = leg.get("mult", 1)
    if leg["lado"] == "long":
        gp = leg_payoff(leg, ST) - leg["prima"]
    else:  # short: cobramos prima
        gp = leg["prima"] + leg_payoff(leg, ST)  # payoff ya es negativo
    return gp * mult

def estrategia_gp_total(pos, ST):
    gp_share = sum(leg_gp_share(l, ST) for l in pos["legs"])
    return gp_share * MULT * pos["contratos"]

def credito_debito_neto(pos):
    """Prima neta por accion: >0 credito, <0 debito."""
    tot = 0.0
    for l in pos["legs"]:
        mult = l.get("mult", 1)
        tot += (l["prima"] * mult) if l["lado"] == "short" else (-l["prima"] * mult)
    return tot

def bs_price(S, K, T, r, sigma, tipo):
    if T <= 0:
        return max(S - K, 0.0) if tipo == "call" else max(K - S, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if tipo == "call":
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
