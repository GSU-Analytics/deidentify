# Usage

## Using the Script
To run the `deidentify.py` script:
```bash
python deidentify.py --config config.yaml --input_dir ./data --input_file demo.csv
```

### Required Arguments
- `--config`: Path to the YAML configuration file.
- `--input_dir`: Directory containing the input CSV file.
- `--input_file`: Name of the input CSV file.

### Example
```bash
python deidentify.py --config config.yaml --input_dir ./data --input_file demo.csv
```

---

## Using MkDocs

This environment also includes MkDocs for generating and managing documentation.

### Preview Documentation

To preview your documentation locally, run:

```bash
mkdocs serve
```

Open your browser and navigate to `http://127.0.0.1:8000/` to view the documentation.

### Build Static Files

To generate static HTML files for deployment:

```bash
mkdocs build
```

The static files will be available in the `site/` directory.
