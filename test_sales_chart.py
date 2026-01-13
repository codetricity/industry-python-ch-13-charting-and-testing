"""
Test file for sales_chart_app.py
Demonstrates using assert statements to test pure functions
"""

from sales_chart_app import calculate_totals, read_csv


def test_calculate_totals_basic():
    """Test calculate_totals with basic data."""
    test_data = [
        {"month": "January", "sales": 1000, "expenses": 500},
        {"month": "February", "sales": 2000, "expenses": 800}
    ]
    
    result = calculate_totals(test_data)
    
    # Test that calculations are correct
    assert result["sales"] == 3000, "Total sales should be 3000"
    assert result["expenses"] == 1300, "Total expenses should be 1300"
    assert result["profit"] == 1700, "Total profit should be 1700"
    
    print("✓ Basic totals test passed!")


def test_calculate_totals_empty():
    """Test calculate_totals with empty data."""
    result = calculate_totals([])
    
    assert result["sales"] == 0, "Empty list should return 0 sales"
    assert result["expenses"] == 0, "Empty list should return 0 expenses"
    assert result["profit"] == 0, "Empty list should return 0 profit"
    
    print("✓ Empty data test passed!")


def test_calculate_totals_single_item():
    """Test calculate_totals with a single item."""
    test_data = [
        {"month": "January", "sales": 5000, "expenses": 3000}
    ]
    
    result = calculate_totals(test_data)
    
    assert result["sales"] == 5000, "Single item sales should be 5000"
    assert result["expenses"] == 3000, "Single item expenses should be 3000"
    assert result["profit"] == 2000, "Single item profit should be 2000"
    
    print("✓ Single item test passed!")


def test_calculate_totals_large_numbers():
    """Test calculate_totals with large numbers."""
    test_data = [
        {"month": "January", "sales": 100000, "expenses": 50000},
        {"month": "February", "sales": 200000, "expenses": 75000}
    ]
    
    result = calculate_totals(test_data)
    
    assert result["sales"] == 300000, "Large numbers should calculate correctly"
    assert result["expenses"] == 125000, "Large expenses should calculate correctly"
    assert result["profit"] == 175000, "Large profit should calculate correctly"
    
    print("✓ Large numbers test passed!")


def test_calculate_totals_loss_scenario():
    """Test calculate_totals when expenses exceed sales (loss)."""
    test_data = [
        {"month": "January", "sales": 1000, "expenses": 2000}
    ]
    
    result = calculate_totals(test_data)
    
    assert result["sales"] == 1000
    assert result["expenses"] == 2000
    assert result["profit"] == -1000, "Profit should be negative when expenses > sales"
    
    print("✓ Loss scenario test passed!")


def test_calculate_totals_zero_values():
    """Test calculate_totals with zero values."""
    test_data = [
        {"month": "January", "sales": 0, "expenses": 0}
    ]
    
    result = calculate_totals(test_data)
    
    assert result["sales"] == 0
    assert result["expenses"] == 0
    assert result["profit"] == 0
    
    print("✓ Zero values test passed!")


def run_all_tests():
    """Run all test functions."""
    print("Running tests for calculate_totals()...\n")
    
    try:
        test_calculate_totals_basic()
        test_calculate_totals_empty()
        test_calculate_totals_single_item()
        test_calculate_totals_large_numbers()
        test_calculate_totals_loss_scenario()
        test_calculate_totals_zero_values()
        
        print("\n" + "="*50)
        print("All tests passed! ✓")
        print("="*50)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise


if __name__ == "__main__":
    run_all_tests()
