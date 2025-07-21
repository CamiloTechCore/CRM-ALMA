ALMA™ v2.0 - Sistema de Gestión de Casos
Este documento describe la arquitectura, hoja de ruta y sprints de desarrollo para la migración de ALMA™ desde una aplicación de Google Apps Script a una arquitectura moderna y escalable usando Python (FastAPI) para el backend y React 18 (Next.js) para el frontend.

1. Filosofía del Proyecto: Andamiaje Cognitivo 🧠
La migración de un sistema funcional es una tarea compleja. Nuestro enfoque se basa en el andamiaje cognitivo:

Empezar desde lo Conocido: Partimos de la lógica de negocio y las funcionalidades que ya existen en Codigo.gs y Index.html.

Construcción Incremental: Dividimos el proyecto en "Sprints" o fases. Cada sprint introduce una nueva capa tecnológica (ej. base de datos, API, componentes de UI) y migra una parte específica de la funcionalidad.

Refuerzo Continuo: Cada nueva fase refuerza los conceptos de la anterior, permitiendo que el conocimiento se asiente antes de introducir más complejidad.

Reducir la Carga Cognitiva: Al enfocarnos en un objetivo a la vez (ej. solo la autenticación), evitamos la sobrecarga de tratar de resolver todo al mismo tiempo.

El resultado es un proceso de desarrollo más predecible, menos propenso a errores y que garantiza una transición suave y sólida.

2. Stack Tecnológico 🛠️
Backend (Python)
Framework: FastAPI. Es extremadamente rápido, moderno, con generación automática de documentación interactiva (muy útil para el desarrollo) y basado en estándares como OpenAPI.

Base de Datos: PostgreSQL. Es la base de datos relacional open-source más robusta y confiable para aplicaciones de este tipo.

ORM (Mapeo Objeto-Relacional): SQLAlchemy 2.0. Permite interactuar con la base de datos usando objetos de Python, lo que hace el código más limpio y seguro.

Migraciones de BD: Alembic. Para gestionar cambios en la estructura de la base de datos de forma versionada y segura.

Validación de Datos: Pydantic V2. Integrado en FastAPI, asegura que los datos que entran y salen de la API tengan la estructura correcta.

Autenticación: python-jose y passlib[bcrypt]. Para la creación/verificación de tokens JWT y el hashing seguro de contraseñas.

WebSockets: FastAPI WebSockets. Para la funcionalidad de notificaciones en tiempo real.

Servidor ASGI: Uvicorn. El servidor que ejecuta la aplicación FastAPI.

Contenerización: Docker. Para empaquetar y desplegar la aplicación y la base de datos de manera consistente.

Frontend (React 18)
Framework: Next.js 14. Un framework de React que ofrece renderizado en el servidor (SSR), generación de sitios estáticos (SSG), optimización de imágenes y un sistema de enrutamiento basado en archivos, lo que lo hace ideal para aplicaciones robustas y de alto rendimiento.

Estilos: Tailwind CSS. Un framework CSS "utility-first" que permite construir diseños complejos rápidamente sin salir del HTML. Es moderno y muy escalable.

Componentes de UI: Shadcn/ui o MUI (Material-UI). Librerías de componentes pre-construidos y personalizables (botones, tablas, modales) para acelerar el desarrollo de la interfaz.

Gestión de Estado: Zustand o React Context + Hooks. Soluciones ligeras y potentes para manejar el estado global de la aplicación (como los datos del usuario autenticado).

Peticiones a la API: Axios o el fetch nativo. Para comunicarse con el backend de FastAPI.

Tablas y Grillas de Datos: TanStack Table (React Table). Para crear las tablas de casos potentes, filtrables y paginadas.

Formularios: React Hook Form. Para manejar formularios complejos con validación de manera eficiente.

3. Hoja de Ruta y Sprints de Desarrollo 🗺️
Este es un cronograma propuesto. Cada sprint está diseñado para durar aproximadamente 2 semanas, pero puede ajustarse según sea necesario.

Sprint 0: La Fundación (Duración: 1 Semana)
Objetivo: Preparar todo el entorno de desarrollo. No se migra funcionalidad, solo se construyen los cimientos.

Fase 1: Control de Versiones y Entorno

[ ] Crear un repositorio en GitHub.

[ ] Configurar el entorno de desarrollo local: Instalar Python 3.10+, Node.js 20+, Docker.

Fase 2: Esqueleto del Backend

