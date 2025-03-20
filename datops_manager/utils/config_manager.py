import os
import yaml
import logging
from logging import handlers
from typing import Dict, Any


class ConfigManager:
    """
    Config-Agent to change and access to project parameters
    """

    def __init__(self, config_file: str = "config.yaml"):
        """
        Initiate configuration tool.

        Args:
            config_file (str, optional): Path/to/config.yaml. Defaults to "config.yaml".
        """
        self.config_file = os.path.join(os.path.dirname(__file__), "config.yaml")
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Loads configuration from YAML file.

        Returns:
            Dict[str, Any]: Dictionary containing the configuration.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file '{self.config_file}' not found.")

        try:
            with open(self.config_file, "r") as file:
                return yaml.safe_load(file) or {}
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML config file: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves a value from the config file by its key.
        Supports nested keys using dot notation.

        Args:
            key (str): The key to access, e.g., "logging.handlers.console".
            default (Any, optional): Default value if key is not found. Defaults to None.

        Returns:
            Any: The value corresponding to the key, or default if key is not found.
        """
        keys = key.split(".")
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default

    def get_logging_config(self) -> Dict[str, Any]:
        """Returns the logging configuration."""
        return self.get("logging", {})

    def get_database_config(self) -> Dict[str, Any]:
        """Returns the database configuration."""
        return self.get("database", {})

    def get_api_config(self) -> Dict[str, Any]:
        """Returns the API configuration."""
        return self.get("api", {})

    def get_docker_config(self) -> Dict[str, Any]:
        """Returns the Docker configuration."""
        return self.get("docker", {})

    def get_kubernetes_config(self) -> Dict[str, Any]:
        """Returns the Kubernetes configuration."""
        return self.get("kubernetes", {})

    def get_security_config(self) -> Dict[str, Any]:
        """Returns the security configuration."""
        return self.get("security", {})

    def get_environment_config(self) -> Dict[str, Any]:
        """Returns the environment configuration."""
        return self.get("environment", {})
