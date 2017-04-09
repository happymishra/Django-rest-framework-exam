from __future__ import unicode_literals
from django.db import migrations
 
 
def create_initial_products(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')
 
    Product(name='Salame', description='Salame Toscano', price=12).save()
    Product(name='Olio Balsamico', description='Olio balsamico di Modena', price=10).save()
    Product(name='Parmigiano', description='Parmigiano Reggiano', price=8.50).save()
    Product(name='Olio', description='Olio Oliva Toscano', price=13).save()
    Product(name='Porchetta', description='Porchetta toscana cotta a legna', price=7.50).save()
    Product(name='Cantucci', description='Cantucci di Prato', price=4).save()
    Product(name='Vino Rosso', description='Vino Rosso del Chianti', price=9.50).save()
    Product(name='Brigidini', description='Brigidini di Lamporecchio', price=3.50).save()
 
 
class Migration(migrations.Migration):
 
    dependencies = [
        ('catalog', '0001_initial'),
    ]
 
    operations = [
        migrations.RunPython(create_initial_products),
    ]