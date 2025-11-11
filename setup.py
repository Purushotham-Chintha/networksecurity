from setuptools import find_packages, setup
from typing import List


def get_requirements():
    '''
    This function will return list of requirements
    '''
    requirements = []
    try:
        with open("requirements.txt", "r") as file:
            # read lines from the file object
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e
                if requirement and requirement != "-e .":
                    requirements.append(requirement)
    except FileNotFoundError:
        print("the requirements.txt file is not found")
    return requirements


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Purushotham Chintha",
    author_email="puruchintha@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
