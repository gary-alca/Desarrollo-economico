# Portafolio de Derivados Financieros — USD 1,000,000

**Proyecto universitario de Derivados Financieros (Futuros y Opciones)**
**Horizonte de gestión: 2 de julio – 9 de julio de 2026 · Presentación: 9 de julio de 2026**
**Rol asumido: gestor profesional de portafolios y analista cuantitativo**

---

## 1. Introducción

Este informe documenta el diseño, la construcción y la administración activa de un portafolio de aproximadamente USD 1,000,000 compuesto exclusivamente por instrumentos derivados —futuros y opciones— negociados en mercados organizados (CME, NYMEX, COMEX y CBOE), durante la semana del 2 al 9 de julio de 2026.

El portafolio se construye con la información de mercado disponible al **jueves 2 de julio de 2026** y se administra dinámicamente hasta el miércoles 8 de julio (última sesión completa antes de la presentación del 9 de julio). El objetivo central no es maximizar la rentabilidad, sino demostrar comprensión del funcionamiento de los derivados, de la gestión del riesgo y de la toma de decisiones financieras fundamentadas en el análisis macroeconómico y de mercado.

El momento elegido resulta excepcionalmente rico para un ejercicio de este tipo: la economía mundial atraviesa las secuelas de la guerra con Irán y de la crisis del Estrecho de Ormuz, con un alto el fuego frágil; la inflación estadounidense se aceleró hasta 4.2% por el choque energético; la Reserva Federal abandonó su sesgo de recortes y contempla subir tasas; el mercado laboral se enfría; y la renta variable muestra una divergencia notable (Dow Jones en máximo histórico mientras el Nasdaq y los semiconductores caen). Es decir: un entorno con rasgos de **estanflación moderada, riesgo geopolítico latente y volatilidad implícita sorprendentemente baja** — terreno natural para estrategias con derivados.

## 2. Objetivos

**Objetivo general.** Diseñar y administrar activamente, durante la semana del 2 al 9 de julio de 2026, un portafolio cercano a USD 1,000,000 en valor nocional, compuesto por futuros y opciones, justificando cada decisión con fundamentos financieros, macroeconómicos y de mercado.

**Objetivos específicos:**

1. Analizar el entorno macroeconómico y financiero global vigente al 2 de julio de 2026.
2. Seleccionar activos subyacentes reales y líquidos negociados en mercados organizados.
3. Aplicar de forma justificada un subconjunto de las estrategias vistas en clase (futuros largos, bull call spread, bear call spread, bull put spread y strangle).
4. Cuantificar para cada posición la pérdida máxima, la ganancia potencial y los escenarios de resultado.
5. Diseñar un sistema de gestión dinámica: hipótesis de inversión, reglas de decisión SI/ENTONCES, plan de monitoreo diario y estrategias alternativas.
6. Evaluar el desempeño y extraer conclusiones académicas al cierre del ejercicio.

## 3. Metodología

1. **Fecha de valoración inicial:** cierre del jueves 2 de julio de 2026. Todos los precios de subyacentes provienen de fuentes públicas verificables (se citan en la sección 16).
2. **Capital y noción de "portafolio de USD 1,000,000":** en un portafolio de derivados el capital no se "invierte" íntegramente como en un portafolio de contado; se compromete en primas de opciones y márgenes de garantía, mientras la exposición económica se mide por el **valor nocional**. Se construyó un portafolio con **valor nocional agregado de ≈ USD 922,000 (92% del objetivo)**, dejando ≈ USD 78,000 como colchón de liquidez para llamadas de margen — práctica estándar de gestión prudente. El capital efectivamente comprometido en primas y márgenes es de ≈ USD 21,000 (2.1% del capital), lo que ilustra el apalancamiento inherente a los derivados; el efectivo restante se asume colocado en T-bills a ~3.6% anual.
3. **Primas de opciones:** los precios de subyacentes, índices, tasas y volatilidad (VIX) son datos reales de mercado. Las primas exactas de cada opción al cierre del 2 de julio no están disponibles públicamente de forma retroactiva sin terminal profesional; por transparencia metodológica, **las primas se estimaron con el modelo Black–Scholes–Merton** usando la volatilidad implícita observable (VIX = 16.59 para SPY; ajustes de +4 pts para QQQ y −2 pts para DIA, consistentes con los diferenciales históricos de volatilidad implícita entre índices; ~38% para opciones sobre WTI, coherente con un OVX elevado tras la guerra). Cada prima estimada se marca con (†). Este supuesto se declara explícitamente conforme a las instrucciones del proyecto.
4. **Gestión dinámica:** el portafolio se revisa cada día de mercado (2, 6, 7 y 8 de julio; el viernes 3 la operativa fue reducida por el festivo del 4 de julio). Cada revisión aplica el protocolo: (i) actualizar datos, (ii) contrastar con la hipótesis de cada posición, (iii) decidir Mantener / Cerrar / Reducir / Aumentar / Reemplazar, (iv) documentar en la bitácora (`bitacora_gestion.md`).
5. **Criterio rector:** prioridad a la gestión del riesgo (pérdidas máximas acotadas y conocidas ex ante en 4 de las 5 posiciones) por encima de la maximización del retorno.

## 4. Contexto macroeconómico (al 2 de julio de 2026)

### 4.1 El choque dominante: la guerra con Irán y el Estrecho de Ormuz

El evento macro definitorio de 2026 es la guerra con Irán y el cierre del Estrecho de Ormuz, que la Agencia Internacional de Energía calificó como "la mayor disrupción de oferta en la historia del mercado petrolero global". El Brent llegó a operar en ~$105/barril, +44% desde el inicio del conflicto. El 14 de junio los mediadores anunciaron un memorando de entendimiento y el **17 de junio** los presidentes de EE. UU. e Irán firmaron un **alto el fuego con periodo de prueba de 60 días**.

El alto el fuego es, sin embargo, **precario**: el 20 de junio Irán declaró nuevamente cerrado el estrecho en respuesta a ataques israelíes en el Líbano (denunciados como violación del acuerdo); el 27 de junio la Joint Maritime Information Center (US Navy) anunció una ruta ampliada por el estrecho cerca de Omán, desafiando el control iraní; y a inicios de julio Irán rehusó reunirse con enviados estadounidenses, enfriando las expectativas. El vicepresidente Vance negoció en Suiza un posible "mecanismo de desconflicto" en el Líbano, que el canciller iraní Araghchi llamó "la primera prueba real" del acuerdo. **Conclusión operativa: la prima de guerra del petróleo se ha desinflado casi por completo, pero el riesgo de re-escalada sigue vivo y es asimétrico.**

### 4.2 Inflación

La inflación estadounidense se aceleró por tercer mes consecutivo: el IPC de mayo subió a **4.2% interanual** (desde 3.8% en abril), máximo desde abril de 2023, impulsado por la energía (+23.5% a/a; gasolina +40.5%; fuel oil +58.9%). La energía explicó más del 60% del alza mensual. La inflación subyacente subió a **2.9%**, máximo desde septiembre de 2025, aunque fuera de las categorías afectadas por la guerra hay señales de moderación (vehículos nuevos, muebles y medicamentos a la baja). El IPC de junio se publica a mediados de julio, **fuera de nuestra ventana**, lo que reduce el riesgo de un dato de inflación sorpresivo durante la semana.

