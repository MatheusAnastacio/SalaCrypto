# Generated by Django 4.2 on 2023-04-13 21:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salacrypto_app', '0005_player_constituicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='chi_arte_div_nev_violeta',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, verbose_name='Chi - Arte Divina da Névoa Violeta Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='chi_arte_div_prof_norte',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, verbose_name='Chi - Arte Divina Profunda do norte Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='chi_manu_nove_yang',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1, verbose_name='Chi - Manual dos Nove Yang Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='chi_manu_nove_yin',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1, verbose_name='Chi - Manual dos Nove Yin Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='chi_postura_sapo',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, verbose_name='Chi - Postura do Sapo Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='chi_tec_desen_musc',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1, verbose_name='Chi - Tec de Desenvolvimento muscular Estrela'),
        ),
        migrations.AddField(
            model_name='player',
            name='nft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='ticket',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Tickets Amarelos:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='constituicao',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], default=1, verbose_name='Constituição'),
        ),
    ]