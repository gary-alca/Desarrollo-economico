# 4. Diseño de evaluación

> **Nota metodológica.** Fortalecimiento de competencias en Excel e Inteligencia Artificial para la empleabilidad en el marco de Beca 18.

## 4.1 Preguntas de investigación e hipótesis

La evaluación de impacto busca responder a la siguiente pregunta general de investigación: ¿la participación voluntaria de becarios de Beca 18 en el último año de su carrera en un programa de formación en Excel avanzado y manejo aplicado de Inteligencia Artificial (IA) incrementa la calidad de su inserción en el mercado laboral durante el primer año posterior al egreso?

A diferencia de un experimento aleatorizado, en el que la asignación al tratamiento garantiza por construcción la equivalencia entre grupos, en esta intervención los becarios deciden inscribirse libremente. La estrategia de identificación descansa, por tanto, en la construcción de un contrafactual creíble por medios estadísticos: el resultado laboral que habrían obtenido los becarios capacitados de no haber llevado el curso. Dado que dicho contrafactual no es observable a nivel individual, se aproxima mediante un grupo de comparación conformado por becarios con características observables equivalentes que no participaron del programa, bajo el supuesto de selección sobre observables (Rosenbaum y Rubin, 1983; Heckman, Ichimura y Todd, 1997; Caliendo y Kopeinig, 2008). La justificación de este enfoque frente al diseño experimental se desarrolla en la sección 4.2.

De la pregunta general se derivan cuatro hipótesis específicas, que serán contrastadas empíricamente. Las tres primeras corresponden a los resultados finales de calidad del empleo y la cuarta a un mecanismo intermedio de productividad:

- **H1 (resultado principal):** Los becarios que participan del programa presentan una tasa de inserción laboral formal —empleo con contrato y derechos registrado en la planilla electrónica— significativamente mayor que la del grupo de comparación, medida a los 6 y 12 meses del egreso.
- **H2:** Los becarios que participan del programa perciben un ingreso laboral mensual bruto inicial significativamente mayor que el del grupo de comparación, asociado al acceso a puestos de mayor calificación (por ejemplo, analista) que demandan competencias digitales.
- **H3:** Los becarios que participan del programa registran una menor velocidad de inserción, esto es, un número significativamente menor de meses transcurridos entre el egreso y el primer empleo profesional calificado.
- **H4 (mecanismo):** Los becarios capacitados reportan un uso más intensivo de herramientas digitales y de IA generativa en sus tareas laborales y un mayor ahorro de tiempo operativo, lo que constituye el canal de productividad que vincula la formación con la mejora en la calidad del empleo.

Para limitar el riesgo de hallazgos espurios derivados de la prueba de múltiples hipótesis, se designa *ex ante* H1 (inserción laboral formal) como resultado primario, único sobre el cual se sustentará la conclusión principal de eficacia, y se clasifican H2, H3 y H4 como resultados secundarios. Las pruebas sobre familias de resultados secundarios y los análisis de heterogeneidad incorporarán correcciones por comparaciones múltiples (por ejemplo, el control de la tasa de error por familia mediante el procedimiento de Romano y Wolf). Esta jerarquización se fijará en un plan de análisis preregistrado, descrito en la sección 4.5.

### Variables de la evaluación

| Tipo | Variables |
| --- | --- |
| **Variables resultado (finales)** | Inserción laboral formal (binaria); ingreso laboral mensual bruto inicial (soles); velocidad de inserción (meses hasta el primer empleo calificado). |
| **Variables intermedias (mecanismo)** | Uso de IA generativa en tareas diarias; horas semanales ahorradas por automatización; aplicación de prueba técnica de Excel/IA en la entrevista de selección. |
| **Variables de control (emparejamiento)** | Carrera y área de conocimiento; institución de educación superior; edad; sexo; región de origen; promedio ponderado histórico; orden de mérito; modalidad de Beca 18; ciclo de egreso. |

*Nota.* Elaboración propia.

## 4.2 Estrategia y diseño de evaluación

