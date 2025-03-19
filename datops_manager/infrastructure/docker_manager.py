class DockerManager:
    def __init__(self, config):
        self.config = config

    def run_container(self, image, name):
        print(f"Running container {name} with image {image}")
