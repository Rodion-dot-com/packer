# Generated by Django 4.2.1 on 2023-06-18 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yama_pack', '0002_repackingcargotype_alter_pack_startpack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repackingcargotype',
            options={'verbose_name': 'Карготип с доупаковкой', 'verbose_name_plural': 'Карготипы с доупаковкой'},
        ),
    ]