### a. Justificación del diseño cuasi-experimental

A diferencia de evaluaciones de programas de capacitación con vacantes limitadas —en las que la sobredemanda permite asignar el acceso por sorteo y sustentar un diseño experimental puro, como en el caso de Jóvenes Productivos—, en el marco de Beca 18 no resulta ética ni administrativamente admisible negar por sorteo una formación complementaria a estudiantes que ya son beneficiarios de una beca del Estado. Privar aleatoriamente a un subconjunto de becarios de un curso voluntario contravendría los principios de equidad de acceso que rigen al Programa Nacional de Becas y Crédito Educativo (Pronabec). Por ello, la metodología idónea es un **diseño cuasi-experimental de emparejamiento por puntaje de propensión (Propensity Score Matching, PSM)**.

El procedimiento opera de la siguiente manera: los becarios se inscriben de forma libre y voluntaria al programa. Al finalizar la intervención, y para cada becario tratado, se busca en las bases de datos administrativas de Pronabec un "gemelo estadístico" —un becario con la misma área de carrera, institución de educación superior comparable, edad y rendimiento académico equivalentes— que **no** haya llevado el curso, y que servirá como unidad de comparación. Formalmente, se estima la probabilidad condicional de participar en el programa, o puntaje de propensión `e(X) = Pr(D = 1 | X)`, mediante un modelo logístico sobre el vector de covariables observables `X`, y se emparejan tratados y no tratados con puntajes próximos (Rosenbaum y Rubin, 1983).

El parámetro de interés es el efecto promedio del tratamiento sobre los tratados (ATT, por sus siglas en inglés):

```
ATT = E[ Y(1) − Y(0) | D = 1 ] = E_{e(X)|D=1} { E[Y | D = 1, e(X)] − E[Y | D = 0, e(X)] }
```

donde `Y(1)` e `Y(0)` denotan los resultados laborales potenciales con y sin participación, y `D` indica la participación efectiva. La identificación descansa en dos supuestos: (i) **independencia condicional** o ausencia de confusores no observados relevantes una vez controlado `X` (Rosenbaum y Rubin, 1983; Heckman et al., 1998); y (ii) **soporte común**, que garantiza la existencia de unidades de comparación con puntajes comparables para cada tratado. El cumplimiento del soporte común se verificará gráfica y numéricamente, restringiendo el análisis a la región de traslape de las distribuciones del puntaje de propensión (Caliendo y Kopeinig, 2008).

### b. Procedimiento de emparejamiento y estratificación

El emparejamiento se realizará de forma **estratificada por áreas de carrera** (por ejemplo, salud con salud, ingeniería con ingeniería, ciencias sociales con ciencias sociales), de modo que cada becario tratado se compare únicamente con potenciales controles de su mismo campo de conocimiento. Esta estratificación responde a una doble finalidad: por un lado, reconoce que la estructura de oportunidades laborales y los niveles salariales difieren sustancialmente entre profesiones; por el otro, permite sostener que las competencias en Excel e IA son transversales y optimizan la productividad —gestión de tiempos, organización de información y automatización de procesos— en cualquier campo profesional, y no solo en aquellos tradicionalmente asociados al análisis cuantitativo.

Como algoritmo principal se empleará el emparejamiento por vecino más cercano dentro de un radio (*caliper*) de 0,2 desviaciones estándar del puntaje de propensión, con reposición y estimación de errores estándar robustos. Como verificación de robustez se replicará el análisis con emparejamiento por kernel y con ponderación por el inverso de la probabilidad (IPW). La calidad del emparejamiento se evaluará mediante pruebas de balance de covariables: se exigirá que el sesgo estandarizado de cada covariable se reduzca por debajo del 5 % y que no persistan diferencias significativas entre grupos tras el emparejamiento (Rosenbaum y Rubin, 1985; Caliendo y Kopeinig, 2008).

### c. Resultados, indicadores y fuentes de datos

