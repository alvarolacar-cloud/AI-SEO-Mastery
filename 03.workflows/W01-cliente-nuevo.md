# W01 — Cliente Nuevo

> **Cuándo usar este workflow:** acaba de firmar un cliente nuevo. No importa si tiene GBP, web, rankings o no — este es siempre el punto de partida.
>
> **Resultado:** al terminar tienes el rank map en mano y sabes exactamente a qué workflow ir.
>
> **Duración estimada:** 10-14 días

---

## Resumen del flujo

```
Firma del cliente
      ↓
[DÍA 1]     Solicitar accesos + configurar rank map (línea base)
      ↓
[DÍA 1-3]   Auditoría del GBP
      ↓
[DÍA 4-7]   Auditoría de la landing page
      ↓
[DÍA 7-10]  Content gap analysis
      ↓
[DÍA 10+]   Leer el rank map → decidir siguiente paso
```

---

## PASO 1 — Solicitar accesos (Día 1)

Enviar este script en vídeo o mensaje al cliente:

> *"Hello, to get started with your SEO campaign, I need access to three things: your Google Business Profile as a Manager, your WordPress website as an Editor, and your Google Search Console with Full permissions. I'll send you step-by-step instructions for each platform along with my agency email address. Once you've added me to all three, just let me know and we can begin improving your search rankings."*

**Los tres accesos necesarios:**

| Plataforma | Rol requerido |
|---|---|
| Google Business Profile | Manager |
| WordPress (o CMS equivalente) | Editor |
| Google Search Console | Full |

> Usar siempre email profesional de agencia, nunca Gmail personal.

No empieces a trabajar hasta tener los tres accesos confirmados.

---

## PASO 2 — Configurar el rank map en Leadsnap (Día 1)

Hacer esto el primer día — necesitas la línea base antes de tocar nada.

1. Entra en Leadsnap y busca el negocio por nombre o dirección
2. Introduce la keyword objetivo: **categoría principal + ciudad** (ej. "Fontanero Madrid")
3. Calibra el tamaño del mapa mirando el Top 3% del competidor #1:
   - Competidor #1 tiene **100% Top 3** → mapa demasiado pequeño, amplíalo
   - Competidor #1 tiene **32% o menos** → mapa demasiado grande, reduce la distancia entre puntos
   - **Objetivo:** el competidor #1 se ve fuerte en el centro pero cae fuera del top 3 en los bordes
4. Activa recurrencia: **cada dos semanas** (no más frecuente — no aporta información adicional útil)
5. Guarda el scan. Este es el punto de referencia de todo el engagement

> **Regla del nombre de ciudad:** una keyword CON el nombre de ciudad produce un mapa más favorable para un negocio ubicado allí. Lanza primero con ciudad.

> **Solo ejecutar rank maps para la categoría primaria + 2-3 servicios críticos.** No para todos los keywords posibles — genera ruido.

> **Ejecutar siempre en horario comercial.** Los scans fuera de horario dan datos inexactos.

---

## PASO 3 — Auditoría del GBP (Días 1-3)

Primer entregable al cliente. Revisa el GBP completo antes de tocar nada.

**Checklist de auditoría:**

- [ ] Categoría principal — ¿es la correcta? ¿coincide con la keyword objetivo?
- [ ] Categorías secundarias — ¿están configuradas? ¿máximo 5?
- [ ] Servicios — ¿hay al menos 20? ¿el cliente los ha validado?
- [ ] Descripción — ¿tiene 750 caracteres? ¿incluye categoría principal + ciudad + USP?
- [ ] Fotos — ¿están geoetiquetadas? ¿hay variedad (exterior, interior, equipo, trabajos)?
- [ ] Posts — ¿están activos? ¿recurrencia configurada en Leadsnap?
- [ ] Horarios — ¿correctos? ¿horarios especiales actualizados?
- [ ] Reseñas — ¿se están respondiendo? ¿hay respuestas pendientes de más de 72h?
- [ ] Perfiles de redes sociales — ¿están enlazados en el GBP?
- [ ] Llamadas automatizadas — ¿están desactivadas? (pueden causar suspensión)
- [ ] Áreas de servicio — ¿si es storefront, están desactivadas? (contradicción para Google)
- [ ] GBP verificado — ¿está activo y visible en Maps?

**Herramienta útil:** GMB Everywhere → Category Finder para identificar categorías adicionales disponibles.

Organiza categorías y servicios propuestos con IA y pide validación al cliente antes de publicar.

> **Referencia:** Bloque 3 → GBP → Elementos del sistema principal

