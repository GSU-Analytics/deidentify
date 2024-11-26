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

# Define functions
def hash_id(identifier):
    """Hash any ID column to a consistent numeric string."""
    hashed = int(hashlib.sha256(str(identifier).encode('utf-8')).hexdigest(), 16) % (10**12)
    return f"{hashed:012}"

def fake_name():
    """Generate a fake name with first and last name."""
    return {"FN": fake.first_name(), "LN": fake.last_name()}

def anonymize_categories(column):
    """Anonymize categorical column to CATEGORY01, CATEGORY02, etc."""
    unique_values = column.unique()
    mapping = {val: f"CATEGORY{str(i+1).zfill(2)}" for i, val in enumerate(unique_values)}
    return column.map(mapping)

def shift_dates(date, years):
    """Shift a date by a number of years."""
    if pd.isna(date):
        return date
    try:
        return (datetime.strptime(date, "%Y-%m-%d").replace(year=datetime.strptime(date, "%Y-%m-%d").year - years)).strftime("%Y-%m-%d")
    except ValueError:
        return date

def shift_semesters(semester, years):
    """Shift semester by a number of years."""
    if pd.isna(semester) or len(str(semester)) != 6:
        return semester
    try:
        year = int(str(semester)[:4]) + years
        month = str(semester)[4:]
        return f"{year}{month}"
    except ValueError:
        return semester

def shift_integer_column(value, mean):
    """Randomly shift an integer value by +/- 1."""
    if pd.isna(value):
        return value
    return value + random.choice([-1, 0, 1])

def shift_float_column(value, mean):
    """Randomly shift a float value by +/- 0.25."""
    if pd.isna(value):
        return value
    return value + random.uniform(-0.25, 0.25)

def generate_fake_email():
    """Generate a fake email address."""
    return fake.email()

def generate_fake_phone():
    """Generate a fake phone number."""
    return fake.phone_number()

def main(config_path, input_dir, input_file):
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