### 4.3 Política monetaria: una Fed que ya no piensa en recortar

En su reunión del **17 de junio de 2026**, el FOMC mantuvo la tasa de fondos federales en **3.50%–3.75%** por cuarta reunión consecutiva (votación 12–0), pero dio un giro claramente restrictivo:

- Eliminó del comunicado el sesgo hacia recortes futuros.
- El *dot plot* elevó la mediana de fin de 2026 a **3.8%** (desde 3.4% en marzo): el comité contempla al menos **una subida** este año. Nueve participantes anticipan al menos una subida, ocho ningún cambio y solo uno un recorte.
- Los mercados descuentan una subida de 25 pb hacia octubre de 2026 y ningún recorte hasta 2027–2028, mientras la Fed evalúa la persistencia del choque inflacionario de la guerra.

La próxima reunión es el 28–29 de julio (fuera de la ventana), pero el **miércoles 8 de julio se publican las minutas de la reunión de junio** — el evento de política monetaria clave de nuestra semana.

### 4.4 Mercado laboral: enfriamiento visible

El informe de empleo de junio, publicado el **2 de julio** (primer día de nuestro ejercicio), mostró:

- Nóminas no agrícolas: **+57,000** vs. +115,000 esperado.
- Revisiones a la baja de abril y mayo por −74,000 acumulado.
- Tasa de desempleo: **4.2%** (bajó, pero por la caída de la participación laboral a 61.5%, mínimo desde marzo de 2021 — una baja "de mala calidad").
- Salarios: +0.3% m/m ($37.64/hora), sin señal de espiral salarial.
- Ocio y hostelería: −61,000, la mayor debilidad sectorial.

**Lectura conjunta 4.2–4.4: cuadro de estanflación moderada.** Inflación alta por oferta (energía), crecimiento del empleo casi nulo y un banco central que —por primera vez en años— no puede acudir al rescate del mercado laboral porque su prioridad es anclar las expectativas de inflación.

### 4.5 Tasas, bonos y dólar

- **Treasury 10 años: 4.49%** al cierre del 2 de julio — elevado pese al mal dato de empleo, reflejo de la prima por inflación y de la Fed restrictiva.
- **Dólar (DXY): 100.8**, retrocediendo tras el dato de empleo (venía de 101.4 y de máximos de más de un año a fines de junio). EUR/USD ≈ 1.143 pese a que el BCE subió tasas el 11 de junio.

### 4.6 Riesgos y eventos programados del 2 al 9 de julio

| Fecha | Evento | Relevancia para el portafolio |
|---|---|---|
| Jue 2 jul | Informe de empleo de junio (publicado) | Ya incorporado: débil; movió Dow al alza y dólar a la baja |
| Vie 3 jul | Operativa reducida por festivo del 4 de julio | Liquidez baja; sin decisiones |
| Lun 6 jul | Reapertura plena; sin datos mayores | Revisión de posiciones |
| Mar 7 jul | Sin datos de primer nivel | Vigilar titulares Irán/Hormuz |
| **Mié 8 jul** | **Minutas del FOMC (reunión de junio)** | **Evento clave: puede mover tasas, dólar, bolsa y oro** |
| Jue 9 jul | Presentación del proyecto; cierre del ejercicio | Valoración final |
| Continuo | Alto el fuego EE. UU.–Irán (día ~15–22 de 60) | Riesgo binario para petróleo, oro y VIX |

## 5. Contexto financiero (al cierre del 2 de julio de 2026)

| Variable | Nivel (2 jul 2026) | Lectura |
|---|---|---|
| S&P 500 (SPX) | 7,483.24 (+0.0% en el día) | Plano; sostenido pero sin dirección |
| Dow Jones | 52,900.07 (**máximo histórico**, +1.14%) | Rotación hacia valor/defensivos tras el mal dato de empleo |
| Nasdaq Composite | 25,832.67 (−0.8%) | Débil: semiconductores en caída, Tesla a la baja |
| VIX | **16.59** | Volatilidad implícita baja para el nivel de riesgo macro/geopolítico |
| Treasury 10 años | 4.49% | Prima por inflación; Fed restrictiva |
| WTI (futuro más cercano) | ≈ $68.1–68.8 | **Mínimo desde el 27 de febrero**; prima de guerra desinflada |
| Brent | $71–73 | Rango estrecho; "fatiga" del mercado con el vaivén del alto el fuego |
| Oro | > $4,100/oz (rebotando desde mínimo de 8 meses de ~$3,987 a fines de junio; el viernes 3 extendió hacia ~$4,200) | Soporte por inflación 4.2% y dólar más débil tras el empleo |
| DXY | 100.8 | Retroceso post-empleo desde máximos de un año |
| EUR/USD | ≈ 1.143 | Dólar aún fuerte en perspectiva |

**Tres asimetrías que definen el posicionamiento:**

1. **Petróleo:** cotiza en mínimos de 4 meses como si la paz fuera definitiva, cuando el alto el fuego está en periodo de prueba y ya fue cuestionado dos veces en dos semanas. El riesgo al alza (re-escalada) es mucho mayor que el riesgo a la baja adicional (la prima de guerra ya se desinfló).
2. **Volatilidad de renta variable:** un VIX de 16.6 no remunera el riesgo de unas minutas del FOMC restrictivas (8 de julio) ni la fragilidad del alto el fuego. La opcionalidad está "barata" en términos relativos.
3. **Divergencia interna de la bolsa:** Dow en máximo histórico con momentum (rotación defensiva/valor) frente a un Nasdaq presionado por semiconductores y por tasas altas que castigan la duración de los flujos tecnológicos.

## 6. Justificación de los activos seleccionados

| Activo | Vehículo | Mercado | ¿Por qué este activo? |
|---|---|---|---|
| Oro | Futuros Micro Gold (MGC) | COMEX (CME Group) | Cobertura clásica ante inflación de 4.2% y riesgo geopolítico; rebote técnico desde mínimo de 8 meses; el retroceso del dólar post-empleo le quita su principal viento en contra. Liquidez excelente; el contrato micro (10 oz) permite dimensionar con precisión. |
| Petróleo WTI | Opciones sobre futuros de crudo (CL/LO, vto. agosto) | NYMEX (CME Group) | Es el activo con la asimetría más clara de la semana: precio en mínimos de 4 meses con un alto el fuego frágil. Se accede vía opciones (no futuros) precisamente para acotar la pérdida si la paz se consolida. |
| Nasdaq-100 | Opciones sobre ETF QQQ | CBOE | Expresa la visión bajista en tecnología (semiconductores débiles, tasas altas) con riesgo definido. El ETF QQQ es el vehículo de opciones sobre Nasdaq-100 más líquido del mundo. |
| S&P 500 | Opciones sobre ETF SPY | CBOE | El índice de referencia global es el vehículo natural para comprar volatilidad barata ante las minutas del FOMC. SPY tiene el mercado de opciones más líquido en renta variable. |
| Dow Jones | Opciones sobre ETF DIA | CBOE | Permite monetizar el momentum del máximo histórico y la rotación defensiva vendiendo puts OTM con riesgo definido, generando ingreso que financia parcialmente las primas compradas. |

