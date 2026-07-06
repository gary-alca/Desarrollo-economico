# PROMPT MAESTRO — PROYECTO DE DERIVADOS FINANCIEROS (VERSIÓN MEJORADA)
### Portafolio de USD 1,000,000 en Futuros y Opciones · Horizonte 18 de junio – 9 de julio de 2026

---

## ROL QUE DEBES ASUMIR

Actúa como un **gestor profesional de portafolios, analista cuantitativo y especialista en derivados financieros (Futuros y Opciones)**, con amplia experiencia en mercados internacionales, gestión de riesgos, macroeconomía y elaboración de informes académicos de nivel universitario.

Quiero un trabajo **bien fundamentado**, con razonamiento financiero profundo, explicaciones claras y decisiones justificadas como si fuera elaborado por un gestor de inversiones profesional, pero redactado a un nivel apropiado para un estudiante universitario. No entregues una respuesta superficial ni un resumen apurado.

---

## CONTEXTO DEL PROYECTO

El profesor solicitó construir un **portafolio de USD 1,000,000** compuesto por instrumentos derivados: **futuros y opciones**.

El objetivo no es solo obtener rentabilidad, sino **demostrar dominio del uso de derivados, la administración del riesgo y la toma de decisiones fundamentadas**. El portafolio **NO es estático**: debe administrarse día a día conforme cambian las condiciones del mercado.

---

## ⏱️ CRONOGRAMA REAL DEL EJERCICIO (LEER CON ATENCIÓN — ESTA ES LA PARTE MÁS IMPORTANTE)

Este proyecto tiene un cronograma con **tres tramos** que NO se deben mezclar. Debes respetar exactamente qué instrumento se usa en cada tramo y con qué fuente de precios:

| Tramo | Fechas | Instrumentos permitidos | Fuente de precios | Naturaleza |
|-------|--------|-------------------------|-------------------|------------|
| **A. Análisis retrospectivo (hindsight)** | 18 jun – 24 jun 2026 | **SOLO FUTUROS** | Liquidaciones diarias reales (CME, ICE, NYMEX, COMEX) | Reconstrucción ilustrativa con datos ya conocidos |
| **B. Apertura de opciones** | **25 jun 2026** | **OPCIONES** (más futuros que sigan corriendo) | **Cadenas de opciones de las fotos adjuntas** (snapshot del 25 de junio) | Precio de entrada / prima pagada o cobrada |
| **C. Administración en tiempo real** | **2 jul – 9 jul 2026** | Opciones (valoración y cierre) + Futuros (se sigue operando) | **MarketWatch** (precios reales del 2 al 9 de julio) | Decisiones reales bajo incertidumbre |

**Reglas duras del cronograma:**

1. **Las opciones se "agarran" (se abren) el 25 de junio de 2026**, usando exclusivamente los precios/primas de las **fotos de cadenas de opciones** que se adjuntan (ese es el *snapshot* de entrada).
2. A partir del **2 de julio y hasta el 9 de julio**, la valoración, el seguimiento y el eventual cierre de esas opciones se hace con **precios reales de MarketWatch** para cada strike/vencimiento. Si un dato puntual no está en MarketWatch, decláralo explícitamente y usa una estimación razonable justificada (por ejemplo, interpolando por moneyness o usando la paridad put-call), nunca un número inventado.
3. **Los futuros se siguen operando durante todo el horizonte** (no se congelan el 25 de junio): su marca a mercado diaria continúa hasta el 9 de julio.
4. El tramo retrospectivo (A) usa **solo futuros** porque sus liquidaciones diarias históricas son verificables; las primas intradía de opciones de fechas pasadas no se pueden reconstruir de forma fiable, por eso las opciones **no** entran en el tramo A.

---

## 🧭 BITÁCORA DE ADMINISTRACIÓN DINÁMICA (18 jun → 9 jul): ABRIR / MANTENER / CERRAR

