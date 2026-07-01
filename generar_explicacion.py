# -*- coding: utf-8 -*-
"""Genera un documento Word explicando paso a paso el cuaderno de la Tarea - Módulo 1."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# --- Estilos base ---------------------------------------------------------
estilo_normal = doc.styles["Normal"]
estilo_normal.font.name = "Calibri"
estilo_normal.font.size = Pt(11)

AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRIS = RGBColor(0x59, 0x59, 0x59)
VERDE = RGBColor(0x2E, 0x7D, 0x32)


def titulo_principal(texto):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto)
    r.bold = True
    r.font.size = Pt(20)
    r.font.color.rgb = AZUL
    return p


def subtitulo(texto):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.font.size = Pt(12)
    r.font.color.rgb = GRIS
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def encabezado(texto, nivel=1):
    h = doc.add_heading(texto, level=nivel)
    for run in h.runs:
        run.font.color.rgb = AZUL
    return h


def parrafo(texto, negrita=False):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.bold = negrita
    return p


def vineta(texto):
    return doc.add_paragraph(texto, style="List Bullet")


def numerado(texto):
    return doc.add_paragraph(texto, style="List Number")


def bloque_codigo(codigo):
    """Inserta un bloque de código con fuente monoespaciada y fondo gris claro."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(codigo)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    # Sombreado de fondo
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "F2F2F2")
    p._p.get_or_add_pPr().append(shd)
    return p


