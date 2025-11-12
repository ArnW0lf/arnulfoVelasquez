# TAREAS Y ENTREGABLES POR CLASE
## Sistema Multi-Red Social con LLM

---

## ESTRUCTURA GENERAL

### Cada clase tiene 2 componentes obligatorios:

#### 1️⃣ EXPOSICIÓN (40% de la nota de clase)
- Duración: 10-20 minutos
- Presentar conceptos investigados
- Mostrar decisiones técnicas
- Explicar challenges y soluciones
- Slides o presentación visual

#### 2️⃣ CÓDIGO + DEMO (60% de la nota de clase)
- Repositorio Git actualizado
- Código funcional del componente de la clase
- Demo en vivo funcionando
- README documentado
- Sin API keys en el código

---

## CLASE 1 - Martes 11 nov
### Tema: Investigación de APIs y Selección de Stack

### EXPOSICIÓN (40%)
**Duración:** 15 minutos

**Contenido a presentar:**
1. Comparativa de APIs investigadas
2. Decisión de stack tecnológico (justificada)
3. Arquitectura propuesta del sistema
4. Plan de implementación

**Formato:**
- Slides o presentación visual
- Tablas comparativas
- Diagramas de arquitectura

### CÓDIGO/INVESTIGACIÓN (60%)

**Entregable:** Documento de investigación (PDF o Markdown)

**Parte 1: Investigación de APIs (40%)**

Documentar para cada API:

**Meta Business API (Facebook + Instagram):**
- Proceso de creación de app de desarrollador
- Permisos necesarios (pages_manage_posts, instagram_basic, etc.)
- Rate limits (ej: 200 llamadas/hora)
- Proceso de autenticación OAuth 2.0
- Screenshots de la app creada
- Link a documentación relevante

**LinkedIn Share API:**
- Requisitos de acceso
- Proceso de autenticación
- Limitaciones de publicación
- Formatos soportados

**TikTok Content Posting API:**
- ¿Es accesible para desarrollo académico?
- ¿Requiere verificación de negocio?
- Si no es viable, ¿cuál es el plan B?
- Alternativas consideradas

**WhatsApp Business API:**
- Comparativa Twilio vs Meta
- Costos (si aplica)
- Proceso de setup
- Limitaciones del sandbox

**Parte 2: Características de Redes Sociales (30%)**

Tabla detallada que incluya:

| Red | Max Chars | Tono | Hashtags | Emojis | Formato Especial | Mejores Prácticas |
|-----|-----------|------|----------|--------|------------------|-------------------|
| Facebook | ... | ... | ... | ... | ... | ... |
| Instagram | ... | ... | ... | ... | ... | ... |
| LinkedIn | ... | ... | ... | ... | ... | ... |
| TikTok | ... | ... | ... | ... | ... | ... |
| WhatsApp | ... | ... | ... | ... | ... | ... |

**Parte 3: Selección de LLM (20%)**

Comparativa de modelos:
- OpenAI (GPT-4o-mini, GPT-3.5-turbo)
- Anthropic (Claude Sonnet, Haiku)
- Ollama (Llama 3.1, Mistral)

Para cada uno incluir:
- Costo por 1M tokens
- Latencia aproximada
- Calidad de respuestas
- Facilidad de acceso
- **Decisión final justificada**

**Parte 4: Propuesta de Arquitectura (10%)**

- Diagrama de arquitectura del sistema completo
- Stack tecnológico elegido (Backend, Frontend, BD, etc.)
- Diseño preliminar de base de datos (schema)
- Justificación de elecciones

**Formato de entrega:**
- Documento PDF o Markdown de 5-10 páginas
- Incluir fuentes y referencias
- Capturas de pantalla donde aplique
- Subir a repositorio Git

**Repositorio Git:**
- Crear repositorio del proyecto
- README inicial con descripción
- Documento de investigación en `/docs/clase-01-investigacion.md`

---

## CLASE 2 - Jueves 13 nov
### Tema: Prototipo de Adaptación con LLM

### EXPOSICIÓN (40%)
**Duración:** 15 minutos

**Contenido a presentar:**
1. LLM seleccionado y configuración
2. Estrategia de prompting para cada red
3. Ejemplos de transformaciones
4. Challenges encontrados y soluciones

### CÓDIGO + DEMO (60%)

**Entregable 1: Sistema de Adaptación Funcionando**

**Requisitos técnicos:**

Sistema que exponga API o módulo con:

**Input:**
```json
{
  "titulo": "Nueva funcionalidad en nuestra plataforma",
  "contenido": "Hoy lanzamos una nueva característica que permite...",
  "target_networks": ["facebook", "instagram", "linkedin", "tiktok", "whatsapp"]
}
```

