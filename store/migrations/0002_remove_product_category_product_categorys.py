# Generated by Django 4.2.12 on 2024-05-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='categorys',
            field=models.ManyToManyField(to='store.category'),
        ),
    ]