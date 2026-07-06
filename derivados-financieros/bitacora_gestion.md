# Bitácora de gestión dinámica del portafolio de derivados

**Complemento del `informe_portafolio_derivados.md` · Periodo: 2–9 de julio de 2026**

Protocolo de cada entrada: (1) datos nuevos → (2) contraste con la hipótesis de cada posición → (3) decisión: **Mantener / Cerrar / Reducir / Aumentar / Reemplazar** → (4) justificación.

---

## Jueves 2 de julio de 2026 — Apertura del portafolio

**Datos del día:** empleo de junio muy débil (+57k vs. 115k esperado; revisiones −74k); desempleo 4.2% por caída de participación a 61.5%. Reacción: Dow +1.14% a máximo histórico (52,900.07), S&P plano (7,483.24), Nasdaq −0.8% (25,832.67) con semiconductores cayendo; 10Y en 4.49%; DXY cae a 100.8; oro salta sobre $4,100; WTI ≈ $68.5, mínimo desde febrero; VIX 16.59.

**Acción:** apertura de las 5 posiciones al cierre (ver informe, sección 7). La sesión confirmó las tres asimetrías de la tesis: rotación Dow/tech, oro reactivado por dólar débil, crudo sin prima de riesgo.

**Estado al cierre:** 5/5 posiciones abiertas. P&L: $0 (línea de base).

---

## Viernes 3 de julio de 2026 — Sesión festiva (4 de julio)

**Datos del día:** operativa reducida y volumen bajo por el festivo de la Independencia. La tecnología rebotó y el oro extendió su avance hacia ~$4,200. Sin datos macro.

**Decisión: MANTENER todo. No se opera.** Regla de liquidez: no ajustar posiciones en sesiones de volumen anómalo — las horquillas anchas castigan cualquier ejecución y los movimientos festivos suelen revertirse o confirmarse el lunes con volumen real.

**Notas de vigilancia:** el rebote tecnológico enciende la primera alerta sobre la posición #3 (bear call QQQ, strike corto 685). Se activa vigilancia estrecha para el lunes.

---

## Lunes 6 de julio de 2026 — Primera revisión completa

**Datos nuevos (pre-apertura y sesión):**
- Los futuros estadounidenses mantienen las ganancias del viernes, con la **tecnología extendiendo su rebote** (Bloomberg, 6-jul). Asia al alza (Kospi +1.8%, MSCI Asia Pacific +0.3%).
- **El petróleo cede levemente** ("oil edged lower") — sigue sin prima de riesgo; sin titulares nuevos de ruptura del alto el fuego, pero tampoco avances confirmados en el mecanismo de desconflicto del Líbano.
- Oro consolidando la zona $4,150–4,200 tras el rebote de la semana pasada.
- Sin datos macro relevantes hoy; el mercado ya mira a las minutas del FOMC del miércoles 8.

**Contraste con las hipótesis y decisiones:**