Esta es una exigencia central del trabajo. **No basta con construir el portafolio una vez.** Debes narrar y justificar, con formato de bitácora fechada, **qué se hizo con cada posición en cada momento relevante del horizonte**, respondiendo siempre:

- **¿Se ABRIÓ una posición nueva?** → activo, estrategia, fecha, precio/prima de entrada, por qué se abrió ese día y no antes.
- **¿Se MANTIENE la posición?** → por qué la tesis sigue vigente, qué indicadores lo confirman.
- **¿Se CERRÓ la posición?** → fecha y precio de cierre, resultado realizado (ganancia/pérdida), por qué se cerró (¿se alcanzó el objetivo de 50–60% del máximo?, ¿se rompió el soporte?, ¿cambió la tesis?).
- **¿Se REDUJO / AUMENTÓ / REEMPLAZÓ?** → cuánto, por qué, con qué nueva estructura.

Presenta esto como una **línea de tiempo de decisiones** (por ejemplo: 25 jun apertura → 2 jul revisión → 3 jul ajuste → … → 9 jul cierre/vencimiento), no como una foto única. Cada decisión debe estar anclada a un dato de mercado real de esa fecha.

> Regla de oro: **no mantengas una posición solo porque estaba en el plan original.** Si la tesis dejó de tener sentido, ciérrala o reemplázala y explica el motivo.

---

## 📸 ACTIVOS DE OPCIONES DISPONIBLES (CADENAS EN LAS FOTOS ADJUNTAS)

Se adjuntan cadenas de opciones (calls y puts, con LAST, CHG, BID, ASK, VOL, OPEN INT. por strike) para los siguientes subyacentes. **Úsalas como fuente de primas/entrada del 25 de junio** y luego valora con MarketWatch del 2 al 9 de julio:

- **AAPL (Apple)** — cadena con *current price* ~**275.15** (snapshot 25 jun 2026).
- **MSFT (Microsoft)** — cadena con *current price* ~**352.83** (snapshot 25 jun 2026).
- **NVDA (Nvidia)** — cadena adjunta.
- **DAL (Delta Air Lines)** — cadena adjunta, vencimiento julio.
- **SPY (S&P 500 ETF)** — cadena adjunta, con vencimientos julio y diciembre.

> Nota: si el *current price* que ves en una foto de julio (por ejemplo AAPL ~308, MSFT ~390) difiere del precio de entrada del 25 de junio, **eso es esperado**: la foto del 25 de junio marca la ENTRADA y la de julio/MarketWatch marca la VALORACIÓN. Deja explícito en el informe qué precio corresponde a qué fecha.

---

## ✅ IDEAS DE OPCIONES RECOMENDADAS (SEMILLA DEL PORTAFOLIO — VALIDAR Y AJUSTAR)

Parte de estas cuatro operaciones (ordenadas de mayor a menor confianza) como **base**. Debes **validarlas con los datos reales de las cadenas y de MarketWatch**, ajustar strikes/vencimientos si conviene, y justificar cada una con el marco completo de preguntas de este prompt. Si alguna deja de tener sentido con los precios reales, dilo y propón la alternativa.

**Idea 1 — DAL · Bull Put Spread (mayor confianza).** Vender put strike 90 (cobrar prima) y comprar put strike 85 (red de seguridad). Vencimiento 10 o 17 de julio. Tesis: reporta el viernes con volatilidad inflada → *IV crush* posterior abarata las opciones vendidas; petróleo a la baja por distensión EE.UU.–Irán (≈ −USD 300 M de costo de combustible); 22 de 24 analistas en "compra fuerte" y 4 sorpresas positivas seguidas; soporte técnico en ~92.7. Riesgo: BPA esperado cae ~32% interanual; si da mala guía y rompe soporte, pierdes, pero **la pérdida está topada** por el spread. Regla de salida: cerrar al 50–60% del máximo.

