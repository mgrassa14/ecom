# Generated by Django 4.2.12 on 2024-05-22 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_is_sale_product_is_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categorys',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
