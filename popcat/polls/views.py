from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html', {

    })


def count(request):
    return render(request, 'polls/count.html')


def start(request):
    return render(request, 'polls/start.html')


def win(request):
    return render(request, 'polls/win.html')
