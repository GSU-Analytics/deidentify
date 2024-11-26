# Deidentify

`deidentify` is a Python package for de-identifying sensitive data. It provides a flexible configuration system to anonymize identifiers, shift dates, generate fake names/emails, and more.

## Features

- Hash unique identifiers
- Anonymize categorical data
- Shift dates and semesters
- Generate fake names, emails, and phone numbers
- Randomly adjust numerical data

---

## Documentation

For full documentation, visit: [Deidentify Documentation](https://gsu-analytics.github.io/deidentify/)

---

## Installation

### Remote Installation

Follow these steps to set up your local environment using Conda and install the package remotely from GitHub.

#### 1. Set Up a Conda Environment

First, create and activate a Conda environment to isolate the dependencies of this project from your system's global environment.

1. **Create a Conda environment**:
   
   Run the following command to create a new environment with Python 3.10:

   ```bash
   conda create -n deidentify python=3.10
   ```

   This will create a new environment named `deidentify` with Python version 3.10.

2. **Activate the Conda environment**:

   Activate the environment using:

   ```bash
   conda activate deidentify
   ```

   Once the environment is activated, you will see the environment name (`deidentify`) in your terminal prompt.

#### 2. Install the Package from GitHub

Now that the environment is set up, install the `deidentify` package from the GitHub repository:

1. **Install the package**:
   
   Run the following command to install the package directly from GitHub:

   ```bash
   pip install git+https://github.com/GSU-Analytics/deidentify.git
   ```

   This command installs the latest version of the `deidentify` package from the GitHub repository.

2. **Verify the Installation**:

   To ensure the package has been installed, run:

   ```bash
   pip list
   ```

   Look for `deidentify` in the list of installed packages.

---

### Local Installation

#### 1. Clone the Repository

To install the package locally:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/GSU-Analytics/deidentify.git
   cd deidentify
   ```

2. Install the package using `pip`:
   ```bash
   pip install .
   ```

#### 2. Install Using Conda

Alternatively, if you prefer using Conda, you can create an environment using the included `deidentify-env.yaml` file:

1. **Create the environment**:
   ```bash
   conda env create -f deidentify-env.yaml
   ```

2. **Activate the environment**:
   ```bash
   conda activate deidentify
   ```

---

## Usage

Run the `deidentify.py` script with the required configuration file and input data:

```bash
python deidentify.py --config config.yaml --input_dir ./data --input_file demo.csv
```

---

## Example Files

The package includes example files to help you get started:

- **`demo.csv`**: Example input data with sensitive information.
- **`demo_deidentified.csv`**: Example output after running the `deidentify.py` script.
- **`config.yaml`**: Example configuration file to customize the de-identification process.

---

## Copying Examples

To copy the example files (`demo.csv`, `demo_deidentified.csv`, `config.yaml`, etc.) to a specific directory, run:

```bash
copy_examples <destination_directory>
```

Replace `<destination_directory>` with the path where you want to copy the files.
