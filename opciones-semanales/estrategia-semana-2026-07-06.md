# Estrategia semanal de opciones — Semana del 6 al 10 de julio de 2026

> **Aviso**: Este documento es un análisis educativo, no asesoría financiera personalizada.
> Los strikes y primas son aproximados (verificar la cadena de opciones en tiempo real antes de operar).

## 1. Contexto de mercado

| Indicador | Lectura | Implicancia |
|---|---|---|
| S&P 500 | 7,483 (+1.8% la semana pasada, zona de máximos) | Sesgo alcista, pero poco margen de error |
| VIX | ~15.8 (banda media-baja 12–20) | Prima de opciones **barata**: favorece comprar direccional con riesgo definido; vender prima "desnuda" paga poco en índices |
| Fed | Nuevo presidente Kevin Warsh, tono *hawkish* en Sintra. Minutas FOMC el **miércoles 8 de julio** | Único evento macro capaz de mover el mercado esta semana |
| Probabilidad de recorte en septiembre | ~60–65% | Fondo de liquidez aún favorable a renta variable |
| Temporada de resultados Q2 | Arranca esta semana: **PepsiCo (jue 9)**, **Delta (vie 10)**, Levi's | IV inflada solo en nombres puntuales → ahí sí conviene **vender** prima |
| Rotación | Flujo hacia value/cíclicos; crecimiento de beneficios S&P estimado >24% | Los cíclicos (aerolíneas) tienen viento a favor |
| Petróleo | A la baja tras el tratado interino EEUU–Irán | Beneficia directamente a aerolíneas (Delta: ~$300M de beneficio extra en refinería) |

**Situación de los subyacentes candidatos:**

- **AAPL ($308.6)**: fuerte momentum, a ~4% de superar a Nvidia como la empresa más valiosa del mundo. Sus earnings son a fin de mes (fuera de esta ventana).
- **MSFT ($384)**: la peor del "Magnificent 7", −24% en el año, en mínimos desde 2023 por dudas sobre el capex en centros de datos. Michael Burry compró calls apostando a $700–750 en 2028. Pesimismo extremo ya en precio.
- **NVDA**: sin catalizador propio hasta fines de agosto; rehén del sentimiento sobre IA, que está nervioso. Precio objetivo promedio de analistas $301 (+55%), pero sin gatillo esta semana.
- **DAL (soporte técnico $92.7)**: reporta el viernes 10 antes de la apertura. 22 de 24 analistas en "Strong Buy", 4 trimestres seguidos superando estimaciones, combustible más barato. Consenso: EPS ~$1.43–1.54, ingresos ~$17.5B.

## 2. Las 4 operaciones recomendadas

### Idea 1 — DAL: **Bull Put Spread** sobre earnings (la mejor relación riesgo/beneficio de la semana)

- **Estructura**: vender put 90 / comprar put 85, vencimiento 10 o 17 de julio.
- **Por qué esta estrategia**: la IV de DAL está inflada antes del reporte del viernes. El *IV crush* posterior al earnings trabaja a favor del vendedor de prima. El spread (y no la venta de put desnuda) define el riesgo máximo en $500 − crédito por contrato.
- **Tesis**: combustible barato (tratado EEUU–Irán), historial de sorpresas positivas, rotación hacia cíclicos, soporte en $92.7 que da colchón adicional.
- **Riesgo**: se espera una caída interanual del EPS de ~32%; si la guía decepciona y rompe el soporte, se asume la pérdida definida. Cerrar al 50–60% del crédito máximo si se alcanza antes del viernes.

### Idea 2 — MSFT: **Venta de Put** (cash-secured) o Bull Put Spread

- **Estructura**: vender put 370 (cash-secured) o spread 370/360, vencimiento 17 de julio — **antes** de sus earnings de fin de mes, para no exponerse al evento.
- **Por qué esta estrategia**: tras −24%, la IV de MSFT está elevada respecto a su historia y el pesimismo parece capitulación (mínimos desde 2023 con Burry comprando calls). Vender el put te paga por comprometerte a comprar ~4% más abajo: si no llega, cobras la prima; si llega, entras con doble descuento.
- **Riesgo**: el cuchillo puede seguir cayendo si el mercado sigue castigando el capex en IA. Solo con capital dispuesto a ser asignado (o usar el spread para definir riesgo).

### Idea 3 — AAPL: **Bull Call Spread**

