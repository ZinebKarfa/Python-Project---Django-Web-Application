# Generated by Django 4.1.6 on 2023-02-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=190, null=True)),
                ('lastName', models.CharField(max_length=190, null=True)),
                ('age', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=190, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]