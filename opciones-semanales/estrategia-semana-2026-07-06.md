# Qué opciones operar esta semana — Guía explicada paso a paso
## Semana del 6 al 10 de julio de 2026

> **Documento educativo.** No es asesoría financiera personalizada. Los precios (strikes) y primas son
> aproximados: verifica la cadena de opciones real de tu bróker antes de operar.

## Antes de empezar: diccionario rápido

- **Opción**: contrato que te da el DERECHO (no la obligación) de comprar o vender una acción a un precio fijo antes de una fecha. Pagas o cobras una "prima" por ese derecho.
- **Call (opción de compra)**: derecho a COMPRAR la acción a un precio fijo. Ganas valor si la acción SUBE.
- **Put (opción de venta)**: derecho a VENDER la acción a un precio fijo. Ganas valor si la acción BAJA.
- **Strike (precio de ejercicio)**: el precio fijo pactado. "Put 90" = derecho a vender a $90.
- **Prima**: el precio de la opción. El COMPRADOR la paga; el VENDEDOR la cobra y se la queda si la opción expira sin valor.
- **Comprar vs. Vender una opción**: comprar = pagas prima, pérdida limitada a lo que pagaste. Vender = cobras prima por adelantado, apuestas a que NO ocurra el movimiento (ganancia limitada a la prima, riesgo mayor).
- **Spread (diferencial)**: combinar dos opciones a la vez (una comprada, una vendida). Abarata la operación y PONE UN TOPE a la pérdida máxima. Es la versión "con red de seguridad".
- **Vencimiento**: la fecha en que la opción muere. Si no sirve, vale cero.
- **Volatilidad implícita (IV)**: el "nerviosismo" esperado. IV alta = opciones CARAS (bueno para el que vende). IV baja = opciones BARATAS (bueno para el que compra).
- **VIX**: el "termómetro del miedo" del mercado general. Bajo (~16 hoy) = mercado tranquilo, opciones baratas.
- **Earnings (resultados trimestrales)**: día en que una empresa publica sus cuentas. Antes sube la IV; justo después se desploma.
- **IV crush**: la caída brusca de la volatilidad (y del precio de las opciones) justo DESPUÉS de un earnings. Perjudica al comprador, beneficia al vendedor.
- **Theta (desgaste por tiempo)**: las opciones pierden valor cada día, como un hielo derritiéndose. Perjudica al comprador, beneficia al vendedor.

## 1. Cómo está el mercado esta semana

En pocas palabras: el mercado está en máximos y tranquilo (poco miedo). Dos consecuencias prácticas:

1. **Las opciones están baratas en general** → cuando queramos apostar a una dirección, conviene COMPRAR prima barata en lugar de venderla.
2. **La excepción son las empresas que reportan esta semana** (Delta y PepsiCo) → en ellas la volatilidad está inflada y ahí sí conviene VENDER prima cara.

| Dato | Cómo está | Qué significa para nosotros |
|---|---|---|
| S&P 500 (índice general de EE.UU.) | 7,483, en máximos (+1.8% la semana pasada) | Tendencia al alza, pero cara: poco margen para errores |
| VIX (termómetro del miedo) | ~15.8, nivel bajo-normal | Opciones baratas: mejor comprar apuestas direccionales que venderlas |
| Reserva Federal (banco central) | Publica sus "minutas" el miércoles 8 | Único evento capaz de sacudir el mercado esta semana |
| Resultados trimestrales | PepsiCo (jue 9), Delta (vie 10) | Volatilidad inflada solo en estas: ahí conviene vender prima |
| Petróleo | Cayendo (paz interina EE.UU.–Irán) | Muy bueno para aerolíneas como Delta (menos costo de combustible) |

## 2. Las 4 operaciones recomendadas (de mayor a menor confianza)

### Idea 1 — Delta (DAL): apostar a que NO caerá mucho antes de sus resultados

**Estrategia: Bull Put Spread** ("diferencial alcista con puts"). Cobras dinero hoy apostando a que la acción se mantiene por encima de cierto nivel, y compras una segunda opción como red de seguridad para que la pérdida nunca sea ilimitada.

- **Cómo se arma**: vendes una put strike 90 (cobras prima) y compras una put strike 85 (pagas menos prima). Vencimiento 10 o 17 de julio. Te quedas la diferencia si Delta cierra por encima de $90.
- **Por qué tiene sentido**: cuatro razones apuntan a lo mismo. (a) Delta reporta el viernes con la volatilidad inflada, y justo después se desploma (IV crush), lo que abarata las opciones que vendimos y nos da ganancia. (b) El petróleo bajó por la paz EE.UU.–Irán, ahorrándole a Delta ~$300 millones. (c) 22 de 24 analistas la califican "compra fuerte" y ha superado previsiones 4 trimestres seguidos. (d) Tiene un soporte técnico en $92.7 (nivel donde los compradores suelen frenar caídas).
- **El riesgo**: se espera que su ganancia por acción caiga ~32% frente al año pasado. Si da malas previsiones y rompe el soporte, perderías — pero la pérdida está TOPADA por el spread. Regla: cerrar al llevar 50–60% del máximo.

### Idea 2 — Microsoft (MSFT): cobrar por comprometerte a comprarla más barata

