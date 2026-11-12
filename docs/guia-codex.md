---
title: "Instala Mister WhatsApp en Codex"
---

# Instala Mister WhatsApp en Codex

Construye un agente de atención por WhatsApp a partir de los datos de tu negocio. Esta edición está preparada para Codex y conserva el conocimiento técnico completo del kit. Distribución 1.0.0.

<section class="provider-recommendation" aria-label="Proveedor recomendado">
<h2>Proveedor recomendado para empezar: Zernio</h2>
<p>Recomendamos Zernio si estás empezando: reúne la conexión con WhatsApp Business, el inbox y la configuración de webhooks. Si ya tienes una integración propia en Meta Cloud API, puedes seguir ese camino. Revisa los requisitos y las tarifas vigentes para tu cuenta antes de contratar.</p>
<a class="library-primary" href="https://zernio.com/" target="_blank" rel="noopener noreferrer">Ir a Zernio</a>
</section>

## Instalación para Codex: elige una opción

### 1. Desde GitHub con ayuda del asistente

Copia este prompt en una sesión de Codex con acceso a tu equipo:

> Instala la edición Codex de Mister WhatsApp desde https://github.com/Alanmezaoficial/mister-whatsapp. Lee docs/guia-codex.md. Conserva completa la carpeta codex/mister-whatsapp con SKILL.md, referencias, LICENSE y NOTICE. Usa scripts/install.py o copia a la carpeta personal de skills que corresponda a este host, sin reemplazar una instalación existente. Comprueba archivos y explica la activación en una sesión nueva. Limita este trabajo a instalar: no construyas el agente, no instales sus dependencias, no conectes cuentas, no despliegues ni envíes mensajes. Si faltan permisos o herramientas explica el paso pendiente sin afirmar que se instaló.

### 2. Con el ZIP y su prompt

Descarga **mister-whatsapp-codex-1.0.0.zip** desde la ficha de esta edición. Adjunta el ZIP o indica su ruta y pega:

> Instala Mister WhatsApp para Codex desde el ZIP que te comparto o cuya ruta te indico. Lee INSTALAR.md. Extrae de forma segura y copia la carpeta mister-whatsapp completa a la carpeta de skills del host, sin sobrescribir versiones existentes. Conserva referencias, LICENSE y NOTICE. Comprueba la estructura y explica la activación en una sesión nueva. No generes el agente ni conectes proveedores o envíes mensajes durante la instalación.

Para copiarlo manualmente, descomprime el ZIP en una carpeta nueva. Dentro encontrarás `mister-whatsapp/SKILL.md` y `INSTALAR.md`. Copia la carpeta completa `mister-whatsapp` a `~/.agents/skills/`. Si ya existe ese destino, detente y revisa su versión; no mezcles carpetas.

### 3. Con comandos manuales

En PowerShell:

```powershell
$waRepo = Join-Path $env:USERPROFILE 'mister-whatsapp-kit'
git clone https://github.com/Alanmezaoficial/mister-whatsapp.git $waRepo
if ($LASTEXITCODE -ne 0) { throw 'Revisa la descarga antes de continuar.' }
python (Join-Path $waRepo 'scripts/install.py') --edition codex --destination "$env:USERPROFILE/.agents/skills/mister-whatsapp"
if ($LASTEXITCODE -ne 0) { throw 'Revisa la instalación antes de continuar.' }
```

En macOS o Linux:

```bash
git clone https://github.com/Alanmezaoficial/mister-whatsapp.git "$HOME/mister-whatsapp-kit"
python3 "$HOME/mister-whatsapp-kit/scripts/install.py" --edition codex --destination "$HOME/.agents/skills/mister-whatsapp"
```

El instalador usa la biblioteca estándar de Python y rechaza destinos que ya existen. No instala dependencias del agente ni modifica configuraciones globales. Si Python tiene otro ejecutable, sustituye solo ese comando por el intérprete verificado de tu equipo.

### Comprueba la activación

La ruta final personal es `~/.agents/skills/mister-whatsapp/SKILL.md`. Abre una sesión nueva y usa `$mister-whatsapp`. También puedes pedir «Usa Mister WhatsApp para construir un agente de atención». El asistente debe leer sus referencias y empezar por el objetivo y la carpeta del proyecto, sin pedir claves en el chat.

Esta edición se instala como skill nativa de Codex. No necesita instalar Claude Code, ejecutar Bash ni registrar plugins de Claude. Las referencias se cargan desde la carpeta instalada y el agente se genera en una carpeta distinta. El agente de atención sigue usando la API de Anthropic; adaptar el constructor a Codex no cambia esa parte del stack.

