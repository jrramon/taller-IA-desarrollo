# Guía del Facilitador — Taller: IA para Ingenieros que Programan

**Duración:** 3 horas (180 min)
**Audiencia:** Ingenieros industriales, programan en Python, nivel variado
**Formato:** Presencial, participativo, hands-on
**Herramienta:** Cursor con API Key de Claude (Sonnet 4.6)

---

## Antes del taller

### Logística (1 semana antes)

- [ ] Enviar email con instrucciones de instalación:
  - Descargar Cursor desde cursor.com
  - Descargar Node.js LTS (por si acaso)
  - Tener Python instalado y funcionando
- [ ] Crear API Key en console.anthropic.com
- [ ] Configurar spending limit (50-100€)
- [ ] Probar el ejercicio completo tú mismo en Cursor con la key
- [ ] Imprimir o tener a mano la cheat sheet de prompts (Anexo A)

### Preparación de sala (30 min antes)

- [ ] Proyector funcionando
- [ ] Compartir por chat/email: API Key + script `setup-taller-cursor.ps1`
- [ ] Tener el CSV y el EJERCICIO.md en una carpeta compartida (USB, red, o link)
- [ ] Pizarra o flipchart disponible
- [ ] Post-its y rotuladores (para la dinámica de cierre)

### Tu setup como facilitador

- Cursor abierto con el ejercicio resuelto (para mostrar si alguien se atasca)
- Terminal abierto por si hay que depurar problemas de instalación
- Este documento abierto como referencia

---

## Estructura general

```
 00:00 - 00:20  Apertura y setup técnico
 00:20 - 00:45  Demo en vivo: de problema a solución con IA
 00:45 - 00:55  Principios clave (micro-teoría)
 00:55 - 01:00  Pausa (5 min)
 01:00 - 01:50  Ejercicio guiado: análisis de producción
 01:50 - 02:00  Pausa (10 min)
 02:00 - 02:30  Ejercicio libre + retos
 02:30 - 02:50  Puesta en común y reflexión
 02:50 - 03:00  Cierre y siguientes pasos
```

---

## Bloque 1 — Apertura y setup (20 min)

### Objetivos

- Que todos tengan Cursor funcionando con la API Key
- Romper el hielo y calibrar el nivel del grupo

### Guión del facilitador

**[00:00 - 00:05] Bienvenida (5 min)**

> "Hoy vamos a aprender a programar **con** IA, no a programar IA. La diferencia es importante: no vamos a entrenar modelos ni hacer machine learning. Vamos a usar IA como copiloto mientras programamos lo que ya programáis normalmente."

Pregunta al grupo (a mano alzada, rápido):

- "¿Quién ha usado ChatGPT o similar alguna vez?" (casi todos)
- "¿Quién lo ha usado para escribir código Python?" (algunos)
- "¿Quién lo usa integrado en su editor mientras programa?" (pocos)

> "Perfecto. Hoy vamos a ir del segundo al tercer grupo. Vamos a tener la IA dentro del editor, como un compañero que conoce vuestro código."

**[00:05 - 00:20] Setup técnico (15 min)**

Proyecta los pasos en pantalla:

1. Abrir Cursor
2. `Ctrl + ,` → Models → pegar API Key de Anthropic
3. Activar `claude-sonnet-4-6`
4. Desactivar Cursor Tab (para controlar costes)
5. Abrir la carpeta del ejercicio
6. Probar: `Ctrl+L` → escribir "Hola, ¿funcionas?" → Enter

**Tip facilitador:** Mientras van configurando, pasa por las mesas. Los problemas más comunes:

| Problema | Solución rápida |
|----------|----------------|
| "No me sale Models" | Settings → buscar "models" en la barra |
| "No me responde" | Comprobar que la key empieza por sk-ant- |
| "No tengo Python" | Instalar desde python.org, reiniciar Cursor |
| "No encuentro el ejercicio" | File → Open Folder → seleccionar la carpeta |

