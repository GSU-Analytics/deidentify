# Functions

## `hash_id`
Hash a unique identifier into a consistent numeric string.

**Arguments**:

- `identifier`: The identifier to hash.

**Returns**:

A 12-digit hashed numeric string.

**Example**:

```python
>>> hash_id("12345")
'098765432109'
```

---

## `fake_name`
Generate a fake first and last name.

**Returns**:

A dictionary with keys `FN` (first name) and `LN` (last name).

**Example**:

```python
>>> fake_name()
{'FN': 'John', 'LN': 'Doe'}
```

---

## `anonymize_categories`
Anonymize a categorical column by mapping values to generic labels.

**Arguments**:

- `column (pd.Series)`: A Pandas Series containing the categorical data.

**Returns**:

A Pandas Series with the anonymized categories.

**Example**:

```python
>>> anonymize_categories(pd.Series(['A', 'B', 'A']))
0    CATEGORY01
1    CATEGORY02
2    CATEGORY01
dtype: object
```

---

## `shift_dates`
Shift a date backward by a specified number of years.

**Arguments**:

- `date (str)`: The date string to be shifted.
- `years (int)`: The number of years to subtract.

**Returns**:

The adjusted date string, or the original value if invalid.

**Example**:

```python
>>> shift_dates("2024-01-01", 2)
'2022-01-01'
```

---

## `shift_semesters`
Shift a semester identifier (YYYYMM) by a specified number of years.

**Arguments**:

- `semester (str or int)`: The semester identifier to be adjusted.
- `years (int)`: The number of years to add to or subtract from the semester.

**Returns**:

The adjusted semester identifier, or the original value if invalid.

**Example**:

```python
>>> shift_semesters("202401", -2)
'202201'
```

---

## `shift_integer_column`
Randomly adjust an integer value by -1, 0, or +1.

**Arguments**:

- `value (int or float)`: The value to adjust.
- `mean (float)`: The mean of the column (not used in the current implementation).

**Returns**:

The adjusted integer value, or the original value if invalid.

**Example**:

```python
>>> shift_integer_column(5, 4.5)
6
```

---

## `shift_float_column`
Randomly adjust a float value by a small amount (-0.25 to +0.25).

**Arguments**:

- `value (float)`: The value to adjust.
- `mean (float)`: The mean of the column (not used in the current implementation).

**Returns**:

The adjusted float value, or the original value if invalid.

**Example**:

```python
>>> shift_float_column(3.5, 3.6)
3.3
```

---

## `generate_fake_email`
Generate a fake email address.

**Returns**:

A fake email address.

**Example**:

```python
>>> generate_fake_email()
'john.doe@example.com'
```

---

## `generate_fake_phone`
Generate a fake phone number.

**Returns**:

A fake phone number.

**Example**:

```python
>>> generate_fake_phone()
'(555) 123-4567'
```