from app.database import products
from app.schemas import Product


def get_products():
    return products


def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return None


def create_product(product: Product):
    products.append(product)
    return product


def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    return None


def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return True
    return False