**Señal de que puedes avanzar:** Al menos el 80% ha recibido respuesta de Claude en Cursor. Si alguien se queda atrás, que se siente con un compañero que ya funcione (pair programming natural).

---

## Bloque 2 — Demo en vivo (25 min)

### Objetivo

Mostrar el potencial en 3 escenarios progresivos. Tú programas en directo con Cursor proyectado. Ellos observan.

### Guión del facilitador

> "Antes de que os lancéis vosotros, voy a hacer tres cosas en directo para que veáis cómo trabajo yo con IA. Fijaos en **cómo pido las cosas**, no solo en lo que pido."

**[00:20 - 00:28] Escenario 1 — Exploración de datos (8 min)**

Abre un Python vacío. En el chat de Cursor (`Ctrl+L`), escribe:

```
Carga el archivo datos_produccion.csv con pandas.
Muéstrame un resumen: cuántos registros hay, qué columnas tiene,
si hay valores nulos, y las estadísticas básicas de las columnas numéricas.
```

- Ejecuta el código que genera Claude
- Señala en voz alta: *"Fijaos que le he dado contexto: le he dicho qué archivo, qué quiero ver, y en qué orden. Si le digo solo 'analiza el CSV' el resultado es peor."*

**[00:28 - 00:36] Escenario 2 — Iterar sobre un resultado (8 min)**

El resumen inicial probablemente es genérico. Ahora pide algo específico:

```
Calcula la tasa de defectos (unidades_defectuosas / unidades_producidas)
por turno. ¿Hay diferencia significativa entre turnos?
Muéstralo en una tabla y haz un gráfico de barras.
```

Cuando salga el resultado, **critica algo en voz alta**:

> "El gráfico está bien pero las etiquetas están en inglés y el título no dice nada. Voy a pedirle que lo mejore."

```
Pon el gráfico en español. Título: "Tasa de defectos por turno".
Añade el valor de cada barra encima. Usa colores: verde mañana, naranja tarde, rojo noche.
```

**Mensaje clave:** *"La primera respuesta de la IA rara vez es la definitiva. Iterar es el proceso normal. No es que la IA sea mala — es que vosotros sabéis lo que queréis y ella no."*

**[00:36 - 00:45] Escenario 3 — La IA se equivoca (9 min)**

Pide algo donde Claude probablemente cometa un error o haga una suposición incorrecta:

```
Calcula el OEE por línea. Usa la fórmula estándar.
```

Claude probablemente inventará la capacidad teórica o usará valores incorrectos. Pausa y di:

> "¿Veis? Ha asumido una capacidad teórica sin preguntarme. Eso está **mal**. Yo sé que L1 tiene capacidad 1250 y L2 tiene 850. La IA no lo sabe. Si no reviso el código, tengo un informe con números incorrectos que parecen correctos."

Corrige:

```
La capacidad teórica es 1250 para L1 y 850 para L2.
Cada turno dura 480 minutos. Recalcula.
```

**Mensaje clave:** *"La IA es un becario muy rápido. Produce mucho, pero si no le dais contexto y no revisáis su trabajo, os va a meter en problemas. Vosotros sois los ingenieros."*

---

## Bloque 3 — Principios clave (10 min)

### Objetivo

Anclar 5 ideas antes de que empiecen a practicar. No es una clase magistral — son 2 minutos por idea, con ejemplo de cada una.

### Guión del facilitador

Proyecta (o escribe en la pizarra) estas 5 reglas:

> **1. Sé específico**
> Mal: "Haz un gráfico"
> Bien: "Haz un gráfico de barras del OEE por turno, coloreado por línea, en español, con valores encima"

> **2. Da contexto**
> "Estos son datos de producción de una planta de fabricación con 2 líneas y 3 turnos. La capacidad teórica de L1 es 1250 unidades por turno."

> **3. Itera**
> El primer resultado es un borrador. Dile qué cambiar: "las etiquetas se solapan", "ordénalo de mayor a menor", "usa porcentajes en vez de decimales".

