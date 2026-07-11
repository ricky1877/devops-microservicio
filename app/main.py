from fastapi import FastAPI
from app.routes.products import router as product_router

app = FastAPI(
    title="DevOps Microservice API",
    description="Microservicio desarrollado para la asignatura Ingeniería DevOps",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenido al DevOps Microservice API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


app.include_router(product_router)