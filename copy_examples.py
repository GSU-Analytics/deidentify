import os
import shutil
from pathlib import Path

def copy_examples_to(destination_dir=None):
    """
    Copy example files, configuration files, and the data directory to a user-specified directory.
    
    Parameters:
    - destination_dir (str): Path to the directory where the files should be copied.
                             If not provided, defaults to the current working directory.
    """
    # The package directory
    package_dir = Path(__file__).resolve().parent

    # Paths to files and directories to copy
    files_to_copy = [
        package_dir / "deidentify-env.yaml",
        package_dir / "config.yaml",
        package_dir / "deidentify.py",
    ]
    directories_to_copy = [
        package_dir / "data",
    ]

    # Set destination directory
    if destination_dir is None:
        destination_dir = Path.cwd()
    else:
        destination_dir = Path(destination_dir)

    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    print(f"Destination directory: {destination_dir}")

    # Copy files
    for file in files_to_copy:
        if file.exists():
            shutil.copy(file, destination_dir)
            print(f"Copied '{file.name}' to '{destination_dir}'")
        else:
            print(f"File '{file.name}' not found!")

    # Copy directories
    for directory in directories_to_copy:
        if directory.exists():
            shutil.copytree(directory, destination_dir / directory.name, dirs_exist_ok=True)
            print(f"Copied directory '{directory.name}' to '{destination_dir}'")
        else:
            print(f"Directory '{directory.name}' not found!")

if __name__ == "__main__":
    copy_examples_to()