---

## PASO 4 — Auditoría de la landing page (Días 4-7)

Segundo entregable al cliente. Revisa la página a la que apunta el GBP.

**Checklist de auditoría:**

- [ ] NAP exacto (Nombre, Dirección, Teléfono) — ¿coincide al 100% con el GBP?
- [ ] Schema de Local Business — ¿está implementado?
- [ ] H1 — ¿incluye keyword principal + ciudad?
- [ ] Above the fold — ¿habla al buscador (qué puede hacer por él) o habla del negocio?
- [ ] Embed de reseñas — ¿visible sin hacer scroll?
- [ ] Click-to-call — ¿operativo en móvil?
- [ ] Velocidad de carga — ¿pasa Core Web Vitals?
- [ ] Enlace del GBP — ¿apunta exactamente a esta URL?

> **Regla crítica:** si la landing page ya tiene rankings en algún punto del mapa (posición mejor que 20), **no cambies la URL**. Entrega recomendaciones de mejora del contenido existente, no una reescritura completa.

> **Referencia:** Bloque 3 → WEB → Elementos del sistema principal

---

## PASO 5 — Content gap analysis (Días 7-10)

Identifica exactamente qué páginas del Core 30 faltan. Usar **ChatGPT o1**, no Claude — maneja mejor los CSV grandes.

**Preparación:**
1. Extrae el contenido de la home del cliente (copiar texto)
2. Corre Screaming Frog y exporta: `internal_all.csv` y `links_all.csv`
3. Ten a mano la lista de categorías y servicios del GBP (ya validados en el Paso 3)

**Prompt para ChatGPT o1:**

> *"1. Data Inputs*
> *Screaming Frog Files: links_all.csv / internal_all.csv*
> *Homepage Content: [Paste the homepage copy here]*
> *GBP Categories (primary + secondary): Primary: [ej. Plumber] / Secondary: [ej. Drainage Service, Gas Installation Service]*
> *Services: [List each service]*
> *City Name: [e.g., Anytown]*
>
> *2. Analysis Goals*
> *For each secondary GBP category, confirm there is a dedicated URL whose title tag and H1 includes the keyword phrase in format "GBP Category" + "City Name".*
> *Check that the homepage: mentions each secondary category in the copy, and has an internal link to each secondary category page.*
> *For each service, ensure there is a dedicated URL whose title tag exactly includes "Service City Name".*
> *Assign each service to the most relevant GBP secondary category and make sure there is a link from that category page to the specific service page.*
>
> *3. What to Output*
> *List of missing pages or title tag gaps. Identify if the homepage is missing mentions or internal links to secondary categories. Show services without dedicated page or required title tag. Highlight category pages missing links to service pages. Summarize all gaps in a clear bulleted list."*

> Si ChatGPT dice que no puede leer los CSV, responder: *"I gave you the CSV files necessary. Please use them in the analysis."* — Es normal y casi siempre necesario.

**Resultado:** lista de páginas que faltan → esto define el volumen de trabajo del engagement.

---

## PASO 6 — Leer el rank map y decidir (Día 10+)

Con la línea base del rank map ya disponible, aplica la tabla de decisiones:

| El mapa muestra... | Diagnóstico | Siguiente workflow |
|---|---|---|
| Mayormente rojo — sin verde en ningún punto | Falta de relevancia topical. Google no confía en la autoridad del negocio | → **W02 Fase 1 — Core 30** |
| Verde en el centro, rojo en los bordes (huevo frito) | Problema de proximidad, no de autoridad. El negocio ya es relevante | → **W03 Fase 3 — Landmarks** |
| Rojo persistente después de haber completado el Core 30 | Falta autoridad temática profunda | → **W04 Fase 2 — PAA** |
| Mayormente verde | El sistema está funcionando | → **W05 Mantenimiento** |

> **Nota para dominios nuevos:** los sitios con menos de 3 meses de antigüedad rara vez rankean. No interpretar el mapa rojo como fracaso en las primeras semanas — es normal.

---

## Configurar el tracking desde el primer día

Crea la hoja del cliente en la hoja de tracking con:
- Nombre del cliente y ciudad
- Artículos por mes acordados (el primer mes suele ser menor — incluye el trabajo de auditoría)
- Links a: Google Drive del cliente, cuestionario GBP, rank map en Leadsnap
- Accesos recibidos: GBP ✓ / WordPress ✓ / GSC ✓

> **Referencia:** Bloque 4 → Tracking y Entregables del sistema principal
