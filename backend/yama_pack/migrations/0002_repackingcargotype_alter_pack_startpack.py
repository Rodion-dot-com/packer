# Generated by Django 4.2.1 on 2023-06-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yama_pack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepackingCargotype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargotype', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pack',
            name='startpack',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
