from prometheus_client import Counter , Gauge

# HTTP request counter
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method","endpoint"]
)

# System Metrics
CPU_USAGE = Gauge(
    "system_cpu_usage_percent",
    "System CPU usage percentage"
)

MEMORY_USAGE = Gauge(
    "system_memory_usage_percent",
    "System memory usage percentage"
)