| # | Posición | Contraste con la hipótesis | Decisión | Justificación |
|---|---|---|---|---|
| 1 | Futuros largos oro (5 MGC, entrada ~$4,130) | Hipótesis intacta y reforzada: dólar contenido, oro consolidando por encima de la entrada. P&L latente ≈ +$1,000/+$2,500 | **MANTENER** | Ni el stop ($3,950) ni el objetivo ($4,300) están cerca; los drivers (inflación 4.2%, minutas del miércoles) siguen por delante |
| 2 | Bull call spread WTI 70/75 | El crudo cede levemente: la tesis de re-precio del riesgo aún no se activa, pero tampoco se invalida (WTI > $65, nivel de abandono). El catalizador (fricción del alto el fuego) sigue vivo — Irán sigue sin reunirse con los enviados de EE. UU. | **MANTENER** | La posición fue diseñada para esperar: pérdida acotada al débito, vencimiento 16-jul deja margen. Regla vigente: cerrar si WTI < $65; tomar parciales si > $73 |
| 3 | Bear call spread QQQ 685/700 | **ALERTA.** El rebote tecnológico de viernes y lunes acerca QQQ al strike corto (est. ~678–682 desde 673). La hipótesis de "techo en tech" está siendo desafiada, aunque el catalizador restrictivo (minutas) aún no ha hablado | **MANTENER con regla de salida armada** | Disciplina sobre impulso: la regla escrita ex ante manda — *si QQQ cierra > 685, cerrar/rolar sin esperar al vencimiento*. Hoy no ha cerrado por encima; cerrar ya sería pagar el rebote dos veces si las minutas del miércoles frenan a la tecnología. Riesgo residual acotado a $3,690 |
| 4 | Strangle SPY 735/760 | Mercado lateral-alcista suave; VIX estable en zona 16. El strangle pierde theta (~$300 acumulado est.), pero el evento que lo justifica (minutas) es pasado mañana | **MANTENER** | Vender hoy sería regalar la opcionalidad justo antes del catalizador. Regla vigente: VIX > 20 → monetizar mitad |
| 5 | Bull put spread DIA 520/510 | Hipótesis cumpliéndose: Dow sostenido en zona de máximos, muy lejos del strike corto (520 ≈ Dow 52,000) | **MANTENER** | Theta corre a favor; sin señal alguna de invalidación (DIA > 523 de margen de seguridad) |

**P&L estimado del portafolio al cierre del 6-jul: ≈ +$400 / +$1,500** (oro y DIA a favor; theta del strangle y marca del spread de QQQ en contra). Sin cambios de composición.

**Plan para mañana (martes 7):** día sin datos — última ventana para ajustar antes de las minutas. Puntos de decisión: (i) si QQQ abre/cierra > 685 → ejecutar la regla de cierre/rolo del bear call spread hacia 700/715 pagando la diferencia, o cerrar y esperar a las minutas; (ii) si el WTI pierde $66 intradía → preparar cierre; (iii) confirmar que el colchón de liquidez cubre el margen del oro.

---

## Martes 7 de julio de 2026 — Revisión previa a las minutas *(pendiente de ejecutar)*

Checklist específico del día:
- [ ] ¿QQQ cerró por encima de 685? → aplicar regla (cerrar o rolar el bear call spread).
- [ ] ¿VIX sigue < 17? → mantener strangle completo hacia las minutas.
- [ ] ¿WTI dentro de $66–73? → mantener spread de crudo.
- [ ] ¿Oro dentro de $3,950–4,300? → mantener 5 MGC; revisar DXY (si > 102, reducir a 3).
- [ ] Decidir postura ante las minutas: el portafolio entra al evento largo de volatilidad (strangle) y largo de oro — perfil correcto para un evento binario; no se requieren cambios salvo activación de reglas.

## Miércoles 8 de julio de 2026 — Minutas del FOMC (14:00 ET) *(pendiente de ejecutar)*

- [ ] Leer el tono de las minutas: ¿confirman la inclinación a subir tasas en 2026?
- [ ] SI restrictivas → monetizar la pata ganadora del strangle el mismo día; vigilar dólar/oro (regla DXY 102); mantener bear call QQQ.
- [ ] SI suaves → cerrar bear call QQQ de inmediato; dejar correr DIA; evaluar cierre del strangle si el mercado no se mueve ±1%.
- [ ] Cierre valorativo del portafolio para el informe final (las opciones de equity vencen el viernes 10; se marcan a mercado).
- [ ] Cerrar los 5 MGC al cierre del 8-jul (los futuros no deben quedar abiertos tras el fin del ejercicio).

## Jueves 9 de julio de 2026 — Presentación

- [ ] Consolidar P&L final por posición y del portafolio.
- [ ] Completar la sección de conclusiones del informe con los resultados realizados.
- [ ] Preparar defensa oral: cada posición debe poder explicarse en 60 segundos (tesis → estructura → riesgo máximo → qué pasó → qué se decidió).
