# Generated by Django 5.0.4 on 2024-04-09 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='page.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
