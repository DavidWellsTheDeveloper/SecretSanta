# Generated by Django 4.1.4 on 2022-12-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretSanta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
