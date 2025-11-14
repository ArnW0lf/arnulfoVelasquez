# Tarea para Clase 4
**Entrega:** Martes 19 de noviembre de 2025

---

## Objetivo

Integrar tu sistema de adaptación con LLM (Clase 3) con las APIs reales de **Meta** (Facebook + Instagram) y **LinkedIn** para publicar contenido automáticamente.

---

## Entregables obligatorios

### 1. Integración con Facebook ✅

**Requisitos:**
- [ ] Crear app en Meta for Developers
- [ ] Obtener Page Access Token
- [ ] Implementar endpoint: `POST /api/publish/facebook`
- [ ] Realizar **mínimo 1 publicación real** de prueba
- [ ] Guardar screenshot del post + link público

**Parámetros del endpoint:**
```json
{
  "text": "Contenido adaptado...",
  "access_token": "tu_token"
}
```

**Manejo de errores:**
- Token expirado → mensaje claro
- Permisos insuficientes → instrucciones
- Rate limit → retry automático (3 intentos)

---

### 2. Integración con Instagram ✅

**Requisitos:**
- [ ] Configurar Instagram Business Account
- [ ] Implementar Container Creation + Publish flow
- [ ] Endpoint: `POST /api/publish/instagram`
- [ ] Publicar **mínimo 1 imagen con caption**
- [ ] Screenshot + link del post

**Flow obligatorio:**
1. Crear container con imagen + caption
2. Publicar el container
3. Verificar status de publicación

---

### 3. Integración con LinkedIn ✅

**Requisitos:**
- [ ] Crear app en LinkedIn Developers
- [ ] Implementar OAuth 2.0
- [ ] Endpoint: `POST /api/publish/linkedin`
- [ ] Publicar **mínimo 1 post de prueba**
- [ ] Screenshot + link del post

---

### 4. Sistema de logging 📊

Crear archivo `logs/publications.log` (formato JSONL):

```json
{
  "timestamp": "2025-11-19T10:30:00Z",
  "network": "facebook",
  "status": "success",
  "post_id": "123456789_987654321",
  "content_preview": "Lanzamiento de nueva funcionalidad...",
  "response_time_ms": 1234,
  "error": null
}
```

En caso de error:
```json
{
  "timestamp": "2025-11-19T10:31:00Z",
  "network": "instagram",
  "status": "error",
  "error": "Token expired",
  "error_code": 190,
  "retry_count": 3
}
```

---

### 5. Documentación 📝

**Archivo:** `docs/apis-setup-guide.md`

**Debe incluir:**
- Paso a paso para crear app en Meta for Developers (con screenshots)
- Cómo obtener tokens de acceso
- Paso a paso para crear app en LinkedIn
- Variables de entorno necesarias
- Troubleshooting de errores comunes
- Links a las 3 publicaciones de prueba

**Variables en `.env.example`:**
```env
# LLM Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...

# Meta (Facebook + Instagram)
META_APP_ID=
META_APP_SECRET=
META_PAGE_ACCESS_TOKEN=
META_PAGE_ID=
META_INSTAGRAM_ACCOUNT_ID=

# LinkedIn
LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=
LINKEDIN_ACCESS_TOKEN=
```

---

### 6. Exposición (15 min) 🎤

**Prepara una presentación con:**

**Slide 1: Resumen**
- Qué APIs integraste
- Challenges principales

**Slide 2-4: Proceso por API**
Para cada API (Facebook, Instagram, LinkedIn):
- Proceso de configuración
- Flujo de autenticación
- Ejemplo de request/response
- Errores encontrados y soluciones

**Slide 5: Arquitectura**
- Diagrama de cómo se conecta todo
- LLM → Adaptación → API → Publicación

**Slide 6: Aprendizajes**
- Qué fue más difícil
- Qué aprendiste
- Qué mejorarías

**Demo en vivo:**
1. Mostrar código de un endpoint
2. Hacer 1 publicación en vivo (cualquier red)
3. Verificar en navegador que se publicó
4. Mostrar logs generados

---

## Estructura de entrega

```
lectures/clase-04/[tu-nombre]/
├── README.md
├── src/
│   ├── llm_adapter.py (de Clase 3)
│   ├── publishers/
│   │   ├── facebook_publisher.py
│   │   ├── instagram_publisher.py
│   │   └── linkedin_publisher.py
│   └── main.py (servidor API)
├── docs/
│   ├── apis-setup-guide.md
│   └── prompts.md (actualizado de Clase 3)
├── logs/
│   └── publications.log (ejemplos)
├── screenshots/
│   ├── facebook-post.png
│   ├── instagram-post.png
│   ├── linkedin-post.png
│   ├── meta-app-config.png
│   └── linkedin-app-config.png
├── presentacion.pdf
├── .env.example
└── links.md (URLs públicas de tus posts)
```

---

## Criterios de evaluación (15% de nota final)

### Exposición (40%)
- Claridad en explicación del proceso: 15%
- Profundidad técnica: 15%
- Manejo de preguntas: 10%

### Código + Demo (60%)
- **Funcionalidad (35%):**
  - Facebook funcionando: 12%
  - Instagram funcionando: 12%
  - LinkedIn funcionando: 11%
- **Calidad técnica (15%):**
  - Manejo de errores: 5%
  - Logging estructurado: 5%
  - Código limpio y modular: 5%
- **Demo en vivo (5%):**
  - Publicación exitosa en tiempo real
- **Documentación (5%):**
  - Setup guide completo con screenshots

---

## Checklist antes de entregar

