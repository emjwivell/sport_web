from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from app.models import Player


def make_index(request):
    all_players = Player.objects.all()
    return render_to_response('index.html', {'players': all_players})