**Criterios transversales de selección:** (i) mercados organizados con cámara de compensación (CME Group y CBOE) — sin riesgo de contraparte bilateral; (ii) máxima liquidez en cada clase de activo; (iii) diversificación real: metales preciosos, energía y tres segmentos accionarios con tesis distintas; (iv) coherencia con el horizonte de una semana (vencimientos 10 y ~16 de julio, inmediatamente posteriores al cierre del ejercicio, para que las opciones conserven sensibilidad al subyacente sin pagar valor temporal innecesario).

**Activos considerados y descartados:** futuros de bonos del Tesoro (ZN) — la señal es contradictoria (inflación alta empuja yields arriba, empleo débil los empuja abajo) y una posición sin tesis clara es mala gestión; divisas (6E euro) — la tesis del dólar quedó ambigua tras el dato de empleo; acciones individuales — riesgo idiosincrático (resultados, noticias corporativas) difícil de justificar en una semana sin temporada de resultados.

## 7. Construcción del portafolio

**Capital: USD 1,000,000 · Fecha de apertura: jueves 2 de julio de 2026 (cierre)**

### 7.1 Tabla maestra de posiciones

| # | Activo | Derivado | Estrategia | Posición | Mercado | Apertura | Vencimiento | Precio entrada subyacente | Strikes | Prima (†est.) | Contratos | Valor nocional | Peso |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Oro | Futuro Micro Gold (MGCQ26, ago-26) | Futuros largos | Larga | COMEX | 2-jul-26 | 27-ago-26 (se cerrará el 8-jul) | ≈ $4,130/oz (†) | — | — (margen ≈ $1,700/contrato †) | 5 | $206,500 | 20.7% |
| 2 | WTI | Opciones sobre futuro CL ago-26 | **Bull Call Spread** | Larga call 70 / corta call 75 | NYMEX | 2-jul-26 | ≈ 16-jul-26 | $68.50 | 70 / 75 | Débito neto $1.30/bbl († $1.85 − $0.55) = $3,900 total | 3 | $205,500 | 20.6% |
| 3 | Nasdaq-100 (QQQ) | Opciones sobre ETF | **Bear Call Spread** | Corta call 685 / larga call 700 | CBOE | 2-jul-26 | 10-jul-26 | ≈ $673 (†) | 685 / 700 | Crédito neto $2.70 († $4.00 − $1.30) = $810 total | 3 | $201,900 | 20.2% |
| 4 | S&P 500 (SPY) | Opciones sobre ETF | **Strangle largo** | Larga call 760 + larga put 735 | CBOE | 2-jul-26 | 10-jul-26 | $748.32 | 735 (put) / 760 (call) | Débito $5.90 († put $3.20 + call $2.70) = $1,180 total | 2 | $149,660 | 15.0% |
| 5 | Dow Jones (DIA) | Opciones sobre ETF | **Bull Put Spread** | Corta put 520 / larga put 510 | CBOE | 2-jul-26 | 10-jul-26 | $529.00 | 520 / 510 | Crédito neto $1.50 († $2.20 − $0.70) = $450 total | 3 | $158,700 | 15.9% |
| | | | | | | | | | | | **Total** | **$922,260** | **92.2%** |

(†) Primas y precio de futuros estimados según la metodología de la sección 3 (Black–Scholes con IV observable; QQQ estimado a partir del Nasdaq-100 ≈ 27,600 y ratio QQQ≈NDX/41; futuro de oro ≈ spot + contango leve). El 7.8% restante (USD 77,740) se mantiene como colchón de liquidez en T-bills (~3.6% anual) para llamadas de margen.

### 7.2 Capital comprometido (primas y márgenes)

| Concepto | Monto |
|---|---|
| Débito bull call spread WTI | −$3,900 |
| Débito strangle SPY | −$1,180 |
| Crédito bear call spread QQQ | +$810 |
| Crédito bull put spread DIA | +$450 |
| **Primas netas pagadas** | **−$3,820** |
| Margen futuros MGC (5 × ~$1,700 †) | $8,500 |
| Margen spreads cortos (= pérdida máxima: $3,690 + $2,550) | $6,240 |
| **Capital total comprometido** | **≈ $18,560 (1.9% del capital)** |

Esto ilustra el rasgo esencial de los derivados: con menos del 2% del capital se controla una exposición económica del 92% del portafolio objetivo. El apalancamiento no se usa aquí para amplificar riesgo — la pérdida máxima conjunta está estrictamente acotada (sección 10) — sino para liberar capital que permanece en instrumentos líquidos.

### 7.3 Tablas de distribución

**Por clase de activo (sobre nocional):**

| Clase | Nocional | Peso |
|---|---|---|
| Metales preciosos (oro) | $206,500 | 22.4% |
| Energía (WTI) | $205,500 | 22.3% |
| Renta variable EE. UU. | $510,260 | 55.3% |

**Por sector/segmento accionario:**

| Segmento | Nocional | Sesgo |
|---|---|---|
| Tecnología / crecimiento (QQQ) | $201,900 | Bajista (acotado) |
| Mercado amplio (SPY) | $149,660 | Neutral direccional / largo volatilidad |
| Industrial / valor (DIA) | $158,700 | Alcista (acotado) |

**Por estrategia:**

| Estrategia | Nocional | Peso | Naturaleza |
|---|---|---|---|
| Futuros largos | $206,500 | 22.4% | Direccional pura |
| Bull call spread | $205,500 | 22.3% | Direccional alcista, riesgo definido |
| Bear call spread | $201,900 | 21.9% | Direccional bajista, ingreso, riesgo definido |
| Strangle largo | $149,660 | 16.2% | Volatilidad (no direccional) |
| Bull put spread | $158,700 | 17.2% | Direccional alcista, ingreso, riesgo definido |

**Por perfil de riesgo:**

| Perfil | Posiciones | Pérdida máxima asociada |
|---|---|---|
| Riesgo acotado y conocido ex ante | #2, #3, #4, #5 | $3,900 + $3,690 + $1,180 + $2,550 = $11,320 |
| Riesgo abierto con stop-loss | #1 (futuros de oro; stop en $3,950/oz) | ≈ $9,000 con stop ejecutado |

## 8. Justificación individual de cada posición

### Posición 1 — Futuros largos de oro (5 × MGC agosto, COMEX)

