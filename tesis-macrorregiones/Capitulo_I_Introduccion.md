# CAPÍTULO I: INTRODUCCIÓN

**Tesis:** "El efecto de las macrorregiones sobre los ingresos laborales en el Perú: evidencia de la ENAHO, 2021-2023"
**Autor:** Anderson Riquelme Fretel Rojas
**Docente:** Oscar Chavez Polo
Universidad Nacional Mayor de San Marcos — Facultad de Ciencias Económicas

---

## Nota previa: verificación de consistencia entre la matriz, las apreciaciones del asesor y el Capítulo II

Antes de redactar este capítulo se contrastaron la matriz de consistencia, las apreciaciones del asesor y el Capítulo II ya elaborado. El problema general, los tres problemas específicos, el objetivo general y los tres objetivos específicos que aquí se presentan reproducen exactamente, en variables y sentido, los de la matriz de consistencia. Se detectaron, sin embargo, tres tensiones que convendrá corregir en la próxima revisión del Capítulo II: (i) dicho capítulo emplea en varios pasajes lenguaje causal fuerte ("relación causal", "efecto neto", "efecto territorial genuino"), que contradice la observación del asesor sobre la imposibilidad de interpretar los coeficientes macrorregionales como efectos causales estrictos; el presente Capítulo I adopta desde el planteamiento el lenguaje de brechas salariales condicionadas, de modo que esas expresiones deberán moderarse en la siguiente versión del Capítulo II; (ii) tanto la matriz como el Capítulo II operacionalizan la informalidad laboral únicamente mediante la afiliación a seguro de salud y pensiones (P511A), definición que el asesor pidió precisar y que este capítulo ya anticipa conforme a los criterios del INEI; y (iii) la ecuación presentada en la síntesis del Capítulo II omite las variables dummy temporales que la matriz sí contempla en el método de análisis, detalle que deberá homogeneizarse al redactar el Capítulo III. Ninguna de estas tensiones afecta la correspondencia entre problemas, objetivos e hipótesis, que es exacta.

---

## 1.1 Planteamiento del Problema

### 1.1.1 Identificación del problema

**Antecedentes o contexto**

La desigualdad territorial de ingresos constituye uno de los rasgos más persistentes de la economía peruana. La reconstrucción histórica de Seminario et al. (2019) muestra que la distribución del ingreso entre los departamentos del país es bimodal y notablemente estable: la probabilidad de que un departamento pobre en 1795 continuara siéndolo en 2017 alcanza el 94%, y la desigualdad entre regiones aumentó incluso durante el auge económico de 2000-2017 según los índices de Gini, Theil y Williamson. En la misma dirección, Castillo (2020) documenta con datos de la ENAHO que, si bien la mayor parte de la desigualdad agregada del ingreso se explica por diferencias al interior de las regiones, el componente entre regiones gana relevancia hacia el final del período 2007-2017, justamente cuando la reducción de la desigualdad nacional se desacelera.

La evidencia internacional apunta en el mismo sentido. La Organización Internacional del Trabajo (OIT, 2023) estima, con encuestas de hogares de 58 países, que los trabajadores rurales perciben en promedio 24% menos que sus pares urbanos, y que solo la mitad de esa brecha se explica por diferencias observables en educación, experiencia y ocupación; el resto constituye un componente asociado a la localización que las características individuales no absorben. Storper et al. (2024) documentan, para economías desarrolladas, que desde 1980 las disparidades interregionales han tendido a ampliarse en favor de un grupo reducido de metrópolis con fuertes economías de aglomeración. Para América Latina, Messina y Silva (2021) constatan que, pese a la reducción general de la desigualdad salarial entre 2002 y 2019, las disparidades territoriales son el componente más persistente y resistente a las políticas redistributivas, con la informalidad laboral como su principal canal de reproducción.

Estos antecedentes —que el Capítulo II desarrolla en detalle— delimitan el punto de partida de la presente investigación: las brechas territoriales de ingreso en el Perú no son fluctuaciones coyunturales, sino estructuras persistentes, y una parte de ellas no se explica por los atributos observables de los trabajadores. Lo que la literatura nacional todavía no ofrece es una estimación reciente, con microdatos de panel, del diferencial de ingresos de cada macrorregión respecto de Lima Metropolitana y Callao para el período posterior a la pandemia. Conviene precisar desde el inicio el alcance del término "efecto" que figura en el título y en la matriz de consistencia: dado que la residencia en una macrorregión no se asigna aleatoriamente —está asociada a la estructura productiva local, al costo de vida, al grado de urbanización, a decisiones de migración y a características no observadas del trabajador—, lo que el modelo propuesto puede identificar son brechas salariales condicionadas, es decir, diferenciales de ingreso ajustados por las características observables incluidas en la especificación, y no un efecto causal en sentido estricto. Esta limitación de identificación acompaña la lectura de todos los resultados de la tesis.

