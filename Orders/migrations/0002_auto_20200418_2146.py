# Generated by Django 3.0.5 on 2020-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары в заказах'},
        ),
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
