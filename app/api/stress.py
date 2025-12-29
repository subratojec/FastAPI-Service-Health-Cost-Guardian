from fastapi import APIRouter
import time

router = APIRouter(prefix="/stress",tags=["stress"])

@router.get("/cpu")
async def stress_cpu():
    end = time.time() + 10
    while time.time() < end:
        pass
    return {"status":"cpu stressed"}

@router.get("/memory")
async def stress_memory():
    data=[]
    for _ in range(10_000_000):
        data.append("x"*100)
    return {"status":"memory stressed"}
