# Generated by Django 5.0.6 on 2024-06-01 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0002_remove_icecreamstore_icecream_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecream',
            name='icecream_store',
        ),
        migrations.AddField(
            model_name='icecreamstore',
            name='icecream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='icecream.icecream'),
        ),
        migrations.AlterField(
            model_name='mother',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
