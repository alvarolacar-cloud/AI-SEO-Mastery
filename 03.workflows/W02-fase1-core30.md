# W02 — Fase 1: Core 30 (Mapa Rojo)

> **Cuándo usar este workflow:** el rank map del W01 muestra todo rojo — sin verde en ningún punto, ni siquiera en el centro donde está el negocio.
>
> **Diagnóstico:** Google no confía en que el negocio sea experto en lo que dice ofrecer. El GBP declara categorías y servicios pero la web no los respalda. No existe relevancia topical.
>
> **Objetivo:** construir el espejo de la ficha GBP en la web — una URL dedicada para cada categoría y cada servicio.
>
> **Duración estimada:** 60-90 días para ver impacto en el rank map. Los dominios nuevos (<3 meses) tardan más.

---

## Resumen del flujo

```
Rank map rojo (viene de W01)
      ↓
[FASE A]  Mapear las páginas a crear
      ↓
[FASE B]  Construir la web (estructura + contenido + schema)
      ↓
[FASE C]  Conseguir enlaces externos (1 por URL)
      ↓
[FASE D]  Medir → decidir si continuar en Fase 1, pasar a Fase 2 o Fase 3
```

---

## FASE A — Mapear las páginas antes de crear ninguna

### A1. Extraer categorías y servicios del GBP

1. Abre el GBP del cliente en Leadsnap
2. Lista todas las categorías activas (1 principal + hasta 5 secundarias)
3. Lista todos los servicios activos (mínimo 20)
4. Si aún no están validados por el cliente, hazlo ahora — nunca crees páginas de servicios que el negocio no presta

### A2. Construir la jerarquía de páginas

```
Home / GBP Landing Page          → keyword: [Categoría Principal] + [Ciudad]
├── Categoría 1                  → keyword: [Categoría Secundaria 1] + [Ciudad]
│   ├── Servicio 1.1             → keyword: [Servicio] + [Ciudad]
│   ├── Servicio 1.2
│   └── Servicio 1.3
├── Categoría 2
│   ├── Servicio 2.1
│   └── ...
├── About
└── Contact
```

### A3. Asignar URLs limpias a cada página

| Tipo | Formato de URL |
|---|---|
| Home | `dominio.com` |
| Categoría | `dominio.com/categoria/` |
| Servicio | `dominio.com/servicio/` o `dominio.com/categoria/servicio/` |
| Hub localizaciones | `dominio.com/zonas/` |
| About | `dominio.com/about/` |
| Contact | `dominio.com/contact/` |

> **Regla:** preferir estructura plana. Evitar `/category/subcategory/service/city` — demasiado anidado.

Documenta el esqueleto completo en una hoja antes de crear nada. Este mapa es tu referencia durante todo el engagement.

---

## FASE B — Construir la web

### Opción 1: Sitio nuevo con Lovable

Si el cliente no tiene web o la actual no sirve (no rankea nada, mal estructurada), construir desde cero en Lovable usando la secuencia de 9 prompts. Usar **lovablehtml.com** para output HTML limpio.

**Secuencia de prompts:**

| Prompt | Qué produce |
|---|---|
| **Prompt 0 — Planificación** | Arquitectura completa: URLs, jerarquía, mapa de enlaces internos, navegación |
| **Prompt 1 — Esqueleto** | Estructura visual del sitio, diseño, rutas — SIN contenido real todavía |
| **Prompt 2 — Contenido GBP Landing Page** | Copy de conversión de la home usando el framework goal-completion |
| **Prompt 3 — Build GBP Landing Page** | Implementación visual de la home (Zehl framework: prueba antes que promesas) |
| **Prompt 4 — Páginas de Categoría** | Una página por cada categoría secundaria (1.000-1.200 palabras) |
| **Prompt 5 — Páginas de Servicio Core** | Páginas de los servicios principales (enfoque urgencia/solución) |
| **Prompt 6 — Hub + Servicios Hijo** | Página /services + páginas de servicios individuales (600-800 palabras) |
| **Prompt 7 — About + Contact** | About con E-E-A-T real (foto, bio, credenciales) + Contact con NAP exacto al GBP |
| **Prompt 8 — SEO Técnico** | robots.txt, sitemap.xml, meta tags, validación schema |

> Sitio de referencia: https://ai-seo-pro-gary.lovable.app/plumber-gary-in

### Opción 2: Web existente — añadir páginas que faltan

Si el cliente ya tiene web y rankea algo (aunque sea poco), **no migres de plataforma**. Añade las páginas que faltan según el gap analysis del W01.

**Orden de creación:**
1. GBP Landing Page / Home (si necesita mejoras)
2. Páginas de Categoría
3. Páginas de Servicio
4. About + Contact

### Mínimos por tipo de página

| Tipo | Extensión | Elementos obligatorios |
|---|---|---|
| GBP Landing Page | 800-1.200 palabras | H1 con keyword + ciudad, USPs concretos, reviews embed, links a categorías, CTA, Schema Local Business |
| Categoría | 1.500-2.500 palabras | H1, descripción, links a todos los servicios hijos, FAQs, CTA |
| Servicio | 1.000-2.000 palabras | H1, qué es, proceso, beneficios, cuándo necesitarlo, FAQs, CTA |
| About | 600-1.000 palabras | Foto real (no stock), bio verificable, credenciales, links a RRSS activos |
| Contact | 300-500 palabras | NAP exacto al GBP, mapa embed, formulario, horarios |

