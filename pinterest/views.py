





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views  import View
from pins.models import Pin
from boards.models import Board
from django.db.models import Q



def home(request):
    pins = Pin.objects.select_related('user').exclude(file='')
    boards=Board.objects.select_related('user').all()
    context = {'pins':pins[:49], 'boards':boards}
    return render(request, 'home.html', context)


class Search(View):
    def get(self,  request, *args, **kwargs):
        query=self.request.GET.get('q')
        pins=Pin.objects.select_related('user').filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)
        )
        boards=Board.objects.select_related('user').filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)
        )
        context={
            'pins':pins,
            'boards':boards,
        }
        return render(request, 'home.html', context)