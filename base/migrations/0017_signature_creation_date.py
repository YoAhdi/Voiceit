# Generated by Django 4.2.5 on 2023-11-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_petition_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