### Reglas de arquitectura interna

- La home NO enlaza a más de 7 páginas directamente
- Los enlaces deben estar **dentro del contenido** (body), no solo en menú o footer
- Cada página de servicio enlaza de vuelta a su categoría madre
- Ninguna página puede quedar huérfana (sin enlace interno apuntando a ella)
- Los anchor links (#sección) no cuentan — el GBP necesita URLs reales, no anclas

---

## FASE B2 — Schema

Implementar en el mismo momento en que se publica cada página.

| Schema | Dónde va |
|---|---|
| **Organización** | Header de TODAS las URLs del dominio (via Rank Math o Yoast) |
| **Local Business** | SOLO en la GBP Landing Page — datos idénticos al GBP |
| **Breadcrumb** | Todas las páginas con jerarquía (categorías, servicios, artículos) |
| **FAQ** | Todas las páginas con sección de preguntas frecuentes |
| **Servicio** | Páginas de categoría y servicio |
| **Artículo** | Artículos de soporte y landmarks (solo en Fase 2 y 3) |

**Cómo generar el Schema de Local Business:**

Los datos del schema deben coincidir EXACTAMENTE con el GBP:
- Nombre, tipo de negocio, descripción, dirección, teléfono, email, URL
- Coordenadas GPS (clic derecho en Google Maps → copiar lat/long)
- Horarios, área de servicio, perfiles de redes sociales, logo URL

Prompt en Claude o ChatGPT:
1. *"What information do you need to create local business schema?"*
2. (Dar los datos) → *"With this data, please write local business schema."*

Validar siempre en la herramienta de prueba de datos estructurados de Google antes de publicar.

---

## FASE C — Conseguir enlaces externos

**Regla absoluta:** cada URL que publiques necesita mínimo 1 enlace externo. Sin enlace, la página existe pero Google no la valida.

### Tipo 1 — PBNs (validación, una vez por URL)

- 1 PBN por cada URL nueva publicada
- No necesitan ser relevantes al nicho — son solo señal de indexación
- Anchor text: branded o genérico ("haz clic aquí", "más información")
- Baratos, se usan en volumen

### Tipo 2 — Autoridad local (2-4 por engagement)

Fuentes con impacto real en la confianza del dominio:
- Cámara de Comercio local
- Sponsorship de equipo deportivo juvenil local
- Sponsorship de festival o evento local
- ONG o asociación local

**Proceso:** el negocio hace una donación o patrocinio → la organización publica una página con enlace al sitio. Coste habitual: unos pocos cientos de euros/dólares. El enlace suele ser permanente.

### Distribución de anchor text externo — fórmula 30-20-30-5-15

| Tipo | % | Ejemplo |
|---|---|---|
| Branded | 30% | Nombre del negocio |
| Genérico | 20% | "haz clic aquí", "más información" |
| Partial match | 30% | "fontanero de confianza en Madrid" |
| Exact match | 5% | "fontanero Madrid" — máximo 2-3 instancias totales |
| Variaciones | 15% | Sinónimos sin keyword exacta |

Lleva un registro de los anchor texts ya usados. Nunca repetir el mismo anchor text en múltiples enlaces.

### Diversificación trimestral

Cada 3-4 meses añadir:
- Press release en PR Underground ($75) — genera mención en Google News
- Señales sociales
- Blog commenting (IceCreamTruck.shop o búsqueda manual)

---

## FASE D — Medir y decidir

**Cuándo medir:** a partir del mes 2-3. Los sitios nuevos necesitan mínimo 3-6 meses para rankear.

**Cómo leer el rank map:**

| El mapa muestra | Diagnóstico | Acción |
|---|---|---|
| Sigue todo rojo (sin mejora) | El Core 30 no fue suficiente — falta autoridad temática profunda | → Continuar Fase 1 + preparar **W04 Fase 2 PAA** |
| Verde en el centro, rojo en bordes | La relevancia topical está construida, el problema es geográfico | → Pasar a **W03 Fase 3 Landmarks** |
| Mayormente verde | El sistema ha funcionado | → Pasar a **W05 Mantenimiento** |

> **Regla del 50%:** cuando el 50% o más del mapa está verde, considera pasar a expansión geográfica (Fase 3). Mientras tanto, sigue construyendo autoridad topical.

> **Zonas a priorizar:** puntos en posición 15-18 son los que más responden a contenido adicional. Las zonas con 20+ rara vez se mueven con una sola página nueva.

---

## Checklist de control — antes de dar el mes por cerrado

- [ ] ¿Todas las URLs del Core 30 están publicadas?
- [ ] ¿Cada URL tiene su enlace externo (PBN)?
- [ ] ¿El Schema de Local Business está en la GBP Landing Page y coincide con el GBP?
- [ ] ¿El Schema de Organización está en todas las páginas?
- [ ] ¿No hay páginas huérfanas? (verificar con Screaming Frog)
- [ ] ¿El anchor del GBP en Leadsnap apunta a la URL correcta?
- [ ] ¿Posts semanales activos en el GBP?
- [ ] ¿Reseñas respondidas en menos de 72h?
- [ ] ¿Rank map programado cada 2 semanas?
