---
marp: true
theme: default
paginate: true
header: "CSV Data & Charts Tutorial"
footer: "Flet & Python"
style: |
  section {
    font-size: 28px;
  }
  code {
    background-color: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
  }
---

# Reading CSV Data and Creating Charts

## Learning Objectives

- Read data from CSV files
- Use string methods (`strip()`, `split()`) to parse text data
- Understand tuples, sets, and Python iterators
- Use tuple unpacking for cleaner code
- Create interactive charts using `flet-charts`
- Write tests using `assert` statements

---

# What We're Building

## Sales Data Visualization App

- Read monthly sales and expenses from a CSV file
- Display data in an interactive bar chart
- Show summary statistics (totals, profit)
- Beautiful, modern UI with Flet

**Demo: Show the final running app**

---

# Understanding CSV Files

## Comma-Separated Values

```text
Month,Sales,Expenses
January,4500,3200
February,5200,3400
March,4800,3100
```

- Each line is a **row**
- Values separated by **commas**
- First line often contains **headers**
- Like a spreadsheet saved as text

---

# Reading Files in Python

## Method 1: Basic File Reading

```python
file = open("data.csv", "r")
content = file.read()
file.close()  # Important!
```

**Problem:** Easy to forget to close the file!

---

# Reading Files in Python

## Method 2: Using `with` Statement (Better!)

```python
with open("data.csv", "r") as file:
    content = file.read()
    # File automatically closes here
```

**Benefits:**

- Automatic cleanup
- No memory leaks
- Cleaner code

---

# Reading Files Line by Line

```python
with open("data.csv", "r") as file:
    lines = file.readlines()
    # lines = ["Month,Sales,Expenses\n",
    #          "January,4500,3200\n", ...]
```

- `readlines()` returns a list of lines
- Each line includes the newline character `\n`

---

# String Methods: `split()`

## Breaking Strings Apart

```python
line = "January,4500,3200"
parts = line.split(",")
# parts = ["January", "4500", "3200"]
```

- `split()` breaks a string into a **list**
- Split by any character: `split(",")`, `split(" ")`, etc.

---

# String Methods: `strip()`

## Removing Whitespace

```python
text = "  January  \n"
cleaned = text.strip()
# cleaned = "January"
```

- Removes spaces and newlines from **both ends**
- `rstrip()` - right side only
- `lstrip()` - left side only

**Why important?** CSV files often have extra whitespace!

---

# String Slicing

## Extracting Parts of Strings

```python
month = "January"
first_three = month[0:3]   # "Jan"
last_three = month[-3:]    # "ary"
```

- Use indices to extract substrings
- Negative indices count from the end
- `[start:end]` - includes start, excludes end

---

# Tuples: Immutable Sequences

## Creating Tuples

```python
point = (10, 20)  # Coordinates
month_data = ("January", 4500, 3200)
```

- Use parentheses `()`
- **Immutable** - can't change after creation
- Perfect for fixed data

```python
# This would cause an error:
point[0] = 15  # ❌
```

---

# Tuple Unpacking

## Assigning Multiple Variables at Once

```python
# Instead of:
parts = line.split(",")
month = parts[0]
sales = int(parts[1])
expenses = int(parts[2])

# Use tuple unpacking:
month, sales_str, expenses_str = line.split(",")
```

**Cleaner and more readable!**

---

# Sets: Unique Collections

## Creating Sets

```python
unique_months = {"January", "February", "March"}
numbers = {1, 2, 3, 4, 5}
```

- Use curly braces `{}`
- **Automatically removes duplicates**
- Great for checking membership: `"January" in unique_months`

---

# Sets: Operations

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2        # {1, 2, 3, 4, 5}
intersection = set1 & set2 # {3}
difference = set1 - set2    # {1, 2}
```

Useful for mathematical set operations!

---

# Python Iterators: Comparison

| Type       | Syntax      | Mutable? | Ordered? | Duplicates? |
| ---------- | ----------- | -------- | -------- | ----------- |
| **List**   | `[1, 2, 3]` | ✅ Yes   | ✅ Yes   | ✅ Yes      |
| **Tuple**  | `(1, 2, 3)` | ❌ No    | ✅ Yes   | ✅ Yes      |
| **Set**    | `{1, 2, 3}` | ✅ Yes   | ❌ No    | ❌ No       |
| **Dict**   | `{"a": 1}`  | ✅ Yes   | ✅ Yes   | Keys: No    |
| **String** | `"abc"`     | ❌ No    | ✅ Yes   | ✅ Yes      |

---

# When to Use Each Iterator

- **Lists**: General purpose, can modify
- **Tuples**: Fixed data, coordinates
- **Sets**: Unique values, membership tests
- **Dicts**: Key-value relationships
- **Strings**: Text data

**All can be iterated with `for` loops!**

---

# Parsing CSV Data: Step 1

## Read the File

```python
def read_csv(filename: str) -> list[dict]:
    data = []

    with open(filename, "r") as file:
        lines = file.readlines()
