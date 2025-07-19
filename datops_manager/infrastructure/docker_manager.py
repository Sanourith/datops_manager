import subprocess
from datops_manager.monitoring.logger import get_logger

logger = get_logger("datops_manager.docker")


class DockerManager:
    def __init__(self, config):
        self.config = config
        pass

    def build_image(self, image_name, dockerfile_path="."):
        """Building docker images"""
        cmd = ["docker", "build", "-t", image_name, dockerfile_path]
        try:
            logger.info(f"Executing command : {' '.join(cmd)}")
            result = subprocess.run(cmd, check=True, text=True, capture_output=True)
            logger.info(f"Image {image_name} built successfully: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error building image {image_name}: {e}")
            raise

    def push_image(self, image_name, reg="local"):
        """Pushing docker images"""
        if reg != "local":
            tag_cmd = ["docker", "tag", image_name, f"{reg}/{image_name}"]
            push_cmd = ["docker", "push", f"{reg}/{image_name}"]
        else:
            tag_cmd = []
            push_cmd = ["docker", "push", image_name]

        try:
            if tag_cmd:
                logger.info(f"Tagging image {image_name} as {reg}/{image_name}")
                subprocess.run(tag_cmd, check=True, text=True, capture_output=True)

            logger.info(f"Pushing image {image_name} to registry {reg}")
            result = subprocess.run(
                push_cmd, check=True, text=True, capture_output=True
            )
            logger.info(
                f"Image {image_name} pushed successfully to {reg}: {result.stdout}"
            )
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else str(e)
            logger.error(f"Error while pushing image {image_name}: {error_msg}")
            raise

    # TODO : document this function
    def run_container(self, image, name, rm=False):
        cmd = ["docker", "run", "--name", name, image]
        if rm:
            cmd.append("--rm")
        subprocess.run(cmd, check=True, capture_output=True)


######################################################################################


# # import docker
# import click
# import subprocess
# from datops_manager.monitoring.logger import get_logger, log_function_call

# logger = get_logger("datops_manager.docker")


# @click.group(name="dock")
# def cli():
#     """Docker CLI for images usage"""
#     pass


# @cli.command(name="build")
# @click.argument("image_name")
# @click.argument("dockerfile_path", default=".")
# @log_function_call("datops_manager.docker")
# def build(image_name, dockerfile_path):
#     """Building docker images"""
#     cmd = ["docker", "build", "-t", image_name, dockerfile_path]

#     try:
#         logger.info(f"Executing command : {' '.join(cmd)}")
#         result = subprocess.run(cmd, check=True, text=True, capture_output=True)
#         logger.info(f"Image {image_name} built successfully: {result.stdout}")
#     except subprocess.CalledProcessError as e:
#         logger.error(f"Error building image {image_name}: {e}")
#         raise


# @cli.command(name="push")
# @click.argument("image_name")
# @click.option("--reg", default="local", help="Target registry (default: local)")
# @log_function_call("datops_manager.docker")
# def push(image_name, reg):
#     """Pushing image
#     If --registry is set, pushes image to the specified registry.
#     Else, pushes locally.
#     """
#     if reg != "local":
#         tag_cmd = ["docker", "tag", image_name, f"{reg}/{image_name}"]
#         push_cmd = ["docker", "push", f"{reg}/{image_name}"]
#     else:
#         tag_cmd = []
#         push_cmd = ["docker", "push", image_name]

#     try:
#         if tag_cmd:
#             logger.info(f"Tagging image {image_name} as {reg}/{image_name}")
#             subprocess.run(tag_cmd, check=True, text=True, capture_output=True)

#         logger.info(f"Pushing image {image_name} to registry {reg}")
#         result = subprocess.run(push_cmd, check=True, text=True, capture_output=True)
#         logger.info(f"Image {image_name} pushed successfully to {reg}: {result.stdout}")
#     except subprocess.CalledProcessError as e:
#         error_msg = e.stderr if e.stderr else str(e)
#         logger.error(f"Error while pushing image {image_name}: {error_msg}")
#         raise


# if __name__ == "__main__":
#     cli()
