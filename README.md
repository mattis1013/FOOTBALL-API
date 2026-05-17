# FOOTBALL-API

Ce projet met en place un pipeline de données sur Microsoft Azure permettant de collecter, transformer et stocker des données issues d’une API externe (https://www.api-football.com/).

Il s’appuie sur une architecture Data Engineering cloud avec Python et les services Azure.
---

## Branches

Ce projet est organisé en deux branches principales :

### main

Cette branche contient le code permettant d’exécuter le pipeline en local.  
Les données sont récupérées depuis l’API et peuvent être stockées et testées manuellement.

Utilisée pour le développement, les tests et l’exécution locale.

---

### deploiement-azure-function

Cette branche contient la version automatisée du pipeline déployée sur Azure.

- Exécution via Azure Functions (timer trigger)
- Pipeline entièrement automatisé
- Aucune exécution manuelle nécessaire

Utilisée pour le déploiement cloud et la production.


---

## Déploiement

Le pipeline est conçu pour être déployé sur Azure avec :

- Azure Functions (exécution serverless)
- Azure Blob Storage (stockage des données)
- Azure Key Vault (gestion des secrets)

---

## Étapes principales

- Collecte de données via une API REST externe (Python / requests)
- Authentification sécurisée via Azure Active Directory (Service Principal)
- Récupération sécurisée des secrets via Azure Key Vault
- Stockage des données dans Azure Blob Storage au format JSON
- Structuration des données pour un usage type Data Lake
- Automatisation du pipeline via Azure Functions (timer trigger sur la branche deploiement-azure-function)

---

## Évolution du projet

- Amélioration de la gestion des erreurs API (retry, logging)
- Amélioration de la robustesse des uploads vers Azure Blob Storage
- Ajout de logs pour le suivi du pipeline et le debugging
- Migration vers Managed Identity (évolution future)
- Ajout de monitoring et logging (via Azure services)
- Optimisation de l’architecture data (modularisation et séparation des responsabilités)
-Soon ! :D

---

## Structure du projet
├── function_app.py
├── football_api.py
├── access_key_vault.py
├── access_azure_storage.py
├── requirements.txt
└── .gitignore

## Configuration

Les variables sensibles et de configuration sont stockées dans un fichier `.env` (non versionné).
