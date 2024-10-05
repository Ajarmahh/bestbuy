import pytest
from products import *


def test_empty_name():
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)
