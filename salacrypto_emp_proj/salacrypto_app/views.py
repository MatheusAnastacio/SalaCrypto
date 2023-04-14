from django.shortcuts import render, HttpResponse

from .forms import PlayerForm
from .models import Cla, Classe, Player

# Create your views here.
def index(request):
    return render(request, 'index.html')



def all_player(request):
    emps = Player.objects.all()
    context = {
        'emps': emps
    }

    return render(request, 'view_all_players.html', context)

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
        else:
            context = {'form': form}
            return render(request, "add_player.html", context)

    form = PlayerForm(user=request.user)
    context = {'form': form}
    return render(request, "add_player.html", context)


def remove_player(request):
    return render(request, 'remove_player.html')

def filtro_player(request):
    return render(request, 'filtro_player.html')

def score(request):
    return render(request, 'score.html')

