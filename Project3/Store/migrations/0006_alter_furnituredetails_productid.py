# Generated by Django 5.1.5 on 2025-01-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_furnituredetails_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnituredetails',
            name='productid',
            field=models.IntegerField(),
        ),
    ]
