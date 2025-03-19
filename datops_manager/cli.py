import click
from datops_manager.infrastructure.docker_manager import DockerManager
from datops_manager.infrastructure.k8s_manager import KubernetesManager
from datops_manager.utils.config_manager import ConfigManager
from datops_manager.monitoring.logger import get_logger
from datops_manager.monitoring.logger import log_function_call


# Initializing components
logger = get_logger("datops_manager.cli")
config = ConfigManager()
cli_version = "1.0.0"


@click.group(name="dom")
def cli():
    """
    ***DatOps Manager CLI ***
    Pipeline - DevOps - Data tool.
    """
    pass


# DOCKER COMMANDS
@cli.group(name="dock")
def docker():
    """Docker commands for CLI"""
    pass


@docker.command(name="run")
@click.option("--image", required=True, help="Docker Image to use.")
@click.option("--name", required=True, help="Container's name")
@log_function_call("datops_manager.cli.docker.run")
def run(image, name):
    """Launch a Docker containers"""
    docker_manager = DockerManager(config)
    try:
        docker_manager.run_container(image, name)
        logger.info(f"Container {name} launched with image: {image}")
    except Exception as e:
        logger.error(f"Error launching container : {e}")


# eg : dom dock run


# docker stop / docker rm & ajout stop/rm à run
# docker build & ajout push à build
# docker images & ajout rm à images


# KUBERNETES COMMANDS
@cli.group(name="kub")
def k8s():
    """Deployments tool"""
    pass


@k8s.command(name="apply")
@click.option("--file", required=True, help="Path/to/deploy.yaml")
@click.option(
    "--action",
    required=True,
    type=click.Choice(["deploy", "delete"], case_sensitive=False),
)
@log_function_call("datops_manager.cli.k8s.apply")
def deploy(file, action):
    """Deploy/Delete application on Kubernetes"""
    k8s_manager = KubernetesManager(config)
    try:
        if action == "deploy":
            k8s_manager.deploy(file)
            logger.info(f"Deployment success for {file}")
        elif action == "delete":
            k8s_manager.delete(file)
            logger.info(f"Deployment {file} deleted")
    except Exception as e:
        logger.error(f"Error during {action} of {file} : {e}")


# eg : dom kub apply --file deploy.yaml --action deploy
# eg : dom kub apply --file deploy.yaml --action delete


# @k8s.command(name="del")
# @click.command("--name", required=True, help="Name of deploy to delete")
# @log_function_call("datops_manager.cli.k8s.delete")
# def delete(name):
#     """Delete a deployment by its name"""
#     k8s_manager = KubernetesManager(config)
#     try:
#         k8s_manager.delete(name)
#         logger.info(f"Deployment : {name} deleted")
#     except Exception as e:
#         logger.error(f"Error during deletion of {name}: {e}")


# combiner deploy/delete ?
# get all -n
#


# GITLAB


@cli.command(name="version")
def version():
    """Display CLI version"""
    click.echo(f"DatOps Manager CLI - Version {cli_version}")


@cli.command(name="check")
def check_config():
    """Verify current configuration"""
    click.echo("Current config :")
    for key, value in config.config.items():
        click.echo(f"{key}: {value}")


if __name__ == "__main__":
    cli()
