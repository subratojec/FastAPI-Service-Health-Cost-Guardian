from typing import List, Dict

def calculate_risk(cpu_percent, memory_percent, request_rate, active_alerts=None):
    score = 0
    signals = []

    # CPU risk (correct ordering)
    if cpu_percent > 70:
        score += 3
        signals.append("cpu_critical")
    elif cpu_percent > 30:
        score += 2
        signals.append("cpu_near_limit")

    # Memory risk
    if memory_percent > 85:
        score += 4
        signals.append("memory_critical")
    elif memory_percent > 75:
        score += 3
        signals.append("memory_pressure")

    # Traffic presence (simple & safe)
    if request_rate >= 1:
        score += 2
        signals.append("traffic_present")

    # Alert amplification
    if active_alerts:
        score += 3
        signals.append("alert_firing")

    if score >= 6:
        risk_level = "high"
        recommendation = "shed_load_scale_or_block_deploy"
    elif score >= 3:
        risk_level = "medium"
        recommendation = "monitor_closely_or_scale"
    else:
        risk_level = "low"
        recommendation = "continue_normal_operation"

    return {
        "risk_level": risk_level,
        "score": score,
        "signals": signals,
        "recommendation": recommendation,
        "confidence": round(min(score / 10, 1.0), 2),
    }
