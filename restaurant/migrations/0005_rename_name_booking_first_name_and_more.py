# Generated by Django 5.0 on 2023-12-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_menuitem_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]