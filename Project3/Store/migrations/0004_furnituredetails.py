# Generated by Django 5.1.5 on 2025-01-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_signup_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='furnituredetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productname', models.CharField(max_length=50)),
                ('productimage', models.ImageField(upload_to='productimages')),
                ('productprice', models.IntegerField()),
            ],
        ),
    ]
