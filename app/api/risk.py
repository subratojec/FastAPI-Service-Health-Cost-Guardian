from fastapi import APIRouter
import psutil
import time

from app.core.risk import calculate_risk
from app.core.metrics import  REQUEST_COUNT

router = APIRouter(tags=['risk'])

def get_request_count_1m() -> float:
    """
    Approximate request rate using Prometheus counter.
    Safe approximation for low-traffic services.
    :return:
    """
    try:
        return REQUEST_COUNT._value.get() / max(time.time(),1)
    except Exception :
        return 0.0

@router.get("/risk")
def risk():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    request_rate = get_request_count_1m()  
    active_alerts = []
    return calculate_risk(
        cpu_percent=cpu,
        memory_percent=memory,
        request_rate=request_rate,
        active_alerts=active_alerts,
    )