**Idea 2 — MSFT · Venta de Put cash-secured (o spread 370/360).** Vender put strike 370 con efectivo reservado para asignación; alternativa con red: spread 370/360. Vencimiento 17 de julio (ANTES de earnings de fin de mes). Tesis: MSFT es la más castigada de las grandes tecnológicas (−24%, mínimos desde 2023 por miedo al gasto en centros de datos de IA) → posible capitulación / suelo; señal: Michael Burry compró calls apostando a +700. Si no baja, te quedas la prima; si baja, compras una empresa sólida con descuento. Riesgo: "agarrar un cuchillo que cae"; usar solo capital dispuesto a comprar la acción, o el spread para topar la pérdida.

**Idea 3 — AAPL · Bull Call Spread.** Comprar call strike 310 y vender call strike 322.5. Vencimiento 17 o 24 de julio (evitando earnings). Tesis: AAPL a ~4% de ser la empresa más valiosa del mundo (superar a Nvidia) → titular que atrae compradores y fondos de tendencia; se elige spread y no call simple para que la call vendida compense el desgaste por *theta* en una semana sin catalizadores propios. Riesgo: subida ya muy estirada; pérdida topada a lo pagado. Salir si AAPL pierde los ~300.

**Idea 4 — SPY · Butterfly de calls (con alternativa defensiva).** Mariposa 745/755/765 en calls, vencimiento 10 de julio: cuesta poco y paga bien si el índice se "estaciona" cerca de 755. Tesis: semana de pocos datos (solo minutas de la Fed el miércoles), mercado que sube despacio → entorno ideal para una mariposa. **Alternativa defensiva** (si ya hay acciones): comprar una put de SPY como seguro, aprovechando el VIX bajo (<16) → protección barata. Riesgo del escenario: minutas de la Fed más duras de lo esperado.

**Idea 5 (SUGERIDA) — NVDA · sesgo bajista por sobrecapacidad de IA.** Incorpora una estrategia sobre NVDA que capture la **tesis bajista reciente**: la caída por la incursión de **Meta en la nube** hizo que el mercado interprete que hay **exceso de capacidad de IA no utilizada** (sobre-stock de GPUs), lo que **reduciría el consumo/compra de GPUs** y presionaría los ingresos de Nvidia. Evalúa y compara, con los datos de la cadena de NVDA:
- **Bear Call Spread** (vender call cercana, comprar call más arriba) → cobras prima con pérdida topada si NVDA rebota.
- **Compra de Put** o **Bear Put Spread** → si esperas caída más marcada y controlada en costo.
- Justifica cuál eliges según la volatilidad implícita (si la IV está cara, prioriza estructuras que *vendan* prima como el bear call spread; si está barata, la compra de put es más eficiente).

---

## ANTES DE CONSTRUIR EL PORTAFOLIO — ANÁLISIS DEL ENTORNO

Realiza un análisis completo del entorno financiero con información **real y actualizada** (busca si es necesario e indica fuentes). Incluye como mínimo: economía global, economía de EE.UU., política monetaria, inflación, tasas de interés, rendimientos de los bonos del Tesoro, situación de la Reserva Federal, fortaleza del dólar, mercados bursátiles, volatilidad (VIX), precio del petróleo, precio del oro, riesgos geopolíticos, eventos programados entre el 18 de junio y el 9 de julio, calendario económico y noticias relevantes. **No inventes información.**

---

## SELECCIÓN DE ACTIVOS

Usa instrumentos reales de mercados organizados (**CME, ICE, CBOE, NYMEX, COMEX** u otros reconocidos), sobre índices, acciones o materias primas.

- **Opciones:** AAPL, MSFT, NVDA, DAL, SPY (según las cadenas adjuntas).
- **Futuros:** ver la sección de futuros más abajo (oro, petróleo y al menos una sugerencia adicional tuya).

---

## 🥇 FUTUROS — QUÉ OPERAR Y CÓMO ESTRUCTURARLO

Para el bloque de futuros (tanto en el tramo retrospectivo 18–24 jun como en la operación en tiempo real hasta el 9 jul):

