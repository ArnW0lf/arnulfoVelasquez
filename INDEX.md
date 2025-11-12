# Índice de Navegación - Tópicos Avanzados LLM Applications

**Universidad Autónoma Gabriel René Moreno (UAGRM)**
**Semestre:** 2025-02
**Duración:** 7 nov - 28 nov 2025

---

## Inicio Rápido

### Para Estudiantes
1. Lee [README.md](./README.md) - Visión general del curso
2. Revisa [SYLLABUS.md](./SYLLABUS.md) - Programa completo
3. Consulta [PROYECTO-REDES-SOCIALES.md](./PROYECTO-REDES-SOCIALES.md) - Especificación del proyecto
4. Revisa [TAREAS-Y-ENTREGABLES.md](./TAREAS-Y-ENTREGABLES.md) - Qué entregar en cada clase

### Para Instructores
- [README.instructores.md](./README.instructores.md) - Guía para instructores

---

## Documentación Principal

| Documento | Descripción | Para |
|-----------|-------------|------|
| [README.md](./README.md) | Visión general del curso y quick start | Todos |
| [SYLLABUS.md](./SYLLABUS.md) | Programa académico completo | Estudiantes |
| [PROYECTO-REDES-SOCIALES.md](./PROYECTO-REDES-SOCIALES.md) | Especificación técnica del proyecto | Estudiantes |
| [TAREAS-Y-ENTREGABLES.md](./TAREAS-Y-ENTREGABLES.md) | Entregables detallados por clase | Estudiantes |
| [README.instructores.md](./README.instructores.md) | Guía para instructores | Instructores |

---

## Calendario de Clases

| Fecha | Día | Clase | Material | Estado |
|-------|-----|-------|----------|--------|
| 07 nov | Jueves | Clase 1 · Introductoria | [lectures/clase-01/](./lectures/clase-01/) | ✅ Disponible |
| 11 nov | Martes | Clase 2 · Investigación de APIs + Stack | [lectures/clase-02/](./lectures/clase-02/) | ✅ Disponible |
| 13 nov | Jueves | Clase 3 | Prototipo LLM | Próximamente |
| 18 nov | Martes | Clase 4 | APIs Meta + LinkedIn | Próximamente |
| 20 nov | Jueves | Clase 5 | TikTok + WhatsApp + Backend | Próximamente |
| 25 nov | Martes | Clase 6 | Portal Web Completo | Próximamente |
| 27 nov | Jueves | **Presentación Final** | Demo + Documentación | - |

---

## Material por Clase

### Clase 1 (06 nov) - Introductoria
**Ubicación:** [`lectures/clase-01/`](./lectures/clase-01/)

- [README.md](./lectures/clase-01/README.md) - Guía de la clase
- [SLIDES.md](./lectures/clase-01/SLIDES.md) - Presentación
- [demo-prompts.md](./lectures/clase-01/demo-prompts.md) - Ejemplos de prompts

**Temas:**
- Introducción al proyecto
- Qué son los LLMs
- APIs de redes sociales
- Roadmap del curso

---

### Clase 2 (11 nov) - Investigación de APIs
**Entregable:** Documento de investigación

**Contenido:**
- Investigación de APIs de redes sociales
- Selección de stack tecnológico
- Diseño de arquitectura

---

### Clase 3 (13 nov) - Prototipo LLM
**Ubicación:** [`lectures/clase-02/`](./lectures/clase-02/)
**Entregable:** Sistema de adaptación + Demo

- [README.md](./lectures/clase-02/README.md) - Guía de la clase
- [instructor-guide.md](./lectures/clase-02/instructor-guide.md) - Guía para instructores

**Contenido:**
- Integración con LLM (OpenAI/Claude/Ollama)
- Prompt engineering
- Sistema de adaptación de contenido
- Demo funcional

---

### Clase 4 (18 nov) - APIs Meta + LinkedIn
**Entregable:** 3 redes funcionando

**Contenido:**
- Facebook Graph API
- Instagram Graph API
- LinkedIn Share API
- Sistema de publicación automatizado

---

### Clase 5 (20 nov) - TikTok + WhatsApp + Backend
**Entregable:** Sistema end-to-end

**Contenido:**
- TikTok Content Posting API
- WhatsApp Business API (Twilio)
- Backend con colas (Celery/Bull)
- Orquestación completa

---

### Clase 6 (25 nov) - Portal Web
**Entregable:** UI + 5 redes integradas

**Contenido:**
- Frontend con React
- Dashboard de publicaciones
- Integración completa
- Testing y refinamiento

---

### Presentación Final (27 nov)
**Entregable:** Proyecto completo + Documentación

**Evaluación:**
- Demo en vivo del sistema completo
- Presentación técnica (10-20 min)
- Código en repositorio Git
- Documentación técnica

---

## Recursos Técnicos

