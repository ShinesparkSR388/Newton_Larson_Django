# Generated by Django 4.2.2 on 2023-06-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newton_larson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
