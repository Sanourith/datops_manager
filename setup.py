from setuptools import setup, find_packages

setup(
    name="datops_manager",
    version="0.1",
    description="Un gestionnaire d'opérations pour les pipelines de données",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sanou",
    author_email="ton.email@example.com",
    url="https://github.com/sanourith/datops_manager",
    packages=find_packages(),  # Cherche les packages dans le répertoire 'datops_manager'
    install_requires=[
        "setuptools",
        "docker",
        "kubernetes",
        "requests",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Si tu as des scripts CLI, déclare-les ici
        "console_scripts": [
            "datops-manager-cli = datops_manager.cli:main",  # Point d'entrée vers ton CLI
        ],
    },
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",  # Spécifie où se trouvent les tests
    tests_require=[  # Dépendances supplémentaires pour les tests (par exemple pytest)
        "pytest",
        # Ajoute ici des dépendances de tests si nécessaires
    ],
)
