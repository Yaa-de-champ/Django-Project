# Generated by Django 5.0.2 on 2024-02-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default=' ', max_length=1000),
        ),
    ]