import json
from django.core.management.base import BaseCommand
from api.models import Product, Category

class Command(BaseCommand):
    help = 'Import products from JSON file into database'

    def handle(self, *args, **options):
        # Укажите правильный путь к вашему файлу products.json
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
            
            for product_data in products:
                # Создаем или получаем категорию
                category, created = Category.objects.get_or_create(
                    name=product_data['category']
                )
                
                # Создаем продукт
                Product.objects.create(
                    name=product_data['name'],
                    price=product_data['price'],
                    description=product_data['description'],
                    count=product_data['count'],
                    is_active=product_data['is_active'],
                    category=category
                )
                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(products)} products'))