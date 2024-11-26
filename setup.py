from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deidentify",
    version="0.1.0",
    author="Isaac Kerson",
    author_email="ikerson@gsu.edu",
    description="A package for de-identifying sensitive data using a flexible configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GSU-Analytics/deidentify.git",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        "pandas>=1.1.5",
        "pyyaml>=5.4.1",
        "faker>=13.3.0",
    ],
    package_data={
        'deidentify': [
            'examples/*.yaml',
            'examples/*.csv',
            '*.py',
        ],
    },
    entry_points={
        "console_scripts": [
            "copy_examples=deidentify.copy_examples:copy_examples_to",
        ],
    },
)
