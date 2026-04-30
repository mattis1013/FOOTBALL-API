# FOOTBALL-API

Ce projet consiste à mettre en place un pipeline de données sur Microsoft Azure permettant de collecter, stocker et sécuriser des données issues d’une API externe, https://www.api-football.com/

Il s’appuie sur une architecture Data Engineering cloud avec Python et les services Azure.

## Étapes principales

Collecte de données via une API REST externe (Python)
Stockage des données dans Azure Blob Storage
Gestion sécurisée des secrets via Azure Key Vault
Authentification via Azure Active Directory (Service Principal)
Structuration des données au format JSON pour un usage type Data Lake

## Évolutions prévues
Automatisation du pipeline via Azure Functions
Migration vers Managed Identity
Ajout de monitoring et logging
Amélioration de l’architecture data