Siguiendo la rigurosidad de las evaluaciones de programas de capacitación laboral juvenil en el Perú (por ejemplo, PROJoven), el éxito del programa no se mide con un indicador binario de "trabaja o no trabaja", sino con **indicadores de calidad del empleo** evaluados a los **6 y 12 meses posteriores al egreso**. Para medirlos se combinan dos tipos de fuentes: registros administrativos y una encuesta de seguimiento tipo panel. Los registros tienen la ventaja de ser de bajo costo, de cobertura censal y de no depender de lo que el encuestado declare; la encuesta permite capturar variables de productividad que no quedan registradas en ninguna base administrativa.

**Tabla 1. Indicadores, definición y fuentes de datos**

| Nivel | Indicador | Definición operativa | Fuente |
| --- | --- | --- | --- |
| Resultado principal (H1) | Tasa de inserción laboral formal | Probabilidad de registrar empleo con contrato y derechos en la planilla electrónica | Planilla Electrónica (MTPE) / SUNAT, cruce anonimizado por DNI; a los 6 y 12 meses |
| Resultado secundario (H2) | Ingreso laboral mensual | Remuneración bruta mensual inicial (soles) | Planilla Electrónica (MTPE) / SUNAT; a los 6 y 12 meses |
| Resultado secundario (H3) | Velocidad de inserción | Número de meses entre el egreso y el primer empleo profesional calificado | Planilla Electrónica (MTPE) y encuesta de seguimiento |
| Mecanismo (H4) | Uso de IA y ahorro de tiempo | Uso de IA generativa para automatizar tareas; horas semanales ahorradas; prueba técnica de Excel/IA en la entrevista | Encuesta de seguimiento (panel); a los 6 y 12 meses |

*Nota.* Elaboración propia. El acceso a registros administrativos se realizará mediante convenios de intercambio de datos anonimizados, con resguardo de la confidencialidad descrito en la sección 4.5.

La **estrategia mixta de fuentes** se articula así:

- **Registros administrativos.** Se propone el cruce de datos anonimizados por DNI con la **Planilla Electrónica del MTPE** y los registros de la **SUNAT**, a fin de obtener información objetiva y sin sesgo de declaración sobre formalidad, salario y permanencia en el empleo. Este es el insumo principal del resultado primario (H1).
- **Encuesta de seguimiento telefónica o virtual (tipo panel).** Aplicada a tratados y controles en idénticas ventanas de tiempo, busca medir lo que el registro administrativo no observa. El valor agregado del instrumento radica en preguntas como: ¿le tomaron una prueba técnica de Excel o IA en la entrevista de selección?, ¿utiliza IA generativa para automatizar tareas diarias?, ¿cuántas horas a la semana ahorra en su puesto gracias a estas herramientas? Estas preguntas permiten documentar el mecanismo de productividad subyacente (H4).

### d. Especificación econométrica

Sobre la muestra emparejada, el efecto del programa se estimará mediante una regresión que controla por el conjunto de covariables de emparejamiento, lo que combina las virtudes del PSM con las de la regresión y confiere robustez frente a especificaciones incorrectas (estimador *doblemente robusto*; Imbens y Wooldridge, 2009):

```
Y_i = α + β · D_i + X_i' δ + μ_a + ε_i
```

donde `Y_i` es el resultado laboral del becario `i` (por ejemplo, inserción formal o ingreso); `D_i` vale 1 si el becario participó del programa y 0 si pertenece al grupo de comparación; `X_i` es el vector de covariables observables empleadas en el emparejamiento (promedio ponderado, orden de mérito, edad, sexo, institución, entre otras); `μ_a` son efectos fijos por área de carrera, que absorben las diferencias estructurales de empleabilidad entre campos profesionales; y `ε_i` es el término de error. El coeficiente de interés es `β`, que recoge el efecto causal promedio del programa sobre los participantes (ATT), bajo el supuesto de independencia condicional. Los errores estándar se estimarán de forma robusta y, en las especificaciones con emparejamiento, se ajustarán para reflejar que el puntaje de propensión es estimado (Abadie e Imbens, 2016).

