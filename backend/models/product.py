```python
class Product:
    def __init__(self, product_name, description, product_number, vendor_name, cost, product_image, product_site):
        self.product_name = product_name
        self.description = description
        self.product_number = product_number
        self.vendor_name = vendor_name
        self.cost = cost
        self.product_image = product_image
        self.product_site = product_site

    def to_dict(self):
        return {
            'product_name': self.product_name,
            'description': self.description,
            'product_number': self.product_number,
            'vendor_name': self.vendor_name,
            'cost': self.cost,
            'product_image': self.product_image,
            'product_site': self.product_site
        }
```