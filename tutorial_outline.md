# Tutorial: Reading CSV Data and Creating Charts with Flet

## Learning Objectives

By the end of this tutorial, students will be able to:

- Read data from CSV files
- Use string methods (`strip()`, `split()`) to parse text data
- Understand tuples, sets, and differences between Python iterators
- Use tuple unpacking for cleaner code
- Process CSV-style data manually
- Create interactive charts using `flet-charts`
- Display data visualizations in a Flet application
- Write tests using `assert` statements
- Test pure functions

## Concepts Covered

### From Checklist

- **Section C: File I/O**

  - [x] Read text files
  - [x] CSV-style parsing
  - [x] Strip newline and whitespace

- **Section B: Programming Fundamentals**

  - [x] String slicing and string methods
  - [x] Tuple basics (creation, unpacking)
  - [x] Sets and iterator differences

- **Section J: Testing & Debugging**
  - [x] Use `assert` for lightweight testing
  - [x] Test pure functions

## 1. Introduction & Demo (0:00–2:00)

- Show final running app:
  - A Flet window displaying a bar chart
  - Chart shows monthly sales and expenses data
  - Data loaded from a CSV file
- Explain purpose:
  - Learn to read and process data from files
  - Visualize data using charts
  - Build a practical data analysis tool
- Learning goals:
  - Understand file I/O basics
  - Master string methods for parsing
  - Create data visualizations

---

## 2. Understanding CSV Files (2:00–4:00)

- What is a CSV file?
  - Comma-Separated Values
  - Each line is a row
  - Values separated by commas
  - First line often contains headers
- Show the data file structure:
  - `Month,Sales,Expenses`
  - `January,4500,3200`
  - etc.
- Real-world analogy:
  - Like a spreadsheet saved as text
  - Easy for programs to read and process

---

## 3. Reading Files in Python (4:00–7:00)

### 3.1 Opening and Reading a File

```python
# Open the file
file = open("data.csv", "r")

# Read all lines
content = file.read()

# Close the file
file.close()
```

- Explain file modes: `"r"` for reading
- Show the `read()` method returns the entire file as a string
- **Important**: Always close files!

### 3.2 Using `with` Statement (Better Way)

```python
# Automatically closes the file
with open("data.csv", "r") as file:
    content = file.read()
```

- Explain why `with` is better (automatic cleanup)
- Show reading line by line with `readlines()`

---

## 4. String Methods for Parsing (7:00–12:00)

### 4.1 Splitting Strings

```python
line = "January,4500,3200"
parts = line.split(",")
# parts = ["January", "4500", "3200"]
```

- `split()` breaks a string into a list
- Show splitting by different characters

### 4.2 Stripping Whitespace

```python
text = "  January  \n"
cleaned = text.strip()
# cleaned = "January"
```

- `strip()` removes spaces and newlines from ends
- Why it's important: CSV files often have extra whitespace
- Show `rstrip()` and `lstrip()` variants

### 4.3 String Slicing (Optional)

```python
month = "January"
first_three = month[0:3]  # "Jan"
last_three = month[-3:]   # "ary"
```

- Extract parts of strings using indices
- Negative indices count from the end

---

## 4.4 Tuples, Sets, and Python Iterators (12:00–16:00)

### 4.4.1 Tuples - Immutable Sequences

```python
# Creating tuples
point = (10, 20)  # Coordinates
month_data = ("January", 4500, 3200)  # Month, sales, expenses

# Tuples are immutable (can't change after creation)
# point[0] = 15  # This would cause an error!

# Tuple unpacking
month, sales, expenses = ("January", 4500, 3200)
# month = "January"
# sales = 4500
# expenses = 3200

# Multiple assignment (uses tuple unpacking)
x, y = 10, 20
```

