# Generated by Django 5.1 on 2024-08-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cool_todo', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
