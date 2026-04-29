import pytest
from Ecommerce import calculate_total

def test_calculate_valid_total():
    items=[200,200,400]
    tax_rate=0.5
    result = calculate_total(items,tax_rate)

    assert result == 1200

def test_negative_price():
    items=[200,-200,400]
    tax_rate=0.5
    
    with pytest.raises(ValueError, match = "Price cannot be negative.."):
        calculate_total(items,tax_rate)
    

def test_invalid_taxrate():
    items=[200,200,400]
    tax_rate= 2

    with pytest.raises(ValueError, match = "Invalid tax rate...."):
        calculate_total(items,tax_rate)