[ ] Crear la estructura de carpetas del proyecto FastAPI.

[ ] Configurar un entorno virtual de Python (venv).

[ ] Instalar dependencias iniciales: fastapi, uvicorn, sqlalchemy, psycopg2-binary.

[ ] Crear un endpoint de prueba (/api/health) que devuelva {"status": "ok"}.

Fase 3: Esqueleto del Frontend

[ ] Crear un nuevo proyecto Next.js 14 con npx create-next-app@latest.

[ ] Instalar dependencias iniciales: axios, tailwindcss.

[ ] Limpiar la plantilla inicial y crear una página principal básica.

Fase 4: Contenedor de la Base de Datos

[ ] Crear un archivo docker-compose.yml para levantar un servicio de PostgreSQL.

[ ] Iniciar el contenedor y conectarse a la base de datos usando una herramienta como DBeaver o pgAdmin para verificar que funciona.

Sprint 1: Autenticación de Usuarios y Base de Datos (Duración: 2 Semanas)
Objetivo: Reemplazar el sistema de login de Google Sheets por uno seguro basado en API y PostgreSQL.

Fase 1: Modelo de Datos

[ ] Módulo (Backend): Usando SQLAlchemy, definir el modelo UserModel (tabla usuarios) con campos como id, nombre, username, hashed_password, rol, is_active, created_at.

[ ] Módulo (Backend): Configurar Alembic y crear la primera migración para generar la tabla usuarios en la base de datos.

Fase 2: Lógica de Autenticación (Backend)

[ ] Módulo (Backend): Crear un users_service.py con funciones para:

Crear un nuevo usuario, hasheando la contraseña con passlib/bcrypt.

Verificar un usuario por username y contraseña.

[ ] Módulo (Backend): Crear los endpoints de la API:

POST /api/auth/register: Para registrar un nuevo usuario (inicialmente solo para administradores).

POST /api/auth/token: Para iniciar sesión. Recibe usuario/contraseña, y si son válidos, devuelve un token JWT.

Fase 3: Interfaz de Login (Frontend)

[ ] Módulo (Frontend): Crear el componente <LoginForm> en React.

[ ] Módulo (Frontend): Implementar la lógica para enviar los datos del formulario al endpoint /api/auth/token.

[ ] Módulo (Frontend): Al recibir el token JWT, almacenarlo de forma segura (ej. en una cookie HttpOnly gestionada por el backend o en el estado global).

[ ] Módulo (Frontend): Implementar rutas protegidas. Si el usuario no está autenticado, redirigirlo a la página de login.

Sprint 2: API de Gestión de Casos y Tabla Principal (Duración: 2 Semanas)
Objetivo: Migrar la funcionalidad principal de visualización y carga de casos.

Fase 1: Modelo de Datos de Casos (Backend)

[ ] Módulo (Backend): Definir el modelo CaseModel (tabla casos) con todos los campos relevantes (id, interaction_id, sample_date, oficina, canal, estado_alma, fecha_asignacion, link, etc.). Incluir una clave foránea owner_id que apunte al id de la tabla usuarios.

[ ] Módulo (Backend): Crear y aplicar la migración de Alembic para la tabla casos.

Fase 2: API de Casos (Backend)

[ ] Módulo (Backend): Crear los endpoints CRUD (Crear, Leer, Actualizar, Borrar) para los casos:

GET /api/casos: Devuelve una lista de casos, con filtros (ej. /api/casos?owner_id=123&team=X).

POST /api/casos/bulk-upload: Endpoint para la carga masiva. Recibe un array de casos, los valida y los inserta en la base de datos.

PATCH /api/casos/{case_id}/finalize: Endpoint para finalizar una gestión, actualizando el estado y las marcas (Marca de EG, Marca de CI).

Fase 3: Visualización de Casos (Frontend)

[ ] Módulo (Frontend): Crear el componente principal del dashboard (<DashboardPage>) que será una ruta protegida.

[ ] Módulo (Frontend): Construir el componente <CasesTable> usando TanStack Table.

[ ] Módulo (Frontend): Implementar la lógica para llamar al endpoint GET /api/casos y mostrar los datos en la tabla.

[ ] Módulo (Frontend): Añadir controles de UI para la paginación y los filtros básicos, que volverán a llamar a la API con los parámetros correspondientes.

