# Generated by Django 5.1.5 on 2025-02-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_alter_furnituredetails_productid'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituredetails',
            name='productdesc',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='furnituredetails',
            name='productdime',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AddField(
            model_name='furnituredetails',
            name='productmanu',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