## Un asistente para construir tu agente

Mister WhatsApp te guía para crear un agente que atienda conversaciones con información de tu negocio. Tú decides qué debe contestar y le proporcionas sus datos; el asistente escribe el servidor, la conexión con WhatsApp, la memoria y las pruebas. **El ZIP contiene instrucciones y plantillas: todavía no contiene tu agente funcionando.**

Puedes usarlo para horarios, servicios, preguntas frecuentes, catálogo o información de propiedades. Por ejemplo, una inmobiliaria puede darle políticas de renta confirmadas y pedir que pregunte zona y presupuesto. Eso no autoriza al agente a inventar disponibilidad ni afirmar que una cita quedó reservada.

El agente básico conversa y conserva historial. Agendar, cobrar, modificar inventario o registrar un lead en un CRM requiere conectar herramientas adicionales y probar sus efectos. Que exista un archivo llamado `tools.py` no demuestra que esas funciones estén activas.

## Qué hace cada pieza

| Pieza | Responsabilidad |
| --- | --- |
| Tu asistente constructor | Entrevistarte, generar archivos y ayudarte a probarlos |
| API de Anthropic | Producir respuestas cuando el agente está ejecutándose |
| Zernio o Meta Cloud API | Recibir y enviar mensajes de WhatsApp |
| FastAPI y Uvicorn | Recibir webhooks y exponer el estado del servicio |
| SQLite local o PostgreSQL | Mantener conversaciones y reconocer eventos repetidos |
| Railway | Hospedar el servidor si eliges ese despliegue |

El constructor y la API del agente son cosas distintas. Usar Codex para construirlo no cambia automáticamente el modelo de ejecución ni cubre las llamadas a Anthropic con tu suscripción. Tampoco pagar el asistente incluye WhatsApp, alojamiento o base de datos.

## Antes de comenzar

Necesitas un asistente con acceso a archivos y terminal, Python 3.11 o superior y una carpeta destinada al agente. Git sirve para descargar el kit y subir después el proyecto generado. Para las pruebas reales necesitas acceso a Anthropic y al proveedor de WhatsApp que elijas. Docker es opcional en tu equipo: Railway puede construir desde el Dockerfile.

En Windows abre PowerShell y comprueba:

```powershell
python --version
git --version
```