1. **Incluye obligatoriamente Oro (GC, COMEX) y Petróleo (CL, NYMEX WTI).**
2. **Sugiere y justifica al menos un futuro adicional** con potencial de rendimiento dado el contexto. Opciones a evaluar y comparar (elige y fundamenta):
   - **Gas natural (NG, NYMEX)** — alta volatilidad estacional.
   - **Plata (SI, COMEX)** — beta alto al oro, más volátil.
   - **Futuros de índice E-mini S&P 500 (ES, CME)** — exposición direccional al mercado.
   - **Bonos del Tesoro / Notas a 10 años (ZN, CBOT)** — para jugar el discurso de la Fed y las tasas.
   - **Granos (maíz ZC, trigo ZW, CBOT)** — sensibles a clima y geopolítica.
   - **EUR/USD (6E, CME)** — para operar la fortaleza/debilidad del dólar.
3. Para cada futuro define claramente: **posición (larga/corta), tesis macro, tamaño de contrato, número de contratos, valor nocional, margen inicial y de mantenimiento.**
4. Justifica la **dirección** con el contexto real (p. ej., oro como refugio ante riesgo geopolítico; petróleo a la baja por distensión EE.UU.–Irán; tasas según el tono de las minutas de la Fed).

---

## 📊 ENTREGABLES EN EXCEL (OBLIGATORIO) — DOS LIBROS/HOJAS CON ESTRUCTURA DEFINIDA

Además del informe, **genera archivos Excel operativos** con estas estructuras exactas:

### A) EXCEL DE OPCIONES — una tabla por estrategia (formato "Ejercicio 7")

Para **cada estrategia de opciones** replica el formato del Ejercicio 7. Encabezado de parámetros y tabla de payoff:

**Bloque de parámetros (arriba):**
`Estrategia | Tipo (long/short call/put, spread, butterfly…) | Contratos | Acciones por contrato (100) | Total de acciones | Prima por acción | Inversión/Crédito total | r | T (años) | Strike(s)`

**Tabla de resultados por precio spot al vencimiento (una fila por ST):**

| ST (Spot) | K | PRIMA | EJERCE (SI/NO) | MONEYNESS (ITM/ATM/OTM) | PAYOFF | G o P x acción | G o P total |
|----|---|-------|----------------|--------------------------|--------|----------------|-------------|

- Barre un rango de **ST** alrededor del strike (como en el Ejercicio 7).
- Para **spreads y butterfly**, combina las patas: incluye columnas por pata y una columna de **PAYOFF neto** y **G o P total neto** de la estructura completa.
- Marca **break-even, pérdida máxima y ganancia máxima** de cada estrategia.
- Incluye una fila/resumen con el resultado **real** según el precio de MarketWatch al cierre/vencimiento (2–9 jul).

### B) EXCEL DE FUTUROS — marca a mercado diaria (formato "futuro de trigo")

Para **cada futuro** replica el formato del ejercicio de trigo (mark-to-market con cuenta de margen):

**Bloque de parámetros (arriba):**
`Activo | Mercado | Posición (larga/corta) | N.º de contratos | Tamaño de contrato | Tamaño del portafolio (unidades) | Margen inicial (por contrato y total) | Margen de mantenimiento (por contrato y total) | Precio negociado de entrada`

**Tabla diaria (una fila por día del período):**

| Fecha | Día | Precio negociado | Precio de liquidación | G o P por unidad | G o P total diaria | G o P acumulada | Cuenta de Margen | Margin Call |
|-------|-----|------------------|-----------------------|------------------|--------------------|------------------|------------------|-------------|

- La **Cuenta de Margen** parte del margen inicial y se actualiza cada día con la G o P diaria.
- Cuando la cuenta caiga **por debajo del margen de mantenimiento**, dispara **Margin Call** y repón hasta el margen inicial (indícalo en la columna).
- El signo de la G o P depende de la posición (larga gana si sube; corta gana si baja).
- Usa **precios de liquidación reales** de cada día del período (declara la fuente).

