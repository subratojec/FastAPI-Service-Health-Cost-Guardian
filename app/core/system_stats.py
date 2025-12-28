import psutil
from app.core.metrics import CPU_USAGE , MEMORY_USAGE

def update_system_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().percent)