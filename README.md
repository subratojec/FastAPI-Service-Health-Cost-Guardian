FastAPI Service Health & Cost Guardian
This document provides a detailed overview of the FastAPI Service Health & Cost Guardian project. The project demonstrates production-grade observability, reliability engineering, and cost-risk awareness using modern DevOps and SRE practices.
1. Project Overview
FastAPI Service Health & Cost Guardian is a microservice designed to expose application health, system metrics, and operational signals. It helps identify performance bottlenecks, reliability risks, and potential cost overruns before they impact users.
2. Objectives
- Expose service health and system-level metrics
- Monitor CPU, memory, and request traffic
- Enforce resource limits using Linux cgroups
- Visualize metrics using Grafana
- Detect reliability and cost risks using Prometheus alerts
3. Architecture
Client requests are served by a FastAPI application that exposes health and metrics endpoints. Prometheus scrapes metrics from the service and evaluates alert rules. Grafana queries Prometheus to visualize system behavior and trends.
4. Technology Stack
Backend:
- FastAPI
- Python

Observability:
- Prometheus
- Grafana

Infrastructure:
- Docker
- Docker Compose
- Linux cgroups
5. Key Features
- Health endpoint with system pressure awareness
- Prometheus-compatible metrics exporter
- CPU and memory limits enforced via Docker
- Grafana dashboards for saturation and trends
- Alert rules for CPU, memory, and traffic anomalies
6. Metrics & Alerts
The service exports CPU usage, memory usage, and HTTP request counters. Prometheus alert rules are defined to trigger warnings or critical alerts based on sustained threshold violations.
7. Learning Outcomes
- Understanding of Linux cgroups and container resource isolation
- Practical experience with Prometheus and Grafana
- Ability to correlate traffic patterns with system performance
- Designing actionable alerts while avoiding alert fatigue
8. Conclusion
This project reflects real-world SRE and DevOps workflows. It demonstrates how observability, resource control, and alerting work together to ensure reliable and cost-efficient services.
