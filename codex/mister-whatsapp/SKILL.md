---
name: mister-whatsapp
description: Construye y prueba un agente de atención por WhatsApp mediante entrevista, con FastAPI, Anthropic, memoria y Zernio o Meta Cloud API. Úsala para crear o ajustar el agente; instalar la skill no autoriza conectar cuentas, enviar mensajes ni desplegarlo.
---

# Mister WhatsApp

Lee primero [compatibilidad](references/compatibilidad.md). Antes de generar código lee completo [construcción](references/construccion.md): contiene las cinco fases, preguntas, contratos y plantillas. Las reglas de compatibilidad prevalecen si los ejemplos antiguos contradicen permisos, secretos o comportamiento del host.

Empieza por el objetivo y la carpeta de destino, verifica el entorno y entrevista una pregunta a la vez. Conserva las respuestas ya conocidas. Usa únicamente el proveedor elegido y genera todos los módulos necesarios, no un resumen de las plantillas. Nunca generes el negocio dentro de esta instalación de skill.

Para diagnóstico o cambios posteriores usa las mismas referencias y empieza por evidencia: configuración por nombres, logs redactados y pruebas mínimas. No reinicies la entrevista completa si solo se pide ajustar tono o un fallo conocido. No interpretes interés en un agente como permiso para publicar o mandar WhatsApp.

Conserva el runtime Anthropic aunque el constructor sea Codex. Registra por separado lo probado sin red y lo comprobado con API/proveedor real. Consulta LICENSE y NOTICE para los avisos del software distribuido.
