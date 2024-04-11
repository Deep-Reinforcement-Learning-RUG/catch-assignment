from setuptools import setup

with open('requirements.txt', 'r') as file:
    requirements = [line.strip() for line in file if line.strip()]

setup(
    name='GameOfCatch',
    description='Assignment for Deep Reinforcement Learning at University of Groningen',
    install_requires=requirements,
)