> **4. Revisa siempre**
> La IA puede inventar columnas, asumir valores, o calcular mal. Tú eres el responsable del resultado.

> **5. Pregunta para aprender**
> "¿Por qué has usado groupby?", "¿Qué hace el parámetro aggfunc?", "Explícame esta línea". Usar la IA sin aprender es una oportunidad perdida.

> "Tenéis estas 5 reglas. Ahora vamos a practicar."

**[00:55 - 01:00] Pausa 5 min**

---

## Bloque 4 — Ejercicio guiado: Análisis de producción (50 min)

### Objetivo

Que cada participante complete al menos las partes 1-3 del ejercicio. Los más rápidos llegarán a la 4-5.

### Dinámica

- Trabajan individualmente o en parejas (que elijan ellos)
- Tienen `EJERCICIO.md` abierto con las instrucciones
- Tú circulan por la sala, no te sientas

### Guión del facilitador

**[01:00 - 01:05] Lanzamiento (5 min)**

> "Abrid el archivo EJERCICIO.md. Tiene 6 partes. Las 3 primeras son las que todos deberíais completar. Las otras 3 son para los que vayan más rápido. No hay que llegar al final — lo que importa es que probéis, que iteréis, y que os peleéis un poco con la IA."

> "Una cosa: no copiéis los prompts del compañero. Cada uno que pida las cosas a su manera. Parte del aprendizaje es descubrir qué funciona y qué no funciona cuando le pedís algo a la IA."

**[01:05 - 01:50] Trabajo autónomo (45 min)**

Tu rol como facilitador durante este bloque:

| Minuto | Qué hacer |
|--------|-----------|
| 01:05-01:15 | Circula rápido. Asegúrate de que todos han cargado el CSV y ven datos. Desbloquea a los atascados. |
| 01:15 | Si ves que varios están parados en lo mismo, para al grupo 30 segundos y da la pista en voz alta. |
| 01:20-01:35 | La mayoría debería estar en la parte 2 (KPIs). Pregunta a alguno: "¿Qué OEE te ha salido? ¿Te parece realista?" |
| 01:35 | Aviso al grupo: *"Os quedan 15 minutos para este bloque. Si estáis en la parte 2, intentad llegar al menos a un gráfico."* |
| 01:35-01:50 | Los rápidos estarán en parte 3-4. Los lentos en parte 2. Está bien. |

**Intervenciones tipo:**

Si alguien dice **"no sé qué pedirle"**:
> "Piensa en lo que harías tú a mano. ¿Qué calcularías primero? Dile eso a Claude, como si se lo explicaras a un compañero nuevo."

Si alguien dice **"me ha generado código que no entiendo"**:
> "Perfecto. Selecciona ese código y pregúntale: 'Explícame qué hace cada línea de este bloque'. Eso es exactamente lo que quiero que hagáis."

Si alguien dice **"me da error"**:
> "Copia el error y pégalo en el chat de Claude. Dile: 'Me da este error al ejecutar tu código, corrígelo.'"

Si alguien **copia y pega sin leer**:
> "Para un momento. ¿Qué hace ese código? Léelo antes de ejecutarlo. Si no lo entiendes, pregúntale a Claude que te lo explique."

**[01:50 - 02:00] Pausa 10 min**

> "Descansamos 10 minutos. Cuando volváis vais a elegir un reto libre."

---

## Bloque 5 — Ejercicio libre + retos (30 min)

### Objetivo

Que experimenten con libertad. Este bloque es donde más aprenden porque les toca pensar qué pedir.

### Guión del facilitador

**[02:00 - 02:05] Lanzamiento (5 min)**

> "Ahora tenéis 25 minutos de trabajo libre. Podéis elegir:"

Proyecta las opciones:

> **A) Predicción** — Pide a Claude que prediga cuántas unidades defectuosas habrá mañana basándose en los datos
>
> **B) Dashboard** — Pide a Claude que genere un dashboard interactivo con Streamlit
>
> **C) Anomalías** — Pide a Claude que detecte automáticamente anomalías en los sensores
>
> **D) Tu propio reto** — ¿Tienes un problema real de tu trabajo? Descríbeselo a Claude y pídele que te ayude

