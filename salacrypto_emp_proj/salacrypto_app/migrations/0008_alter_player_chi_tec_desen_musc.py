# Generated by Django 4.2 on 2023-04-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salacrypto_app', '0007_alter_player_nft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chi_tec_desen_musc',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1, verbose_name='Chi - Tecnica de Desenvolvimento Muscular Estrela'),
        ),
    ]
