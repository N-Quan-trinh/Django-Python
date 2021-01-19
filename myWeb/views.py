from datetime import date
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myWeb.models import Game, UserAccount
from myWeb.forms import ModelLogin, ModelRegister

games = Game.objects.all()
UserInfo = UserAccount.objects.all()


# Create your views here.


def hello_world(request):
    time = datetime.now()
    return HttpResponse(request)


def modelTest(request):
    game1 = games[0]
    game2 = games[1]
    return render(request, 'Games.html', {'game1': game1, 'game2': game2})


def AccountLogin(request):
    Error = "Please enter your user name"
    if request.method == 'POST':
        LoginForm = ModelLogin(request.POST)
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data['UserName']
            password = LoginForm.cleaned_data['Password']
            for x in UserInfo:
                if username == x.UserName and password == x.Password:
                    return HttpResponseRedirect('admin/')
                else:
                    Error = 'We were unable to find your username'

    else:
        LoginForm = ModelLogin()
    return render(request, 'Hello.html', {'form': LoginForm, 'Error': Error})


def AccountRegister(request):
    if request == 'POST':
        RegisterAccount = ModelRegister(request.POST)
        if RegisterAccount.is_valid():
            RegisterAccount.save()

    else:
        RegisterAccount = ModelRegister()

    return render(request, 'name.html', {'form': RegisterAccount})