def idea_clave(texto):
    """Recuadro con una idea importante."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.15)
    r = p.add_run("💡 En pocas palabras: ")
    r.bold = True
    r.font.color.rgb = VERDE
    r2 = p.add_run(texto)
    r2.italic = True
    return p


# =========================================================================
# PORTADA
# =========================================================================
titulo_principal("Explicación paso a paso del código")
subtitulo("Tarea — Módulo 1: PBI per cápita (Banco Mundial)")
subtitulo("Comparación entre Perú y Ecuador (2000–2024)")
doc.add_paragraph()

parrafo(
    "Este documento explica, en lenguaje sencillo y línea por línea, qué hace el "
    "cuaderno de Google Colab de la tarea. La idea es que puedas entender no solo "
    "QUÉ hace cada celda, sino POR QUÉ se hace así. Al final tendrás claro todo el "
    "flujo: desde que se descargan los datos de internet hasta que se calcula el "
    "crecimiento y se dibuja el gráfico."
)

parrafo("¿Qué pide la tarea?", negrita=True)
numerado("Elegir un indicador de PBI per cápita del Banco Mundial.")
numerado("Descargarlo para Perú y para un país de comparación (aquí, Ecuador), desde el año 2000 hasta el último disponible.")
numerado("Limpiar los datos y construir un gráfico de líneas claro y bien etiquetado.")
numerado("Calcular la tasa de crecimiento promedio de cada país.")
numerado("Escribir 3 líneas interpretando lo que se ve.")

idea_clave(
    "El cuaderno automatiza todo esto: no hay que subir ningún archivo, porque "
    "los datos se bajan directamente de la página del Banco Mundial."
)

doc.add_page_break()

# =========================================================================
# CONCEPTOS PREVIOS
# =========================================================================
encabezado("Antes de empezar: 3 conceptos que se repiten", 1)

parrafo("PBI per cápita", negrita=True)
parrafo(
    "Es el valor de todo lo que produce un país en un año, dividido entre el número "
    "de habitantes. Sirve como una medida aproximada de qué tan rico es, en promedio, "
    "cada habitante. Se usa la versión en 'dólares constantes de 2015', que quita el "
    "efecto de la inflación para poder comparar el crecimiento REAL entre años."
)

parrafo("Librería (o 'biblioteca')", negrita=True)
parrafo(
    "Es un conjunto de herramientas ya programadas por otras personas que nosotros "
    "solo importamos y usamos. Así no reinventamos la rueda. En este cuaderno se usan "
    "cuatro: requests, pandas, matplotlib y wbgapi."
)

parrafo("DataFrame", negrita=True)
parrafo(
    "Es una tabla (con filas y columnas), como una hoja de Excel pero dentro de "
    "Python. Es la forma en que la librería pandas guarda y manipula los datos."
)

doc.add_paragraph()

# =========================================================================
# CELDA 1 - CONFIGURACIÓN
# =========================================================================
encabezado("Paso 1 — Configuración (qué queremos analizar)", 1)
parrafo(
    "Esta es la única celda que normalmente necesitas modificar. Aquí decides el "
    "indicador, los países y los años."
)
bloque_codigo(
    "import requests\n"
    "import pandas as pd\n"
    "import matplotlib.pyplot as plt\n\n"
    'INDICADOR = "NY.GDP.PCAP.KD"\n\n'
    'PERU = "PER"\n'
    'PAIS_COMPARACION = "ECU"   # cámbialo: "COL", "BRA", "MEX", etc.\n\n'
    "ANIO_INICIO = 2000\n"
    "ANIO_FIN = 2024"
)
parrafo("Explicación línea por línea:")
vineta("Las tres primeras líneas (import ...) traen las herramientas. 'as pd' y 'as plt' son apodos cortos para escribir menos después.")
vineta('INDICADOR = "NY.GDP.PCAP.KD": es el código que el Banco Mundial usa para "PBI per cápita en dólares constantes de 2015". Ese código raro es como el "nombre técnico" del dato.')
vineta('PERU = "PER" y PAIS_COMPARACION = "ECU": son los códigos ISO3 (de 3 letras) de cada país. PER = Perú, ECU = Ecuador.')
vineta("ANIO_INICIO y ANIO_FIN: el rango de años. Si un año todavía no tiene dato publicado, el Banco Mundial simplemente lo ignora.")
idea_clave("Guardar estos valores en variables con NOMBRE permite reutilizarlos en todo el cuaderno sin repetir números sueltos. Si mañana quieres comparar con Colombia, solo cambias 'ECU' por 'COL' aquí y todo lo demás se recalcula solo.")

# =========================================================================
# CELDA 2 - INSTALAR / FUNCIÓN DE DESCARGA
# =========================================================================
encabezado("Paso 2 — Función para descargar datos del Banco Mundial", 1)
parrafo(
    "Primero se instala una librería especializada llamada wbgapi (World Bank API), "
    "que sabe hablar con el Banco Mundial:"
)
bloque_codigo("!pip install wbgapi -q")
vineta("El signo '!' indica que es un comando de instalación, no código Python normal.")
vineta("'-q' significa 'quiet' (silencioso): que no llene la pantalla de mensajes.")

parrafo("Luego se define una FUNCIÓN, que es como una receta reutilizable:")
bloque_codigo(
    "import wbgapi as wb\n"
    "import pandas as pd\n\n"
    "def obtener_datos_banco_mundial(codigo_pais, indicador, anio_inicio, anio_fin):\n"
    "    serie = wb.data.DataFrame(\n"
    "        indicador,\n"
    "        economy=codigo_pais,\n"
    "        time=range(anio_inicio, anio_fin + 1),\n"
    "        numericTimeKeys=True,\n"
    "        labels=False,\n"
    "    )\n"
    "    df = serie.reset_index().melt(\n"
    '        id_vars="economy", var_name="anio", value_name="valor"\n'
    "    )\n"
    '    df = df.rename(columns={"economy": "iso3"})\n'
    '    df["pais"] = codigo_pais\n'
    '    df["anio"] = df["anio"].astype(int)\n'
    '    df = df.sort_values("anio").reset_index(drop=True)\n'
    "    return df"
)
parrafo("¿Qué es una función? ", negrita=True)
parrafo(
    "Es un bloque de código con un nombre, al que le das unos 'ingredientes' (los "
    "parámetros entre paréntesis) y te devuelve un resultado. Aquí la receta se llama "
    "'obtener_datos_banco_mundial' y recibe: el país, el indicador y los años. La "
    "ventaja es que la escribimos UNA vez y la usamos para Perú y para Ecuador sin "
    "copiar y pegar."
)
parrafo("Qué hace por dentro, paso a paso:")
numerado("wb.data.DataFrame(...): le pide al Banco Mundial los datos del indicador, para ese país, en ese rango de años. 'numericTimeKeys=True' hace que los años sean números (2020) y no texto raro ('YR2020').")
numerado("reset_index().melt(...): reordena la tabla para que quede 'larga': una fila por año, con columnas año y valor. Es un formato más cómodo para graficar.")
numerado('rename(columns=...): renombra la columna "economy" a "iso3" (el código del país), para que sea más claro.')
numerado('df["pais"] = codigo_pais: agrega una columna con el nombre del país en cada fila.')
numerado('astype(int): se asegura de que el año sea un número entero.')
numerado('sort_values("anio"): ordena las filas del año más antiguo al más reciente.')
numerado("return df: devuelve la tabla ya lista.")
idea_clave("Esta función es el 'corazón' que trae los datos de internet y los deja convertidos en una tabla ordenada de 4 columnas: iso3, anio, valor y pais.")

# =========================================================================
# CELDA 3 - DESCARGA
# =========================================================================
encabezado("Paso 3 — Descargar los datos de los dos países", 1)
bloque_codigo(
    "df_peru = obtener_datos_banco_mundial(PERU, INDICADOR, ANIO_INICIO, ANIO_FIN)\n"
    "df_comp = obtener_datos_banco_mundial(PAIS_COMPARACION, INDICADOR, ANIO_INICIO, ANIO_FIN)\n\n"
    'print("Perú — primeras filas:")\n'
    "display(df_peru.head())\n\n"
    "display(df_comp.head())"
)
parrafo("Aquí se USA la función que creamos antes, dos veces:")
vineta("df_peru: guarda la tabla de Perú.")
vineta("df_comp: guarda la tabla del país de comparación (Ecuador).")
vineta("display(df_peru.head()): muestra en pantalla las primeras 5 filas, solo para revisar que los datos llegaron bien.")
parrafo(
    "En el resultado se ve, por ejemplo, que Perú en el año 2000 tenía un PBI per "
    "cápita de 3286.27 dólares, y Ecuador 3953.40 dólares. Ecuador arrancó más arriba."
)

# =========================================================================
# CELDA 4 - LIMPIEZA
# =========================================================================
encabezado("Paso 4 — Limpieza de datos", 1)
parrafo(
    "Los datos crudos a veces traen 'huecos' (años sin información). Antes de graficar "
    "hay que dejarlos ordenados y sin errores."
)
bloque_codigo(
    'df_peru = df_peru.dropna(subset=["valor"]).reset_index(drop=True)\n'
    'df_comp = df_comp.dropna(subset=["valor"]).reset_index(drop=True)\n\n'
    'df_peru["valor"] = df_peru["valor"].astype(float)\n'
    'df_comp["valor"] = df_comp["valor"].astype(float)\n\n'
    "tabla = (\n"
    "    pd.concat([df_peru, df_comp])\n"
    '    .pivot(index="anio", columns="pais", values="valor")\n'
    "    .sort_index()\n"
    ")\n"
    "display(tabla)"
)
parrafo("Explicación:")
vineta('dropna(subset=["valor"]): elimina (drop) las filas que NO tienen valor (na = "no disponible"). Así no aparecen huecos en el gráfico.')
vineta("astype(float): convierte los valores a números con decimales, para poder hacer cuentas con ellos.")
vineta('pd.concat([...]).pivot(...): junta las dos tablas y las reorganiza en una sola tabla "ancha": una fila por año y una columna por país (ECU y PER, una al lado de la otra). Es solo para revisarlas cómodamente.')
idea_clave("Limpiar datos es un paso obligatorio en cualquier análisis: garantiza que los cálculos y el gráfico no fallen ni muestren cosas raras.")

# =========================================================================
# CELDA 5 - GRÁFICO
# =========================================================================
encabezado("Paso 5 — Gráfico de líneas comparativo", 1)
bloque_codigo(
    "plt.figure(figsize=(10, 6))\n\n"
    'plt.plot(df_peru["anio"], df_peru["valor"], marker="o", linewidth=2, label="Perú")\n'
    'plt.plot(df_comp["anio"], df_comp["valor"], marker="o", linewidth=2,\n'
    '         label=df_comp["pais"].iloc[0])\n\n'
    "plt.title(...)\n"
    'plt.xlabel("Año")\n'
    'plt.ylabel("PBI per cápita (US$ constantes de 2015)")\n'
    'plt.legend(title="País")\n'
    "plt.grid(True, alpha=0.3)\n"
    "plt.tight_layout()\n"
    "plt.show()"
)
parrafo("Cada línea del gráfico se construye así:")
vineta("plt.figure(figsize=(10, 6)): crea el lienzo del gráfico y define su tamaño (10 de ancho, 6 de alto).")
vineta('plt.plot(...): dibuja una línea. La primera es Perú (eje X = años, eje Y = valores). marker="o" pone un puntito en cada año; linewidth=2 es el grosor; label es el nombre que aparecerá en la leyenda.')
vineta("La segunda plt.plot dibuja al país de comparación encima, para poder compararlos.")
vineta("plt.title / xlabel / ylabel: ponen el título y los nombres de los ejes (esto es lo que pide la tarea: gráfico bien etiquetado).")
vineta("plt.legend: muestra el recuadro que dice qué color es cada país.")
vineta("plt.grid(True, alpha=0.3): añade una cuadrícula suave de fondo para leer mejor. alpha es la transparencia.")
vineta("plt.show(): finalmente muestra el gráfico en pantalla.")

# =========================================================================
# CELDA 6 - CAGR
# =========================================================================
encabezado("Paso 6 — Tasa de crecimiento promedio anual (CAGR)", 1)
parrafo(
    "El CAGR responde a la pregunta: '¿en promedio, cuánto creció cada año el PBI per "
    "cápita?'. Es un promedio 'compuesto', parecido a los intereses de un banco. La "
    "fórmula es:"
)
bloque_codigo("CAGR = (valor_final / valor_inicial) ** (1 / n_años) - 1")
bloque_codigo(
    "def tasa_crecimiento_promedio_anual(df):\n"
    '    primer_anio = df["anio"].min()\n'
    '    ultimo_anio = df["anio"].max()\n'
    '    valor_inicial = df.loc[df["anio"] == primer_anio, "valor"].values[0]\n'
    '    valor_final = df.loc[df["anio"] == ultimo_anio, "valor"].values[0]\n'
    "    n_anios = ultimo_anio - primer_anio\n"
    "    cagr = (valor_final / valor_inicial) ** (1 / n_anios) - 1\n"
    "    return cagr, primer_anio, ultimo_anio"
)
parrafo("Qué hace, paso a paso:")
numerado("Busca el primer año (.min()) y el último año (.max()) con dato.")
numerado("Toma el valor del PBI en el primer año y en el último.")
numerado("Calcula cuántos años pasaron (n_anios).")
numerado("Aplica la fórmula del CAGR. El '**' significa 'elevado a'. El resultado sale en decimal (por ejemplo 0.0303).")
parrafo(
    "Después se llama a la función para los dos países y se arma una tabla resumen "
    "multiplicando por 100 para mostrarlo en porcentaje. El resultado fue: Perú 3.03% "
    "anual y Ecuador 1.75% anual."
)
idea_clave("Perú creció, en promedio, casi el doble de rápido por año que Ecuador. Por el efecto compuesto, esa diferencia se vuelve enorme a lo largo de 24 años.")

# =========================================================================
# CELDA 7 - INTERPRETACIÓN
# =========================================================================
encabezado("Paso 7 — Interpretación (las 3 líneas que pide la tarea)", 1)
parrafo(
    "Esta última parte no es código: es texto donde explicas con tus palabras lo que "
    "muestran el gráfico y la tabla. Tu cuaderno ya trae una buena interpretación que "
    "resume tres ideas:"
)
numerado("Inicio vs. final: en el año 2000 Ecuador estaba por encima de Perú, pero para 2024 Perú lo superó y terminó más arriba (~$6,700 vs ~$6,000).")
numerado("Quién creció más: Perú (3.03% anual) creció más rápido que Ecuador (1.75%). La diferencia parece pequeña, pero acumulada en 24 años es grande.")
numerado("Momentos clave del gráfico: la crisis financiera de 2009, la caída de precios de materias primas (2014–2016) y la pandemia de COVID-19 en 2020, que provocó el desplome más fuerte en ambos países.")

doc.add_paragraph()
encabezado("Resumen del flujo completo", 1)
parrafo(
    "Si tuvieras que explicarle a alguien qué hace el cuaderno en una sola frase por "
    "paso, sería así:"
)
numerado("Configurar: elegir indicador, países y años.")
numerado("Descargar: bajar los datos del Banco Mundial con una función reutilizable.")
numerado("Limpiar: quitar años vacíos y ordenar.")
numerado("Graficar: dibujar las dos líneas comparativas y etiquetarlas.")
numerado("Calcular: obtener el crecimiento promedio anual (CAGR) de cada país.")
numerado("Interpretar: explicar en palabras qué significan los resultados.")

doc.add_paragraph()
p_final = doc.add_paragraph()
r = p_final.add_run(
    "Con esto ya entiendes de principio a fin qué hace cada celda y por qué. "
    "Cualquier duda puntual sobre una línea específica, puedes revisar el apartado "
    "correspondiente de este documento."
)
r.italic = True
r.font.color.rgb = GRIS

# =========================================================================
salida = "/home/user/Desarrollo-economico/Explicacion_Tarea_Modulo1.docx"
doc.save(salida)
print("Documento guardado en:", salida)
