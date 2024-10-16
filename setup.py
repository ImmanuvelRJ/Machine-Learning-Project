from setuptools import find_packages, setup
from typing import List

hyphen_dot = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''this function will return the libraries that are in the requirements.txt file'''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)

setup (
name='Student Performance Problem',
version = '0.0.1',
description = 'Dataset related to students performance over having proper food and not having proper food',
author = 'Immanuvel',
author_email = 'immanuvelrj7@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)