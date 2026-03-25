# Ejercicio: Análisis de datos de producción con IA

## Contexto

Trabajas en una planta de fabricación con **2 líneas de producción** (L1 y L2) que operan en **3 turnos** (mañana, tarde, noche). Tienes datos de una semana de producción en `datos_produccion.csv`.

Tu jefe te ha pedido un análisis rápido para la reunión de mañana.

---

## Parte 1 — Exploración (15 min)

Abre el chat de Cursor (`Ctrl+L`) y pide ayuda para explorar los datos.

**Objetivo:** Obtener un script que cargue el CSV y muestre un resumen básico.

Prueba a pedir cosas como:

- "Carga datos_produccion.csv con pandas y muéstrame un resumen de los datos"
- "¿Cuántos registros hay por línea y turno?"
- "¿Cuál es la tasa de defectos media por turno?"

> **Consejo:** No copies y pegues el primer resultado sin leerlo. Léelo, entiéndelo, y ejecútalo. Si algo no cuadra, dile a Claude qué está mal.

---

## Parte 2 — KPIs de producción (20 min)

Pide a Claude que te ayude a calcular estos indicadores:

1. **OEE simplificado** por línea y turno:
   - Disponibilidad = (480 - tiempo_parada_min) / 480
   - Rendimiento = unidades_producidas / capacidad_teórica
   - Calidad = (unidades_producidas - unidades_defectuosas) / unidades_producidas
   - OEE = Disponibilidad × Rendimiento × Calidad
   - Capacidad teórica: L1=1250, L2=850

2. **Top 3 causas de parada** por tiempo total perdido

3. **Tasa de defectos** por producto

> **Consejo:** Si no sabes qué es el OEE, pregúntale a Claude que te lo explique. Usa la IA también para aprender, no solo para generar código.

---

## Parte 3 — Visualización (20 min)

Pide a Claude que genere gráficos con matplotlib:

1. **Gráfico de barras**: OEE por línea y turno
2. **Gráfico de línea**: Evolución de defectos por día
3. **Pareto**: Causas de parada (barras + línea acumulada)

> **Consejo:** Si el gráfico no se ve bien, describe el problema a Claude. "Las etiquetas se solapan", "quiero los colores por turno", "ponlo en español". Iterar es parte del proceso.

---

## Parte 4 — Correlaciones (15 min)

Investiga con ayuda de Claude:

- ¿Hay relación entre la temperatura del horno y la tasa de defectos?
- ¿El turno de noche siempre tiene peores resultados? ¿Por qué podría ser?
- ¿Qué pasa cuando la presión baja de cierto valor?

Pide a Claude que te haga un análisis de correlación y un scatter plot.

---

## Parte 5 — Informe automático (15 min)

Pide a Claude que genere una función que produzca un informe resumen en texto:

```
=== INFORME DE PRODUCCIÓN SEMANAL ===
Período: 2026-03-02 al 2026-03-06

RESUMEN POR LÍNEA:
  L1: OEE medio = XX% | Defectos = XX% | Paradas = XX min
  L2: OEE medio = XX% | Defectos = XX% | Paradas = XX min

ALERTAS:
  - Turno noche L1: OEE por debajo del 60%
  - Producto PIEZA-C: tasa de defectos > 5%

TOP CAUSAS DE PARADA:
  1. averia_mecanica: XXX min (XX%)
  2. ...
```

---

## Parte 6 — Reto libre (15 min)

Elige uno:

- **A)** Pide a Claude que prediga cuántas unidades defectuosas habrá mañana basándose en los datos históricos
- **B)** Pide a Claude que genere un dashboard interactivo con Streamlit
- **C)** Pide a Claude que detecte automáticamente anomalías en las mediciones de sensores

---

## Trucos para trabajar bien con IA

1. **Sé específico**: "Haz un gráfico" es peor que "Haz un gráfico de barras del OEE por turno, con colores distintos por línea, en español"
2. **Itera**: El primer resultado rara vez es perfecto. Dile qué cambiar.
3. **Pregunta por qué**: "¿Por qué has usado groupby aquí?" te ayuda a aprender.
4. **Revisa siempre**: La IA puede inventar columnas que no existen o calcular mal. Tú eres el ingeniero.
5. **Contexto**: Si le das contexto ("estos son datos de un horno de fundición, la temperatura normal es 185°C"), los resultados mejoran mucho.