Para las variables continuas (ingreso, velocidad de inserción) se utilizará una especificación lineal, en tanto que para los resultados binarios (inserción formal) se reportarán tanto el modelo lineal de probabilidad como estimaciones logísticas, verificando la consistencia de los efectos marginales. En todos los casos se controlará por el valor de línea de base de las covariables predictivas, lo que reduce la varianza residual y mejora la precisión de los estimadores.

### e. Análisis de efectos heterogéneos

Además del efecto promedio, se examinará si el programa beneficia más a unos grupos que a otros. En particular, se estimará la heterogeneidad del impacto según área de carrera, sexo, región de origen y rendimiento académico previo. Esta exploración es relevante de política: permite identificar para qué perfiles de becarios la formación digital genera mayores retornos y, por tanto, orientar la focalización en una eventual fase de escalamiento.

## 4.3 Cálculo de poder y muestra propuesta

El tamaño de muestra se determina mediante un cálculo de poder para la detección del efecto del programa sobre el resultado primario (tasa de inserción laboral formal). El tamaño mínimo del efecto detectable (MDE) se relaciona con el tamaño de muestra, el nivel de significancia y la potencia según la formulación estándar de Bloom (1995). Dado que el PSM descarta del análisis a las unidades fuera del soporte común y que el emparejamiento con reposición reduce la muestra efectiva de comparación, se incorpora un factor de ajuste por pérdida de eficiencia respecto de un diseño con asignación equilibrada.

Como tasa base del resultado principal se adopta una probabilidad de inserción laboral formal en torno al 45 % para egresados jóvenes en su primer año, consistente con los niveles de informalidad laboral juvenil documentados para el Perú (INEI; MTPE). Se busca detectar un MDE de 10 puntos porcentuales —un incremento de la tasa de inserción formal de 45 % a 55 %—, con un nivel de significancia del 5 % (α = 0,05) y una potencia del 80 % (1 − β = 0,80).

**Tabla 2. Parámetros del cálculo de poder**

| Parámetro | Valor propuesto |
| --- | --- |
| Tasa base de inserción laboral formal | 45 % |
| Efecto mínimo detectable (MDE) | 10 puntos porcentuales |
| Nivel de significancia (α) | 0,05 |
| Potencia estadística (1 − β) | 0,80 |
| Razón de emparejamiento (control : tratado) | 1 : 1 |
| Ajuste por pérdida de eficiencia del PSM | ≈ 1,3 |
| Tamaño de muestra por grupo (analítico) | ≈ 390 |
| Tamaño de muestra total (tratados + comparación) | ≈ 780 |

*Nota.* Elaboración propia con base en Bloom (1995). Cifras orientativas sujetas a refinamiento por simulación.

El cálculo es sensible a la tasa base y a la calidad del emparejamiento. Una proporción mayor de unidades fuera del soporte común o un menor poder predictivo del modelo de propensión elevan la muestra requerida; en sentido contrario, la inclusión de covariables predictivas del resultado (en especial el rendimiento académico histórico) reduce la varianza residual y mejora el poder efectivo. Por ello se recomienda contemplar una sobremuestra de seguridad del 15 %–20 % frente a la deserción esperada en la encuesta de seguimiento, y refinar el cálculo mediante simulación una vez se disponga de estimaciones administrativas de las tasas de inserción y de la distribución del puntaje de propensión en la base de Pronabec.

## 4.4 Amenazas a la validez y estrategias de mitigación

El diseño cuasi-experimental enfrenta amenazas a la validez que es preciso anticipar y mitigar explícitamente, en particular ante las objeciones que un jurado evaluador podría plantear.