Sprint 3: Interfaz de Carga de Datos y Métricas (Duración: 2 Semanas)
Objetivo: Replicar la experiencia de carga de datos y el dashboard de métricas.

Fase 1: Carga Masiva (Frontend)

[ ] Módulo (Frontend): Crear una nueva página/modal para el administrador llamada "Cargar Casos".

[ ] Módulo (Frontend): Implementar un componente de "tabla editable" (usando una librería o un simple textarea para empezar) donde el admin pueda pegar los datos desde una hoja de cálculo.

[ ] Módulo (Frontend): Escribir una función que parsee los datos pegados (texto separado por tabulaciones) a un formato JSON.

[ ] Módulo (Frontend): Enviar el JSON de casos al endpoint POST /api/casos/bulk-upload. Mostrar feedback de éxito o error.

Fase 2: Lógica de Asignación (Backend)

[ ] Módulo (Backend): Dentro de la lógica del bulk-upload, implementar la asignación dinámica de casos a los analistas según las reglas de negocio.

Fase 3: Dashboard de Métricas (Full-Stack)

[ ] Módulo (Backend): Crear un nuevo endpoint GET /api/dashboard/metrics. Este endpoint realizará consultas SQL optimizadas (COUNT, GROUP BY) para calcular los casos pendientes, realizados y aperturados, devolviendo un JSON simple como {"pendientes": 150, "realizados": 800, "aperturados": 50}.

[ ] Módulo (Frontend): Crear el componente <MetricCard>.

[ ] Módulo (Frontend): En la página del dashboard, llamar al nuevo endpoint de métricas y pasar los datos a los componentes <MetricCard> para su visualización.

Sprint 4: Módulo QA y Notificaciones en Tiempo Real (Duración: 2 Semanas)
Objetivo: Implementar el seguimiento de QA y las alertas en tiempo real para el administrador.

Fase 1: Módulo QA (Full-Stack)

[ ] Módulo (Backend): Definir el modelo y la migración para la tabla registros_qa.

[ ] Módulo (Backend): Crear los endpoints CRUD para gestionar los registros de QA.

[ ] Módulo (Frontend): Crear la pestaña/página "Seguimiento QA" con su tabla y formulario para crear/editar registros.

Fase 2: Configuración de WebSockets (Backend)

[ ] Módulo (Backend): Configurar un endpoint de WebSocket en FastAPI (ej. /ws/notifications/{user_id}).

[ ] Módulo (Backend): Implementar la lógica para que el servidor envíe mensajes a través del WebSocket cuando ocurran eventos importantes (ej. un caso supera el tiempo límite de gestión).

Fase 3: Panel de Alertas (Frontend)

[ ] Módulo (Frontend): Implementar la lógica del cliente para conectarse al WebSocket del servidor.

[ ] Módulo (Frontend): Crear un componente <AlertsPanel> para el administrador.

[ ] Módulo (Frontend): Cuando se recibe un mensaje por el WebSocket, actualizar el estado del <AlertsPanel> para mostrar la nueva alerta en tiempo real, con un sistema de posicionamiento dinámico que muestre las más antiguas primero.

Sprint 5: Funciones de Administrador, Pruebas y Despliegue (Duración: 2 Semanas)
Objetivo: Finalizar las funcionalidades, asegurar la calidad del software y prepararlo para producción.

Fase 1: Panel de Administración (Full-Stack)

[ ] Módulo (Backend/Frontend): Crear las vistas y endpoints para que el administrador pueda gestionar usuarios (crear, desactivar, cambiar rol).

Fase 2: Pruebas (Testing)

[ ] Módulo (Backend): Escribir pruebas unitarias e de integración para la API usando pytest.

[ ] Módulo (Frontend): Escribir pruebas para los componentes críticos usando Jest y React Testing Library.

Fase 3: Contenerización y Despliegue (DevOps)

[ ] Módulo (Backend): Crear un Dockerfile para empaquetar la aplicación FastAPI.

[ ] Módulo (Infraestructura): Actualizar docker-compose.yml para orquestar el backend, la base de datos y, opcionalmente, un proxy inverso como Nginx.

[ ] Módulo (DevOps): Desplegar la aplicación en un proveedor en la nube (ej. Vercel para el frontend y AWS/DigitalOcean/Render para el backend y la base de datos).

Fase 4: Migración de Datos Final

[ ] Escribir un script final para exportar todos los datos históricos de Google Sheets e importarlos a la base de datos PostgreSQL de producción.