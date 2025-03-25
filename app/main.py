from fastapi import FastAPI
from app.routes.prediction_routes import router_
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las fuentes, usa ["http://localhost:3000"] si quieres restringirlo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permite todos los headers
)
app.include_router(router_)