# Generated by Django 3.1.7 on 2021-05-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
