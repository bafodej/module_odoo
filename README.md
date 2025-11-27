# Gestion des Certifications - Module Odoo

Module de gestion des certifications développé pour répondre aux besoins de certification, formation, et inspection.

## 📋 Description

Ce module permet de gérer le cycle complet des demandes de certification :
- Suivi des demandes de certification
- Planification et suivi des audits
- Gestion des statuts et workflow
- Assignation des auditeurs
- Historique et communication via le chatter

## 🎯 Fonctionnalités

### Workflow de certification
1. **Brouillon** : Création de la demande
2. **Demande Reçue** : Validation de la demande
3. **Audit Planifié** : Date d'audit fixée
4. **Audit Réalisé** : Audit complété
5. **Certifié** : Certification accordée
6. États alternatifs : Rejeté, Annulé

### Types de certifications supportés
- ISO 9001 - Qualité
- ISO 14001 - Environnement
- ISO 45001 - Santé et Sécurité
- Autre (personnalisable)

### Fonctionnalités additionnelles
- Numérotation automatique (CERT00001, CERT00002, etc.)
- Filtres et regroupements avancés
- Tracking des modifications
- Système d'activités et de messagerie intégré
- Vue en liste avec codes couleur par statut

## 🛠️ Installation

### Prérequis
- Odoo 18.0
- PostgreSQL 17
- Docker (recommandé)

### Installation avec Docker
```bash
# Clone le repository
git clone https://github.com/bvfode/certification_management.git

# Créer le réseau Docker
docker network create odoo-network

# Lancer PostgreSQL
docker run -d \
  --name odoo-db \
  --network odoo-network \
  -e POSTGRES_USER=odoo \
  -e POSTGRES_PASSWORD=odoo \
  -e POSTGRES_DB=postgres \
  -v odoo-db-data:/var/lib/postgresql/data \
  postgres:17

# Lancer Odoo avec le module
docker run -d \
  --name odoo \
  --network odoo-network \
  -p 8069:8069 \
  -v $(pwd):/mnt/extra-addons \
  odoo:18
```

### Activation du module

1. Accéder à Odoo : http://localhost:8069
2. Activer le mode développeur (Settings → Developer mode)
3. Apps → Update Apps List
4. Rechercher "Gestion des Certifications"
5. Cliquer sur Install

## 💼 Contexte du projet

Ce module a été développé dans le cadre de ma découverte  et de mon apronfondissement de l'ERP odoo. Il illustre la compréhension :
- De l'architecture MVC d'Odoo
- Du développement de modèles Python avec ORM
- De la création de vues XML personnalisées
- De la gestion des workflows métier
- Des bonnes pratiques de développement Odoo

## 🧑‍💻 Auteur

**Bafode Jaiteh**
- GitHub: [@bvfode](https://github.com/bvfode)
- Formation : Bac+3/4 AI & Data Science - Simplon Lille

## 📝 Licence

LGPL-3

## 🔗 Technologies utilisées

- Python 3.11
- PostgreSQL 17
- Odoo 18.0
- Docker
- XML
