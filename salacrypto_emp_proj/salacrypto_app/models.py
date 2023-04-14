from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

# Create your models here.


User = get_user_model()
class Cla(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Classe(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nick = models.CharField(max_length=100,)
    cla = models.ForeignKey(Cla, on_delete=models.CASCADE)
    power = models.IntegerField( validators=[
            MaxValueValidator(999999),
        ]
    )
    level = models.IntegerField( validators=[
            MaxValueValidator(999),
        ]
    )
    codex = models.IntegerField( validators=[
            MaxValueValidator(9999),
        ]
    )
    constituicao = models.IntegerField("Constituição", default=1, choices=((num, num) for num in range(1,20)))

    chi_tec_desen_musc = models.IntegerField("Chi - Tecnica de Desenvolvimento Muscular Estrela", default=1, choices=((num, num)
    for num in range(1, 19)))

    chi_manu_nove_yin = models.IntegerField("Chi - Manual dos Nove Yin Estrela", default=1, choices=((num, num)
    for num in range(1, 19)))

    chi_manu_nove_yang = models.IntegerField("Chi - Manual dos Nove Yang Estrela", default=1, choices=((num, num)
    for num in range(1, 19)))

    chi_arte_div_nev_violeta = models.IntegerField("Chi - Arte Divina da Névoa Violeta Estrela", default=1, choices=((num, num)
    for num in range(1, 11)))

    chi_arte_div_prof_norte = models.IntegerField("Chi - Arte Divina Profunda do norte Estrela", default=1, choices=((num, num)
    for num in range(1, 11)))

    chi_postura_sapo = models.IntegerField("Chi - Postura do Sapo Estrela", default=1, choices=((num, num)
    for num in range(1, 11)))

    nft = models.BooleanField("NFT", default=False)

    ticket = models.IntegerField("Tickets Amarelos:", validators=[
        MaxValueValidator(99),
    ]
    )

    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    history = HistoricalRecords()



    def __str__(self):
        return f"{self.nick}-{self.cla}-{self.level}-{self.codex}"

