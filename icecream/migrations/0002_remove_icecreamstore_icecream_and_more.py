# Generated by Django 5.0.6 on 2024-06-01 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecreamstore',
            name='icecream',
        ),
        migrations.AddField(
            model_name='icecream',
            name='icecream_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='icecream.icecreamstore'),
        ),
        migrations.AlterField(
            model_name='child',
            name='icecream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='icecream.icecream'),
        ),
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='father',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='icecreamstore',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
