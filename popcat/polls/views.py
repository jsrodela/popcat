from django.shortcuts import render


def start(request):
    return render(request, 'polls/start.html')


def count(request):
    return render(request, 'polls/count.html')


def win(request):
    return render(request, 'polls/win.html')
