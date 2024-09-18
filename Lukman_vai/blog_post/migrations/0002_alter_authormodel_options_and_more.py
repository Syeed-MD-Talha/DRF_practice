# Generated by Django 5.1 on 2024-09-04 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authormodel',
            options={'managed': True, 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'managed': True, 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'managed': True, 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='profilemodel',
            options={'managed': True, 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog_post.authormodel'),
            preserve_default=False,
        ),
    ]