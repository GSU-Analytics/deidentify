# deidentify.py

"""
De-identify a dataset based on a YAML configuration file.

This script reads a CSV file specified by the user, along with a YAML configuration file
that outlines which columns to de-identify and how to process them. The script supports
operations such as hashing IDs, generating fake names and emails, anonymizing categorical
data, and shifting dates and numeric values.

The de-identified file is saved with a "_deidentified" suffix in the same directory as
the input file.

Example usage:
    python deidentify.py --config config.yaml --input_dir ./data --input_file demo_data.csv

Command-line Arguments:
    --config: Path to the YAML configuration file (default: config.yaml).
    --input_dir: Directory containing the input CSV file (default: ./data).
    --input_file: Name of the input CSV file (required).

Functions:
    hash_id(identifier):
        Hashes a unique identifier into a consistent numeric string.

    fake_name():
        Generates a fake first and last name.

    anonymize_categories(column):
        Replaces unique values in a categorical column with generic labels.

    shift_dates(date, years):
        Shifts a date backward by a specified number of years.

    shift_semesters(semester, years):
        Adjusts a semester identifier (in YYYYMM format) by a specified number of years.

    shift_integer_column(value, mean):
        Randomly adjusts an integer value by -1, 0, or +1.

    shift_float_column(value, mean):
        Randomly adjusts a float value by a small amount (-0.25 to +0.25).

    generate_fake_email():
        Creates a fake email address.

    generate_fake_phone():
        Creates a fake phone number.

Main Function:
    main(config_path, input_dir, input_file):
        Orchestrates the de-identification process based on the configuration file.
        Loads the input CSV, applies transformations, and saves the output.

    Args:
        config_path (str): Path to the YAML configuration file.
        input_dir (str): Directory containing the input file.
        input_file (str): Name of the input CSV file.
"""

import os
import yaml
import random
import hashlib
import pandas as pd
from faker import Faker
from datetime import datetime
import argparse

# Initialize Faker
fake = Faker()

def hash_id(identifier):
    """
    Hash a unique identifier into a consistent numeric string.

    This function hashes a given identifier using the SHA-256 algorithm and
    converts it to a 12-digit numeric string.

    Args:
        identifier (str or int): The identifier to be hashed.

    Returns:
        str: A 12-digit numeric string representing the hashed identifier.

    Example:
        >>> hash_id("12345")
        '098765432109'
    """
    hashed = int(hashlib.sha256(str(identifier).encode('utf-8')).hexdigest(), 16) % (10**12)
    return f"{hashed:012}"

def fake_name():
    """
    Generate a fake name with first and last names.

    This function uses the Faker library to generate a random first name
    and last name.

    Returns:
        dict: A dictionary containing a first name under the key 'FN' and a last
              name under the key 'LN'.

    Example:
        >>> fake_name()
        {'FN': 'John', 'LN': 'Doe'}
    """
    return {"FN": fake.first_name(), "LN": fake.last_name()}

def anonymize_categories(column):
    """
    Anonymize a categorical column by mapping values to generic labels.

    Unique values in the column are replaced with labels in the format
    CATEGORY01, CATEGORY02, etc.

    Args:
        column (pd.Series): A Pandas Series containing the categorical data.

    Returns:
        pd.Series: A Pandas Series with the anonymized categories.

    Example:
        >>> anonymize_categories(pd.Series(['A', 'B', 'A']))
        0    CATEGORY01
        1    CATEGORY02
        2    CATEGORY01
        dtype: object
    """
    unique_values = column.unique()
    mapping = {val: f"CATEGORY{str(i+1).zfill(2)}" for i, val in enumerate(unique_values)}
    return column.map(mapping)

def shift_dates(date, years):
    """
    Shift a date backward by a specified number of years.

    This function adjusts the year of a date string by subtracting the specified
    number of years. Dates must be in the format YYYY-MM-DD.

    Args:
        date (str): The date string to be shifted.
        years (int): The number of years to subtract.

    Returns:
        str: The adjusted date string, or the original value if invalid.

    Example:
        >>> shift_dates("2024-01-01", 2)
        '2022-01-01'
    """
    if pd.isna(date):
        return date
    try:
        return (datetime.strptime(date, "%Y-%m-%d").replace(year=datetime.strptime(date, "%Y-%m-%d").year - years)).strftime("%Y-%m-%d")
    except ValueError:
        return date
    
def shift_semesters(semester, years):
    """
    Shift a semester identifier (YYYYMM) by a specified number of years.

    Args:
        semester (str or int): The semester identifier to be adjusted.
        years (int): The number of years to add to or subtract from the semester.

    Returns:
        str: The adjusted semester identifier, or the original value if invalid.

    Example:
        >>> shift_semesters("202401", -2)
        '202201'
    """
    if pd.isna(semester) or len(str(semester)) != 6:
        return semester
    try:
        year = int(str(semester)[:4]) + years
        month = str(semester)[4:]
        return f"{year}{month}"
    except ValueError:
        return semester