**Sesgo de selección por variables no observables (motivación).** La principal objeción es que el grupo que llevó el curso podría ser intrínsecamente más motivado por el solo hecho de inscribirse, de modo que parte del efecto estimado reflejaría esa motivación y no el programa. Esta amenaza se mitiga por dos vías. Primero, se incorporan al modelo de propensión variables *proxy* de la disciplina y la motivación académica —el **promedio ponderado histórico** y el **orden de mérito** del becario—, que permiten controlar estadísticamente el componente observable de la motivación. Segundo, se aplicará un **análisis de sensibilidad de Rosenbaum** (*Rosenbaum bounds*) para cuantificar cuán fuerte tendría que ser un confusor no observado para invalidar las conclusiones, lo que ofrece una medida transparente de la robustez de los hallazgos frente al sesgo de selección (Rosenbaum, 2002; DiPrete y Gangl, 2004).

**Efecto de contaminación (spillover).** Podría argumentarse que los participantes transmitirán los contenidos a sus pares por mensajería instantánea, contaminando al grupo de comparación. Frente a ello cabe precisar que el programa no evalúa el acceso a un archivo o a un texto, sino el **desarrollo de una competencia técnica auditable en vivo por las empresas** —diseño de macros, ingeniería de *prompts* avanzados y automatización de flujos de trabajo—, capacidad que no se adquiere reenviando un material, sino mediante práctica supervisada. Adicionalmente, se priorizará la conformación del grupo de comparación con becarios de instituciones distintas a las de los tratados, reduciendo la probabilidad de contacto directo, y se incluirá en la encuesta un ítem de verificación de exposición a contenidos del curso para descartar contaminación efectiva.

**Carreras que "no usan" Excel o IA.** Podría objetarse que estas herramientas son irrelevantes para ciertas profesiones. El emparejamiento estratificado por áreas de carrera responde a esta objeción: cada tratado se compara con un control de su mismo campo, de modo que el efecto se estima dentro de la profesión y no entre profesiones. La evidencia internacional respalda, además, que las competencias digitales se han vuelto transversales y elevan la productividad en cualquier ocupación (Banco Mundial; OCDE; Foro Económico Mundial).

**Deserción (attrition) y sesgo de medición.** La pérdida diferencial de seguimiento en la encuesta panel puede sesgar los estimadores si se correlaciona con los resultados. Se mitigará priorizando el resultado primario sobre fuentes administrativas (Planilla Electrónica), de cobertura censal y baja atrición, realizando pruebas de atrición diferencial y reportando cotas de Lee cuando corresponda. El sesgo de medición por autorreporte en las variables de mecanismo se atenúa con preguntas conductuales concretas y verificables (horas ahorradas, prueba técnica en la entrevista) y con la triangulación entre encuesta y registro administrativo.

**Efectos Hawthorne y John Henry.** El conocimiento de ser observado podría alterar la conducta de los tratados (Hawthorne) o estimular un esfuerzo compensatorio en el grupo de comparación (John Henry). Ambos se atenúan mediante la medición de resultados a partir de registros administrativos —no reactivos— y mediante una comunicación neutra del seguimiento, que no enfatice la condición de tratamiento o comparación de cada participante.

**Tabla 3. Principales amenazas a la validez y estrategias de mitigación**

| Amenaza | Estrategia de mitigación |
| --- | --- |
| Sesgo de selección por motivación (no observables) | Proxies de motivación (promedio ponderado, orden de mérito); análisis de sensibilidad de Rosenbaum |
| Contaminación (spillover) | Competencia técnica auditable; comparación entre instituciones distintas; ítem de verificación de exposición |
| Relevancia por carrera | Emparejamiento estratificado por área de carrera; efectos fijos por área |
| Deserción (attrition) | Resultado primario sobre registros administrativos; pruebas de atrición; cotas de Lee |
| Sesgo de medición | Preguntas conductuales verificables; triangulación encuesta–registro |
| Efectos Hawthorne y John Henry | Resultados no reactivos (administrativos); comunicación neutra del seguimiento |
| Soporte común insuficiente | Restricción a la región de traslape; verificación de balance de covariables |

*Nota.* Elaboración propia.

## 4.5 Consideraciones éticas, preregistro y datos

