# Generated by Django 4.2 on 2023-04-14 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salacrypto_app', '0008_alter_player_chi_tec_desen_musc'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
