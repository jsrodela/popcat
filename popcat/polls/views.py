import json

from django.shortcuts import render

from . import consumers


def index(request):
    return render(request, 'polls/index.html')


def win(request):
    secret = ''
    if 'secret' in request.GET:
        secret = request.GET['secret']
    return render(request, 'polls/win.html', {
        'secret': secret
    })


def admin(request):
    if request.POST:
        if 'numbers' in request.POST:
            numbers = request.POST.get('numbers')
            consumers.reset_lucky_number(json.loads(numbers))
        elif 'number' in request.POST:
            number = request.POST.get('number')
            consumers.reset_count(int(number))
        else:
            print("Unknown request", request.POST)
    return render(request, 'polls/admin.html', {
        'numbers': json.dumps(consumers.LUCKY),
        'number': consumers.count
    })
