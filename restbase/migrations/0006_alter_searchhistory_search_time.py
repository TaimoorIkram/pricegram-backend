# Generated by Django 4.2 on 2023-06-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbase', '0005_searchhistory_search_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhistory',
            name='search_time',
            field=models.DateField(),
        ),
    ]
