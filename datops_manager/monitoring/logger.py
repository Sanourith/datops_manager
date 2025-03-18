import logging
import logging.config
import os
import yaml
from functools import wraps

# Load logs configuration
LOG_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "log_config.yaml")

if os.path.exists(LOG_CONFIG_PATH):
    with open(LOG_CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] - %(message)s",
    )


def get_logger(name="datops_manager"):
    """Return named logger"""
    return logging.getLogger(name)


def log_function_call(logger_name="datops_manager"):
    """Decorator for app-calls auto logs"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(f"{logger_name}.{func.__name__}")
            logger.info(f"Calling {func.__name__} with args = {args} kwargs = {kwargs}")
            result = func(*args, **kwargs)
            logger.info(f"Result for {func.__name__}: {result}")
            return result

        return wrapper

    return decorator


# Usage eg 1 > with decorator:
# from datops_manager.monitoring.logger import log_function_call

# @log_function_call("datops_manager.etl")
# def transform_data(data):
#     return [x * 2 for x in data]


# Usage eg 2 > with getLogger():
# from datops_manager.monitoring.logger import get_logger

# class DataPipeline:
#     def __init__(self):
#         self.logger = get_logger("datops_manager.etl.pipeline")

#     def run(self):
#         self.logger.info("Démarrage de la pipeline...")
#         try:
#             # Code métier
#             self.logger.debug("Transformation en cours...")
#         except Exception as e:
#             self.logger.error(f"Erreur dans la pipeline: {e}")
