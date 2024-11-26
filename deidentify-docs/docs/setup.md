# Setup Guide

This guide explains how to set up your environment to run the `deidentify.py` script using various installation methods.

---

## Prerequisites

Ensure you have the following installed on your system:

- **Conda**: Install Miniconda or Anaconda ([Download Conda](https://docs.conda.io/en/latest/miniconda.html)).
- **Git** (optional): For cloning the repository if hosted on a platform like GitHub.

---

## Installation Methods

### 1. Install Using Conda and the `deidentify-env.yaml` File

#### View the `deidentify-env.yaml` File

The `deidentify-env.yaml` file specifies the required dependencies for the `deidentify` package:

```yaml
# deidentify-env.yaml

name: deidentify
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pandas
  - pyyaml
  - faker
  - pip
  - pip:
      - mkdocs
      - mkdocs-material
```

#### Create the Conda Environment

Run the following command to create the environment:

```bash
conda env create -f deidentify-env.yaml
```

This will:
- Create a Conda environment named `deidentify`.
- Install Python 3.10, the required dependencies, and the `pip`-installed packages (`mkdocs` and `mkdocs-material`).

#### Activate the Environment

Activate the environment with:

```bash
conda activate deidentify
```

You are now ready to run the `deidentify.py` script.

---

### 2. Install the Package Remotely from GitHub

Follow these steps to install the package directly from GitHub:

#### Create a Conda Environment

1. Create a Conda environment named `deidentify` with Python 3.10:
```bash
conda create -n deidentify python=3.10
```

2. Activate the Conda environment:
```bash
conda activate deidentify
```

#### Install the Package from GitHub

Install the package using `pip`:

```bash
pip install git+https://github.com/GSU-Analytics/deidentify.git
```

Verify the installation:

```bash
pip list
```

---

### 3. Local Installation (Clone the Repository)

If you want to work with the package locally, follow these steps:

#### Clone the Repository

1. Clone the repository:
```bash
git clone https://github.com/GSU-Analytics/deidentify.git
cd deidentify
```

#### Install Locally Using `pip`

Install the package and dependencies with `pip`:

```bash
pip install .
```

#### Alternatively, Use Conda

You can also use the `deidentify-env.yaml` file to create a Conda environment:

1. Create the environment:
```bash
conda env create -f deidentify-env.yaml
```

2. Activate the environment:
```bash
conda activate deidentify
```

---

## Running the Script

After installation, run the `deidentify.py` script using the following command:

```bash
python deidentify.py --config config.yaml --input_dir ./data --input_file demo.csv
```

- Replace `config.yaml`, `./data`, and `demo.csv` with the appropriate paths for your project.

---

## Copying Example Files

To copy the example files (`demo.csv`, `demo_deidentified.csv`, `config.yaml`, etc.) to a specific directory, use the `copy_examples` script:

```bash
copy_examples <destination_directory>
```

Replace `<destination_directory>` with the path to your desired location.

---

## Deactivating the Environment

When you're done working, deactivate the Conda environment with:

```bash
conda deactivate
```

---

## Updating the Environment

If new dependencies are added to the `deidentify-env.yaml` file, update your environment with:

```bash
conda env update -f deidentify-env.yaml --prune
```