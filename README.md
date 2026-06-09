# PFE DevSecOps Kubernetes

## Sujet

Conception et mise en œuvre d'une plateforme DevSecOps basée sur Kubernetes pour l'automatisation du déploiement sécurisé d'applications conteneurisées.

## Objectif

Mettre en place une architecture DevSecOps simple basée sur :

- Un cluster Kubernetes K3s à deux nœuds
- Une application web conteneurisée
- Un pipeline CI/CD
- Des scans de sécurité automatisés
- Une supervision avec Prometheus et Grafana

## Architecture du Projet

```text
GitHub Repository
        |
        v
GitHub Actions CI/CD
        |
        v
Docker Image Build
        |
        v
Security Scan - Trivy
        |
        v
Docker Registry
        |
        v
Kubernetes K3s Cluster OVH
        |
        v
Monitoring Prometheus / Grafana
# trigger pipeline