Si `python` abre la tienda o falla, no significa que el kit esté roto: indica al asistente la ruta del Python que tengas instalado. Descárgalo desde [Python](https://www.python.org/downloads/) si hace falta. En macOS y Linux el comando suele ser `python3`. Verifica la versión antes de continuar y no cambies configuraciones globales por rutina.

Prepara la información de tu negocio: nombre, actividad, servicios, horarios con zona horaria, políticas y un documento con respuestas frecuentes. No necesitas subir datos de clientes para empezar. Usa información ficticia en las primeras pruebas.

## Distingue instalar la skill de crear el agente

Primero instalas la herramienta en tu asistente. Después la invocas y eliges dónde construir tu negocio. Son dos operaciones distintas: la instalación no debe crear cuentas, instalar paquetes Python del agente, abrir webhooks ni enviar mensajes.

La carpeta de la skill conserva el conocimiento reutilizable. El proyecto del negocio va en otra carpeta, con su propio entorno virtual y su propia configuración. Así puedes crear varios agentes sin que uno sobrescriba el otro ni modifique la instalación del kit.

## Tres maneras de instalar

Las instrucciones específicas de tu edición aparecen arriba y en su ficha del Bunker. Puedes pedirle al asistente que instale desde GitHub, darle el ZIP junto con su prompt o copiar los archivos manualmente. Las tres opciones deben conservar `SKILL.md`, las referencias completas, `.env.example`, `LICENSE` y `NOTICE`.

Antes de sustituir una instalación existente revisa su versión. Si el asistente no puede acceder al archivo o ejecutar comandos, debe explicarlo y darte pasos manuales; adjuntar un ZIP a un chat no equivale a instalar una skill.

## El proceso completo, en cinco fases

Primero se comprueba el entorno. Después se realiza la entrevista y se genera el agente. Luego se prueba localmente y se decide si publicarlo. No necesitas autorizar todas las fases a la vez. Puedes parar después de revisar los archivos o continuar otro día con las respuestas guardadas sin secretos.

### 1. Entorno y carpeta del negocio

El asistente identifica Python, comprueba acceso a la carpeta y propone un entorno virtual. Antes de instalar dependencias debe mostrar qué necesita. Los archivos generados deben incluir `agent/`, `config/`, `tests/`, dependencias y empaquetado; no se da por completada la fase por crear carpetas vacías.

### 2. La entrevista: diez temas

La herramienta pregunta de uno en uno y espera tu respuesta. Si ya diste un dato, debe aprovecharlo.

| Tema | Cómo responder para obtener un mejor agente |
| --- | --- |
| Nombre del negocio | Tu nombre comercial, sin inventar otra marca |
| Actividad | Qué vendes o atiendes y en qué ubicación o mercado |
| Objetivo | Qué conversaciones quieres resolver y cuáles pasar a una persona |
| Nombre del agente | Cómo se presenta ante tus clientes |
| Tono | Formal, cercano o técnico, con un ejemplo de respuesta |
| Horario | Días, horas, zona horaria y qué decir fuera de horario |
| Conocimiento | Documentos con precios, catálogo y políticas confirmadas |
| Acceso a Anthropic | Solo confirmar si la clave está configurada fuera del chat |
| Proveedor WhatsApp | Elegir Zernio o Meta directo con las condiciones actuales |
| Configuración del proveedor | Confirmar por nombre qué variables están listas, sin pegar valores |

Una respuesta útil es: «Atendemos rentas en Tijuana. Quiero que explique requisitos y pregunte zona, presupuesto y mascotas. Si falta disponibilidad, debe derivar a una persona; no puede confirmar visitas».

### 3. Generación del proyecto

`agent/main.py` recibe eventos; `brain.py` prepara las consultas al modelo; `memory.py` guarda historial; `providers/` implementa el proveedor elegido. `config/business.yaml` describe tu negocio y `config/prompts.yaml` contiene las instrucciones de atención. `tests/test_local.py` permite conversar desde la terminal.

La herramienta debe generar solamente el adaptador que elegiste, conservar una interfaz común y comprobar los ejemplos contra la documentación actual. Debe verificar disponibilidad del modelo, versiones compatibles y dependencias, sin sustituir el modelo que acordaste para ahorrar por su cuenta.

### 4. Pruebas locales

Comienza con dobles de prueba que no llaman APIs ni envían mensajes. Después, si autorizas consumo, prueba el simulador con Anthropic. El simulador comprueba el diálogo, pero no valida la entrega por WhatsApp ni la configuración del webhook.

```powershell
python tests/test_local.py
```

Para comprobar el servidor generado:

```powershell
python -m uvicorn agent.main:app --host 127.0.0.1 --port 8000
```

En otra terminal:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/
```

Un proceso que arranca no implica que todas las conexiones estén listas. Revisa los campos del estado: puede estar operativo, sin configurar o degradado si falta una conexión. El asistente debe señalar exactamente qué comprobó y qué queda pendiente.

### 5. Despliegue opcional

Solo después de las pruebas se prepara la publicación. Revisa qué archivos se subirán, a qué cuenta y qué datos contendrán. La construcción del agente no autoriza crear recursos de pago, conectar tu número o ponerlo a atender clientes automáticamente.

## Configurar las claves sin exponerlas

Entra a [Claude Platform](https://platform.claude.com/) con tu cuenta, busca la gestión de API Keys y crea una clave para el proyecto. Guarda su valor en un gestor de contraseñas y configúralo como `ANTHROPIC_API_KEY` en el entorno local; en el servidor irá en su panel de variables. Revisa límites de gasto y permisos antes de la primera prueba real.

No pegues claves en el chat ni las incluyas en capturas, repositorios o documentos de negocio. El asistente necesita saber que la variable existe, no su valor. Si una clave se expone, revócala y reemplázala; borrarla de la última versión del archivo no la retira del historial Git.

`ANTHROPIC_MODEL` identifica el modelo elegido. `ANTHROPIC_EFFORT` y `ANTHROPIC_MAX_TOKENS` se usan solo si el modelo y SDK los admiten. No copies una tabla antigua de precios como si describiera tu cuenta actual.

## Elegir el proveedor de WhatsApp

**Zernio** ofrece una capa de integración sobre WhatsApp Business. Puede simplificar el alta y la gestión del inbox; verifica disponibilidad, permisos, sandbox y costos en [Zernio](https://zernio.com/) y su [documentación de WhatsApp](https://docs.zernio.com/platforms/whatsapp).

**Meta Cloud API directo** te deja configurar la aplicación y sus permisos en [Meta for Developers](https://developers.facebook.com/docs/whatsapp/cloud-api/). Necesitas identificar la cuenta de WhatsApp Business, el número, el token y el secreto de aplicación que corresponden al proyecto. Los requisitos de verificación y acceso dependen de tu cuenta y del uso solicitado.

No se conecta un WhatsApp personal como si fuera una cuenta Business de API. Comprueba las opciones de migración o coexistencia del número antes de modificar una línea que ya usa tu negocio. Elegir un proveedor no autoriza migrar el número.

## Camino Zernio, paso a paso

1. Entra a tu cuenta y revisa el flujo para conectar WhatsApp Business. Completa el alta de Meta que indique el proveedor.
2. Comprueba qué cuenta y número quedaron asociados. Si vas a usar sandbox, revisa sus límites vigentes y autoriza expresamente la prueba antes de iniciar una sesión o recibir un mensaje.
3. Genera la API key en la gestión de claves del panel y guárdala fuera del chat. Su variable es `ZERNIO_API_KEY`.
4. Genera un secreto aleatorio fuerte para el webhook; al menos 32 bytes de aleatoriedad es una referencia apropiada. Configúralo como `ZERNIO_WEBHOOK_SECRET` tanto en el agente como en el alta del webhook.
5. Deja el webhook pendiente hasta tener una URL HTTPS comprobada. No inventes una dirección ni uses localhost como destino del proveedor.
6. Revisa los identificadores: para responder importan `conversationId` y `accountId`, no solo el teléfono. Las identidades alternativas del remitente también deben conservarse cuando el evento las use.

`ZERNIO_ACCOUNT_ID` puede servir al chequeo de conexión; no sustituye el contexto de cada conversación. La URL base de la API debe ser la oficial, nunca un enlace de registro o afiliación.

## Camino Meta, paso a paso

1. En Meta for Developers crea o selecciona la aplicación del negocio y agrega la configuración de WhatsApp disponible para tu cuenta.
2. Localiza el identificador del número y configúralo en `META_PHONE_NUMBER_ID`.
3. Usa un token con permisos y vigencia adecuados para el entorno y configúralo como `META_ACCESS_TOKEN`. Un token temporal sirve para probar, pero no se convierte en credencial permanente al copiarlo al servidor.
4. Obtén el secreto de la aplicación por el procedimiento del panel y configúralo como `META_APP_SECRET`, sin compartirlo en la conversación.
5. Genera `META_VERIFY_TOKEN` y usa el mismo valor en ambos extremos para el alta del webhook. Este token de verificación y el App Secret cumplen funciones distintas.
6. Revisa `META_API_VERSION` contra una versión soportada. El asistente debe comprobar permisos, suscripciones y eventos antes de afirmar que la cuenta está conectada.

El alta usa una petición GET con un challenge. El agente debe devolver exactamente el challenge como texto cuando el token coincida y rechazarlo cuando sea incorrecto o esté vacío. La autenticación de los mensajes POST se comprueba aparte mediante HMAC.

## Qué ocurre con cada mensaje

El proveedor manda un evento al webhook. El servidor verifica su firma sobre el cuerpo original, normaliza los datos y comprueba si el evento ya existe. Después confirma la recepción y procesa la conversación en segundo plano. Consulta el historial de esa identidad, solicita una respuesta al modelo y la envía usando el contexto del proveedor.

Esta separación mantiene rápida la recepción del webhook. En Zernio la documentación pide responder 2xx en cinco segundos y contempla entregas repetidas; el ID del evento es imprescindible para deduplicar. Consulta el contrato vigente en [Webhooks de Zernio](https://docs.zernio.com/webhooks).

Sin secreto configurado esta adaptación **rechaza los webhooks**. El modo de pruebas local no debe abrir una excepción pública de firma. Para probar el diálogo sin WhatsApp se usa el simulador.

## Fiabilidad: lo que sí aporta y su límite

La base de datos permite detectar eventos repetidos y separar los historiales. El diseño básico usa `BackgroundTasks` y candados dentro del proceso; esas piezas no sobreviven como una cola duradera al reinicio de la aplicación ni coordinan varias réplicas.

Si el servidor devuelve 200 y cae antes de responder al cliente, el proveedor puede considerar el evento entregado. Liberar su marca en la base no provoca por sí solo otro intento del proveedor. Por eso esta versión básica necesita un refuerzo antes de usarse donde perder un mensaje sea inaceptable: una bandeja persistente, estados de procesamiento, worker y reintentos controlados con idempotencia de salida.

Pide esa ampliación explícitamente y valida las pruebas de reinicio. Hasta entonces no se debe prometer entrega garantizada, ausencia absoluta de duplicados ni alta disponibilidad. No escales réplicas pensando que un candado local coordina todo el servicio.

## Subir tu proyecto generado a GitHub

El repositorio de la skill y el de tu negocio son distintos. Genera el agente fuera del clon y crea un repositorio privado para él salvo que elijas publicar su contenido. No borres `.git` ni reemplaces el remoto del kit para conseguirlo.

Antes de subir, revisa `.gitignore`: debe excluir `.env`, `.env.*`, bases locales, entorno virtual, sesiones y documentos privados, conservando `.env.example`. Debe permitir `agent/`, pruebas, dependencias, Dockerfile y la configuración revisada necesaria para ejecutar el agente.

Excluir `knowledge/` no basta: si sus textos se incorporaron a `config/prompts.yaml`, ya existen en ese segundo archivo. Revisa también `business.yaml` y cualquier resumen de entrevista. No publiques catálogos privados o datos de clientes solo porque el archivo original estaba excluido.

Pide al asistente mostrar el estado y los archivos que entrarían al commit. Un repositorio que solo contiene instrucciones no alcanza para desplegar el agente; comprueba que el código generado realmente quedó versionado.

## Railway: servidor, base de datos y variables

1. Crea o selecciona el proyecto autorizado y conecta el repositorio del agente. Revisa costos y cuenta antes de desplegar.
2. Agrega PostgreSQL si vas a mantener historial en producción. No dependas de un archivo SQLite dentro de un contenedor efímero.
3. En el servicio del agente agrega la referencia de `DATABASE_URL` del servicio PostgreSQL. Crear la base no significa que la aplicación ya recibió su URL.
4. Configura `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, `WHATSAPP_PROVIDER`, `ENVIRONMENT=production` y las variables del único proveedor elegido.
5. Respeta el puerto entregado por Railway. El Dockerfile debe arrancar Uvicorn en `0.0.0.0` y usar `PORT`; no añadas un puerto fijo a ciegas.
6. Revisa el build, los logs redactados y el estado del servicio. Genera el dominio público desde la configuración de red si aún no existe.
7. Abre la URL HTTPS y comprueba el endpoint de salud antes de registrar el webhook.

Los nombres del panel pueden cambiar. Usa [la documentación de Railway](https://docs.railway.com/) para localizar repositorios, variables de referencia y red pública. No se conecta ningún proyecto Railway durante la instalación de esta skill.

## Activar el webhook y hacer la prueba real

Usa `https://tu-dominio/webhook`. En Zernio registra el evento de mensajes entrantes y el mismo secreto aleatorio del agente. En Meta completa la validación GET y las suscripciones correspondientes. Si el panel rechaza la URL, revisa HTTPS, token y respuesta antes de desactivar controles.

Autoriza una prueba desde un remitente de prueba. Verifica una respuesta real en el dispositivo, el estado del proveedor y el historial correcto. Después prueba una firma incorrecta y un evento repetido con datos sintéticos. Que un POST manual responda 200 no demuestra que el cliente haya recibido WhatsApp.

La ventana de atención limita cuándo puedes enviar texto libre; fuera de ella pueden requerirse plantillas aprobadas. Revisa permisos y reglas actuales antes de iniciar conversaciones o campañas. Este kit está orientado a atender mensajes, no a enviar publicidad masiva.

## Trece pedidos que puedes usar durante el recorrido

1. **Empezar:** «Usa Mister WhatsApp. Quiero crear un agente para mi negocio en una carpeta nueva. Comprueba el entorno y hazme las preguntas una por una; todavía no conectes cuentas».
2. **Ordenar conocimiento:** «Revisa estos documentos autorizados. Identifica horarios, precios y políticas que faltan o se contradicen. No completes información inventada».
3. **Preparar claves:** «Muéstrame solamente los nombres de variables que debo configurar para este proveedor y dónde hacerlo. Yo introduciré los secretos fuera del chat».
4. **Revisar el alcance:** «Resume qué va a contestar el agente y cuándo pasará la conversación a una persona. Distingue las acciones que todavía no puede ejecutar».
5. **Generar:** «Con mis respuestas confirmadas, genera el proyecto en esta carpeta. Conserva la instalación de la skill y muestra el inventario de archivos creados».
6. **Probar sin gasto:** «Prepara y ejecuta pruebas con dobles para API y proveedor. Comprueba firmas, duplicados, aislamiento de historial y errores; no mandes mensajes reales».
7. **Conversar localmente:** «Indícame el consumo esperado del simulador y, cuando lo autorice, ayúdame a probar una conversación con la API configurada».
8. **Ajustar el diálogo:** «Haz el tono más breve y cercano, manteniendo literalmente las condiciones confirmadas. Muéstrame ejemplos antes y después».
9. **Preparar GitHub:** «Revisa qué se subiría al repositorio privado del agente. Busca secretos y conocimiento privado incrustado; confirma que incluye el código ejecutable».
10. **Preparar Railway:** «Diseña el despliegue con PostgreSQL y referencia DATABASE_URL. Muéstrame recursos, variables y costos; espera autorización antes de crearlos».
11. **Probar WhatsApp:** «Con la publicación autorizada, verifica el webhook firmado y propón una prueba desde mi remitente de pruebas. Espera mi permiso antes de enviarla».
12. **Conectar una acción:** «Quiero consultar disponibilidad de citas. Define la herramienta, valida argumentos y permisos, conecta su ejecución al bucle del modelo y demuestra el resultado con pruebas; no confirmes reservas inexistentes».
13. **Mejorar continuidad:** «Evalúa el riesgo de perder tareas tras un 200 o un reinicio. Propón una inbox/outbox durable con pruebas de recuperación antes de ampliar el alcance».

## Cuando algo no funciona

| Síntoma | Qué comprobar primero |
| --- | --- |
| No aparece la skill | Carpeta final, SKILL.md y sesión nueva en el host correcto |
| No se generan archivos | Si solo la instalaste; invócala y acuerda carpeta y entrevista |
| Error de greenlet o driver PostgreSQL | Dependencias probadas, extra asyncio de SQLAlchemy y asyncpg |
| El chat local funciona pero WhatsApp no | Firma, evento, número, permisos y contexto de conversación |
| HTTP 401 en webhook | Secreto correcto y cuerpo crudo; no permitas firma vacía |
| Meta no acepta la URL | Verify token, challenge en texto, HTTPS y suscripción |
| Railway arranca pero no responde | Host 0.0.0.0, puerto PORT, dominio y ruta de salud |
| Se pierde historial | DATABASE_URL real del servicio y persistencia, no SQLite efímero |
| Un mensaje se queda sin respuesta tras reinicio | ACK previo y tareas en memoria; evaluar persistencia de trabajos |
| Dice que reservó pero no hay cita | tools.py no conectado o efecto no confirmado; retirar promesa y probar integración |

No compartas logs completos con teléfonos, texto de clientes o tokens. Pide un extracto redactado que muestre el tipo de error y la fase afectada.

## Costos y mantenimiento

La skill se entrega sin costo de licencia de uso bajo sus términos, pero el servicio generado tiene consumos independientes: API Anthropic, proveedor WhatsApp, mensajes o plantillas aplicables, servidor y base de datos. Consulta las tarifas oficiales y las de tu cuenta antes de crear recursos. No se garantizan planes gratuitos, límites de sandbox ni tiempos de aprobación.

Para estimar el modelo suma tokens de entrada y salida por sus precios vigentes. La entrada incluye las instrucciones del negocio y el historial que se vuelve a enviar en cada turno. Un catálogo grande aumenta el consumo; recorta contexto irrelevante sin borrar condiciones necesarias. Supervisa errores, gasto, vencimiento de credenciales, almacenamiento e intentos de entrega.

Conserva respaldos con acceso limitado y define cuánto tiempo mantendrás conversaciones. Actualiza dependencias y reglas del proveedor en un entorno de prueba antes de publicarlas. Cambiar el constructor de Claude a Codex no sustituye estas tareas.

## Qué está incluido y qué debes comprobar en tu entorno

Se conservan las cinco fases, diez temas de entrevista, contratos, módulos y ejemplos de generación, con correcciones documentadas de seguridad y compatibilidad. Los avisos del software distribuido están en LICENSE y NOTICE.

La revisión de plantillas y del paquete no demuestra que un agente personalizado ya se haya construido o conectado. La activación en una sesión nueva, las respuestas del modelo, tu número y tu cuenta de proveedor deben verificarse de manera separada. No se usan credenciales ni se envían WhatsApps por descargar esta herramienta.
