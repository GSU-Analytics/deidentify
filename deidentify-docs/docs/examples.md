# Examples

This page demonstrates the functionality of the `deidentify.py` script using example input and output files.

## Copying Example Files

To copy the example files (`demo.csv`, `demo_deidentified.csv`, `config.yaml`, etc.) to a specific directory, use the `copy_examples` script:

```bash
copy_examples <destination_directory>
```

---

## Input File: `demo.csv`

The following is an example input CSV file (`demo.csv`). It contains sample student data, including personally identifiable information (PII) such as names, emails, and phone numbers.

```csv
PIDM,FIRST_NAME,LAST_NAME,MOST_RECENT_STUDENT_LEVEL,COLLEGE,MAJOR,ASTD_STATUS,SAP_STATUS,COHORT,GRAD_TERM,MOST_RECENT_TERM_ENROLLED,EMAIL,PHONE,PANTHERID,HOURS_EARNED,OUTSTANDING_FINANCIAL_BALANCE,INSTITUTIONAL_GPA,OVERALL_GPA
123456,John,Doe,Freshman,Arts,History,Active,Good,202101,202305,202401,john.doe@example.com,555-123-4567,890123,15,500.50,3.4,3.6
234567,Jane,Smith,Sophomore,Engineering,Computer Science,Active,Warning,202002,202406,202402,jane.smith@example.com,555-987-6543,123456,30,0.00,3.8,3.9
345678,Alice,Brown,Junior,Science,Biology,Inactive,Probation,202003,202405,202403,alice.brown@example.com,555-456-7890,789012,45,1200.75,2.5,2.6
456789,Bob,Johnson,Senior,Business,Marketing,Active,Good,202004,202404,202404,bob.johnson@example.com,555-321-6548,567890,60,200.25,3.2,3.3
567890,Mary,White,Freshman,Nursing,Nursing,Active,Good,202005,202303,202405,mary.white@example.com,555-789-1234,345678,12,800.10,4.0,3.9
678901,James,Davis,Senior,Law,Pre-Law,Inactive,Good,202006,202406,202406,james.davis@example.com,555-654-9876,234567,60,100.00,2.9,3.0
```

---

## Output File: `demo_deidentified.csv`

After running the `deidentify.py` script on `demo.csv`, the output file (`demo_deidentified.csv`) contains de-identified data. The script replaces PII with hashed or fake values and anonymizes other sensitive columns.

### Output Example

```csv
PIDM,FIRST_NAME,LAST_NAME,MOST_RECENT_STUDENT_LEVEL,COLLEGE,MAJOR,ASTD_STATUS,SAP_STATUS,COHORT,GRAD_TERM,MOST_RECENT_TERM_ENROLLED,EMAIL,PHONE,PANTHERID,HOURS_EARNED,OUTSTANDING_FINANCIAL_BALANCE,INSTITUTIONAL_GPA,OVERALL_GPA
432019864722,Elizabeth,Swanson,CATEGORY01,CATEGORY01,CATEGORY01,CATEGORY01,CATEGORY01,202301,202505,202601,rebeccasanchez@example.org,8189337672,314032743269,16,500.6063399559087,3.203057793008891,3.6061180075905495
566881358185,Matthew,Moore,CATEGORY02,CATEGORY02,CATEGORY02,CATEGORY01,CATEGORY02,202202,202606,202602,trichard@example.net,(786)315-0721x7795,432019864722,29,-0.19413324184944286,3.9646301652937486,4.092289707854811
197119148968,Jamie,Johnson,CATEGORY03,CATEGORY03,CATEGORY03,CATEGORY02,CATEGORY03,202203,202605,202603,rita51@example.net,(951)427-9904x122,284893643451,46,1200.8592521436192,2.470694643359418,2.5655249945213976
234889864989,Sharon,Hughes,CATEGORY04,CATEGORY04,CATEGORY04,CATEGORY01,CATEGORY01,202204,202604,202604,andreamendoza@example.org,509-634-9063x814,849592214141,59,200.43628504721414,3.1988226475227637,3.2212546949824254
849592214141,Daniel,Allison,CATEGORY01,CATEGORY05,CATEGORY05,CATEGORY01,CATEGORY01,202205,202503,202605,becksusan@example.org,+1-266-489-8789x51883,197119148968,13,799.9231303982539,3.825228675431672,3.7616782781797102
```

---

## How to Use the Example Files

1. Confirm `demo.csv` is in the `data` directory. If not, use the `copy_examples` command outlined above.
2. Use the following configuration in your `config.yaml` file:

```yaml
file_path: "./data/demo.csv"
id_column: PIDM
first_name_column: FIRST_NAME
last_name_column: LAST_NAME
email_column: EMAIL
phone_column: PHONE
shift_years: 2
categorical_columns:
  - MOST_RECENT_STUDENT_LEVEL
  - COLLEGE
  - MAJOR
semester_columns:
  - COHORT
  - GRAD_TERM
  - MOST_RECENT_TERM_ENROLLED
integer_columns:
  - HOURS_EARNED
float_columns:
  - OUTSTANDING_FINANCIAL_BALANCE
  - INSTITUTIONAL_GPA
  - OVERALL_GPA
```

3. Run the script:
  ```bash
  python deidentify.py --config config.yaml --input_dir ./data --input_file demo.csv
  ```

4. The output file (`demo_deidentified.csv`) will be saved in the same directory.