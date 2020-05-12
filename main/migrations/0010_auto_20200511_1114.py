# Generated by Django 3.0.4 on 2020-05-11 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_product_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, default=None, to='main.Cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
    ]