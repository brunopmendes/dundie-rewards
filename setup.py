# setuptools
from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    packages=find_packages() #tudo com __init__ é considerado um pacote
)