**Output:**
```json
{
  "facebook": {
    "text": "🎉 Gran noticia...",
    "hashtags": ["#Innovación", "#Tecnología"],
    "character_count": 245,
    "tone": "casual"
  },
  "instagram": {
    "text": "✨ Nueva función...",
    "hashtags": ["#Tech", "#Innovation", "#NewFeature"],
    "character_count": 180,
    "suggested_image_prompt": "Modern tech interface..."
  },
  // ... resto de redes
}
```

**Entregable 2: Diseño de Prompts**

Documentar en `/docs/prompts.md`:
- Prompt system para cada red social
- Estrategia de few-shot examples (si aplica)
- Variables de temperatura y otros parámetros
- Iteraciones realizadas y mejoras

**Entregable 3: Demo Funcional**

**Casos de prueba (mínimo 3):**
1. Noticia formal/corporativa
2. Noticia de producto/servicio
3. Anuncio de evento

**DEMO EN VIVO:**
- Mostrar sistema funcionando
- Input → LLM → Output para las 5 redes
- Explicar diferencias en adaptaciones
- Mostrar validaciones (character count, etc.)

**Código debe incluir:**
- Manejo de errores del LLM
- Validación de límites de caracteres
- Logging básico
- Tests unitarios (opcional pero recomendado)

**Repositorio Git:**
```
/src
  /services
    llm_adapter.py (o .ts)
/docs
  prompts.md
  clase-02-desarrollo.md
/tests (opcional)
README.md actualizado
.env.example
```

---

## CLASE 3 - Martes 18 nov
### Tema: Integración con APIs (Meta + LinkedIn)

### EXPOSICIÓN (40%)
**Duración:** 15 minutos

**Contenido a presentar:**
1. Proceso de integración con cada API
2. Challenges de autenticación
3. Manejo de rate limits y errores
4. Screenshots de publicaciones de prueba

### CÓDIGO + DEMO (60%)

**Entregable 1: Integración con Meta (Facebook + Instagram)**

**Facebook:**
- App de Meta creada y configurada (screenshot)
- OAuth 2.0 implementado
- Endpoint funcional:
  ```
  POST /api/publish/facebook
  {
    "text": "Contenido...",
    "image_url": "https://..." (opcional),
    "access_token": "..."
  }
  ```
- Mínimo 1 publicación de prueba exitosa (screenshot con link)
- Manejo de errores (token expirado, permisos, etc.)

**Instagram:**
- Container creation + publish flow
- Publicación de imagen + caption
- Mínimo 1 publicación de prueba exitosa (screenshot)

**Entregable 2: Integración con LinkedIn**

- Autenticación OAuth 2.0
- Share API implementada
- Endpoint funcional:
  ```
  POST /api/publish/linkedin
  {
    "text": "Contenido...",
    "access_token": "..."
  }
  ```
- Mínimo 1 publicación de prueba exitosa (screenshot)

**Entregable 3: Sistema de Logging y Manejo de Errores**

En `/logs/publications.log` (JSONL):
```json
{
  "timestamp": "2025-11-19T10:30:00Z",
  "network": "facebook",
  "status": "success",
  "post_id": "123456789",
  "response_time_ms": 1234
}
```

**Código debe incluir:**
- Validaciones antes de publicar
- Reintentos automáticos (3 intentos)
- Manejo de rate limiting
- Logs estructurados

**Documentación:**
- Guía de setup de apps de desarrollador
- Variables de entorno necesarias
- Troubleshooting de errores comunes
- Screenshots del proceso

**DEMO EN VIVO:**
- Publicar en Facebook en tiempo real
- Publicar en Instagram en tiempo real
- Publicar en LinkedIn en tiempo real
- Mostrar posts publicados en cada plataforma

**Repositorio Git:**
```
/src
  /services
    llm_adapter.py
    facebook_publisher.py
    instagram_publisher.py
    linkedin_publisher.py
/logs
  .gitkeep
/docs
  apis-setup-guide.md
  clase-03-integracion.md
.env.example (con todas las variables)
```

---

## CLASE 4 - Jueves 20 nov
### Tema: Integración Completa (TikTok + WhatsApp + Backend)

### EXPOSICIÓN (40%)
**Duración:** 20 minutos

**Contenido a presentar:**
1. Integración TikTok (o plan alternativo)
2. Integración WhatsApp
3. Arquitectura del backend
4. Sistema de colas
5. Flujo end-to-end

### CÓDIGO + DEMO (60%)

**Entregable 1: Integración TikTok**

