"""
Sales Data Visualization Tutorial
Reads CSV data and displays it in a bar chart using flet-charts
"""

import flet as ft
from flet_charts import BarChart, BarChartGroup, BarChartRod, ChartAxis, ChartAxisLabel


def read_csv(filename: str) -> list[dict]:
    """
    Read a CSV file and return a list of dictionaries.

    Each dictionary contains:
    - "month": month name
    - "sales": sales amount (int)
    - "expenses": expenses amount (int)
    """
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


def create_sales_chart(data: list[dict]) -> BarChart:
    """
    Create a bar chart from the sales data.

    Shows sales and expenses as side-by-side bars for each month.
    """
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
    # Use ft.Text controls to ensure consistent formatting
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
            label_spacing=12,  # Increased spacing between labels
        ),
        bottom_axis=ChartAxis(title=ft.Text("Month"), labels=bottom_labels),
    )

    return chart


def calculate_totals(data: list[dict]) -> dict:
    """Calculate total sales and expenses."""
    total_sales = sum(item["sales"] for item in data)
    total_expenses = sum(item["expenses"] for item in data)
    total_profit = total_sales - total_expenses

    return {"sales": total_sales, "expenses": total_expenses, "profit": total_profit}


def main(page: ft.Page):
    """Main function to set up and run the Flet app."""
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