**Manifestación o indicio del problema**

La magnitud actual de la brecha es verificable con las estadísticas oficiales más recientes. En 2023, el ingreso promedio mensual proveniente del trabajo en Lima Metropolitana se situó en S/ 1 909.8 (Instituto Nacional de Estadística e Informática [INEI], 2024a), mientras que a nivel nacional dicho ingreso fue de S/ 1 607.8 en el año móvil julio 2022-junio 2023, con una brecha pronunciada entre el área urbana (S/ 1 757.8) y la rural (S/ 862.9) (INEI, 2023). Es decir, un trabajador del ámbito rural —concentrado principalmente en las macrorregiones Sur y Oriente— percibe, en promedio, menos de la mitad del ingreso de un trabajador limeño. Esta disparidad de ingresos coexiste con una distribución igualmente desigual de la calidad del empleo: la informalidad laboral alcanzó al 71.1% de la población ocupada en 2023, pero con enorme heterogeneidad territorial, pues afecta al 94.1% de los ocupados rurales frente al 65.6% de los urbanos (INEI, 2024a). A ello se suma que la pobreza monetaria llegó en 2023 al 29.0% de la población nacional y al 39.8% en el área rural (INEI, 2024b).

Frente a esta situación observada, el referente normativo es explícito: la Ley de Bases de la Descentralización (Ley N.° 27783, 2002) establece como finalidad del proceso descentralizador el desarrollo integral, armónico y sostenible del país, lo que supone una trayectoria de convergencia de ingresos entre territorios; y, en términos teóricos, en un mercado laboral espacialmente integrado los trabajadores de productividad comparable deberían percibir remuneraciones similares con independencia de su lugar de residencia. La evidencia disponible sugiere lo contrario: brechas amplias, un componente territorial no explicado por atributos individuales (OIT, 2023) y una historia de divergencia antes que de convergencia (Seminario et al., 2019). Adicionalmente, el período de estudio estuvo marcado por un episodio inflacionario relevante: el índice de precios al consumidor de Lima Metropolitana acumuló cerca de 19% entre diciembre de 2020 y diciembre de 2023 (6.4% en 2021, 8.5% en 2022 —la tasa más alta en más de un cuarto de siglo— y 3.2% en 2023) (Banco Central de Reserva del Perú [BCRP], 2024), lo que obliga a analizar los ingresos laborales en términos reales, pues las comparaciones en soles corrientes confundirían recuperación nominal con mejora efectiva del poder adquisitivo.

**Causas del problema**

La literatura permite ordenar las causas de la brecha macrorregional en cinco mecanismos. Primero, la heterogeneidad de la estructura productiva regional: mientras Lima Metropolitana y, en menor medida, la macrorregión Norte concentran servicios y manufactura, en las macrorregiones Sur y Oriente predominan actividades agrícolas y extractivas de baja productividad media, que fijan techos salariales bajos con independencia de las características del trabajador. Segundo, las economías de aglomeración: Lima Metropolitana y Callao concentran una fracción cercana a la mitad del producto nacional (INEI, 2022) y, conforme a la Nueva Geografía Económica (Krugman, 1991), esa concentración genera externalidades —profundidad del mercado laboral, encadenamientos productivos, derrames de conocimiento— que elevan la productividad y los salarios del núcleo frente a la periferia. Tercero, la informalidad heterogénea: la probabilidad de empleo informal aumenta con el trabajo en microempresas, la juventud y la pobreza, y disminuye con la educación superior (Medina-Quispe et al., 2026), condiciones distribuidas de manera desigual entre macrorregiones. Cuarto, las diferencias de capital humano: la cobertura y la calidad educativas difieren marcadamente entre Lima y el resto del país, y los retornos a la escolaridad son heterogéneos según el entorno económico regional (Montenegro y Patrinos, 2014). Quinto, el aislamiento geográfico, particularmente severo en la macrorregión Oriente, cuyos altos costos de transporte y baja densidad económica limitan los encadenamientos con el núcleo productivo del país.

**Efectos del problema**

