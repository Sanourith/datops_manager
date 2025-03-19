import os
import yaml
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
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Loads configuration from YAML

        Returns:
            Dict[str, Any]: Dictionnary of the config
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config_file '{self.config_file} not found.")

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
            default (Any, optional): Default value if key is not found.
            Defaults to None.

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
        """Returns the logging configuration"""
        return self.get("logging", {})


if __name__=="__main__":
    try:
        config_manager = ConfigManager()
        logger.info()