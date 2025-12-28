import psutil #process and system utilities
from fastapi import APIRouter , status

router = APIRouter(prefix="/health",tags=["health"])

@router.get("",status_code=status.HTTP_200_OK)
async def health_check():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    return {
        "status": "healthy",
        "cpu_percent":cpu_percent,
        "memory":memory.percent,
    }