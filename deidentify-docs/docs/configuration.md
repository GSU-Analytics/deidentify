# Configuration File

The `config.yaml` file customizes how data is de-identified. This file allows you to define how each column in your dataset should be processed.

---

## Example `config.yaml`

```yaml
file_path: "./data/demo.csv"

# Column configurations
id_column: PIDM  # Unique identifier to hash
first_name_column: FIRST_NAME  # Optional first name column for de-identification
last_name_column: LAST_NAME  # Optional last name column for de-identification

# Year shift for dates
shift_years: 2  # Number of years to shift backward (set to 0 for no shift)

# Columns to be anonymized
categorical_columns:
  - MOST_RECENT_STUDENT_LEVEL
  - COLLEGE
  - MAJOR
  - ASTD_STATUS
  - SAP_STATUS

# Semester columns in YYYYMM format to shift
semester_columns:
  - COHORT
  - GRAD_TERM
  - MOST_RECENT_TERM_ENROLLED

# Optional columns to de-identify
email_column: EMAIL  # De-identify email column
phone_column: PHONE  # De-identify phone number column
student_id_column: PANTHERID  # Another ID column to hash

# Integer columns to adjust randomly by +/- 1
integer_columns:
  - HOURS_EARNED

# Float columns to adjust randomly by +/- 0.25
float_columns:
  - OUTSTANDING_FINANCIAL_BALANCE
  - INSTITUTIONAL_GPA
  - OVERALL_GPA
```

---

## Key Descriptions

### `file_path`
- **Description**: Path to the input CSV file to be de-identified.
- **Type**: String
- **Example**:

```yaml
file_path: "./data/demo.csv"
```

---

### `id_column`
- **Description**: Name of the column containing unique identifiers to hash.
- **Type**: String
- **Example**:

```yaml
id_column: PIDM
```

---

### `first_name_column` (Optional)
- **Description**: Name of the column containing first names to de-identify by replacing with fake names.
- **Type**: String
- **Example**:

```yaml
first_name_column: FIRST_NAME
```

---

### `last_name_column` (Optional)
- **Description**: Name of the column containing last names to de-identify by replacing with fake names.
- **Type**: String
- **Example**:

```yaml
last_name_column: LAST_NAME
```

---

### `shift_years`
- **Description**: Number of years to shift date and semester columns backward. Use `0` for no shifting.
- **Type**: Integer
- **Default**: 0
- **Example**:

```yaml
shift_years: 2
```

---

### `categorical_columns`
- **Description**: List of columns containing categorical data to anonymize.
- **Type**: List of Strings
- **Example**:

```yaml
categorical_columns:
    - MOST_RECENT_STUDENT_LEVEL
    - COLLEGE
    - MAJOR
```

---

### `semester_columns`
- **Description**: List of columns containing semester identifiers in the format `YYYYMM` to adjust.
- **Type**: List of Strings
- **Example**:

```yaml
semester_columns:
- COHORT
- GRAD_TERM
```

---

### `email_column` (Optional)
- **Description**: Name of the column containing email addresses to replace with fake emails.
- **Type**: String
- **Example**:

```yaml
email_column: EMAIL
```

---

### `phone_column` (Optional)
- **Description**: Name of the column containing phone numbers to replace with fake numbers.
- **Type**: String
- **Example**:

```yaml
phone_column: PHONE
```

---

### `student_id_column` (Optional)
- **Description**: Name of the column containing student IDs to hash.
- **Type**: String
- **Example**:

```yaml
student_id_column: PANTHERID
```

---

### `integer_columns`
- **Description**: List of columns containing integer values to randomly adjust by +/- 1.
- **Type**: List of Strings
- **Example**:

```yaml
integer_columns:
- HOURS_EARNED
```

---

### `float_columns`
- **Description**: List of columns containing float values to randomly adjust by +/- 0.25.
- **Type**: List of Strings
- **Example**:

```yaml
float_columns:
- OUTSTANDING_FINANCIAL_BALANCE
- INSTITUTIONAL_GPA
- OVERALL_GPA
```