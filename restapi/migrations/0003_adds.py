# Generated by Django 2.1.5 on 2019-01-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='adds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=2000)),
            ],
        ),
    ]