La persistencia de la brecha macrorregional de ingresos produce, al menos, cuatro consecuencias. En primer lugar, perpetúa la pobreza regional: los territorios con menores ingresos laborales coinciden con los de mayor incidencia de pobreza monetaria (INEI, 2024b), de modo que la brecha salarial se traduce en brechas de bienestar. En segundo lugar, alimenta la migración interna hacia Lima Metropolitana, reforzando el patrón de macrocefalia urbana mediante el mecanismo de causalidad circular acumulativa que describe la Nueva Geografía Económica: los trabajadores siguen a los salarios y las empresas siguen a los mercados. En tercer lugar, implica una pérdida de productividad agregada, pues la concentración espacial extrema coexiste con territorios cuyo potencial productivo permanece subutilizado por falta de conectividad, capital humano y empleo formal. Finalmente, configura una desigualdad de oportunidades: si dos trabajadores con la misma educación, experiencia, sexo y condición de formalidad perciben ingresos sistemáticamente distintos por residir en macrorregiones diferentes, el lugar de residencia opera como un determinante del bienestar ajeno al esfuerzo y a la productividad individual.

**Pronóstico**

De no mediar política pública informada, la evidencia histórica sugiere que la brecha no se corregirá sola: la probabilidad de persistencia de la posición relativa de los territorios peruanos es extremadamente alta (Seminario et al., 2019) y la experiencia internacional posterior a 1980 muestra divergencia, no convergencia, entre regiones núcleo y periféricas (Storper et al., 2024). El escenario pasivo es, entonces, la consolidación de un patrón centro-periferia con mayor presión migratoria sobre Lima, congestión urbana creciente e informalidad persistente en los territorios expulsores. En contraste, disponer de estimaciones actualizadas y desagregadas de la brecha salarial condicionada de cada macrorregión —y de su evolución entre 2021 y 2023— permitiría orientar políticas de descentralización productiva, formalización laboral e inversión en conectividad hacia los territorios donde el diferencial no explicado por capital humano es mayor, y evaluar en el tiempo si dichas brechas se cierran o se amplían.

**Límites del estudio**

El estudio se acota con precisión en tres dimensiones. En el tiempo, abarca el período 2021-2023, correspondiente a la recuperación posterior a la crisis de la COVID-19; los resultados describen ese trienio y no son extrapolables a otros períodos. En el espacio, comprende el Perú organizado en las cinco macrorregiones definidas en la matriz de consistencia —Lima Metropolitana y Callao (categoría de referencia), Norte, Centro, Sur y Oriente—, construidas a partir de la variable DOMINIO/UBIGEO de la ENAHO. En el contenido, la variable explicada es el logaritmo del ingreso laboral mensual de la ocupación principal (I524A1) y las variables explicativas son la macrorregión de residencia y los controles de educación (P301A), experiencia potencial y su cuadrado, sexo (P207) e informalidad laboral; quedan fuera del alcance los ingresos de ocupaciones secundarias y no laborales, la calidad del empleo más allá de la formalidad, las habilidades no observadas y los diferenciales de costo de vida entre regiones, cuya omisión debe considerarse al interpretar las brechas estimadas.

Dentro de estos límites corresponde reconocer cuatro precisiones metodológicas. Primera, la muestra es un panel balanceado de la submuestra rotativa de la ENAHO (individuos observados en 2021, 2022 y 2023), diseño que favorece la comparabilidad intertemporal pero puede excluir a trabajadores más móviles, informales, jóvenes o con trayectorias laborales inestables, generando un posible sesgo de selección que limita la representatividad de los resultados frente al total de la PEA ocupada. Segunda, los ingresos se analizarán en términos reales, deflactados por el índice de precios al consumidor, dada la inflación acumulada del período; el tratamiento de los ingresos iguales a cero, los valores extremos y los datos perdidos se precisará en el capítulo metodológico. Tercera, la informalidad laboral se aproximará siguiendo los criterios del INEI —que combinan sector institucional, tamaño de empresa, registro tributario, tipo de ocupación y acceso a beneficios—, reconociendo que la sola afiliación a seguro de salud o pensiones mide protección social antes que informalidad en sentido estricto. Cuarta, dado que la macrorregión de residencia es prácticamente invariante en el tiempo para la mayoría de los individuos del panel, la elección del estimador (MCO agrupado o efectos aleatorios, en lugar de efectos fijos individuales) se justificará en el Capítulo III; asimismo, allí se discutirá el uso de los factores de expansión de la ENAHO y el alcance con que los resultados pueden considerarse representativos de la población ocupada nacional o solo de la submuestra de panel balanceado.

### 1.1.2 Formulación del problema

