# FOOTBALL-API

Ce projet consiste à mettre en place un pipeline de données sur Microsoft Azure permettant de collecter, stocker et sécuriser des données issues d’une API externe, https://www.api-football.com/

Il s’appuie sur une architecture Data Engineering cloud avec Python et les services Azure.


## Déploiement

Le pipeline est conçu pour être déployé sur Azure avec :

Azure Functions (exécution serverless)
Azure Blob Storage (stockage des données)
Azure Key Vault (gestion des secrets)


## Étapes principales

Collecte de données via une API REST externe (Python)
Stockage des données dans Azure Blob Storage
Gestion sécurisée des secrets via Azure Key Vault
Authentification via Azure Active Directory (Service Principal)
Structuration des données au format JSON pour un usage type Data Lake
Automatisation du pipeline via Azure Functions/ trigger_function


## Evolution
Migration vers Managed Identity
Ajout de monitoring et logging
Amélioration de l’architecture data 


## Structure du projet
.
├── function_app.py
├── main.py
├── access_key_vault.py
├── access_azure_storage.py
├── requirements.txt
├── host.json
└── .gitignore