> "La opción D es la más valiosa si tenéis algo real. Si no, elegid A, B o C."

**[02:05 - 02:30] Trabajo autónomo (25 min)**

- Circula, observa, toma notas mentales de momentos interesantes para la puesta en común
- Si alguien elige la opción D con un problema real, dedícale atención especial — esa es la mejor prueba de valor del taller
- Si alguien intenta el dashboard Streamlit, necesitará `pip install streamlit` y ejecutar con `streamlit run app.py`

---

## Bloque 6 — Puesta en común y reflexión (20 min)

### Objetivo

Consolidar aprendizajes. Este bloque es lo que convierte un "taller de herramientas" en un taller de verdad.

### Guión del facilitador

**[02:30 - 02:40] Ronda de descubrimientos (10 min)**

No hagas una ronda clásica — es lenta y aburrida. En su lugar:

> "Voy a hacer 4 preguntas. Levantad la mano si queréis compartir algo. Si no, paso a la siguiente."

**Pregunta 1:** *"¿Alguien ha descubierto algo en los datos que le haya sorprendido?"*
- Esperas que mencionen: turno noche mucho peor, temperatura correlaciona con defectos, averías eléctricas solo en L2 noche.
- Si nadie lo menciona, dilo tú: *"¿Os habéis fijado en que el turno de noche tiene 5 veces más defectos? ¿Y que la temperatura del horno sube justo en esos turnos?"*

**Pregunta 2:** *"¿En qué momento la IA os ha dado algo mal o que no tenía sentido?"*
- Aquí quieres reforzar el mensaje de revisión. Ejemplos comunes: inventar columnas, asumir la capacidad teórica, calcular mal un porcentaje.

**Pregunta 3:** *"¿Qué habéis aprendido sobre **cómo pedir** cosas?"*
- Esperas respuestas tipo: "ser más específico", "darle contexto", "decirle el formato que quiero".

**Pregunta 4:** *"¿Alguien ha probado algo de su trabajo real?"*
- Si alguien lo ha hecho, que lo cuente. Es la mejor publicidad para la adopción.

**[02:40 - 02:50] Reflexión con post-its (10 min)**

Reparte post-its de dos colores. Pide:

- **Color 1:** "Una cosa que voy a empezar a hacer la semana que viene con IA"
- **Color 2:** "Una preocupación o duda que me llevo"

Que los peguen en la pizarra. Lee algunos en voz alta y comenta brevemente.

Preocupaciones típicas y cómo responder:

| Preocupación | Respuesta |
|-------------|-----------|
| "¿Y si pego código confidencial?" | "Buen punto. Con la API Key, los datos van directo a Anthropic y no se usan para entrenar. Pero consultad la política de vuestra empresa antes de pegar datos sensibles." |
| "¿No nos va a hacer peores programadores?" | "Si dejáis de pensar, sí. Si lo usáis para ir más rápido y aprender más, no. La clave es revisar y entender siempre." |
| "¿Cuánto cuesta?" | "Cursor tiene free tier. Copilot cuesta 10$/mes. Claude API depende del uso — para lo que hacéis vosotros, 10-20€/mes probablemente." |
| "¿Qué herramienta elijo?" | "Probad Cursor esta semana con lo que habéis aprendido hoy. Es la más fácil para empezar." |

---

## Bloque 7 — Cierre (10 min)

### Guión del facilitador

**[02:50 - 03:00] Cierre**

> "Tres cosas para llevaros a casa:"

> **1. Empezad esta semana.** No la que viene, no cuando tengáis tiempo. Mañana. Abrid Cursor con un script que tengáis a medias y pedidle ayuda. El hábito se crea usándolo, no pensando en usarlo.

> **2. La IA amplifica lo que sabéis.** Vosotros sabéis de producción, de calidad, de procesos. La IA sabe de código. Juntos sois más rápidos. Pero si no sabéis qué pedir o no revisáis lo que genera, no funciona.

