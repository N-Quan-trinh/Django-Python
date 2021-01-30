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
    Error = False
    loginSub = 'loginSubmit'
    registerSub = 'registerSubmit'
    if request.method == 'POST':
        if loginSub in request.POST:
            loginAccount = ModelLogin(request.POST)
            if loginAccount.is_valid():
                loginName = loginAccount.cleaned_data["UserName"]
                loginPass = loginAccount.cleaned_data["Password"]
                for x in UserInfo:
                    if x.UserName == loginName and x.Password == loginPass:
                        return HttpResponseRedirect("/admin")
                    else:
                        Error = True
        elif registerSub in request.POST:
            registerAccount = ModelRegister(request.POST)
            if registerAccount.is_valid():
                registerAccount.save()
                return HttpResponseRedirect("/admin")
    else:
        loginAccount = ModelLogin()
        registerAccount = ModelRegister()

    return render(request, 'Hello.html', {'form': loginAccount, 'RegForm': registerAccount, 'error': Error})


def AccountRegister(request):
    if request.method == 'POST':
        RegisterAccount = ModelRegister(request.POST)
        if RegisterAccount.is_valid():
            RegisterAccount.save()

    else:
        RegisterAccount = ModelRegister()

    return render(request, 'name.html', {'form': RegisterAccount})
