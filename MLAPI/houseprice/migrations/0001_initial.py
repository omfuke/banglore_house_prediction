# Generated by Django 3.0.2 on 2020-03-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('square_feet', models.IntegerField()),
                ('Bath', models.IntegerField()),
                ('BHK', models.IntegerField()),
            ],
        ),
    ]