El diseño respeta los principios éticos básicos de la evaluación de impacto. A diferencia de un experimento, ningún becario es privado del curso por sorteo: el acceso es voluntario y abierto a todos los becarios elegibles, lo que preserva la equidad de acceso propia de Beca 18. La construcción del grupo de comparación se realiza *ex post* a partir de registros existentes, sin alterar las prestaciones a las que cada becario tiene derecho.

El estudio requerirá el **consentimiento informado** de los participantes en la encuesta de seguimiento y la aprobación de un comité de ética. El cruce de registros administrativos (Pronabec, Planilla Electrónica del MTPE, SUNAT) se efectuará bajo convenios de intercambio de datos con **anonimización** y seudonimización por DNI, en cumplimiento de la Ley de Protección de Datos Personales, de modo que el equipo evaluador no acceda a identidades nominales.

Con el fin de fortalecer la credibilidad de los resultados, se elaborará y depositará un **plan de análisis preregistrado** en un registro público, en el que se fijarán con anticipación el resultado primario (H1), las hipótesis secundarias, las dimensiones de heterogeneidad y las especificaciones econométricas, incluidos el algoritmo de emparejamiento y las pruebas de robustez. El preregistro reduce los grados de libertad del investigador y el riesgo de búsqueda selectiva de especificaciones, práctica recomendada para reforzar la transparencia y la replicabilidad de las evaluaciones de impacto (Casey, Glennerster y Miguel, 2012). En el marco de los principios de **Open Science**, el código de estimación y los datos anonimizados se depositarán en un repositorio público una vez concluida la evaluación.

Por último, junto a la estimación de impacto, la evaluación incorporará un análisis de **costo-efectividad** que compare el costo por inserción laboral formal adicional generada por el programa con el de intervenciones alternativas de empleabilidad, de modo que los resultados sean directamente útiles para la toma de decisiones de Pronabec y comparables con la evidencia internacional sobre programas activos del mercado laboral (Card, Kluve y Weber, 2018).

---

### Referencias citadas en esta sección

- Abadie, A. e Imbens, G. W. (2016). Matching on the estimated propensity score. *Econometrica*, 84(2), 781–807.
- Bloom, H. S. (1995). Minimum detectable effects: A simple way to report the statistical power of experimental designs. *Evaluation Review*, 19(5), 547–556.
- Caliendo, M. y Kopeinig, S. (2008). Some practical guidance for the implementation of propensity score matching. *Journal of Economic Surveys*, 22(1), 31–72.
- Card, D., Kluve, J. y Weber, A. (2018). What works? A meta-analysis of recent active labor market program evaluations. *Journal of the European Economic Association*, 16(3), 894–931.
- Casey, K., Glennerster, R. y Miguel, E. (2012). Reshaping institutions: Evidence on aid impacts using a preanalysis plan. *The Quarterly Journal of Economics*, 127(4), 1755–1812.
- DiPrete, T. A. y Gangl, M. (2004). Assessing bias in the estimation of causal effects: Rosenbaum bounds on matching estimators. *Sociological Methodology*, 34(1), 271–310.
- Heckman, J. J., Ichimura, H. y Todd, P. E. (1997). Matching as an econometric evaluation estimator: Evidence from evaluating a job training programme. *The Review of Economic Studies*, 64(4), 605–654.
- Heckman, J. J., Ichimura, H. y Todd, P. (1998). Matching as an econometric evaluation estimator. *The Review of Economic Studies*, 65(2), 261–294.
- Imbens, G. W. y Wooldridge, J. M. (2009). Recent developments in the econometrics of program evaluation. *Journal of Economic Literature*, 47(1), 5–86.
- Rosenbaum, P. R. (2002). *Observational Studies* (2.ª ed.). Springer.
- Rosenbaum, P. R. y Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70(1), 41–55.
- Rosenbaum, P. R. y Rubin, D. B. (1985). Constructing a control group using multivariate matched sampling methods that incorporate the propensity score. *The American Statistician*, 39(1), 33–38.