- **Estructura**: comprar call 310 / vender call 322.5, vencimiento 17 o 24 de julio (evitando earnings).
- **Por qué esta estrategia**: con VIX en 15.8 el débito es razonable, y el spread reduce el costo frente a la compra de call seca (la call vendida financia parte de la prima y neutraliza theta). El catalizador narrativo — destronar a Nvidia como la más valiosa — puede atraer flujo pasivo/momentum esta misma semana.
- **Riesgo**: el rally está extendido; pérdida máxima = débito pagado (~1/3 del ancho del spread). No usar compra de call simple: pagarías theta completa en una semana sin evento propio.

### Idea 4 — SPY: **Butterfly de calls** (o Put protector si ya tienes cartera)

- **Estructura**: mariposa 745/755/765 calls, vencimiento 10 de julio.
- **Por qué esta estrategia**: semana de pocos datos (lo relevante llega el miércoles con las minutas), mercado en máximos con deriva lenta al alza y volatilidad realizada baja — el escenario ideal para una mariposa: costo mínimo, pago máximo si el índice "se estaciona" cerca del cuerpo.
- **Alternativa defensiva**: si tienes cartera larga, la **Compra de Put** OTM de SPY está históricamente barata con VIX <16 — es el momento de comprar seguro, no de venderlo. Unas minutas más hawkish de lo esperado de Warsh son el riesgo de cola de la semana.

## 3. Estrategias del listado que NO conviene usar esta semana

| Estrategia | Por qué no |
|---|---|
| **Straddle / Strangle largos** (sobre earnings) | El IV crush post-reporte destruye la prima aunque aciertes dirección; con VIX 15.8 tampoco hay expectativa de movimiento explosivo en índices |
| **Strip / Strap** | Exigen expectativa de movimiento violento con sesgo direccional; nada en el calendario lo justifica |
| **Box Spread** | Es arbitraje de tasas; tras comisiones y horquillas, el retail no captura valor |
| **Venta de Call desnuda** (NVDA/AAPL) | Riesgo ilimitado contra un mercado en máximos con momentum; si quieres sesgo bajista, usa Bear Call Spread |
| **Bear Put / Bear Call Spreads** en índices | Luchar contra la tendencia primaria alcista sin catalizador bajista confirmado es pagar por tener razón "algún día" |

## 4. Reglas de gestión

1. No arriesgar más de 1–2% del capital por idea.
2. En los spreads de crédito (DAL, MSFT), tomar ganancias al 50–60% del crédito máximo.
3. En el Bull Call Spread de AAPL, salir si el subyacente pierde ~$300 (invalidación técnica del momentum).
4. Revisar las minutas del FOMC del miércoles 8: si el tono es más hawkish de lo esperado, reducir exposición direccional alcista.

## Fuentes

- [Charles Schwab — Weekly Trader's Outlook](https://www.schwab.com/learn/story/weekly-traders-outlook)
- [Tradingkey — US Stock Market This Week 2026-07-06](https://www.tradingkey.com/tools/market-update/us-stock-market-this-week-20260706)
- [Yahoo Finance — VIX](https://finance.yahoo.com/quote/%5EVIX/)
- [Kiplinger — Earnings Calendar July 6-10](https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks)
- [StockTitan — PepsiCo Q2 2026 earnings date](https://www.stocktitan.net/news/PEP/pepsi-co-announces-timing-and-availability-of-second-quarter-2026-qw5aeek7utzl.html)
- [Barchart — What to Expect From Delta's Q2 2026 Earnings](https://www.barchart.com/story/news/2639811/what-to-expect-from-delta-air-lines-q2-2026-earnings-report)
- [FX Leaders — DAL anchors $92.73 support ahead of Q2 earnings](https://www.fxleaders.com/news/2026/07/05/delta-air-lines-dal-stock-forecast-delta-anchors-92-73-support-as-fuel-relitigation-pivots-ahead-of-q2-earnings/)
- [The Motley Fool — Apple ~4% from overtaking Nvidia](https://www.fool.com/investing/2026/07/03/apple-is-about-4-away-from-overtaking-nvidia-as-th/)
- [WEEX — Nvidia vs Microsoft 2026](https://www.weex.com/learn/articles/nvidia-vs-microsoft-stock-2026-qijgkpg2x3v4ewsppkhs2hbq)
- [StockAnalysis — NVDA](https://stockanalysis.com/stocks/nvda/)