> **3. Compartid.** Si descubrís un prompt que funciona bien, si la IA os resuelve algo chulo, compartidlo con el equipo. Así todos mejoran más rápido.

Proyecta o comparte:

```
RECURSOS PARA SEGUIR

- Cursor: cursor.com (editor con IA integrada)
- Claude: claude.ai (para conversaciones más largas)
- Prompt engineering: buscar "Anthropic prompt engineering guide"
- Si usáis VS Code: extensión GitHub Copilot (free tier)
```

> "Gracias por venir y por probar. Si tenéis dudas después del taller, ya sabéis dónde encontrarme."

---

## Anexo A — Cheat sheet de prompts para participantes

Imprime esto o compártelo por chat al inicio del taller.

```
╔══════════════════════════════════════════════════════════════╗
║  CHEAT SHEET — PROMPTS PARA EL TALLER                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  EXPLORAR DATOS                                              ║
║  "Carga datos_produccion.csv con pandas y muéstrame          ║
║   un resumen: filas, columnas, tipos, nulos, estadísticas"   ║
║                                                              ║
║  CALCULAR                                                    ║
║  "Calcula la tasa de defectos por turno y línea.             ║
║   La fórmula es: defectuosas / producidas.                   ║
║   Muéstralo en una tabla pivotada."                          ║
║                                                              ║
║  VISUALIZAR                                                  ║
║  "Haz un gráfico de barras de [X] por [Y].                  ║
║   Coloreado por [Z]. En español. Con valores encima."        ║
║                                                              ║
║  CORREGIR                                                    ║
║  "Me da este error: [pegar error]. Corrígelo."               ║
║                                                              ║
║  MEJORAR                                                     ║
║  "El gráfico está bien pero [problema]. Cámbialo."           ║
║                                                              ║
║  ENTENDER                                                    ║
║  "Explícame qué hace cada línea de este código."             ║
║  "¿Por qué usas groupby aquí?"                               ║
║  "¿Qué es OEE? Explícamelo en 3 frases."                    ║
║                                                              ║
║  DAR CONTEXTO                                                ║
║  "Son datos de producción industrial. 2 líneas (L1, L2).     ║
║   3 turnos. Capacidad teórica: L1=1250, L2=850.             ║
║   Turno = 480 minutos."                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Anexo B — Plan de contingencia

| Problema | Plan B |
|----------|--------|
| La API Key no funciona | Tener una segunda key preparada. Si falla Anthropic, usar el free tier de Cursor (tiene créditos propios). |
| Internet cae | Tienes los datos en local. Pueden practicar Python sin IA y tú haces la demo desde el móvil como hotspot. |
| Alguien no tiene Cursor | Que trabaje en pareja con un compañero. Si tiene VS Code, instalar extensión de Copilot como alternativa. |
| El grupo es más lento de lo esperado | Sacrifica el bloque 5 (ejercicio libre). Extiende el bloque 4 y haz la puesta en común sobre lo que hayan llegado a hacer. |
| El grupo es más rápido de lo esperado | Adelanta el ejercicio libre y añade un reto extra: "Genera un informe PDF automático" o "Crea una CLI que reciba el CSV como argumento". |
| Alguien es muy avanzado y se aburre | Pídele que ayude a los demás. O dale un reto: "Haz que el script se ejecute como un pipeline con argparse, logging y tests." |
| Spending limit alcanzado | Cambiar a un modelo más barato (Haiku) o reducir el grupo a parejas para compartir la cuota restante. |

---

## Anexo C — Checklist post-taller

- [ ] Borrar la API Key de console.anthropic.com
- [ ] Revisar el gasto real en la consola
- [ ] Enviar email a los participantes con:
  - El CSV y los ejercicios
  - La cheat sheet de prompts
  - Links a recursos
  - Tu contacto para dudas
- [ ] Anotar qué funcionó y qué no para la siguiente edición
