```python
from models.product import Product
from utils.search import search_product_alternatives

def create_product(product_data):
    new_product = Product(**product_data)
    new_product.save()
    return new_product

def read_product(product_id):
    product = Product.get_by_id(product_id)
    if product:
        return product
    else:
        return None

def update_product(product_id, product_data):
    product = Product.get_by_id(product_id)
    if product:
        for key, value in product_data.items():
            setattr(product, key, value)
        product.save()
        return product
    else:
        return None

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if product:
        product.delete()
        return True
    else:
        return False

def export_product_list():
    products = Product.get_all()
    product_list = [product.to_dict() for product in products]
    return product_list

def search_alternatives(product_id):
    product = Product.get_by_id(product_id)
    if product:
        alternatives = search_product_alternatives(product.name)
        return alternatives
    else:
        return None
```