- **¿Por qué este activo?** El oro es el único activo que se beneficia simultáneamente de los dos riesgos dominantes del momento: inflación de 4.2% (máximo en 3 años) y re-escalada geopolítica. Además, acaba de rebotar desde un mínimo de 8 meses (~$3,987 a fines de junio) y su principal lastre —el dólar en máximos de un año— acaba de ceder (DXY 101.4 → 100.8 tras el mal dato de empleo).
- **¿Por qué esta estrategia (futuros largos)?** Es la expresión más limpia y barata de una visión direccional alcista: sin pago de prima, sin decaimiento temporal (theta = 0), liquidez inmediata y delta 1. El contrato micro (10 oz) permite calibrar la exposición a ~20% del portafolio, imposible con el contrato estándar GC (100 oz ≈ $413,000, que forzaría un 41%).
- **¿Qué espero que ocurra?** Continuación del rebote hacia $4,250–4,300 durante la semana, apoyada en el dólar débil post-empleo y en unas minutas del FOMC que confirmen la preocupación por la persistencia de la inflación.
- **¿Qué riesgo intento aprovechar?** La combinación inflación alta + geopolítica frágil + dólar cediendo, con el mercado saliendo de un extremo pesimista en oro (mínimo de 8 meses hace una semana).
- **Escenario ganador:** dólar sigue débil, minutas confirman inflación persistente, o cualquier titular negativo sobre el alto el fuego. Oro a $4,250+ → +$6,000 o más.
- **Escenario perdedor:** consolidación creíble de la paz + minutas que sugieran que la subida de tasas es inminente → dólar arriba, oro de vuelta a $4,000.
- **Pérdida máxima:** teóricamente abierta (es un futuro); **gestionada con stop-loss en $3,950/oz** (bajo el mínimo de fines de junio): pérdida ≈ (4,130 − 3,950) × 50 oz = **$9,000 (0.9% del capital)**.
- **Ganancia potencial:** ilimitada en teoría; objetivo de la semana $4,300 → (4,300 − 4,130) × 50 = **+$8,500**.
- **Eventos a favor:** ruptura del alto el fuego, minutas restrictivas que eleven la prima por riesgo de inflación, dólar débil, dato débil adicional de actividad.
- **Eventos en contra:** avance del "mecanismo de desconflicto" en el Líbano, retórica de subida inminente que dispare el dólar y los yields reales.
- **¿Por qué no otra estrategia?** Una compra de call habría pagado una volatilidad implícita elevada tras el rebote (prima cara y theta en contra en una semana); un bull call spread limitaría el recorrido justo cuando el rebote puede extenderse. Con stop-loss disciplinado, el futuro ofrece mejor perfil coste/beneficio.
- **Ventajas:** sin theta, sin prima, liquidez, ejecución inmediata del stop. **Desventajas:** riesgo abierto sin el stop, exposición a huecos de apertura (gap risk) nocturnos, llamadas de margen si el mercado va en contra.

### Posición 2 — Bull Call Spread sobre WTI (3 × call 70 comprada / call 75 vendida, opciones sobre CL agosto, NYMEX)

- **¿Por qué este activo?** El WTI a $68.5 cotiza en su nivel más bajo desde el 27 de febrero: el mercado ha eliminado prácticamente toda la prima de guerra, pese a que el alto el fuego (día ~15 de 60) ya fue puesto en duda dos veces (cierre declarado del estrecho el 20 de junio; negativa iraní a reunirse con enviados de EE. UU. el 1 de julio). La distribución de riesgos es asimétrica: poco recorrido adicional a la baja, mucho al alza si algo se rompe.
- **¿Por qué esta estrategia?** El bull call spread compra esa asimetría con **pérdida máxima conocida y pequeña** (el débito de $3,900) y sin exposición a que la paz se consolide más allá de esa prima. Vender la call 75 financia un 30% del coste de la call 70 y renuncia solo al recorrido por encima de $75 (+9.5%), improbable en una semana salvo re-escalada mayor — y si ocurre, el spread ya paga su máximo.
- **¿Qué espero que ocurra?** No necesariamente una ruptura del alto el fuego: basta con que el mercado re-precie algo de prima de riesgo (WTI $71–74) ante cualquier fricción en las negociaciones.
- **¿Qué riesgo intento aprovechar?** La complacencia del mercado petrolero ("fatiga" con el vaivén del alto el fuego, según OilPrice) frente a un proceso de paz objetivamente frágil.
- **Escenario ganador:** WTI ≥ $75 al vencimiento → ganancia máxima = (5.00 − 1.30) × 1,000 × 3 = **+$11,100** (ratio beneficio/riesgo 2.85:1). Con WTI en $72, el spread vale ≈ $2.6–3.0 → +$4,000–5,000.
- **Escenario perdedor:** paz consolidada, WTI ≤ $70 al vencimiento → pérdida del débito.
- **Pérdida máxima:** **$3,900** (0.39% del capital), pagada por adelantado.
- **Ganancia potencial:** **$11,100** (máx.).
- **Eventos a favor:** cualquier incidente en Hormuz o Líbano, fracaso de la reunión con enviados de EE. UU., datos de inventarios EIA a la baja.
- **Eventos en contra:** firma del mecanismo de desconflicto, aumento de oferta OPEP+, datos débiles de demanda china.
- **¿Por qué no otra estrategia?** Futuros largos de crudo expondrían a pérdidas grandes si la paz avanza (el escenario base de los mediadores); una call seca (70) costaría ~$1.85/bbl con theta intenso; un strangle sobre crudo es caro con la volatilidad implícita del petróleo aún elevada (~38%) — precisamente conviene *comprar* opcionalidad donde la IV es baja (equities) y *estructurarla en spread* donde es alta (crudo).
- **Ventajas:** riesgo definido, coste reducido por la venta de la 75, se beneficia de la asimetría. **Desventajas:** ganancia limitada, theta neto negativo si el crudo no se mueve, vencimiento (~16 jul) poco después del cierre del ejercicio obliga a valorar a mercado el 8 de julio.

### Posición 3 — Bear Call Spread sobre Nasdaq-100 (3 × call 685 vendida / call 700 comprada, QQQ, CBOE, vto. 10-jul)

- **¿Por qué este activo?** La tecnología es el eslabón débil de la bolsa: el 2 de julio el Nasdaq cayó 0.8% (con el Dow en máximo histórico), los semiconductores encadenan caídas y las tasas altas (10Y en 4.49%, Fed sin recortes a la vista) castigan a los activos de larga duración.
- **¿Por qué esta estrategia?** El bear call spread permite cobrar prima si el Nasdaq **no sube con fuerza** — no exige acertar una caída, solo que QQQ no supere 685 (+1.8%) en la semana. Es una visión bajista "de baja convicción direccional pero alta convicción de techo", con riesgo definido.
- **¿Qué espero que ocurra?** Nasdaq lateral o a la baja mientras el liderazgo rota a valor/defensivos y las minutas del FOMC recuerdan que no habrá recortes.
- **¿Qué riesgo intento aprovechar?** La continuación de la rotación sectorial y la presión de tasas sobre múltiplos tecnológicos.
- **Escenario ganador:** QQQ ≤ 685 el 10 de julio → se retiene el crédito íntegro: **+$810**.
- **Escenario perdedor:** rebote fuerte de la tecnología (recompra de semiconductores, resultados o guías positivas) → QQQ ≥ 700 → pérdida máxima.
- **Pérdida máxima:** (15 − 2.70) × 100 × 3 = **$3,690** (0.37% del capital).
- **Ganancia potencial:** **$810** (el crédito).
- **Eventos a favor:** minutas restrictivas, yields al alza, más debilidad de semiconductores.
- **Eventos en contra:** rebote técnico del sector chips (sobrevendido a corto plazo — riesgo real), caída de yields por datos débiles.
- **¿Por qué no otra estrategia?** Futuros cortos de Nasdaq (MNQ) tendrían riesgo abierto al alza en un índice que sigue en tendencia alcista estructural — imprudente; una compra de put exige que la caída ocurra *ya* (theta en contra); el bear call spread gana también en escenario lateral, que es el más probable en semana festiva.
- **Ventajas:** cobra theta, gana en 2 de 3 escenarios (baja y lateral), riesgo definido. **Desventajas:** perfil asimétrico desfavorable (arriesga $3,690 por ganar $810 — requiere probabilidad de éxito alta, estimada >75% con el strike a 0.6σ), vulnerable a un rally violento.