De acuerdo con la matriz de consistencia, y entendiendo el término "efecto" en el sentido de brecha salarial condicionada —diferencial de ingresos ajustado por características observables respecto de la categoría de referencia—, el problema se formula en las siguientes preguntas.

**Problema general**

¿Cuál es el efecto de la macrorregión de residencia sobre los ingresos laborales mensuales de los trabajadores en el Perú durante el período 2021-2023, controlando educación, experiencia laboral, sexo e informalidad laboral?

**Problemas específicos**

- **PE1:** ¿Cuál es la magnitud de la brecha salarial entre los trabajadores residentes en Lima Metropolitana y Callao y los residentes en las macrorregiones Norte, Centro, Sur y Oriente en el Perú durante el período 2021-2023?
- **PE2:** ¿Cuál es el efecto de las variables de capital humano (educación y experiencia) y las características sociodemográficas y laborales (sexo e informalidad) sobre los ingresos laborales en el Perú durante el período 2021-2023?
- **PE3:** ¿La desventaja salarial de las macrorregiones periféricas respecto a Lima Metropolitana y Callao persiste durante el período 2021-2023 o muestra una tendencia hacia la convergencia de ingresos laborales entre regiones?

En las tres preguntas la variable dependiente es el ingreso laboral mensual del trabajador; la variable independiente central es la macrorregión de residencia (PE1 y PE3), y las variables de capital humano y características laborales —educación, experiencia, sexo e informalidad— actúan como variables explicativas de interés en la PE2 y como controles en las demás. Debe subrayarse, conforme a la observación del asesor, que la desventaja salarial a la que aluden las preguntas es relativa a Lima Metropolitana y Callao como categoría base, y no una característica negativa intrínseca de las macrorregiones Norte, Centro, Sur u Oriente.

## 1.2 Justificación del estudio

**Justificación teórica**

La investigación se justifica teóricamente porque somete a contraste empírico, en la realidad peruana posterior a la pandemia, las tres teorías que el Capítulo II desarrolla como marco explicativo de la relación entre territorio e ingresos. De la Teoría del Capital Humano (Schultz, 1961; Becker, 1964; Mincer, 1974) evalúa si los retornos a la educación y a la experiencia mantienen el signo y la magnitud que la evidencia internacional documenta —en torno al 9.3% por año adicional de escolaridad para América Latina (Montenegro y Patrinos, 2014)—; de la Nueva Geografía Económica (Krugman, 1991) examina si, una vez controlado el capital humano, subsisten diferenciales sistemáticos de ingreso entre el núcleo limeño-chalaco y las macrorregiones periféricas, como predice el modelo centro-periferia; y de la Teoría de los Mercados Laborales Duales (Piore, 1971) verifica si la informalidad conlleva una penalidad salarial significativa en un mercado donde alcanza a siete de cada diez ocupados. El aporte metodológico frente a los estudios nacionales previos es concreto: Castillo (2020) y Seminario et al. (2019) midieron la desigualdad regional con indicadores agregados (Gini, Theil, Williamson) y con datos que llegan hasta 2017, mientras que esta tesis estima directamente, mediante una ecuación de Mincer ampliada sobre un panel balanceado de microdatos de la ENAHO 2021-2023, la brecha salarial condicionada de cada macrorregión respecto de Lima Metropolitana y Callao y su evolución anual, lo que permite separar el componente territorial del componente de composición individual que los índices agregados confunden.

**Justificación práctica**

Los resultados serán de utilidad directa para los formuladores de política vinculados al empleo y al desarrollo territorial. Al Ministerio de Trabajo y Promoción del Empleo le proporcionan una medida de la penalidad salarial asociada a la informalidad y de su distribución territorial, insumo para focalizar las estrategias de formalización laboral en las macrorregiones donde el empleo informal es más prevalente. A los gobiernos regionales y a las entidades rectoras de la descentralización y la planificación (Presidencia del Consejo de Ministros, CEPLAN) les ofrecen una cuantificación actualizada de la brecha de ingresos de sus territorios respecto de Lima, ajustada por capital humano, útil para priorizar inversión productiva, conectividad y cierre de brechas de servicios allí donde el diferencial no se explica por la composición de la fuerza laboral. La estimación de la dinámica 2021-2023 permite, además, monitorear si la recuperación pospandemia redujo o amplió las disparidades territoriales. Finalmente, para los investigadores del mercado laboral peruano, la tesis aporta una línea de base replicable —definiciones, especificación y estrategia de estimación documentadas sobre datos públicos de la ENAHO— que puede extenderse a períodos posteriores o refinarse con estrategias de identificación más exigentes.

## 1.3 Objetivos de la Investigación