```

- Open file with `with` statement
- Read all lines into a list

---

# Parsing CSV Data: Step 2

## Skip Header and Process Lines

```python
    # Skip the header line (first line)
    for line in lines[1:]:
        line = line.strip()  # Remove newline

        if not line:  # Skip empty lines
            continue
```

- `lines[1:]` skips first line (header)
- `strip()` removes whitespace
- Skip empty lines

---

# Parsing CSV Data: Step 3

## Parse Each Line

```python
        # Split by comma and use tuple unpacking
        month, sales_str, expenses_str = line.split(",")

        # Extract and convert values
        month = month.strip()
        sales = int(sales_str.strip())
        expenses = int(expenses_str.strip())
```

- Tuple unpacking makes code cleaner
- Convert strings to integers

---

# Parsing CSV Data: Step 4

## Store in Dictionary

```python
        # Store in dictionary
        data.append({
            "month": month,
            "sales": sales,
            "expenses": expenses
        })

    return data
```

- Build a list of dictionaries
- Each dictionary represents one month

---

# Error Handling

```python
try:
    data = read_csv("data.csv")
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Could not convert to number!")
```

**Better:** Build error handling into the function!

---

# Calculating Totals

```python
def calculate_totals(data: list[dict]) -> dict:
    total_sales = sum(item["sales"] for item in data)
    total_expenses = sum(item["expenses"] for item in data)
    total_profit = total_sales - total_expenses

    return {
        "sales": total_sales,
        "expenses": total_expenses,
        "profit": total_profit
    }
