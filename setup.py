from typing import List
from setuptools import setup, find_packages
import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Declearing Variables for setup function
PROJECT_REPO_NAME = "DL-Coccidiosis_Disease_Detection"
VERSION = "0.0.1"
AUTHOR_USER_NAME = "junaid-o"
DESCRIPTION = """Coccidiosis Disease Detector WebApp Compatible With Python=3.10.12"""
LONG_DESCRIPTION = long_description
REQUIREMENTS_FILE_NAME = "requirements.txt"

REPO_URL = f"https://github.com/{AUTHOR_USER_NAME}/{PROJECT_REPO_NAME}"
PROJECT_URL = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{PROJECT_REPO_NAME}/issues",}

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ]

def get_requirements_list() ->  List[str]:
    """
    This function returns list of requirements mentioned in 
    requirements.txt file
    return This function is going to return list 
    which contains name of libraries mentioned in requirements.txt file
    """
        
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(name= PROJECT_REPO_NAME,
      version=VERSION,
      author=AUTHOR_USER_NAME,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content= "text/markdown",      
      packages= find_packages(where="."),
      install_requires=get_requirements_list(),
      license="MIT",
      classifiers = CLASSIFIERS,
      url= REPO_URL,
      project_urls=PROJECT_URL,
    )
