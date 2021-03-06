# Generated by Django 4.0.6 on 2022-07-07 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address_lat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('address_long', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('volume', models.FloatField(null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.building')),
            ],
        ),
    ]