### Posición 4 — Strangle largo sobre S&P 500 (2 × call 760 + put 735, SPY, CBOE, vto. 10-jul)

- **¿Por qué este activo?** El S&P 500 es el índice donde el mispricing de volatilidad es más claro: VIX en 16.59 — nivel de calma— en una semana con minutas del FOMC (8-jul), un alto el fuego en periodo de prueba y un mercado laboral que acaba de sorprender muy a la baja.
- **¿Por qué esta estrategia?** El strangle largo compra movimiento **en cualquier dirección** sin apostar por una: si las minutas son muy restrictivas, el índice cae (gana la put); si el mercado celebra un giro suave o se rompe el alto el fuego con vuelo a calidad... cada cola tiene su pata. Se eligió strangle y no straddle porque las patas OTM (±1.6/1.7%) cuestan la mitad y el escenario que se juega es un movimiento *grande*, no uno marginal.
- **¿Qué espero que ocurra?** Un movimiento del SPX superior a ±1.6% en la semana, o un repunte del VIX (de 16.6 hacia 20+) que revalorice ambas patas por vega antes del vencimiento.
- **¿Qué riesgo intento aprovechar?** Volatilidad implícita barata frente a un calendario de eventos denso: compro seguro barato antes de la tormenta posible.
- **Escenario ganador:** |ΔSPX| > ~2.4% al vencimiento (breakeven: 735 − 5.9 = 729.1 o 760 + 5.9 = 765.9 en SPY) o repunte de VIX que permita cerrar antes con ganancia por vega.
- **Escenario perdedor:** semana lateral y tranquila → ambas patas expiran sin valor.
- **Pérdida máxima:** el débito total: **$1,180** (0.12% del capital).
- **Ganancia potencial:** ilimitada al alza, muy elevada a la baja (la put paga hasta 735 × 100 × 2 por debajo del strike).
- **Eventos a favor:** minutas con sorpresa (en cualquier sentido), titular geopolítico, movimiento brusco de yields.
- **Eventos en contra:** el enemigo es el tiempo: cada día lateral cuesta theta (~$150–200/día estimado en el tramo final).
- **¿Por qué no otra estrategia?** Un straddle ATM costaría ≈ el doble con breakevens similares en porcentaje; strip o strap añadirían sesgo direccional que no tengo; comprar solo put dejaría sin cobertura el escenario de rally.
- **Ventajas:** riesgo mínimo en dólares, convexidad pura, cubre el riesgo de cola del resto del portafolio (si todo cae con violencia, la put del strangle amortigua). **Desventajas:** theta muy negativo en vencimiento corto, requiere movimiento pronto, probabilidad de perder el 100% de la prima es alta (>50%) — por eso su peso en prima es el menor del portafolio.

### Posición 5 — Bull Put Spread sobre Dow Jones (3 × put 520 vendida / put 510 comprada, DIA, CBOE, vto. 10-jul)

- **¿Por qué este activo?** El Dow acaba de marcar máximo histórico (52,900) subiendo 1.14% *el mismo día* de un mal dato de empleo: la rotación hacia valor/defensivos tiene momentum propio y es el segmento más fuerte del mercado.
- **¿Por qué esta estrategia?** Vender un put spread OTM (strike corto 520, −1.7% del spot) monetiza ese momentum sin pagar prima: gana si el Dow sube, se queda lateral o incluso cae hasta −1.7% en la semana. Los créditos de esta posición y de la #3 financian el 107% del débito del strangle — el portafolio compra volatilidad casi "gratis".
- **¿Qué espero que ocurra?** Dow sostenido por encima de 52,000 (DIA > 520) hasta el 10 de julio.
- **¿Qué riesgo intento aprovechar?** La persistencia a corto plazo de la rotación sectorial (los flujos hacia valor no se revierten en tres sesiones) y el "suelo" psicológico de un máximo histórico reciente.
- **Escenario ganador:** DIA ≥ 520 al vencimiento → crédito íntegro: **+$450**.
- **Escenario perdedor:** shock de mercado amplio (minutas muy duras, evento geopolítico) que arrastre también al Dow más de 1.7%.
- **Pérdida máxima:** (10 − 1.50) × 100 × 3 = **$2,550** (0.26% del capital) si DIA ≤ 510.
- **Ganancia potencial:** **$450**.
- **Eventos a favor:** continuación de la rotación, estabilidad de yields. **Eventos en contra:** los mismos shocks que benefician al strangle del S&P — por diseño: esta posición está parcialmente **cubierta por la put 735 de SPY** (sección 9).
- **¿Por qué no otra estrategia?** Futuros largos del Dow duplicarían el riesgo direccional alcista sin protección; una compra de call paga theta contra un índice que puede simplemente consolidar el máximo; el bull put spread gana también en lateral.
- **Ventajas:** ingreso, theta a favor, gana en 2 de 3 escenarios, riesgo definido. **Desventajas:** asimetría riesgo/beneficio desfavorable (típica de venta de prima), correlacionada con shocks sistémicos.

## 9. Estrategia general del portafolio

**Tesis central:** *entorno de estanflación moderada con riesgo geopolítico infravalorado.* El portafolio no es una apuesta direccional sobre la bolsa: es una cartera de **asimetrías**:

1. **Largo activos reales** (oro con delta 1, petróleo con riesgo acotado) contra el riesgo inflacionario y geopolítico.
2. **Neutral-vendido en el agregado bursátil con pares internos:** bajista acotado en tecnología (QQQ) contra alcista acotado en valor (DIA) — una apuesta de *rotación relativa*, no de dirección; el nocional bajista tech ($202k) y el alcista Dow ($159k) se compensan en gran parte.
3. **Largo volatilidad** (strangle SPY) financiado con la venta de prima de los dos spreads de crédito (+$1,260 de créditos vs. −$1,180 de débito del strangle).

**Interacción entre posiciones (cómo se cubren entre sí):**

- Si estalla un **shock geopolítico**: pierden DIA (−$2,550 máx.) y nada más del lado corto de prima; ganan simultáneamente el oro, el spread de crudo, el bear call de QQQ y la put del strangle → resultado neto muy positivo.
- Si hay **calma total y rally tecnológico**: pierden el strangle (−$1,180), el bear call QQQ (−$3,690 máx.), el oro (parcial) y el spread de crudo (−$3,900 máx.); gana DIA (+$450). Es el peor escenario del portafolio, y aun así la pérdida está acotada (~−1.5%).
- Si el mercado queda **lateral**: los dos spreads de crédito cobran ($1,260), el strangle pierde ($1,180), oro y crudo dependen de sus propios drivers → resultado ≈ neutro. El portafolio no "sangra" en lateral: la venta de prima paga la compra de prima.

**Exposición direccional neta aproximada (en delta-nocional):** renta variable ≈ −$45k (ligeramente corto: −$202k tech +$159k Dow, strangle ≈ delta 0); materias primas ≈ +$310k (oro delta 1 por $206k + crudo delta ≈ 0.5 por $205k). El portafolio está, en síntesis, **largo economía real / inflación y plano-defensivo en renta variable**.

