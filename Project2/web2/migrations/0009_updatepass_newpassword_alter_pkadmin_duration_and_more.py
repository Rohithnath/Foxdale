# Generated by Django 5.1.5 on 2025-01-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web2', '0008_updatepass'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatepass',
            name='newpassword',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pkadmin',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pkadmin',
            name='packprice',
            field=models.CharField(max_length=50),
        ),
    ]
