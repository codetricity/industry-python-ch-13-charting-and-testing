# File I/O and Charts Tutorial

This tutorial teaches students how to read CSV files, parse data using string methods, and create visualizations using `flet-charts`.

## Learning Objectives

- Read text files in Python
- Parse CSV-style data using string methods (`split()`, `strip()`)
- Understand tuples, sets, and differences between Python iterators
- Use tuple unpacking for cleaner code
- Create interactive bar charts with `flet-charts`
- Build a complete data visualization application
- Write tests using `assert` statements
- Test pure functions

## Files

- `tutorial_outline.md` - Detailed tutorial outline with step-by-step instructions
- `sales_chart_app.py` - Complete working example application
- `test_sales_chart.py` - Test file demonstrating `assert` and testing pure functions
- `../plan/data.csv` - Sample data file (monthly sales and expenses)

## Prerequisites

- Basic Python knowledge (variables, lists, dictionaries, functions)
- Familiarity with Flet basics (Page, adding controls)
- `flet` and `flet-charts` packages installed

## Installation

```bash
uv add flet flet-charts
```

Or with pip:

```bash
pip install flet flet-charts
```

## Running the Example

```bash
uv run sales_chart_app.py
```

Or:

```bash
python sales_chart_app.py
```

## Running the Tests

```bash
uv run test_sales_chart.py
```

Or:

```bash
python test_sales_chart.py
```

## Concepts Covered

### File I/O (Section C)
- Reading text files with `open()` and `with` statement
- CSV-style parsing
- Stripping newlines and whitespace

### String Methods (Section B)
- `split()` - breaking strings into lists
- `strip()` - removing whitespace
- String slicing with indices

### Tuples and Sets (Section B)
- Tuple basics (creation, unpacking)
- Sets and unique collections
- Differences between Python iterators (list, tuple, set, dict, string)
- When to use each data type

### Data Visualization
- Creating bar charts with `flet-charts`
- Displaying multiple data series
- Adding tooltips and labels

### Testing (Section J)
- Using `assert` for lightweight testing
- Testing pure functions
- Writing test cases for edge cases

## Tutorial Structure

The tutorial is designed for high school or first-year CS students and includes:

1. **Introduction** - What we're building and why
2. **Understanding CSV Files** - File format basics
3. **Reading Files** - File I/O in Python
4. **String Methods** - Parsing text data
5. **Tuples, Sets, and Iterators** - Understanding Python data types
6. **Parsing CSV Data** - Step-by-step data processing
7. **Creating Charts** - Visualization with flet-charts
8. **Complete Example** - Full application walkthrough
9. **Testing** - Using assert and testing pure functions
10. **Practice Exercises** - Hands-on challenges

## Next Steps

After completing this tutorial, students can:

- Try different chart types (LineChart, PieChart)
- Add data filtering and calculations
- Write processed data back to files
- Connect to APIs for real-time data
