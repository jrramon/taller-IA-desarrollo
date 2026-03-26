# Guía del instructor

## Antes del ejercicio

- Asegúrate de que todos tienen Cursor abierto con la API Key configurada
- Que abran la carpeta `alumno` en Cursor
- Que tengan pandas y matplotlib instalados: `pip install pandas matplotlib`

## Datos: qué hay escondido en el CSV

Los datos están diseñados con patrones intencionados para que el análisis sea interesante:

| Patrón | Qué deberían descubrir |
|--------|----------------------|
| Turno noche siempre peor | Más defectos, más paradas, OEE bajo. ¿Fatiga? ¿Menos supervisión? |
| Temperatura sube → defectos suben | Correlación clara en turno noche (temperatura se descontrola) |
| Presión baja → más defectos | Cuando presión < 3.0 en L1 o < 4.0 en L2, hay problemas |
| Avería mecánica es la causa top | ~60% del tiempo de parada total |
| PIEZA-C tiene más defectos | Producto más difícil de fabricar |
| L2 noche tiene averías eléctricas | Solo L2, solo noche — patrón sospechoso |

## Tiempos

| Parte | Duración | Qué hacer si van lentos |
|-------|----------|------------------------|
| 1. Exploración | 15 min | Muestra tu pantalla con un ejemplo, que repliquen |
| 2. KPIs | 20 min | Si no saben qué es OEE, explícalo 2 min en pizarra |
| 3. Visualización | 20 min | Si matplotlib da problemas, que usen `print()` y tablas |
| 4. Correlaciones | 15 min | Pueden saltar si van justos |
| 5. Informe | 15 min | Pueden saltar si van justos |
| 6. Reto libre | 15 min | Para los que van rápido |

**Total: ~100 min** (1h 40min). Deja 20 min de colchón para dudas y problemas técnicos.

## Prompts de ejemplo que funcionan bien

### Parte 1
```
Carga el archivo datos_produccion.csv con pandas. Muéstrame las primeras filas,
los tipos de datos, y un resumen estadístico. Dime si hay valores nulos o raros.
```

### Parte 2
```
Con los datos cargados, calcula el OEE simplificado por línea y turno.
La capacidad teórica es 1250 unidades para L1 y 850 para L2.
El turno dura 480 minutos.
OEE = Disponibilidad x Rendimiento x Calidad.
Muestra el resultado en una tabla ordenada de peor a mejor OEE.
```

### Parte 3
```
Genera un gráfico de Pareto con las causas de parada.
Barras con el tiempo total por causa (ordenado de mayor a menor)
y una línea con el porcentaje acumulado.
Todo en español, con título y etiquetas claras.
```

### Parte 4
```
Haz un scatter plot de temperatura_horno vs tasa_de_defectos
(unidades_defectuosas / unidades_producidas), coloreado por turno.
¿Hay correlación? Calcula el coeficiente de Pearson.
```

## Errores comunes y cómo ayudar

| Problema | Solución |
|----------|----------|
| "No encuentra el archivo" | Que abran la carpeta correcta en Cursor, no un archivo suelto |
| "No tengo pandas" | `pip install pandas matplotlib` en el terminal de Cursor |
| Claude genera código con columnas que no existen | Diles que peguen las primeras filas del CSV en el prompt como contexto |
| El gráfico no se muestra | Añadir `plt.show()` o guardar con `plt.savefig('grafico.png')` |
| Se atascan sin saber qué pedir | Proyecta los prompts de ejemplo |

## Mensaje clave al cerrar

> "La IA no reemplaza lo que sabéis de ingeniería de producción. Vosotros sabéis que un OEE del 60% en turno noche es un problema, y sabéis que la temperatura del horno descontrolada puede ser la causa. La IA os ayuda a llegar a esa conclusión más rápido, con mejor código y mejores gráficos. Pero la interpretación y la decisión siguen siendo vuestras."
