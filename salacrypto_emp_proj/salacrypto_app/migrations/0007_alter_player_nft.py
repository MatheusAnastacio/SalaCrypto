# Generated by Django 4.2 on 2023-04-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salacrypto_app', '0006_player_chi_arte_div_nev_violeta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nft',
            field=models.BooleanField(default=False, verbose_name='NFT'),
        ),
    ]