```

- Use list comprehensions with `sum()`
- Return a dictionary with totals

---

# Installing flet-charts

```bash
uv add flet-charts
```

- Flet extension for creating charts
- Works seamlessly with Flet apps

---

# Importing Chart Components

```python
import flet as ft
from flet_charts import (
    BarChart,
    BarChartGroup,
    BarChartRod,
    ChartAxis,
    ChartAxisLabel
)
```

- `BarChart` - the main chart
- `BarChartGroup` - group of bars (e.g., one month)
- `BarChartRod` - individual bar
- `ChartAxis` - axis configuration
- `ChartAxisLabel` - custom axis labels

---

# Creating a Bar Chart: Step 1

## Find Maximum Value

```python
def create_sales_chart(data):
    # Find max value to determine y-axis range
    max_value = max(max(item["sales"], item["expenses"])
                    for item in data)
    max_y = ((max_value // 1000) + 1) * 1000
```

- Calculate max value from data
- Round up to nearest 1000 for clean labels

---

# Creating a Bar Chart: Step 2

## Create Bar Groups

```python
    groups = []
    bottom_labels = []

    for index, item in enumerate(data):
        month_short = item["month"][:3]  # "Jan", "Feb", etc.

        group = BarChartGroup(
            x=index,  # Must be integer!
            rods=[...]
        )
```

- `x` must be an **integer**, not a string
- Use `enumerate()` to get index

---

# Creating a Bar Chart: Step 3

## Create Individual Bars

```python
        group = BarChartGroup(
            x=index,
            rods=[
                BarChartRod(
                    from_y=0,
                    to_y=item["sales"],
                    color=ft.Colors.BLUE_400,
                    width=25,
                    tooltip=f"Sales: ${item['sales']:,}",
                ),
                BarChartRod(
                    from_y=0,
                    to_y=item["expenses"],
                    color=ft.Colors.RED_400,
                    width=25,
                    tooltip=f"Expenses: ${item['expenses']:,}",
                ),
            ],
            spacing=4,  # Space between bars
        )
```

---

# Creating a Bar Chart: Step 4

## Create Custom Axis Labels

```python
        # X-axis labels
        bottom_labels.append(
            ChartAxisLabel(value=index, label=month_short)
        )

    # Y-axis labels
    left_labels = []
    for value in range(0, max_y + 1000, 1000):
        label_text = f"{value // 1000}K" if value > 0 else "0"
        left_labels.append(
            ChartAxisLabel(value=value, label=ft.Text(label_text))
        )
```

- Custom labels for better formatting
- Use `ft.Text` for consistent rendering

---

# Creating a Bar Chart: Step 5

## Build the Chart

```python
    chart = BarChart(
        groups=groups,
        group_spacing=12,
        width=900,
        height=450,
        margin=ft.Margin.only(left=24),
        left_axis=ChartAxis(
            labels=left_labels,
            label_size=18,
            label_spacing=12,
        ),
        bottom_axis=ChartAxis(
            title=ft.Text("Month"),
            labels=bottom_labels
        ),
    )

    return chart
```

---

# Flet 0.80+ API Changes

## Important Updates

- `ft.colors` → `ft.Colors` (uppercase)
- `ft.app(target=main)` → `ft.run(main)`
- `ft.margin.only()` → `ft.Margin.only()`
- `ft.border.all()` → `ft.Border.all()`

**Make sure you're using the correct syntax!**

---

# Building the Complete App

## Main Function Structure

```python
def main(page: ft.Page):
    page.title = "Sales Data Visualization"
    page.padding = 30

    # 1. Read data
    data = read_csv("data.csv")

    # 2. Calculate totals
    totals = calculate_totals(data)

    # 3. Create chart
    chart = create_sales_chart(data)

    # 4. Build UI
    page.add(...)
```

---

# Building the UI

## Add Components to Page

```python
    page.add(
        # Title
        ft.Text("Monthly Sales and Expenses",
                size=28, weight=ft.FontWeight.BOLD),

        # Summary statistics
        ft.Row([...totals...]),

        # Chart
        ft.Container(content=chart, ...),

        # Legend
        ft.Row([...legend items...]),
    )
```

---

# Running the App

```python
if __name__ == "__main__":
    ft.run(main)
```

**Run with:**

```bash
uv run flet main.py
```

---

# Testing with `assert`

## Why Test Code?

- Catch bugs before users see them
- Make sure code works correctly
- Confidence when making changes

**Types:**

- Manual testing (running the app)
- Automated testing (code that tests code)

---

# Understanding `assert`

```python
# assert checks if something is True
assert 2 + 2 == 4  # ✅ Passes (does nothing)

assert 2 + 2 == 5  # ❌ Fails (raises AssertionError)
```

- If condition is `True` → nothing happens
- If condition is `False` → raises `AssertionError`
- Use to verify code does what you expect

---

# Pure Functions

## What Makes a Function "Pure"?

- Always returns the same output for the same input
- Doesn't modify anything outside the function
- Doesn't depend on external state (files, network, time)

**Examples:**

- ✅ `calculate_totals()` - pure function
- ❌ `read_csv()` - NOT pure (depends on file system)

---

# Testing `calculate_totals()`

```python
def test_calculate_totals():
    test_data = [
        {"month": "January", "sales": 1000, "expenses": 500},
        {"month": "February", "sales": 2000, "expenses": 800}
    ]

    result = calculate_totals(test_data)

    assert result["sales"] == 3000
    assert result["expenses"] == 1300
    assert result["profit"] == 1700

    print("All tests passed!")
```

---

# Testing Edge Cases

```python
def test_calculate_totals_empty():
    result = calculate_totals([])

    assert result["sales"] == 0
    assert result["expenses"] == 0
    assert result["profit"] == 0

def test_calculate_totals_single_item():
    test_data = [{"month": "January",
                  "sales": 5000,
                  "expenses": 3000}]
    result = calculate_totals(test_data)

    assert result["sales"] == 5000
    assert result["profit"] == 2000
```

**Always test edge cases!**

---

# Key Takeaways

- Files are opened with `open()` and closed (or use `with`)
- String methods (`split()`, `strip()`) help parse text data
- Tuples are immutable sequences, perfect for fixed data
- Tuple unpacking makes code cleaner and more readable
- Sets store unique values and support set operations
- Different iterators have different use cases
- CSV files are just text files with a specific format
- Charts make data easier to understand

---

# What's Next?

- Try different chart types (LineChart, PieChart)
- Read data from APIs instead of files
- Add interactivity (click to filter, hover for details)
- Write data back to files
- Write more tests for your functions
- Learn about unit testing frameworks (like `pytest`)

---

# Practice Exercises

1. Modify the chart: Change colors or bar widths
2. Add calculations: Show profit as a third bar
3. Filter data: Only show months with sales > 6000
4. Write to file: Save processed data to a new CSV
5. Write tests: Create tests for `calculate_totals()` with different data
6. Test edge cases: Empty data, negative numbers, large numbers
7. Use tuples: Modify code to return tuples instead of dictionaries
8. Use sets: Create a set of unique month names

---

# Questions?

## Let's Build Something Amazing! 🚀