**Objetivo general**

Determinar el efecto de las macrorregiones sobre los ingresos laborales en el Perú durante el período 2021-2023, utilizando datos de la ENAHO y controlando características individuales del trabajador (educación, experiencia, sexo e informalidad laboral).

**Objetivos específicos**

- **OE1:** Estimar la magnitud de la brecha de ingresos laborales entre las macrorregiones Norte, Centro, Sur y Oriente respecto a Lima Metropolitana y Callao durante el período 2021-2023, mediante la estimación de coeficientes de variables dummy macrorregionales.
- **OE2:** Analizar el efecto de las variables de capital humano (educación y experiencia) y las características laborales (sexo e informalidad) sobre los ingresos laborales en el Perú durante 2021-2023, evaluando la magnitud y significancia estadística de sus coeficientes estimados.
- **OE3:** Evaluar la evolución temporal de las brechas de ingresos laborales entre macrorregiones durante el período 2021-2023, identificando si las disparidades salariales muestran una tendencia hacia la convergencia o persistencia en el tiempo.

## Referencias

Banco Central de Reserva del Perú. (2024). *Memoria 2023*. https://www.bcrp.gob.pe/publicaciones/memoria-anual.html

Becker, G. S. (1964). *Human capital: A theoretical and empirical analysis, with special reference to education*. Columbia University Press / National Bureau of Economic Research.

Castillo, L. E. (2020). *Dinámica regional de la desigualdad de ingresos en Perú* (Documento de Trabajo N.° 004-2020). Banco Central de Reserva del Perú. https://www.bcrp.gob.pe/docs/Publicaciones/Documentos-de-Trabajo/2020/documento-de-trabajo-004-2020-esp.pdf

Instituto Nacional de Estadística e Informática. (2022). *Producto bruto interno por departamentos 2021*. https://www.inei.gob.pe/biblioteca-virtual/boletines/pbi-departamental/

Instituto Nacional de Estadística e Informática. (2023). *Comportamiento de los indicadores del mercado laboral a nivel nacional* (Informe técnico de empleo, trimestre abril-mayo-junio 2023). https://www.inei.gob.pe/biblioteca-virtual/boletines/informe-de-empleo/

Instituto Nacional de Estadística e Informática. (2024a). *Comportamiento de los indicadores del mercado laboral a nivel nacional y en 27 ciudades, año 2023* (Informe técnico de empleo). https://www.inei.gob.pe/biblioteca-virtual/boletines/informe-de-empleo/

Instituto Nacional de Estadística e Informática. (2024b). *Perú: Evolución de la pobreza monetaria 2014-2023* (Informe técnico). https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/pobreza2023/

Krugman, P. (1991). Increasing returns and economic geography. *Journal of Political Economy, 99*(3), 483-499. https://doi.org/10.1086/261763

Ley N.° 27783, Ley de Bases de la Descentralización. (2002, 20 de julio). Congreso de la República del Perú. Diario Oficial El Peruano.

Medina-Quispe, F., et al. (2026). Socioeconomic determinants of informal employment in Peru: An analysis for the period 2020-2022. *Economía & Negocios*. https://doi.org/10.33326/27086062.2026.1.2039

Messina, J., & Silva, J. (2021). *Twenty years of wage inequality in Latin America* (Policy Brief N.° IDB-PB-343). Banco Interamericano de Desarrollo.

Mincer, J. (1974). *Schooling, experience, and earnings*. Columbia University Press / National Bureau of Economic Research.

Montenegro, C. E., & Patrinos, H. A. (2014). *Comparable estimates of returns to schooling around the world* (Policy Research Working Paper N.° 7020). Banco Mundial.

Organización Internacional del Trabajo. (2023). *Employment and wage disparities between rural and urban areas* (Working Paper N.° 107). Oficina Internacional del Trabajo.

Piore, M. J. (1971). The dual labor market: Theory and implications. En D. M. Gordon (Ed.), *Problems in political economy: An urban perspective* (pp. 90-94). Lexington Books.

Schultz, T. W. (1961). Investment in human capital. *American Economic Review, 51*(1), 1-17.

Seminario, B., Zegarra, M. A., & Palomino, L. (2019). *Estimación del PBI departamental y análisis de la desigualdad regional en el Perú: 1795-2017* (Documento de Trabajo N.° 1016). Banco Interamericano de Desarrollo.

Storper, M., et al. (2024). Nature, causes, and consequences of inter-regional inequality. *Journal of Economic Geography, 24*(3), 353-389. https://doi.org/10.1093/jeg/lbae022