## 10. Gestión del riesgo

### 10.1 Mapa de riesgos

| Riesgo | Evaluación | Mitigación |
|---|---|---|
| **De mercado** | Exposición neta bursátil casi plana; direccional concentrado en oro y crudo | Stop-loss en oro ($3,950); riesgo de crudo limitado al débito |
| **De volatilidad (vega)** | Neto largo vega (strangle) — el portafolio se *beneficia* de un repunte del VIX | Es cobertura, no riesgo: la posición corta de vega de los spreads es menor y lejana del dinero |
| **De liquidez** | Todos los instrumentos son de máxima liquidez mundial (MGC, CL, SPY, QQQ, DIA); semana festiva reduce volumen el 3 y 6 de julio | No operar en la sesión reducida; órdenes limitadas siempre |
| **De apalancamiento** | Nocional 92% del capital con solo 1.9% comprometido — apalancamiento *disponible* pero no *utilizado* | Colchón de $78k en T-bills cubre >8 veces la peor llamada de margen concebible de la semana |
| **De concentración** | Máx. 22.4% de nocional por activo; 5 subyacentes, 3 clases de activo, 5 estrategias distintas | Límite autoimpuesto de 25% por subyacente |
| **De evento (gap)** | Minutas FOMC 8-jul y alto el fuego pueden abrir mercados con hueco | El strangle largo es la cobertura explícita de gaps; riesgo abierto solo en oro (a favor del gap típico de estos eventos) |

### 10.2 Pérdida máxima agregada

Suma de peores casos simultáneos (escenario imposible por construcción, pues exige a la vez rally tech, calma total y desplome del oro, pero útil como cota superior absoluta):

$3,900 (crudo) + $3,690 (QQQ) + $1,180 (strangle) + $2,550 (DIA) + $9,000 (oro con stop) = **$20,320 = 2.03% del capital**.

La pérdida *plausible* en el peor escenario coherente (sección 11, pesimista) es ≈ −$15,000 (−1.5%).

### 10.3 Griegas del portafolio (análisis conceptual y aproximado)