### Funcionalidad
- [ ] Facebook: 1+ publicación real exitosa
- [ ] Instagram: 1+ publicación con imagen exitosa
- [ ] LinkedIn: 1+ publicación real exitosa
- [ ] Logging funcionando y guardando en archivo
- [ ] Manejo de errores implementado
- [ ] Retry automático en caso de fallo

### Código
- [ ] Repositorio actualizado en Git
- [ ] Sin API keys ni tokens en el código
- [ ] `.env.example` con todas las variables
- [ ] Código comentado y organizado
- [ ] Requirements.txt o package.json actualizado

### Documentación
- [ ] README.md con instrucciones de instalación
- [ ] Setup guide con screenshots
- [ ] Links a publicaciones reales
- [ ] Screenshots de las 3 publicaciones
- [ ] Variables de entorno documentadas

### Presentación
- [ ] Slides preparados (PDF o PPTX)
- [ ] Demo probada al menos 1 vez
- [ ] Conexión a internet verificada
- [ ] Plan B si algo falla (screenshots/video)

---

## Guía rápida de inicio

### Paso 1: Crear app en Meta for Developers

1. Ve a https://developers.facebook.com/apps
2. Click en "Crear app"
3. Selecciona "Empresa" como tipo
4. Completa información básica
5. Agrega producto "Facebook Login"
6. Configura permisos: `pages_manage_posts`, `pages_read_engagement`
7. Obtén el Page Access Token desde Graph API Explorer

### Paso 2: Configurar Instagram

1. Asegúrate de tener un Instagram Business Account
2. Vincula tu página de Facebook
3. En Graph API Explorer, busca el `instagram_business_account` de tu página
4. Guarda el ID

### Paso 3: Crear app en LinkedIn

1. Ve a https://www.linkedin.com/developers/apps
2. Click en "Create app"
3. Completa información
4. En "Auth" configura OAuth 2.0
5. Agrega permisos: `w_member_social`, `r_liteprofile`
6. Genera Access Token

### Paso 4: Prueba con cURL primero

Antes de codear, haz una prueba manual:

**Facebook:**
```bash
curl -X POST "https://graph.facebook.com/v18.0/{page-id}/feed" \
  -d "message=Test post" \
  -d "access_token={your-token}"
```

**Instagram:**
```bash
# 1. Crear container
curl -X POST "https://graph.facebook.com/v18.0/{ig-account-id}/media" \
  -d "image_url={url}" \
  -d "caption=Test caption" \
  -d "access_token={token}"

# 2. Publicar
curl -X POST "https://graph.facebook.com/v18.0/{ig-account-id}/media_publish" \
  -d "creation_id={container-id}" \
  -d "access_token={token}"
```

### Paso 5: Integra en tu código

Solo después de que funcione manualmente, intégralo en tu aplicación.

---

## Recursos útiles

### Documentación oficial
- **Meta Graph API:** https://developers.facebook.com/docs/graph-api
- **Instagram API:** https://developers.facebook.com/docs/instagram-api
- **LinkedIn Share API:** https://learn.microsoft.com/linkedin/marketing/integrations/community-management/shares/share-api

### Herramientas
- **Graph API Explorer:** https://developers.facebook.com/tools/explorer
- **Postman:** Testing de APIs
- **ngrok:** Para webhooks (si necesitas)

### Tutoriales
- OAuth 2.0: https://auth0.com/docs/get-started/authentication-and-authorization-flow
- Rate limiting: https://developers.facebook.com/docs/graph-api/overview/rate-limiting

---

## Errores comunes y soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `Invalid OAuth access token` | Token expirado o incorrecto | Regenera el token |
| `Permissions error` | Faltan permisos en la app | Agrega permisos en configuración |
| `Rate limit exceeded` | Demasiadas llamadas | Implementa retry con delay |
| `Invalid image URL` | Instagram no puede acceder a la URL | Usa URL pública HTTPS |
| `OAuthException` | Muchas causas posibles | Lee el mensaje de error detallado |

---

## Preguntas frecuentes

**P: ¿Necesito una página de Facebook real?**
R: Sí, necesitas una página donde puedas publicar. Puedes crear una página de prueba.

**P: ¿Y si no puedo conseguir tokens de LinkedIn?**
R: Documenta el intento completo. Si tienes un error bloqueante, muestra el proceso y propón alternativa.

**P: ¿Puedo usar bibliotecas de terceros?**
R: Sí (ej: `facebook-sdk`, `python-linkedin`), pero debes entender qué hacen.

**P: ¿Qué pasa si mi demo falla en vivo?**
R: Por eso debes tener screenshots y/o video de backup que demuestren que funcionó antes.

**P: ¿Cuánto cuesta usar estas APIs?**
R: Todas son gratuitas para uso de desarrollo/prueba con las limitaciones de rate limit.

---

## Consejos finales

### ✅ Empieza YA
No esperes al último día. La configuración de apps puede tomar tiempo.

### ✅ Documenta TODO
Screenshots de cada paso. Te servirá para tu exposición y para debugging.

### ✅ Prueba manual primero
Usa cURL o Postman antes de codear. Verifica que tus tokens funcionan.

### ✅ Lee los errores
Las APIs dan mensajes de error muy descriptivos. Léelos con atención.

### ✅ Versiona frecuentemente
Haz commits pequeños y frecuentes. Nunca hagas commit de tokens.

---

¡Éxito con la integración! 🚀

**Fecha de entrega:** Martes 19 de noviembre
**Formato:** Exposición en clase + código en `lectures/clase-04/[tu-nombre]/`
