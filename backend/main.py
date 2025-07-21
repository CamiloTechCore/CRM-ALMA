# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crea una instancia de la aplicación FastAPI
app = FastAPI(title="ALMA™ v2.0 API")

# Configuración de CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # El origen del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define un endpoint para la raíz de la API (ESTA ES LA CORRECCIÓN)
@app.get("/", tags=["Root"])
def read_root_message():
    """Devuelve un mensaje de bienvenida para la raíz de la API."""
    return {"message": "Welcome to ALMA™ v2.0 API. Go to /docs for documentation."}

# Define un endpoint de prueba para verificar que el servidor está funcionando
@app.get("/api/health", tags=["Server Health"])
def read_root():
    """Devuelve un mensaje de estado para confirmar que la API está activa."""
    return {"status": "ok", "message": "ALMA™ API is running!"}