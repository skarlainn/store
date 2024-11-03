from unittest.mock import patch

import pytest

from src.products import Product


def test_products(product) -> None:
    assert product.description == 'Я сама "вечность"'
    assert product.name == "Nokia 3310"
    assert product.price == 9.99
    assert product.quantity == 1
    assert str(product) == "Nokia 3310, 9.99 руб. Остаток: 1 шт."


def test_new_product(new_product):
    result = Product.new_product(new_product)
    assert result.name == "Samsung Galaxy C23 Ultra"
    assert result.description == "256GB, Серый цвет, 200MP камера"
    assert result.price == 180000.0
    assert result.quantity == 5


def test_new_price(product):
    product.price = 100.0
    assert product.price == 100


def test_new_price_negative(capsys, product):
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


@patch("builtins.input", side_effect="y")
def test_new_price_low(mock, product):
    product.price = 5
    assert product.price == 5


def test_add(product2, product3):
    assert product2 + product3 == 2580000.0


def test_add_error(smartphone1, lawn_grass_1):
    with pytest.raises(TypeError):
        smartphone1 + lawn_grass_1


def test_add_products(new_product):
    products = [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 100000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
    ]
    result = Product.new_product(new_product, products)
    assert result.quantity == 10
    assert result.price == 180000.0
    assert result.name == "Samsung Galaxy C23 Ultra"

def test_product_non_quantity():
    with pytest.raises(ValueError):
        Product("test", "test", 1.1, 0)