> Puedes entregar los Excel como archivos `.xlsx` reales (con fórmulas) y/o como tablas Markdown que yo pueda pegar en Excel. Prioriza que las **fórmulas y los totales cuadren**.

---

## CONSTRUCCIÓN DEL PORTAFOLIO PRINCIPAL — DATOS POR POSICIÓN

Para cada posición (opciones y futuros) incluye: activo subyacente, tipo de derivado, estrategia, posición larga/corta, mercado, fecha de apertura, fecha de vencimiento, precio de entrada, strike (si aplica), prima pagada o recibida, cantidad de contratos, valor nocional y peso dentro del portafolio (objetivo total ≈ USD 1,000,000).

---

## ANÁLISIS RETROSPECTIVO (18 – 24 DE JUNIO) — SECCIÓN SEPARADA Y ETIQUETADA

Sección aparte, titulada **"Análisis Retrospectivo"**, con estas reglas:

- **Solo futuros** (no opciones), por la verificabilidad de las liquidaciones diarias (CME, ICE, NYMEX, COMEX).
- Puedes usar varias estrategias de futuros (p. ej., largo en un índice, corto en una materia prima, uno sobre tasas o el dólar), cada una justificada con el contexto macro **real de esas fechas**.
- Cada posición declara: activo, mercado, fecha de apertura y cierre, precio de entrada y salida reales, resultado obtenido, y el fundamento macro/financiero disponible **en esas fechas** (no con información posterior).
- **Nota metodológica obligatoria** al inicio y al final: es una **reconstrucción con datos ya conocidos (hindsight)**, con fines ilustrativos, que **no** representa decisiones tomadas en tiempo real. La condición de "tiempo real bajo incertidumbre" aplica solo al período del 2 al 9 de julio.
- No mezclar con el portafolio principal ni con la administración dinámica semanal.

---

## JUSTIFICACIÓN INDIVIDUAL DE CADA POSICIÓN (PORTAFOLIO PRINCIPAL)

Para **cada** posición responde con detalle: ¿Por qué este activo? ¿Por qué esta estrategia? ¿Qué esperas que ocurra? ¿Qué riesgo intentas aprovechar? ¿Qué escenario da ganancia? ¿Qué escenario da pérdida? ¿Pérdida máxima? ¿Ganancia potencial? ¿Qué eventos la favorecen? ¿Qué eventos la perjudican? ¿Por qué no otra estrategia? ¿Ventajas? ¿Desventajas?

---

## ANÁLISIS DEL PORTAFOLIO

Explica: nivel de riesgo, diversificación, exposición sectorial, exposición por tipo de activo, exposición direccional, coberturas existentes, relación riesgo-retorno y cómo interactúan las posiciones entre sí (por ejemplo, cómo la put de SPY cubre el sesgo alcista de AAPL, o cómo el corto en petróleo se relaciona con la tesis de DAL).

---

## TABLAS

Tablas profesionales, **separando siempre el portafolio principal (25 jun / 2–9 jul) del bloque retrospectivo (18–24 jun)**. Incluye:

`| Activo | Derivado | Estrategia | Posición | Precio | Strike | Prima | Contratos | Valor nocional | Peso |`

Y además: distribución por sectores, por activos, por estrategias y por nivel de riesgo.

---

## ESCENARIOS

Tres escenarios para el portafolio principal (18 jun – 9 jul): **optimista, base, pesimista**. Para cada uno: resultado por posición, resultado del portafolio, rentabilidad y explicación económica de por qué ocurrió.

---

## GESTIÓN DEL RIESGO

Analiza: riesgo de mercado, de volatilidad, de liquidez, por apalancamiento y de concentración; sensibilidad aproximada del portafolio; y explica **Delta, Gamma, Theta, Vega y Rho** de las estrategias con opciones de forma conceptual o aproximada (p. ej., por qué el bull put spread de DAL se beneficia del *IV crush* = Vega corta; por qué el bull call spread de AAPL sufre *theta* y por eso se usa spread).

---

## PLAN DE MONITOREO DIARIO (2 – 9 DE JULIO)

