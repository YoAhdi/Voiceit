# Generated by Django 4.2.5 on 2023-11-05 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_petition_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='category',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]