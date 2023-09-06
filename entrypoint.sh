#!/bin/bash
echo $POSTGRES_HOST
echo $FASTAPI_INTERNAL_PORT
# Esperar a que PostgreSQL esté listo
while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  sleep 2
done

# Iniciar FastAPI
uvicorn main:app --host 0.0.0.0 --port $FASTAPI_INTERNAL_PORT