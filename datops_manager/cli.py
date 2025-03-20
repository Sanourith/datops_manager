import click
from datops_manager.infrastructure.docker_manager import DockerManager
from datops_manager.infrastructure.k8s_manager import KubernetesManager
from datops_manager.monitoring.logger import get_logger, log_function_call
from datops_manager.utils.config_manager import ConfigManager


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


@cli.command(name="info")
def info():
    """Display information about the project and current configuration."""
    logger.info(f"CLI Version: {cli_version}")
    logger.info(f"Logging Config: {config.get_logging_config()}")
    logger.info(f"Database Config: {config.get_database_config()}")
    logger.info(f"API Config: {config.get_api_config()}")
    logger.info(f"Docker Config: {config.get_docker_config()}")
    logger.info(f"Kubernetes Config: {config.get_kubernetes_config()}")


#######################################################################################

#                               CLI's DOCKER PART


#######################################################################################
# @cli.group(name="dock")
# def docker():
#     """Docker commands for CLI"""
#     pass


# RUN_CMD IS A FIRST EXAMPLE
# TODO : make a command run to run_container
@cli.command(name="run")
@click.option("--image", required=True, help="Docker Image to use.")
@click.option("--name", required=True, help="Container's name")
@click.option("--rm", is_flag=True, help="Remove container after it stops.")
@log_function_call("datops_manager.cli.docker")
def run(image, name, remove):
    """Launch a Docker container"""
    docker_manager = DockerManager(config)
    try:
        docker_manager.run_container(image, name, remove)
        logger.info(f"Container {name} launched with image: {image}")
    except Exception as e:
        logger.error(f"Error launching container {name}: {e}")


# eg : dom run --image my_image --name my_container --rm


@cli.command(name="build")
@click.argument("image_name")
@click.argument("dockerfile_path", default=".")
@log_function_call("datops_manager.cli.docker")
def build(image_name, dockerfile_path):
    """Building docker images"""
    docker_manager = DockerManager(config)
    try:
        docker_manager.build_image(image_name, dockerfile_path)
        logger.info(f"Image {image_name} built successfully.")
    except Exception as e:
        logger.error(f"Error building image {image_name}: {e}")


# eg : dom build my_image ./Dockerfile


@cli.command(name="push")
@click.argument("image_name")
@click.option("--reg", default="local", help="Target registry (default: local)")
@log_function_call("datops_manager.cli.docker")
def push(image_name, reg):
    """Pushing docker images"""
    docker_manager = DockerManager(config)
    try:
        docker_manager.push_image(image_name, reg)
        logger.info(f"Image {image_name} pushed successfully to {reg}.")
    except Exception as e:
        logger.error(f"Error pushing image {image_name}: {e}")


# eg : dom push my_image --reg my_registry


# docker stop / docker rm & ajout stop/rm à run
# docker build & ajout push à build
# docker images & ajout rm à images


#######################################################################################

#                               CLI's KUBERNETES PART


#######################################################################################
# @cli.group(name="kub")
# def k8s():
#     """Deployments tool"""
#     pass


# TODO : create k8s_manager.py
@cli.command(name="apply")
@click.option("--file", required=True, help="Path/to/deploy.yaml")
@click.option(
    "--action",
    required=True,
    type=click.Choice(["deploy", "delete"], case_sensitive=False),
)
@log_function_call("datops_manager.cli.k8s")
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


# eg : dom apply --file deploy.yaml --action deploy
# eg : dom apply --file deploy.yaml --action delete


# combiner deploy/delete ?
# get all -n
#


#######################################################################################

#                               CLI's GITLAB PART


#######################################################################################


#######################################################################################

#                               CLI's GENERAL PART


#######################################################################################
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


cli.add_command(build)
cli.add_command(push)
cli.add_command(info)
cli.add_command(version)
cli.add_command(check_config)

if __name__ == "__main__":
    cli()
