
from django.contrib import admin
from .models import Player, Classe, Cla
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.


admin.site.register(Classe)
admin.site.register(Cla)

#admin.site.register(Player, SimpleHistoryAdmin)
@admin.register(Player)
class PlayerAdmin(SimpleHistoryAdmin):
    history_list_display = ["level", "power"]
    fieldsets = (
        (None, {"fields": ("dono", "nick", ("level", "power"),"constituicao",)}),
        ("Chi ", {"fields": (("chi_tec_desen_musc", "chi_manu_nove_yin", "chi_manu_nove_yang"), ("chi_arte_div_nev_violeta",
                             "chi_arte_div_prof_norte", "chi_postura_sapo"), )}),
        (None, {"fields": ("nft", "ticket", "classe")}),
    )
