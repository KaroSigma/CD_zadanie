import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.3"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="cd_zadanie",
    version=version,
    author="Karolina Gluza",
    author_email="karolina.gluza@edu.uekat.pl",
    url="https://github.com/KaroSigma/cd_zadanie",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["cd_zadanie=src:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)