- **Delta:** ligeramente positivo total (dominado por el oro, +50 oz ≈ delta $206k; equities casi neto cero; crudo +Δ≈0.5×3 contratos). Interpretación: el portafolio gana con "más inflación/riesgo real" más que con "más bolsa".
- **Gamma:** positiva neta cerca de los strikes del strangle (SPY 735/760): ante un movimiento grande del S&P, el delta del portafolio se ajusta *a favor* automáticamente. Los spreads cortos aportan gamma negativa pero limitada por sus patas largas.
- **Theta:** aproximadamente neutra por diseño: el strangle pierde ~$150–200/día, los dos spreads de crédito cobran en conjunto una cifra similar. El bull call de crudo aporta theta negativa moderada. El portafolio no paga renta por esperar.
- **Vega:** positiva neta (~+$300 por punto de VIX, estimado): un salto del VIX de 16.6 a 22 aportaría ≈ +$1,600 solo por revalorización de volatilidad, además del efecto direccional.
- **Rho:** marginal en una semana; indirectamente, subidas de yields perjudican a QQQ (a favor de la posición #3) y al oro (en contra de la #1) — otra compensación interna.

## 11. Escenarios (horizonte: cierre del 8 de julio / vencimientos 10 y 16 de julio)

### Escenario OPTIMISTA para el portafolio (prob. estimada ~25%): fricción geopolítica + minutas restrictivas

Supuestos: incidente o retórica dura en torno al alto el fuego; minutas del 8-jul confirman sesgo de subida. WTI +8% → $74; oro +3% → $4,254; SPX −3%; Nasdaq −4%; Dow −2.5%.

| Posición | Resultado | Explicación |
|---|---|---|
| Oro (futuros) | **+$6,200** | Vuelo a calidad + prima inflacionaria |
| Bull call WTI | **+$6,300** | Spread se revaloriza a ~$3.40 con WTI en 74 |
| Bear call QQQ | **+$810** | QQQ cae lejos de 685: crédito íntegro |
| Strangle SPY | **+$680** | Put 735 entra en dinero (SPY ~725.9) + vega |
| Bull put DIA | **−$810** | DIA ~515.8: put 520 en dinero; pérdida parcial |
| **Total** | **≈ +$13,200 (+1.3% en la semana)** | Las asimetrías compradas pagan; la única pérdida es la posición pro-cíclica, acotada |

### Escenario BASE (prob. ~50%): semana lateral, minutas sin sorpresas

Supuestos: WTI $69; oro $4,150; SPX +0.5%; Nasdaq +1%; Dow +0.5%.

| Posición | Resultado | Explicación |
|---|---|---|
| Oro (futuros) | **+$1,000** | Deriva leve al alza con dólar contenido |
| Bull call WTI | **−$600** | Valoración a mercado el 8-jul: pierde algo de valor temporal |
| Bear call QQQ | **+$810** | QQQ ~679.7 < 685: crédito íntegro |
| Strangle SPY | **−$1,180** | Sin movimiento: ambas patas expiran sin valor |
| Bull put DIA | **+$450** | DIA > 520: crédito íntegro |
| **Total** | **≈ +$480 (+0.05%)** | El portafolio "flota" en lateral: la prima vendida paga la comprada — diseño intencional |

### Escenario PESIMISTA para el portafolio (prob. ~25%): paz consolidada + rally tecnológico

Supuestos: avance creíble del mecanismo de desconflicto; minutas menos duras de lo temido; recompra de semiconductores. WTI −7% → $63.7; oro −4% → $3,965 (salta el stop en 3,950 sin ejecutarse aún: valoramos a 3,965); Nasdaq +5% → QQQ ~707; SPX +2.5%; Dow +2%.

| Posición | Resultado | Explicación |
|---|---|---|
| Oro (futuros) | **−$8,250** | Sin demanda refugio y con dólar/tasas reales arriba |
| Bull call WTI | **−$3,900** | Prima de guerra eliminada del todo: pérdida máxima |
| Bear call QQQ | **−$3,690** | QQQ > 700: pérdida máxima del spread |
| Strangle SPY | **+$220** | La call 760 entra en dinero (SPY ~767): amortigua |
| Bull put DIA | **+$450** | Dow sube: crédito íntegro |
| **Total** | **≈ −$15,200 (−1.5%)** | Peor escenario coherente; nótese que aun así la pérdida es 1.5% del capital gracias al riesgo definido en 4 de 5 posiciones |

**Lectura económica conjunta:** el perfil es convexo a favor del gestor: +1.3% / +0.05% / −1.5% con probabilidades 25/50/25 da una esperanza ≈ +$270 y, más importante, **ninguna trayectoria destruye el capital**. En derivados, sobrevivir a la semana mala vale más que optimizar la buena.

## 12. Plan de monitoreo diario (2–9 de julio)

Checklist a ejecutar cada mañana antes de la apertura (8:00 ET) y al cierre:

| # | Variable | Fuente rápida | ¿Por qué importa a ESTE portafolio? |
|---|---|---|---|
| 1 | Titulares Irán / Hormuz / Líbano | Reuters, OilPrice | Driver binario de crudo (#2), oro (#1) y VIX (#4) |
| 2 | Calendario económico del día | TradingEconomics | Evita sorpresas; el 8-jul (minutas) es el evento de la semana |
| 3 | Comunicación de la Fed (discursos, minutas) | federalreserve.gov | Redefine tasas, dólar, oro y múltiplos tech |
| 4 | Inflación (expectativas, breakevens) | FRED | Sostiene la tesis del oro; el IPC de junio cae fuera de la ventana pero los breakevens se mueven a diario |
| 5 | Empleo (peticiones semanales de desempleo, jueves) | BLS/DOL | Confirma o desmiente el enfriamiento del 2-jul |
| 6 | PIB / PMI (nowcasts) | Atlanta Fed GDPNow | Contexto de crecimiento para la rotación valor/tech |
| 7 | Treasury 10Y (4.49% de partida) | CNBC/FRED | >4.60% presiona a QQQ (a favor de #3) y al oro (contra #1); <4.35% lo contrario |
| 8 | VIX (16.59 de partida) | CBOE | El strangle (#4) vive de esto: >20 = evaluar toma de ganancias por vega |
| 9 | S&P 500 (7,483) | — | Breakevens del strangle: 7,291 / 7,659 aprox. en índice |
| 10 | Nasdaq (25,833) / semiconductores (SOX) | — | Strike corto QQQ 685 ≈ Nasdaq-100 28,085: la línea roja de #3 |
| 11 | Dow (52,900) | — | Strike corto DIA 520 ≈ Dow 52,000: la línea roja de #5 |
| 12 | WTI ($68.5) y Brent ($71–73) | CME/ICE | Zona de pago de #2 desde $71.30 (breakeven) |
| 13 | Oro ($4,130 entrada) | COMEX | Stop $3,950; objetivo $4,300 |
| 14 | Dólar DXY (100.8) | — | Correlación negativa con oro y crudo |
| 15 | Volatilidad implícita por activo (OVX, IV de QQQ) | CBOE | Decide si conviene rolar spreads o monetizar el strangle |
| 16 | Volumen y open interest de nuestras opciones | CME/CBOE | Salud de la liquidez para salir sin castigo de horquilla |
| 17 | Eventos geopolíticos no-Irán (Asia, Rusia) | — | Riesgo de cola adicional que el strangle cubriría |

## 13. Reglas para modificar el portafolio (SI → ENTONCES)

**Volatilidad**
- SI el VIX supera 20 → ENTONCES vender la mitad del strangle SPY (monetizar vega) y mantener la otra mitad hasta las minutas.
- SI el VIX cae bajo 14 → ENTONCES cerrar el strangle (el mercado niega el escenario de evento; salvar valor temporal restante) y evaluar añadir un segundo bull put spread en DIA con el ingreso.

**Renta variable**
- SI el S&P rompe 7,550 (resistencia = zona de máximos) con amplitud → ENTONCES cerrar el bear call de QQQ antes de que el rally lo arrastre y dejar correr la call 760 del strangle.
- SI el S&P pierde 7,300 (soporte ≈ breakeven inferior del strangle) → ENTONCES cerrar el bull put de DIA (limitar pérdida antes del máximo) y dejar correr la put 735.
- SI QQQ cierra por encima de 685 (strike corto) cualquier día → ENTONCES cerrar o rolar el bear call spread: la regla es no esperar al vencimiento con el strike corto en dinero.
- SI DIA cierra bajo 523 (margen de 3 puntos sobre el strike corto) → ENTONCES cerrar el bull put spread con pérdida parcial pequeña.

**Petróleo**
- SI el WTI supera $73 antes del 8-jul → ENTONCES vender la mitad del bull call spread (asegurar ganancia) y mantener el resto por si hay ruptura del alto el fuego.
- SI el WTI cae bajo $65 → ENTONCES cerrar el spread y aceptar la pérdida parcial: la tesis de re-precio de riesgo habría fallado.
- SI se rompe formalmente el alto el fuego → ENTONCES mantener todo el spread hasta cerca del máximo ($75+) y subir el stop del oro a breakeven.

**Oro**
- SI el oro toca $3,950 → ENTONCES stop-loss automático: cerrar los 5 MGC sin discusión.
- SI el oro supera $4,300 → ENTONCES vender 2 de los 5 contratos (realizar 40%) y subir el stop del resto a $4,150 (entrada).
- SI el DXY recupera 102 → ENTONCES reducir oro a 3 contratos aunque no toque el stop: el viento en contra invalida parcialmente la tesis.

**Tasas y Fed**
- SI las minutas del 8-jul son claramente restrictivas (subida "pronto") → ENTONCES esperar el movimiento, monetizar la pata ganadora del strangle el mismo día (la put, previsiblemente) y cerrar el oro si el dólar salta.
- SI las minutas son más suaves de lo esperado → ENTONCES cerrar el bear call de QQQ inmediatamente (el alivio de tasas dispara la tecnología) y dejar correr DIA.
- SI el 10Y supera 4.65% → ENTONCES mantener QQQ corto, vigilar stop del oro (los yields reales altos lo castigan).

**Empleo e inflación**
- SI las peticiones semanales de desempleo (jueves) saltan por encima de ~260k → ENTONCES el mercado re-precia recortes pese a la Fed: cerrar QQQ bear call, mantener oro.
- SI los breakevens de inflación suben 10 pb en la semana → ENTONCES añadir 2 MGC (la tesis del oro se refuerza).

**Geopolítica**
- SI ocurre un evento geopolítico mayor fuera de Irán → ENTONCES el strangle y el oro son la cobertura; no sobre-reaccionar: revisar el mapa de riesgos antes de tocar nada.

## 14. Estrategias alternativas (si la hipótesis deja de cumplirse)

| Situación nueva | Estrategia de reemplazo (del temario) | Justificación del cambio |
|---|---|---|
| La paz se consolida de forma creíble (crudo bajo $65, oro bajo $4,000) | Sustituir el bull call de WTI por un **bear put spread** (p. ej. 66/61) | La asimetría se invierte: el exceso de oferta y la normalización de Hormuz harían del crudo un activo en tendencia bajista con la OPEP+ recuperando cuota |
| La tecnología confirma suelo y lidera de nuevo | Reemplazar el bear call de QQQ por un **bull call spread** en QQQ (o cerrar y no reemplazar) | Contra la cinta no se lucha: si el liderazgo vuelve al growth, la posición de rotación pierde su base |
| El VIX salta a >25 (pánico) | Cambiar el strangle largo por venta parcial + **butterfly** de puts (comprar 1 put ATM, vender 2 OTM, comprar 1 más OTM) | Con IV alta ya no conviene ser comprador neto de volatilidad; el butterfly monetiza la IV cara apuntando al rango de aterrizaje |
| Convicción bajista fuerte tras minutas muy duras | **Strip** sobre SPY (2 puts + 1 call) en vez de strangle | Mantiene cobertura al alza pero dobla la sensibilidad al escenario bajista que habría ganado probabilidad |
| Convicción alcista fuerte tras minutas suaves | **Strap** sobre SPY (2 calls + 1 put) | Simétrico del anterior |
| El Dow pierde el momentum (cierra bajo 52,000) | Cerrar bull put de DIA; si la debilidad es general, **bear call spread** en DIA | La tesis del momentum del máximo histórico quedaría invalidada; no se promedia a la baja una posición de venta de prima |
| Se desea neutralizar todo el riesgo direccional a un coste conocido | **Box spread** en SPY (bull call + bear put con los mismos strikes) | Convierte la posición en renta fija sintética: útil solo como ejercicio de arbitraje/aparcamiento de valor, no como especulación |
| El oro rompe $4,300 con fuerza | Sustituir 2 MGC por **compra de call** OTM sobre GC | Convierte ganancia no realizada en riesgo limitado manteniendo exposición a la continuación |

## 15. Conclusiones

1. **Decisiones acertadas (evaluación al 6 de julio, se completará el 8–9):** construir el portafolio alrededor de asimetrías y no de predicciones puntuales; financiar la compra de volatilidad con venta de prima OTM; usar contratos micro para dimensionar el oro; y acceder al petróleo mediante spreads en lugar de futuros — la posición habría sufrido si la paz avanza, y con el spread la pérdida está acotada a 0.39% del capital.
2. **Riesgos asumidos conscientemente:** riesgo abierto (con stop) en oro; riesgo de rebote técnico en tecnología (la posición #3 es la más vulnerable de la cartera, como confirmó el rebote tecnológico del 3–6 de julio — véase bitácora); theta del strangle si la semana resulta anodina.
3. **Aprendizajes:** (i) en derivados, la pregunta correcta no es "¿qué va a pasar?" sino "¿qué está mal precificado?"; (ii) la estructura (spread vs. posición seca, strangle vs. straddle, micro vs. estándar) importa tanto como la dirección; (iii) un portafolio de opciones bien construido puede tener pérdida máxima total inferior al 2% del capital y aun así exposición económica de 92% — el apalancamiento es una herramienta de eficiencia de capital, no necesariamente de riesgo; (iv) la gestión dinámica con reglas escritas ex ante (sección 13) elimina la tentación de improvisar bajo presión.
4. **Qué modificaría con retrospectiva:** habría dimensionado el bear call spread de QQQ con el strike corto más lejos (700 en vez de 685) aceptando menos crédito: la sesión del 2 de julio ya insinuaba que el castigo a los semiconductores estaba maduro para un rebote; y habría abierto el strangle el martes 7 en lugar del jueves 2, pagando menos theta por el mismo evento (minutas del 8).
5. **Si el horizonte fuera de un mes (hasta el 8 de agosto):** cambiaría la arquitectura: (i) vencimientos de agosto/septiembre para reducir el coste relativo de theta; (ii) incluiría la reunión del FOMC del 28–29 de julio y el IPC de junio (14 de julio) como eventos centrales — probablemente con un **straddle** sobre SPY de vencimiento posterior al FOMC; (iii) el día ~60 del alto el fuego (mediados de agosto) caería dentro del horizonte: el bull call spread de crudo se construiría sobre vencimiento septiembre con strikes más ambiciosos (72/80); (iv) añadiría una posición en tasas (futuros cortos de ZN o bear call spread sobre TLT) que en una semana no tenía tesis clara pero que a un mes, con una Fed inclinada a subir, sí la tiene; y (v) el tamaño por posición bajaría (máx. 15% de nocional) porque a mayor horizonte, mayor probabilidad de eventos no previstos.

**Nota final:** la administración dinámica día a día (apertura del 2 de julio, festivo, revisión del 6 de julio con el rebote tecnológico, decisión previa a las minutas del 7, reacción a las minutas del 8 y cierre valorativo) se documenta en el archivo complementario **`bitacora_gestion.md`**, que forma parte integral de este trabajo.

## 16. Referencias

Datos y hechos utilizados (consultados el 6 de julio de 2026):

- CNBC — [Fed interest rate decision June 2026: Fed holds rates steady](https://www.cnbc.com/2026/06/17/fed-interest-rate-decision-june-2026.html); [Jobs report June 2026](https://www.cnbc.com/2026/07/02/jobs-report-june-2026-.html); [Dow jumps nearly 600 points to record close; Nasdaq slides](https://www.cnbc.com/2026/07/01/stock-market-today-live-updates.html)
- Federal Reserve — [FOMC statement, June 17, 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm); [Meeting calendars and information](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- BLS — [Employment Situation — June 2026](https://www.bls.gov/news.release/archives/empsit_07022026.htm)
- TradingKey — [June Fed Decision: dot plot raised, 9 back continued rate hikes in 2026](https://www.tradingkey.com/analysis/economic/central-banks/261973912-fed-federal-fomc-2-economic-projections-decision-rates-tradingkey)
- Trading Economics — [US Inflation Rate (May 2026: 4.2%)](https://tradingeconomics.com/united-states/inflation-cpi); [Crude Oil](https://tradingeconomics.com/commodity/crude-oil); [Gold](https://tradingeconomics.com/commodity/gold); [US Dollar](https://tradingeconomics.com/united-states/currency)
- CBS News — [Inflation topped 4% in May as CPI surged](https://www.cbsnews.com/news/cpi-report-today-may-2026-inflation-iran-war-trump/); [Iran war economic impact](https://www.cbsnews.com/news/iran-war-economic-impact-gas-prices-inflation-2026/)
- Wikipedia — [2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war); [2026 Strait of Hormuz crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis); [Economic impact of the 2026 Iran war](https://en.wikipedia.org/wiki/Economic_impact_of_the_2026_Iran_war)
- OilPrice — [Oil Markets Grow Numb to U.S.-Iran Ceasefire Drama](https://oilprice.com/Energy/Crude-Oil/Oil-Markets-Grow-Numb-to-US-Iran-Ceasefire-Drama.amp.html)
- Business Standard — [Oil prices rise as Iran's refusal to meet US envoys dims ceasefire hopes](https://www.business-standard.com/amp/markets/commodities/oil-prices-rise-as-iran-s-refusal-to-meet-us-envoys-dims-ceasefire-hopes-126070100098_1.html)
- Advisor Perspectives — [Treasury Yields Snapshot: July 2, 2026 (10Y: 4.49%)](https://www.advisorperspectives.com/dshort/updates/2026/07/02/treasury-yields-snapshot-july-2-2026)
- TheStreet — [Stock Market Today (July 2, 2026): Dow closes at all-time high](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-2-2026)
- Bloomberg — [Stock Market Today: Dow, S&P Live Updates for July 6](https://www.bloomberg.com/news/articles/2026-07-05/stock-market-today-dow-s-p-live-updates)
- Kiplinger — [Economic calendar July 6–10: FOMC minutes Wednesday](https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar)
- Yahoo Finance — [June jobs report: payrolls +57,000, missing expectations](https://finance.yahoo.com/economy/article/june-jobs-report-us-payrolls-rose-by-57000-missing-expectations-190000748.html); [Stock market today (July 2)](https://finance.yahoo.com/markets/live/stock-market-today-thursday-july-2-223136955.html)
- CME Group — [Crude Oil Futures Quotes](https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.quotes.html)

*Los datos marcados con (†) —primas de opciones, precio del futuro de oro de agosto, nivel exacto de QQQ y márgenes— son estimaciones razonables documentadas en la sección 3 (Metodología), al no estar disponible públicamente la cadena de opciones histórica intradía. Todos los demás niveles de mercado son datos reales de las fuentes citadas.*
