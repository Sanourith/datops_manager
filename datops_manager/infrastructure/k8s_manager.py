from kubernetes import client, config
from kubernetes.client.rest import ApiException
import os
from datops_manager.monitoring.logger import get_logger


logger = get_logger("dataops_manager.infra.k8s_manager")


class KubernetesManager:
    def __init__(self, config_manager):
        """Initialize Kubernetes Manager with configuration manager"""
        self.config_manager = config_manager
        self.load_kube_config()

    def load_kube_config(self):
        """Load kubeconfig from kubeconfig file
        If KUBERNETES_SERVICE_HOST is set, assumes running inside a kube cluster.
        """
        kube_config_path = self.config_manager.get_kube_config_path()
        if kube_config_path:
            try:
                config.load_kube_config(kube_config_path)
                logger.info(f"Loaded Kubernetes config from {kube_config_path}")
            except Exception as e:
                logger.error(f"Error loading Kubernetes config: {e}")
        else:
            try:
                config.load_incluster_config()
                logger.info("Loaded Kubernetes config from in-cluster config.")
            except Exception as e:
                logger.error(f"Error loading in-cluster config: {e}")

    def deploy(self, file_path):
        """
        Deploy a Kubernetes resource from a YAML file.

        Args:
            file_path (str): path/to/file.yaml
        """
        if not os.path.exists(file_path):
            logger.error(f"File {file_path} does not exist.")
            raise FileNotFoundError(f"File {file_path} does not exist.")

        with open(file_path, "r") as f:
            yaml_data = f.read()

        try:
            k8s_client = client.ApiClient()
            k8s_client.call_api(
                "/apis/apps/v1/namespaces/default/deployments",
                "POST",
                body=yaml_data,
                header_params={"Content-Type": "application/yaml"},
            )
            logger.info(f"Deployment created from {file_path}")
        except ApiException as e:
            logger.error(f"Exception when deploying: {file_path} // {e}")

    def delete(self, name):
        """
        Delete a deployment on Kubernetes by name

        Args:
            name (str): Name of the deployment to delete
        """
        try:
            k8s_client = client.AppsV1Api()
            k8s_client.delete_namespaced_deployment(name, namespace="default")
            logger.info(f"Deployment {name} deleted successfully.")
        except ApiException as e:
            logger.error(f"Exception when deleting the deployment {name}: {e}")
