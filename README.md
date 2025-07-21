# ALMA™ v2.0 - Sistema de Gestión de Casos

Este proyecto detalla la migración del sistema de gestión de casos **ALMA™** desde su implementación original en Google Apps Script hacia una arquitectura moderna, robusta y escalable.

---

## Filosofía del Proyecto: Andamiaje Cognitivo 🧠

La migración se aborda mediante un enfoque de **andamiaje cognitivo**, lo que nos permite construir sobre una base sólida de manera incremental y controlada. Partimos de la lógica de negocio existente para dividir el proyecto en fases o "Sprints". Cada sprint introduce una nueva capa tecnológica y migra una funcionalidad específica, reforzando el conocimiento adquirido antes de añadir más complejidad y reduciendo la carga cognitiva general.

El resultado es un proceso de desarrollo más predecible, menos propenso a errores y que garantiza una transición suave y sólida.

---

## Stack Tecnológico 🛠️

Se ha seleccionado un stack tecnológico moderno y eficiente para garantizar el rendimiento, la escalabilidad y la mantenibilidad del sistema.

| Área | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Backend** | [Python](https://www.python.org/) + [FastAPI](https://fastapi.tiangolo.com/) |  Framework de alto rendimiento para construir APIs. |
| | [PostgreSQL](https://www.postgresql.org/) | Robusta base de datos relacional open-source. |
| | [SQLAlchemy 2.0](https://www.sqlalchemy.org/) | ORM para interactuar con la base de datos usando objetos de Python. |
| | [Alembic](https://alembic.sqlalchemy.org/) | Herramienta para gestionar migraciones de la base de datos. |
| | [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI que ejecuta la aplicación FastAPI. |
| **Frontend** | [React 18](https://react.dev/) + [Next.js 14](https://nextjs.org/) | Framework de React para aplicaciones de alto rendimiento. |
| | [Tailwind CSS](https://tailwindcss.com/) | Framework CSS "utility-first" para diseños rápidos y escalables. |
| | [TanStack Table](https://tanstack.com/table/v8) | Librería para crear tablas y grillas de datos potentes. |
| **Contenerización**| [Docker](https://www.docker.com/) |  Empaqueta y despliega aplicaciones de manera consistente. |

---

## Hoja de Ruta y Sprints de Desarrollo 🗺️

El proyecto se divide en los siguientes sprints, cada uno con objetivos y entregables claros.

### **Sprint 0: La Fundación** (Duración: 1 Semana)
* **Objetivo:** Preparar todo el entorno de desarrollo, sentando las bases tecnológicas sin migrar funcionalidad.
* **Hitos a Revisar:**
    * Repositorio en GitHub configurado.
    * Entorno de desarrollo local (Python, Node.js, Docker) listo.
    * Estructura del proyecto FastAPI creada con un endpoint de prueba `/api/health`.
    * Proyecto base de Next.js 14 inicializado.
    * Contenedor de la base de datos PostgreSQL funcionando y accesible.
* **Gestión de Conflictos:** Al finalizar, se documentará cualquier problema de configuración de entorno y las soluciones aplicadas para estandarizar el setup de todos los desarrolladores.

### **Sprint 1: Autenticación de Usuarios y Base de Datos** (Duración: 2 Semanas)
* **Objetivo:** Reemplazar el login de Google Sheets por un sistema seguro basado en API y PostgreSQL.
* **Hitos a Revisar:**
    * Modelo de datos y tabla `usuarios` creados en PostgreSQL mediante SQLAlchemy y Alembic.
    * API de autenticación con endpoints para registro (`/register`) y login (`/token`) usando JWT.
    * Interfaz de login en React que consume la API de autenticación.
    * Sistema de rutas protegidas en el frontend para redirigir a usuarios no autenticados.
* **Gestión de Conflictos:** Se registrarán las decisiones sobre el almacenamiento de tokens JWT (ej. cookies HttpOnly vs. Local Storage) y los desafíos encontrados al proteger rutas.

### **Sprint 2: API de Gestión de Casos y Tabla Principal** (Duración: 2 Semanas)
* **Objetivo:** Migrar la funcionalidad principal de visualización y carga de casos.
* **Hitos a Revisar:**
    * Modelo de datos y tabla `casos` definidos y migrados, incluyendo la relación con la tabla `usuarios`.
    * API de casos con endpoints CRUD (Crear, Leer, Actualizar, Borrar).
    * Endpoint de carga masiva (`/bulk-upload`) para insertar múltiples casos.
    * Dashboard principal con una tabla de casos (TanStack Table) que muestra los datos obtenidos de la API, con paginación y filtros básicos.
* **Gestión de Conflictos:** Se documentarán los retos de rendimiento al consultar y filtrar grandes volúmenes de casos y las optimizaciones de SQL implementadas.

### **Sprint 3: Interfaz de Carga de Datos y Métricas** (Duración: 2 Semanas)
* **Objetivo:** Replicar la experiencia de carga de datos y el dashboard de métricas.
* **Hitos a Revisar:**
    * Interfaz de carga masiva donde un administrador puede pegar datos desde una hoja de cálculo.
    * Función en el frontend para parsear datos tabulados a JSON y enviarlos a la API.
    * Lógica de asignación dinámica de casos a los analistas implementada en el backend.
    * Endpoint de métricas (`/api/dashboard/metrics`) que realiza cálculos agregados.
    * Componentes de UI en el frontend para visualizar las métricas clave.
* **Gestión de Conflictos:** Se registrarán las complejidades de la lógica de negocio para la asignación de casos y las estrategias de parsing de datos para manejar diferentes formatos.

### **Sprint 4: Módulo QA y Notificaciones en Tiempo Real** (Duración: 2 Semanas)
* **Objetivo:** Implementar el seguimiento de QA y alertas en tiempo real.
* **Hitos a Revisar:**
    * Módulo de QA completo (modelo de datos, API y vistas en el frontend).
    * Endpoint de WebSockets configurado en FastAPI para notificaciones.
    * Lógica para emitir eventos en tiempo real (ej. casos vencidos).
    * Panel de alertas en el frontend que se conecta al WebSocket y muestra notificaciones.
* **Gestión de Conflictos:** Se documentarán los desafíos en la gestión de conexiones WebSocket y la lógica para la visualización dinámica de alertas sin sobrecargar la interfaz.

### **Sprint 5: Administración, Pruebas y Despliegue** (Duración: 2 Semanas)
* **Objetivo:** Finalizar funcionalidades, asegurar la calidad del software y prepararlo para producción.
* **Hitos a Revisar:**
    * Panel de administración para la gestión de usuarios (crear, desactivar, cambiar roles).
    * Pruebas unitarias y de integración para la API (Pytest).
    * Pruebas de componentes para el frontend (Jest y React Testing Library).
    * Dockerfile para la aplicación FastAPI y `docker-compose.yml` actualizado.
    * Plan de despliegue definido para frontend (Vercel) y backend (AWS/Render/DigitalOcean).
    * Script de migración final de datos históricos.
* **Gestión de Conflictos:** Se registrarán las lecciones aprendidas durante el proceso de contenerización, las estrategias de prueba y cualquier problema encontrado durante el despliegue piloto.

---

## Cronograma y Progresión Semanal

El proyecto tiene una duración estimada de **10 semanas**, comenzando el lunes 21 de julio de 2025. El siguiente gráfico muestra el porcentaje de avance del proyecto acumulado al final de cada semana.