# Generated by Django 4.2.12 on 2024-05-07 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_Sale',
            new_name='is_sale',
        ),
    ]