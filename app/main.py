from fastapi import FastAPI, Request
from app.api.health import router as health_router
from app.core.metrics import REQUEST_COUNT
from app.api.metrics import router as metrics_router
# from app.api.stress import router as stress_router
import asyncio
from app.core.system_stats import update_system_metrics

app = FastAPI(
    title="FastAPI Service Health & Cost Guardian",
    version="1.0.0"
)
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()
    return response

@app.on_event("startup")
async def start_metrics_collector():
    async def collect():
        while True:
            update_system_metrics()
            await asyncio.sleep(5)
    asyncio.create_task(collect())


app.include_router(health_router) # Registerring the Health Router
app.include_router(metrics_router)

# app.include_router(stress_router)


@app.get("/")
async def root():
    return {"message": "Service is running"}

