#!/bin/bash

read -p "Entrez le nom du projet: " PROJECT_NAME
read -p "Entrez le chemin où créer le projet (ex: /home/user/): " PROJECT_PATH
PROJECT_DIR="$PROJECT_PATH/$PROJECT_NAME"

# Définition des dossiers et fichiers
DIRECTORIES=(
    "$PROJECT_NAME/datops_manager/infrastructure"
    "$PROJECT_NAME/datops_manager/etl"
    "$PROJECT_NAME/datops_manager/data_migration"
    "$PROJECT_NAME/datops_manager/monitoring"
    "$PROJECT_NAME/datops_manager/orchestration"
    "$PROJECT_NAME/datops_manager/utils"
    "$PROJECT_NAME/tests/test_etl"
    "$PROJECT_NAME/tests/test_infrastructure"
    "$PROJECT_NAME/tests/test_data_migration"
    "$PROJECT_NAME/tests/test_monitoring"
    "$PROJECT_NAME/examples"
    "$PROJECT_NAME/docs"
    "$PROJECT_NAME/scripts"
)

FILES=(
    "$PROJECT_NAME/setup.py" "$PROJECT_NAME/pyproject.toml" "$PROJECT_NAME/requirements.txt" "$PROJECT_NAME/requirements-dev.txt" "$PROJECT_NAME/LICENSE" "$PROJECT_NAME/README.md"
    "$PROJECT_NAME/datops_manager/__init__.py" "$PROJECT_NAME/datops_manager/cli.py"
    "$PROJECT_NAME/datops_manager/infrastructure/__init__.py" "$PROJECT_NAME/datops_manager/infrastructure/k8s_manager.py"
    "$PROJECT_NAME/datops_manager/infrastructure/terraform_deployer.py" "$PROJECT_NAME/datops_manager/infrastructure/docker_manager.py"
    "$PROJECT_NAME/datops_manager/etl/__init__.py" "$PROJECT_NAME/datops_manager/etl/pipeline.py" "$PROJECT_NAME/datops_manager/etl/extract.py"
    "$PROJECT_NAME/datops_manager/etl/transform.py" "$PROJECT_NAME/datops_manager/etl/load.py" "$PROJECT_NAME/datops_manager/etl/validator.py"
    "$PROJECT_NAME/datops_manager/data_migration/__init__.py" "$PROJECT_NAME/datops_manager/data_migration/db_sync.py"
    "$PROJECT_NAME/datops_manager/data_migration/migration_manager.py"
    "$PROJECT_NAME/datops_manager/monitoring/__init__.py" "$PROJECT_NAME/datops_manager/monitoring/logger.py"
    "$PROJECT_NAME/datops_manager/monitoring/metrics.py" "$PROJECT_NAME/datops_manager/monitoring/alert_manager.py"
    "$PROJECT_NAME/datops_manager/orchestration/__init__.py" "$PROJECT_NAME/datops_manager/orchestration/airflow_manager.py"
    "$PROJECT_NAME/datops_manager/orchestration/spark_runner.py"
    "$PROJECT_NAME/datops_manager/utils/__init__.py" "$PROJECT_NAME/datops_manager/utils/config_manager.py"
    "$PROJECT_NAME/datops_manager/utils/secret_manager.py" "$PROJECT_NAME/datops_manager/utils/helpers.py"
    "$PROJECT_NAME/tests/__init__.py"
    "$PROJECT_NAME/examples/etl_pipeline_example.py" "$PROJECT_NAME/examples/k8s_deployment_example.py"
    "$PROJECT_NAME/examples/data_migration_example.py"
    "$PROJECT_NAME/docs/index.md" "$PROJECT_NAME/docs/etl.md" "$PROJECT_NAME/docs/infrastructure.md" "$PROJECT_NAME/docs/monitoring.md"
    "$PROJECT_NAME/scripts/install_dependencies.sh" "$PROJECT_NAME/scripts/setup_dev_environment.sh"
)

# Création des dossiers et fichiers
mkdir -p "$PROJECT_DIR"
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$PROJECT_PATH/$dir"
done

for file in "${FILES[@]}"; do
    touch "$PROJECT_PATH/$file"
done

echo "Projet $PROJECT_NAME créé avec succès dans $PROJECT_DIR"