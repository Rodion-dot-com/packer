# Generated by Django 4.2.1 on 2023-06-15 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderkey', models.CharField(max_length=32, unique=True)),
                ('startpack', models.DateTimeField(auto_now_add=True)),
                ('endpack', models.DateTimeField(blank=True, null=True)),
                ('selected_carton', models.CharField(blank=True, max_length=64)),
                ('recommended_carton', models.CharField(blank=True, max_length=64)),
                ('who', models.CharField(blank=True, max_length=64)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='yama_pack.status')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