**Opción A (ideal):**
- Video + caption posting funcionando
- Mínimo 1 publicación de prueba

**Opción B (mínimo aceptable):**
- Generación automática de caption optimizado
- Documentación de limitaciones encontradas
- Plan de cómo se subiría el video

**Entregable 2: Integración WhatsApp**

**Usando Twilio (recomendado):**
- Sandbox configurado
- Envío de mensajes funcionando
- Formateo apropiado (saltos de línea, emojis)
- Mínimo 3 mensajes de prueba (screenshots)

**Entregable 3: Backend Central**


**API REST implementada:**

```
POST   /api/posts              - Crear nuevo post
GET    /api/posts              - Listar posts
GET    /api/posts/:id          - Ver detalles
POST   /api/posts/:id/adapt    - Adaptar contenido (LLM)
POST   /api/posts/:id/publish  - Publicar en redes
GET    /api/posts/:id/status   - Ver estado publicaciones
```

**DEMO EN VIVO:**

**Flujo completo:**
1. Crear post vía API
2. Adaptar contenido con LLM
3. Ver preview de adaptaciones
4. Publicar en las 5 redes
5. Verificar en dashboard de estados

**Código debe incluir:**
- Migrations de base de datos
- Seeds/fixtures de ejemplo
- API REST completa
- Sistema de colas funcionando
- Tests de integración (opcional)

**Repositorio Git:**
```
/src
  /api
    /routes
    /controllers
    /services
  /database
    /migrations
    /models
  /queue
/docs
  api-documentation.md
  database-schema.md
  clase-04-backend.md
docker-compose.yml
```

---

## CLASE 5 - Martes 25 nov
### Tema: Portal Web y Sistema Completo

### EXPOSICIÓN (40%)
**Duración:** 20 minutos

**Contenido a presentar:**
1. Diseño del portal web
2. Features implementados
3. Sistema completo funcionando
4. Preparación para demo final

### CÓDIGO + DEMO (60%)

**Entregable 1: Portal Web Funcionando**

**Página 1: Crear Publicación**

Componentes:
- Input de título (texto)
- Textarea de contenido (max 5000 chars)
- Checkboxes para seleccionar redes
- Botón "Generar Preview"
- Botón "Publicar"

**Página 2: Preview de Adaptaciones**

Mostrar para cada red seleccionada:
- Texto adaptado
- Character count
- Hashtags
- Emojis
- Botón "Editar" (opcional)
- Botón "Confirmar y Publicar"

**Página 3: Dashboard**

Tabla con:
- Lista de publicaciones recientes
- Estado por red (✅ exitoso, ⏳ pendiente, ❌ fallido)
- Fecha de publicación
- Links a publicaciones
- Filtros (por estado, por red, por fecha)

**Tecnologías sugeridas:**
- React + Vite
- Tailwind CSS o Material-UI
- React Query o SWR
- Axios

**Entregable 2: Las 5 Redes Funcionando**

Verificar que TODAS las redes publican correctamente:
- ✅ Facebook
- ✅ Instagram
- ✅ LinkedIn
- ✅ WhatsApp
- ✅ TikTok (mínimo caption)

**Entregable 3: Documentación Completa**

**README.md:**
- Descripción del proyecto
- Arquitectura (diagrama actualizado)
- Tecnologías utilizadas
- Setup instructions detalladas
- Variables de entorno
- Cómo ejecutar el proyecto
- Troubleshooting

**API Documentation:**
- Endpoints disponibles
- Request/Response examples
- Códigos de error
- Rate limiting

**Entregable 4: Video Demo**

Video de 2-3 minutos mostrando:
1. Interfaz del portal
2. Creación de una publicación
3. Preview de adaptaciones
4. Publicación exitosa
5. Verificación en las 5 redes

**DEMO EN VIVO:**

**Escenario completo:**
1. Abrir portal web
2. Crear nueva publicación
3. Generar preview
4. Publicar en las 5 redes
5. Ver dashboard actualizado
6. Verificar publicaciones en cada plataforma

**Repositorio Git:**
```
/backend
  (todo el código del backend)
/frontend
  /src
    /components
    /pages
    /services
  package.json
/docs
  README.md
  ARCHITECTURE.md
  API.md
  SETUP.md
  video-demo.md (con link)
docker-compose.yml
.gitignore
```

---

## CLASE 6 - Jueves 27 nov
### PRESENTACIÓN FINAL

### PRESENTACIÓN (40% de nota final)
**Duración total:** 60 minutos

**Estructura obligatoria:**

**Parte 1: Presentación Técnica**

1. **Introducción**
   - Problema que resuelve
   - Objetivos del proyecto