- Tuples are like lists but **immutable** (can't be changed)
- Use parentheses `()` to create tuples
- Perfect for fixed data that shouldn't change
- Tuple unpacking lets you assign multiple variables at once

### 4.4.2 Sets - Unique Collections

```python
# Creating sets
unique_months = {"January", "February", "March"}
numbers = {1, 2, 3, 4, 5}

# Sets automatically remove duplicates
duplicates = {1, 2, 2, 3, 3, 3}
# duplicates = {1, 2, 3}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2  # {1, 2, 3, 4, 5}
intersection = set1 & set2  # {3}
difference = set1 - set2  # {1, 2}
```

- Sets store **unique** values (no duplicates)
- Use curly braces `{}` to create sets
- Great for checking membership: `"January" in unique_months`
- Useful for mathematical set operations

### 4.4.3 Python Iterators - Understanding the Differences

Python has several iterable types. Here's when to use each:

| Type       | Syntax      | Mutable? | Ordered? | Duplicates?           | Use Case                        |
| ---------- | ----------- | -------- | -------- | --------------------- | ------------------------------- |
| **List**   | `[1, 2, 3]` | ✅ Yes   | ✅ Yes   | ✅ Yes                | General purpose, can modify     |
| **Tuple**  | `(1, 2, 3)` | ❌ No    | ✅ Yes   | ✅ Yes                | Fixed data, coordinates         |
| **Set**    | `{1, 2, 3}` | ✅ Yes   | ❌ No    | ❌ No                 | Unique values, membership tests |
| **Dict**   | `{"a": 1}`  | ✅ Yes   | ✅ Yes\* | Keys: No, Values: Yes | Key-value pairs                 |
| **String** | `"abc"`     | ❌ No    | ✅ Yes   | ✅ Yes                | Text data                       |

\* Dicts maintain insertion order (Python 3.7+)

```python
# All can be iterated with for loops
for item in [1, 2, 3]:  # List
    print(item)

for item in (1, 2, 3):  # Tuple
    print(item)

for item in {1, 2, 3}:  # Set
    print(item)

for key in {"a": 1, "b": 2}:  # Dict (iterates keys)
    print(key)

for char in "abc":  # String
    print(char)
```

- **Lists**: Use when you need to add, remove, or modify items
- **Tuples**: Use for fixed data, coordinates, or when you want immutability
- **Sets**: Use when you need unique values or fast membership testing
- **Dicts**: Use for key-value relationships
- **Strings**: Use for text data

### 4.4.4 Using Tuple Unpacking in CSV Parsing

```python
# Instead of accessing by index:
parts = line.split(",")
month = parts[0]
sales = int(parts[1])
expenses = int(parts[2])

# We can use tuple unpacking:
parts = line.split(",")
month, sales_str, expenses_str = parts[0], parts[1], parts[2]
sales = int(sales_str)
expenses = int(expenses_str)

# Or even more concisely:
month, sales_str, expenses_str = line.split(",")
sales = int(sales_str)
expenses = int(expenses_str)
```

- Tuple unpacking makes code cleaner and more readable
- Reduces errors from index mistakes
- Shows intent more clearly

---

## 5. Parsing CSV Data (16:00–22:00)

### 5.1 Step-by-Step Parsing

```python
def read_csv(filename: str) -> list[dict]:
    data = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Skip the header line (first line)
        for line in lines[1:]:
            # Remove newline and any extra whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split by comma and use tuple unpacking
            month, sales_str, expenses_str = line.split(",")

            # Extract and convert values
            month = month.strip()
            sales = int(sales_str.strip())
            expenses = int(expenses_str.strip())

            # Store in dictionary
            data.append({"month": month, "sales": sales, "expenses": expenses})

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []
    except ValueError as e:
        print(f"Error: Could not parse data - {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

    return data
```

- Walk through each step
- Explain why we skip the first line (header)
- Show converting strings to integers
- Build a list of dictionaries

### 5.2 Calculating Totals

```python
def calculate_totals(data: list[dict]) -> dict:
    """Calculate total sales and expenses."""
    total_sales = sum(item["sales"] for item in data)
    total_expenses = sum(item["expenses"] for item in data)
    total_profit = total_sales - total_expenses

    return {"sales": total_sales, "expenses": total_expenses, "profit": total_profit}
```

- Show how to calculate summary statistics
- Use list comprehensions with `sum()`
- Return a dictionary with totals

### 5.3 Error Handling

```python
# Error handling is built into read_csv function
data = read_csv("data.csv")

if not data:
    # Handle the case where data couldn't be loaded
    print("Could not load data!")
```

- Handle missing files
- Handle invalid data

---

## 6. Installing and Using flet-charts (22:00–26:00)

### 6.1 Installation

```bash
uv add flet-charts
```

- Show adding the package
- Explain it's a Flet extension for charts

### 6.2 Importing

```python
import flet as ft
from flet_charts import BarChart, BarChartGroup, BarChartRod, ChartAxis, ChartAxisLabel
```

- Show the import statements
- Explain the chart components
- `ChartAxis` and `ChartAxisLabel` are needed for custom axis labels

---

## 7. Creating a Bar Chart (26:00–34:00)

### 7.1 Setting Up the Chart

```python
def create_sales_chart(data):
    groups = []
    bottom_labels = []

    # Find max value to determine y-axis range
    max_value = max(max(item["sales"], item["expenses"]) for item in data)
    # Round up to nearest 1000 for clean axis labels
    max_y = ((max_value // 1000) + 1) * 1000

    for index, item in enumerate(data):
        # Use first 3 letters of month name for x-axis label
        month_short = item["month"][:3]

        # Create a group with two bars: sales and expenses
        # x must be an integer index
        group = BarChartGroup(
            x=index,
            rods=[
                # Sales bar (blue)
                BarChartRod(
                    from_y=0,
                    to_y=item["sales"],
                    color=ft.Colors.BLUE_400,
                    width=25,
                    tooltip=f"Sales: ${item['sales']:,}",
                ),
                # Expenses bar (red)
                BarChartRod(
                    from_y=0,
                    to_y=item["expenses"],
                    color=ft.Colors.RED_400,
                    width=25,
                    tooltip=f"Expenses: ${item['expenses']:,}",
                ),
            ],
            spacing=4,  # Space between rods in the group
        )
        groups.append(group)

        # Create custom label for x-axis
        bottom_labels.append(ChartAxisLabel(value=index, label=month_short))

    # Create custom labels for y-axis (left axis) with proper formatting
    left_labels = []
    # Create labels every 1000 (0, 1K, 2K, 3K, etc.)
    for value in range(0, max_y + 1000, 1000):
        if value == 0:
            label_text = "0"
        else:
            label_text = f"{value // 1000}K"
        # Use ft.Text to ensure consistent horizontal rendering
        left_labels.append(ChartAxisLabel(value=value, label=ft.Text(label_text)))

    # Create the chart with all groups
    chart = BarChart(
        groups=groups,
        group_spacing=12,
        width=900,
        height=450,
        margin=ft.Margin.only(left=24),  # Add padding to the left for Y-axis labels
        left_axis=ChartAxis(
            labels=left_labels,
            label_size=18,
            label_spacing=12,
        ),
        bottom_axis=ChartAxis(title=ft.Text("Month"), labels=bottom_labels),
    )

    return chart
```

- Explain each component
- Show how bars are positioned using integer indices
- Explain that `x` must be an integer, not a string
- Show how to create custom axis labels with `ChartAxisLabel`
- Explain colors using `ft.Colors` (uppercase) for Flet 0.80+
- Explain tooltips with number formatting
- Show how to calculate max value for proper y-axis range

### 7.2 Adding Chart to Flet Page

```python
def main(page: ft.Page):
    page.title = "Sales Data Visualization"
    page.padding = 30
    page.scroll = "auto"

    # Read data from CSV file
    data = read_csv("data.csv")

    if not data:
        # Show error message if no data loaded
        page.add(
            ft.Text(
                "Error: Could not load data from CSV file.",
                color=ft.Colors.RED,
                size=18,
            )
        )
        return

    # Calculate totals
    totals = calculate_totals(data)

    # Create chart
    chart = create_sales_chart(data)

    # Build the UI
    page.add(
        # Title
        ft.Text(
            "Monthly Sales and Expenses",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_700,
        ),
        # Summary statistics
        ft.Container(
            content=ft.Row(
                [
                    ft.Text(
                        f"Total Sales: ${totals['sales']:,}",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLUE_700,
                    ),
                    ft.Text(
                        f"Total Expenses: ${totals['expenses']:,}",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.RED_700,
                    ),
                    ft.Text(
                        f"Total Profit: ${totals['profit']:,}",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.GREEN_700,
                    ),
                ],
                spacing=30,
            ),
            margin=ft.Margin.only(bottom=20),
        ),
        # Chart
        ft.Container(
            content=chart,
            padding=20,
            border=ft.Border.all(1, ft.Colors.GREY_300),
            border_radius=10,
        ),
        # Legend
        ft.Row(
            [
                ft.Container(
                    width=20, height=20, bgcolor=ft.Colors.BLUE_400, border_radius=4
                ),
                ft.Text("Sales", size=14),
                ft.Container(width=30),  # Spacing
                ft.Container(
                    width=20, height=20, bgcolor=ft.Colors.RED_400, border_radius=4
                ),
                ft.Text("Expenses", size=14),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            margin=ft.Margin.only(top=20),
        ),
    )


if __name__ == "__main__":
    ft.run(main)
```

- Show complete app structure
- Explain the flow: read → process → calculate → visualize
- Note: Use `ft.run(main)` instead of `ft.app(target=main)` for Flet 0.80+
- Use `ft.Colors` (uppercase) instead of `ft.colors` for Flet 0.80+
- Use `ft.Margin.only()` and `ft.Border.all()` instead of `ft.margin.only()` and `ft.border.all()`

---

## 8. Complete Example Walkthrough (34:00–39:00)

- Show the complete code
- Run the application
- Explain each section
- Answer common questions

---

## 9. Testing with `assert` (39:00–46:00)

### 9.1 What is Testing?

- Why test code?
  - Catch bugs before users see them
  - Make sure code works correctly
  - Confidence when making changes
- Types of testing:
  - Manual testing (running the app)
  - Automated testing (code that tests code)

### 9.2 Understanding `assert`

```python
# assert checks if something is True
assert 2 + 2 == 4  # This passes (does nothing)

assert 2 + 2 == 5  # This fails (raises AssertionError)
```

- `assert` is a simple way to check if code works correctly
- If the condition is `True`, nothing happens
- If the condition is `False`, Python raises an `AssertionError`
- Use it to verify your code does what you expect

### 9.3 What are Pure Functions?

- **Pure functions**:
  - Always return the same output for the same input
  - Don't modify anything outside the function
  - Don't depend on external state (like files, network, time)
- Examples from our code:
  - `calculate_totals()` - pure function
  - `read_csv()` - NOT pure (depends on file system)
- Why test pure functions?
  - Easy to test (same input → same output)
  - No side effects to worry about
  - Fast to run

### 9.4 Testing `calculate_totals()`

```python
def test_calculate_totals():
    # Test data
    test_data = [
        {"month": "January", "sales": 1000, "expenses": 500},
        {"month": "February", "sales": 2000, "expenses": 800}
    ]

    # Call the function
    result = calculate_totals(test_data)

    # Test the results
    assert result["sales"] == 3000, "Total sales should be 3000"
    assert result["expenses"] == 1300, "Total expenses should be 1300"
    assert result["profit"] == 1700, "Total profit should be 1700"

    print("All tests passed!")

# Run the test
test_calculate_totals()
```

- Walk through each assertion
- Explain the test data
- Show what happens when tests pass
- Show what happens when tests fail

### 9.5 Testing Edge Cases

```python
def test_calculate_totals_empty():
    # Test with empty data
    result = calculate_totals([])

    assert result["sales"] == 0, "Empty list should return 0 sales"
    assert result["expenses"] == 0, "Empty list should return 0 expenses"
    assert result["profit"] == 0, "Empty list should return 0 profit"

    print("Empty data test passed!")

def test_calculate_totals_single_item():
    # Test with one item
    test_data = [{"month": "January", "sales": 5000, "expenses": 3000}]
    result = calculate_totals(test_data)

    assert result["sales"] == 5000
    assert result["expenses"] == 3000
    assert result["profit"] == 2000

    print("Single item test passed!")
```

- Test with empty data
- Test with one item
- Test with negative numbers (if applicable)
- Explain why edge cases matter

### 9.6 Writing Helper Functions to Test

```python
def calculate_profit(sales: int, expenses: int) -> int:
    """Calculate profit from sales and expenses."""
    return sales - expenses

# Test the helper function
def test_calculate_profit():
    assert calculate_profit(1000, 500) == 500
    assert calculate_profit(500, 1000) == -500  # Loss
    assert calculate_profit(0, 0) == 0
    print("Profit calculation tests passed!")
```

- Create simple, testable functions
- Show how to test them
- Build confidence in your code

### 9.7 Running Tests

- Create a separate test file: `test_sales_chart.py`
- Run tests: `python test_sales_chart.py`
- See which tests pass or fail
- Fix bugs when tests fail

---

## 10. Practice Exercises

1. **Modify the chart**: Change colors or bar widths
2. **Add calculations**: Show profit (sales - expenses) as a third bar
3. **Filter data**: Only show months with sales > 6000
4. **Add a title**: Display total sales at the top
5. **Write to file**: Save processed data to a new CSV file
6. **Write tests**: Create tests for `calculate_totals()` with different data
7. **Test edge cases**: Test with empty data, negative numbers, very large numbers
8. **Use tuples**: Modify the code to return tuples instead of dictionaries
9. **Use sets**: Create a set of unique month names from the data
10. **Compare iterators**: Write code that demonstrates differences between list, tuple, and set

---

## 11. Summary & Next Steps

- **Key Takeaways**:

  - Files are opened with `open()` and closed (or use `with`)
  - String methods (`split()`, `strip()`) help parse text data
  - Tuples are immutable sequences, perfect for fixed data
  - Tuple unpacking makes code cleaner and more readable
  - Sets store unique values and support set operations
  - Different iterators (list, tuple, set, dict, string) have different use cases
  - CSV files are just text files with a specific format
  - Charts make data easier to understand

- **What's Next**:
  - Try different chart types (LineChart, PieChart)
  - Read data from APIs instead of files
  - Add interactivity (click to filter, hover for details)
  - Write data back to files
  - Write more tests for your functions
  - Learn about unit testing frameworks (like `pytest`)
