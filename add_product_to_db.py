import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectStore.settings')
django.setup()

from store.models import Product, Category

category = Category.objects.get(name='Fruits')
obj = Product(name='Apple', description='Яблоко', price=120,
             image='static/products/product-10.jpg',
             category=category)
obj.save()

# ------------------

obj = Product.objects.create(name='Garlic',
                            description='Garlic',
                            price=120,
                            image='static/products/product-11.jpg',
                            category=Category.objects.get(name='Vegetables'))

# ------------------

data = ({'name': 'Chilli',
        'price': 120.00,
        'description': "Chilli",
        'image': 'static/products/product-12.jpg',
        'category': 'Vegetables'},)

categ = {'Fruits': Category.objects.get(name='Fruits'),
        'Vegetables': Category.objects.get(name='Vegetables')}

objects_to_create = [Product(name=val['name'],
                            description=val['description'],
                            price=val['price'],
                            image=val['image'],
                            category=categ[val['category']]) for val in data]

Product.objects.bulk_create(objects_to_create)
