# Generated by Django 5.1.5 on 2025-01-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web2', '0007_alter_pkadmin_packimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='updatepass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