### APIs de Redes Sociales
- [Meta Graph API](https://developers.facebook.com/docs/graph-api) - Facebook + Instagram
- [LinkedIn API](https://docs.microsoft.com/en-us/linkedin/) - LinkedIn Share API
- [TikTok API](https://developers.tiktok.com/) - Content Posting API
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [Twilio WhatsApp](https://www.twilio.com/docs/whatsapp)

### LLMs
- [OpenAI Platform](https://platform.openai.com/docs) - GPT-4, GPT-3.5
- [Anthropic Claude](https://docs.anthropic.com) - Claude Sonnet, Haiku
- [Ollama](https://ollama.ai) - Llama 3.1 local

### Herramientas de Desarrollo
- [Postman](https://www.postman.com/) - Testing de APIs
- [ngrok](https://ngrok.com/) - Webhooks locales
- [Meta Graph API Explorer](https://developers.facebook.com/tools/explorer) - Testing Meta APIs

---

## Estructura del Repositorio

```
topicos-2025-02-project-2/
├── README.md                      # Visión general del curso
├── INDEX.md                       # Este archivo - Navegación
├── SYLLABUS.md                    # Programa académico
├── PROYECTO-REDES-SOCIALES.md     # Especificación del proyecto
├── TAREAS-Y-ENTREGABLES.md        # Entregables por clase
├── README.instructores.md         # Guía para instructores
│
├── lectures/                      # Material de clases
│   ├── clase-01/                  # Clase introductoria
│   │   ├── README.md             # Guía de la clase
│   │   ├── SLIDES.md             # Presentación
│   │   └── demo-prompts.md       # Ejemplos de prompts
│   ├── clase-02/                  # Investigación de APIs
│   │   ├── README.md             # Guía de la clase
│   │   └── instructor-guide.md   # Guía para instructores
│   ├── clase-03/                  # APIs Meta + LinkedIn (próximamente)
│   ├── clase-04/                  # TikTok + WhatsApp (próximamente)
│   ├── clase-05/                  # Portal Web (próximamente)
│   └── clase-06/                  # Presentación final (próximamente)
│
└── examples/                      # Ejemplos de código
    ├── .env.example              # Template de configuración
    ├── backend-python/           # Ejemplo FastAPI (próximamente)
    └── backend-nodejs/           # Ejemplo NestJS (próximamente)
```

---

## Stack Tecnológico Sugerido

### Backend
- **Python:** FastAPI + SQLAlchemy + Celery + Redis
- **Node.js:** NestJS + Prisma + Bull + Redis

### Frontend
- React + Vite + TypeScript
- Tailwind CSS o Material-UI

### Base de Datos
- PostgreSQL (recomendado) o MongoDB

### Infraestructura
- Redis (sistema de colas)
- Docker + Docker Compose

### LLM
- OpenAI (GPT-4o-mini, GPT-3.5) - Pago con créditos gratis
- Anthropic Claude (Sonnet, Haiku) - Pago
- Ollama + Llama 3.1 - Local y gratis

---

## Requisitos Previos

### Conocimientos
- Programación en Python o JavaScript/TypeScript
- Conceptos de APIs REST
- Git básico
- Bases de datos relacionales

### Software Necesario
- Node.js >= 20 o Python >= 3.10
- PostgreSQL o MongoDB
- Redis
- Git
- VS Code (recomendado)

### Cuentas Necesarias
- GitHub o GitLab
- OpenAI API (opcional - tiene costo)
- Meta for Developers
- LinkedIn Developers
- Twilio (para WhatsApp)

---

## Navegación Rápida por Tipo de Usuario

### Soy Estudiante - ¿Por dónde empiezo?
1. [README.md](./README.md) - Lee esto primero
2. [PROYECTO-REDES-SOCIALES.md](./PROYECTO-REDES-SOCIALES.md) - Entiende qué vas a construir
3. [TAREAS-Y-ENTREGABLES.md](./TAREAS-Y-ENTREGABLES.md) - Revisa qué debes entregar
4. [lectures/clase-01/](./lectures/clase-01/) - Material de la primera clase

### Soy Instructor
1. [README.instructores.md](./README.instructores.md) - Guía del instructor
2. [SYLLABUS.md](./SYLLABUS.md) - Programa completo
3. [lectures/clase-02/instructor-guide.md](./lectures/clase-02/instructor-guide.md) - Guías por clase

### Estoy buscando recursos técnicos
- [PROYECTO-REDES-SOCIALES.md](./PROYECTO-REDES-SOCIALES.md) - Sección de APIs y stack
- [examples/](./examples/) - Código de ejemplo
- Ver sección "Recursos Técnicos" arriba

### Necesito entender la evaluación
- [TAREAS-Y-ENTREGABLES.md](./TAREAS-Y-ENTREGABLES.md) - Criterios detallados
- Ver sección "Evaluación" arriba

---

## Tips para el Éxito

1. **Empieza temprano** - No dejes todo para el último día
2. **Commitea frecuentemente** - Git es tu mejor amigo
3. **Documenta decisiones** - Explica el "por qué" de tus elecciones técnicas
4. **Prueba constantemente** - Haz demos frecuentes para detectar problemas temprano
5. **Usa .env** - NUNCA hagas commit de API keys
6. **Pide ayuda** - Usa las horas de consulta
7. **Lee documentación oficial** - Es tu mejor recurso

---

## Contacto

**Docente:** [Nombre del docente]
**Email:** [Email]
**Horario de consultas:** [Definir]

---

**Última actualización:** 7 de noviembre de 2025

---

[⬆️ Volver arriba](#índice-de-navegación---tópicos-avanzados-llm-applications)