def shift_integer_column(value, mean):
    """
    Randomly adjust an integer value by -1, 0, or +1.

    Args:
        value (int or float): The value to adjust.
        mean (float): The mean of the column (not used in the current implementation).

    Returns:
        int: The adjusted integer value, or the original value if invalid.

    Example:
        >>> shift_integer_column(5, 4.5)
        6
    """
    if pd.isna(value):
        return value
    return value + random.choice([-1, 0, 1])

def shift_float_column(value, mean):
    """
    Randomly adjust a float value by a small amount (-0.25 to +0.25).

    Args:
        value (float): The value to adjust.
        mean (float): The mean of the column (not used in the current implementation).

    Returns:
        float: The adjusted float value, or the original value if invalid.

    Example:
        >>> shift_float_column(3.5, 3.6)
        3.3
    """
    if pd.isna(value):
        return value
    return value + random.uniform(-0.25, 0.25)

def generate_fake_email():
    """
    Generate a fake email address.

    This function uses the Faker library to generate a random email address.

    Returns:
        str: A fake email address.

    Example:
        >>> generate_fake_email()
        'john.doe@example.com'
    """
    return fake.email()

def generate_fake_phone():
    """
    Generate a fake phone number.

    This function uses the Faker library to generate a random phone number.

    Returns:
        str: A fake phone number.

    Example:
        >>> generate_fake_phone()
        '(555) 123-4567'
    """
    return fake.phone_number()

def main(config_path, input_dir, input_file):
    """
    Execute the de-identification process based on the provided configuration.

    This function orchestrates the de-identification workflow by:
    - Loading a configuration YAML file.
    - Reading the input CSV file from the specified directory.
    - Applying transformations (e.g., hashing, anonymization, date shifting) based on the configuration.
    - Saving the de-identified data to a new CSV file with a "_deidentified" suffix.

    Args:
        config_path (str): Path to the YAML configuration file.
        input_dir (str): Directory containing the input CSV file.
        input_file (str): Name of the input CSV file.

    Returns:
        None

    Example:
        >>> main("config.yaml", "./data", "demo_data.csv")
        De-identified file saved to: ./data/demo_data_deidentified.csv
    """
        
    # Load config from YAML
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Construct the input file path
    input_file_path = os.path.join(input_dir, input_file)
    df = pd.read_csv(input_file_path, low_memory=False)

    # De-identify the dataset
    if 'id_column' in config and config['id_column'] in df.columns:
        id_column = config['id_column']
        df[id_column] = df[id_column].apply(hash_id)

        if 'first_name_column' in config and config['first_name_column'] in df.columns:
            first_name_column = config['first_name_column']
            df[first_name_column] = df[id_column].map(lambda x: fake_name()['FN'])

        if 'last_name_column' in config and config['last_name_column'] in df.columns:
            last_name_column = config['last_name_column']
            df[last_name_column] = df[id_column].map(lambda x: fake_name()['LN'])

    if 'categorical_columns' in config:
        for column in config['categorical_columns']:
            if column in df.columns:
                df[column] = anonymize_categories(df[column])

    shift_years = config.get('shift_years', 0)

    if 'time_date_columns' in config:
        for column in config['time_date_columns']:
            if column in df.columns:
                df[column] = df[column].apply(lambda x: shift_dates(x, shift_years))

    if 'semester_columns' in config:
        for column in config['semester_columns']:
            if column in df.columns:
                df[column] = df[column].apply(lambda x: shift_semesters(x, shift_years))

    if 'email_column' in config and config['email_column'] in df.columns:
        df[config['email_column']] = df[config['email_column']].apply(lambda x: generate_fake_email() if not pd.isna(x) else x)

    if 'student_id_column' in config and config['student_id_column'] in df.columns:
        df[config['student_id_column']] = df[config['student_id_column']].apply(hash_id)

    if 'integer_columns' in config:
        for column in config['integer_columns']:
            if column in df.columns:
                mean = df[column].mean()
                df[column] = df[column].apply(lambda x: shift_integer_column(x, mean))

    if 'float_columns' in config:
        for column in config['float_columns']:
            if column in df.columns:
                mean = df[column].mean()
                df[column] = df[column].apply(lambda x: shift_float_column(x, mean))

    if 'phone_column' in config and config['phone_column'] in df.columns:
        df[config['phone_column']] = df[config['phone_column']].apply(lambda x: generate_fake_phone() if not pd.isna(x) else x)

    # Generate the output file path with "_deidentified" suffix
    output_file_path = os.path.splitext(input_file_path)[0] + "_deidentified.csv"

    # Save the transformed DataFrame
    df.to_csv(output_file_path, index=False)

    print(f"De-identified file saved to: {output_file_path}")

if __name__ == "__main__":
    import argparse
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="De-identify a CSV file using a configuration YAML file.")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the YAML configuration file (default: config.yaml)."
    )
    parser.add_argument(
        "--input_dir",
        default="./data",
        help="Directory containing the input CSV file (default: ./data)."
    )
    parser.add_argument(
        "--input_file",
        required=True,
        help="Name of the input CSV file."
    )
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(config_path=args.config, input_dir=args.input_dir, input_file=args.input_file)


