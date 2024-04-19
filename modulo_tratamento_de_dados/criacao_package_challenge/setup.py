from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package-template-master",
    version="0.0.2",
    author="Neoprot",
    author_email="kaua.seichi.gomes@gmail.com",
    description="Image Processing Package using Skimage",
    url="",
    install_requires=requirements,
    packages=find_packages(),
    python_requires='>=3.8',
)