**Estrategia: Venta de Put** (cash-secured = con el dinero reservado para comprar si te toca). Te pagan hoy por prometer que comprarías Microsoft un poco más abajo del precio actual.

- **Cómo se arma**: vendes una put strike 370 y reservas el efectivo por si te asignan las acciones. Alternativa con red: spread 370/360. Vencimiento 17 de julio, ANTES de sus resultados de fin de mes.
- **Por qué tiene sentido**: Microsoft es la peor de las grandes tecnológicas: ha caído 24% y está en mínimos desde 2023 por miedo a que gaste demasiado en centros de datos para IA. Cuando todos ya están pesimistas, el precio suele estar cerca de un suelo ("capitulación"). Señal reveladora: el famoso inversor Michael Burry compró calls apostando a que subirá a $700+. Al vender la put, si NO baja te quedas la prima; y si baja, compras una empresa sólida con doble descuento.
- **El riesgo**: si el mercado sigue castigando el gasto en IA, podría seguir cayendo. Hazlo solo con dinero que estés dispuesto a usar para comprar la acción, o usa el spread para limitar la pérdida.

### Idea 3 — Apple (AAPL): apostar a una subida moderada, barato

**Estrategia: Bull Call Spread** ("diferencial alcista con calls"). Apuestas a que sube, pero abaratas la apuesta vendiendo otra opción más arriba.

- **Cómo se arma**: compras una call strike 310 (apuestas a que sube) y vendes una call strike 322.5 (esa venta devuelve dinero y reduce el costo). Vencimiento 17 o 24 de julio, evitando sus earnings.
- **Por qué tiene sentido**: Apple ($308.6) está a solo ~4% de ser la empresa más valiosa del mundo, superando a Nvidia. Ese titular atrae compradores y fondos que siguen la tendencia, y puede empujarla esta misma semana. Elegimos el SPREAD y no la call sola porque, en una semana sin noticias propias de Apple, una call sola perdería valor cada día por el desgaste del tiempo (theta); la call vendida compensa ese desgaste.
- **El riesgo**: la subida ya viene muy estirada; si se frena, pierdes lo que pagaste (nada más, está topado). Salir si Apple pierde los ~$300.

### Idea 4 — El índice SPY: cobrar si el mercado se queda quieto, o comprar un seguro barato

**Estrategia principal: Butterfly ("mariposa") de calls.** Una apuesta barata a que el índice termina la semana cerca de un nivel concreto, sin moverse mucho.

- **Cómo se arma**: mariposa 745/755/765 en calls, vencimiento 10 de julio. Cuesta poco y paga mucho si el índice se "estaciona" cerca de 755.
- **Por qué tiene sentido**: semana con pocos datos (lo único fuerte son las minutas de la Fed el miércoles) y mercado que sube despacio y sin sobresaltos. Ese ambiente de "poco movimiento" es donde una mariposa rinde mejor: arriesgas poco para ganar bastante si el índice no se dispara ni se hunde.
- **Alternativa defensiva (si ya tienes acciones)**: comprar una Put de SPY como SEGURO. Con el miedo tan bajo (VIX <16), ese seguro está barato — es el mejor momento para comprar protección, no para venderla. El único susto posible sería que las minutas de la Fed salgan más duras de lo esperado.

## 3. Estrategias del listado que NO conviene usar esta semana

| Estrategia | Qué es (en simple) | Por qué NO esta semana |
|---|---|---|
| Compra de Call / Put (solas) | Apuesta directa a que sube (call) o baja (put) | Pierden valor cada día por el desgaste del tiempo; sin catalizador claro es tirar prima. Mejor dentro de un spread |
| Venta de Call desnuda | Cobrar prima apostando a que NO sube, sin red | Riesgo ILIMITADO si la acción se dispara, y el mercado está en máximos con impulso |
| Straddle / Strangle | Comprar call y put a la vez, apostando a un movimiento fuerte en cualquier dirección | Con el mercado tranquilo (VIX 16) no se espera ese movimiento; tras earnings el IV crush destruye la prima aunque aciertes |
| Strip / Strap | Variantes del straddle con más peso a un lado | Necesitan un movimiento violento con dirección; nada en el calendario lo justifica |
| Box Spread | Combinación que en teoría "asegura" un rendimiento fijo | Es arbitraje de tasas; tras comisiones, el inversor particular no saca ventaja |
| Bear Call / Bear Put Spread | Apuestas a que el mercado BAJA, con riesgo limitado | La tendencia general es alcista; apostar a la baja sin razón concreta es remar contra la corriente |

**Nota**: los "Bull Put Spread" y "Bull Call Spread" SÍ los usamos (ideas 1 y 3), y el "Butterfly" también (idea 4). Solo descartamos los que no encajan con el mercado de esta semana.

## 4. Reglas para no equivocarse

1. No arriesgar más del 1–2% de tu capital total en cada idea.
2. En las operaciones donde cobras prima (Delta y Microsoft): cerrar y llevarte la ganancia al alcanzar el 50–60% del máximo posible. No ser codicioso.
3. En Apple: salir si el precio pierde los ~$300 (señal de que la subida se rompió).
4. Mirar las minutas de la Fed el miércoles 8: si el tono es más duro de lo esperado, reducir las apuestas alcistas.

## Fuentes consultadas

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