2. **Arquitectura y Tecnologías**
   - Diagrama de arquitectura completo
   - Stack tecnológico y justificación
   - Componentes principales

3. **Componente LLM**
   - Modelo utilizado
   - Estrategia de prompts
   - Ejemplo de adaptación
   - Challenges y soluciones

4. **Integraciones con APIs**
   - Proceso por plataforma
   - Challenges específicos
   - Rate limits y errores
   - Autenticación

5. **Backend y Orquestación**
   - Base de datos
   - Sistema de colas
   - API REST

**Parte 2: Demo en VIVO**

**Escenario:** Publicar noticia real en las 5 redes

1. **Ingresar contenido**
   - Mostrar interfaz
   - Llenar formulario
   - Seleccionar redes

2. **Generar adaptaciones**
   - Click en generar
   - Mostrar adaptaciones
   - Explicar diferencias
   - Validaciones

3. **Publicar**
   - Confirmar publicación
   - Ver logs en tiempo real

4. **Verificar publicaciones**
   - Facebook: mostrar post
   - Instagram: mostrar post
   - LinkedIn: mostrar post
   - WhatsApp: mostrar mensaje
   - TikTok: mostrar caption

5. **Dashboard**
   - Ver historial
   - Estados

**Parte 3: Challenges y Aprendizajes**
- Retos técnicos principales
- Soluciones implementadas
- Lecciones aprendidas
- Mejoras futuras

**Parte 4: Q&A**

### CÓDIGO FINAL (20% de nota final)

**Entregable:** Sistema completo funcionando

**Checklist obligatorio:**

**Funcionalidad:**
- [ ] Portal web funcionando
- [ ] Creación de posts
- [ ] Adaptación con LLM para 5 redes
- [ ] Publicación en Facebook
- [ ] Publicación en Instagram
- [ ] Publicación en LinkedIn
- [ ] TikTok (mínimo caption)
- [ ] WhatsApp funcionando
- [ ] Dashboard con historial
- [ ] Manejo de errores robusto

**Código:**
- [ ] Repositorio Git completo
- [ ] Sin credenciales en código
- [ ] .env.example con todas las variables
- [ ] Código comentado
- [ ] Arquitectura clara

**Documentación (5% de nota final):**
- [ ] README.md completo
- [ ] ARCHITECTURE.md con diagramas
- [ ] API.md con endpoints
- [ ] SETUP.md paso a paso
- [ ] Video demo 2-3 min
- [ ] Screenshots de publicaciones

**Formato de entrega:**
- Link a repositorio Git
- Link a video demo
- Slides de presentación (PDF)

---

## RESUMEN DE EVALUACIÓN

### Distribución de Notas

---

## TIPS IMPORTANTES

### Para las Exposiciones
✅ Prepara slides visuales (diagramas, tablas, screenshots)
✅ Practica el timing (no te pases del tiempo)
✅ Anticipa preguntas técnicas
✅ Ten ejemplos concretos listos

### Para el Código
✅ Commitea frecuentemente con mensajes descriptivos
✅ NUNCA hagas commit de API keys
✅ Usa .env para configuración
✅ Documenta decisiones importantes en código
✅ README claro con instrucciones de setup

### Para las Demos
✅ Prueba TODO antes de presentar
✅ Ten plan B si algo falla (screenshots)
✅ Asegura buena conexión a internet
✅ Prepara datos de prueba limpios
✅ Muestra los logs en tiempo real

### Para la Presentación Final
✅ Ensaya el flujo completo varias veces
✅ Ten backup de todo (video, screenshots)
✅ Verifica que todas las credenciales funcionan
✅ Prepara respuestas a preguntas difíciles
✅ Controla el tiempo estrictamente

---

## PREGUNTAS FRECUENTES

**P: ¿Qué pasa si no puedo acceder a alguna API?**
R: Documenta el intento, explica las razones y propón alternativa. No penaliza si está bien documentado.

**P: ¿Puedo usar librerías/frameworks adicionales?**
R: Sí, pero justifica su uso y documenta la instalación.

**P: ¿Qué pasa si la demo en vivo falla?**
R: Por eso debes tener screenshots/video de backup. Muestra el backup y explica qué pasó.

**P: ¿Cuánto código es necesario?**
R: Lo suficiente para cumplir los requisitos. Calidad > Cantidad.

**P: ¿Debo usar Docker?**
R: No es obligatorio, pero facilita el setup. Es un plus.

**P: ¿Tests unitarios son obligatorios?**
R: No obligatorios, pero son un plus y demuestran calidad.

---

¡Éxito con el proyecto! 🚀
