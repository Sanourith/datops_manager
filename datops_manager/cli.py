import click
from datops_manager.infrastructure.docker_manager import DockerManager
from datops_manager.infrastructure.k8s_manager import KubernetesManager
from datops_manager.utils.config_manager import ConfigManager
from datops_manager.monitoring.logger import get_logger

# Initializing components
logger = get_logger("datops_manager.cli")
config = ConfigManager()


@click.group()
def cli():
    """
    ***DatOps Manager CLI ***
    Pipeline - DevOps - Data tool.
    """
    pass


### DOCKER COMMANDS
@cli.group()
def docker():
    """Docker commands for CLI"""
    pass


@docker.command()
@click.option("--image", required=True, help="Docker Image to use.")
@click.option("--name", required=True, help="Container's name")
def run(image, name):
    """Launch a Docker containers"""
    docker_manager = DockerManager(config)
    try:
        docker_manager.run_container(image, name)
        logger.info(f"Container {name} launched with image: {image}")
    except Exception as e:
        logger.error(f"Error launching container : {e}")


# docker stop / docker rm & ajout stop/rm à run
# docker build & ajout push à build
# docker images & ajout rm à images


### KUBERNETES COMMANDS
@cli.group()
def k8s():
    """Deployments tool"""
    pass


@k8s.command()
@click.option("--file", required=True, help="Path/to/deploy.yaml")
def deploy(file):
    """Deploy application on Kubernetes"""
    k8s_manager = KubernetesManager(config)
    try:
        k8s_manager.deploy(file)
        logger.info(f"Deployment success for {file}")
    except Exception as e:
        logger.error(f"Error deploying on Kubernetes {file} : {e}")


@k8s.command()
@click.command("--name", required=True, help="Name of deploy to delete")
def delete(name):
    """Delete a deployment by its name"""
    k8s_manager = KubernetesManager(config)
    try:
        k8s_manager.delete(name)
        logger.info(f"Deployment : {name} deleted")
    except Exception as e:
        logger.error(f"Error during deletion of {name}: {e}")


# combiner deploy/delete ?
# get all -n
#


## GITLAB
