from aioredis import Redis
from fastapi import FastAPI
from api.routes import router as api_router
import os
from core.database import engine, Base
from dotenv import load_dotenv
from core.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title='Task One',
              description='This is a proyect fast api',
              version='1.0.1')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def startup():
    app.state.redis = Redis.from_url(os.getenv("REDIS_URL"))
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown():
    app.state.redis.close()


app.include_router(api_router, prefix="/api")
