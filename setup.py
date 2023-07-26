from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
REQUIREMENTS_FILE_PATH = '/Users/deepjyotibhattacharjee/Developer/test_ml_project/requirements.txt'

def install_requirements(file_path) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='test_ml_project',
    version='0.0.1',
    author='Deepjyoti Bhattacharjee',
    author_email='deepjyotibhattacharjee217@gmail.com',
    packages=find_packages(),
    install_requires=install_requirements(REQUIREMENTS_FILE_PATH)
)
