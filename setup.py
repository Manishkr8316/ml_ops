from setuptools import setup, find_packages
from typing import List

# Define the trigger constant
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            # Read lines and strip whitespace/newlines in one go
            requirements = [line.strip() for line in file_obj.readlines()]

            # Remove '-e .' if it exists in the list
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
                
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Manish Kumar",
    author_email="manishkr8316@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)