Checklist diario con: noticias económicas, calendario económico, Fed, inflación, empleo, PIB, PMI, bonos, VIX, S&P 500, Nasdaq, Dow Jones, petróleo, oro, dólar, volatilidad implícita, volumen y eventos geopolíticos. Explica **por qué** cada variable importa para las posiciones concretas del portafolio.

---

## REGLAS DE DECISIÓN (SI → ENTONCES)

Construye reglas accionables para cada posición. Ejemplos: si sube/baja la volatilidad; si el S&P 500 rompe resistencia/soporte; si el petróleo supera cierto nivel; si cae el oro; si el dólar se fortalece; si cambian los rendimientos de los bonos; si la Fed cambia el discurso; si la inflación o el empleo sorprenden; si ocurre un evento geopolítico. Para cada caso, di **exactamente qué harías** (abrir, mantener, reducir, aumentar, cerrar o reemplazar).

---

## ESTRATEGIAS ALTERNATIVAS

Si una hipótesis deja de cumplirse, propón alternativas usando solo las herramientas vistas en clase (Call, Put, Bull/Bear Call Spread, Bull/Bear Put Spread, Butterfly, Box, Straddle, Strangle, Strip, Strap, Futuros) y justifica el cambio.

---

## MI FORMA DE TRABAJAR CONTIGO

Durante la semana (2–9 jul) volveré a consultarte varias veces. Cada vez, actúa como gestor: reanaliza el mercado con información actualizada, compara con la hipótesis original y responde claramente **Mantener / Cerrar / Reducir / Aumentar / Reemplazar**, siempre con el porqué. No mantengas una posición solo porque estaba en el plan.

---

## ESTRUCTURA DEL INFORME FINAL

1. Introducción (con nota metodológica del cronograma: tiempo real 2–9 jul; retrospectivo con futuros 18–24 jun; apertura de opciones 25 jun)
2. Objetivos
3. Metodología
4. Contexto macroeconómico
5. Contexto financiero
6. Análisis Retrospectivo (18–24 jun, solo futuros, con nota de hindsight)
7. Justificación de los activos seleccionados (portafolio principal)
8. Construcción del portafolio (apertura 25 jun; administración 2–9 jul)
9. Justificación individual de cada posición
10. **Bitácora de administración dinámica (abrir/mantener/cerrar día a día)**
11. Estrategia general del portafolio
12. Gestión del riesgo (incluye griegas)
13. Escenarios (optimista/base/pesimista)
14. Plan de monitoreo diario
15. Reglas para modificar el portafolio
16. Estrategias alternativas
17. **Entregables Excel: (A) Opciones formato Ejercicio 7 · (B) Futuros formato marca a mercado con cuenta de margen**
18. Conclusiones
19. Referencias

---

## REGLAS IMPORTANTES (NO NEGOCIABLES)

- Usa información **real y actualizada**; si necesitas buscar, hazlo, e indica fuentes.
- **No inventes** precios, primas, volatilidades ni datos de mercado, ni en el portafolio principal ni en el retrospectivo. Si un dato no está disponible, dilo y usa una estimación razonable **explicando el supuesto** (interpolación por moneyness, paridad put-call, etc.).
- Respeta el cronograma: **opciones desde el 25 de junio con las fotos**, **valoración 2–9 de julio con MarketWatch**, **futuros operando en todo el horizonte**, **retrospectivo 18–24 jun solo con futuros**.
- Justifica **todas** las decisiones con fundamentos financieros, macro y de mercado, y explica el razonamiento paso a paso.
- Si hay varias estrategias viables, **compáralas** antes de elegir y explica por qué descartaste las demás.
- Prioriza la **gestión del riesgo** y la **calidad del análisis** por encima de maximizar la rentabilidad.
- Verifica que cada operación sea coherente con el horizonte, el capital (≈ USD 1,000,000) y el perfil del portafolio.
- Entrega los **dos Excel** con las estructuras indicadas y con los totales cuadrados.
