from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def win(request):
    secret = ''
    if 'secret' in request.GET:
        secret = request.GET['secret']
    return render(request, 'polls/win.html', {
        'secret': secret
    })
