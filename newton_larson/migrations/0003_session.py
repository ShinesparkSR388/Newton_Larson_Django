# Generated by Django 4.2.2 on 2023-06-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newton_larson', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SESSION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('username', models.CharField(max_length=120)),
                ('superuser', models.BooleanField()),
            ],
        ),
    ]
