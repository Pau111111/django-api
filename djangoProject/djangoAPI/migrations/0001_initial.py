# Generated by Django 3.2.3 on 2021-06-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
    ]
