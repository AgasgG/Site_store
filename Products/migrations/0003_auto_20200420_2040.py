# Generated by Django 3.0.5 on 2020-04-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
