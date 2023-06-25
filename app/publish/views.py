from django.shortcuts import render, redirect
from publish.models import Claim 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    """
    Show landing page and handle form to publish post.
    """
    if request.user.is_authenticated:
        search_text = request.GET.get('name', '')
        if search_text != "":
            print('!!!!:' + search_text)
            claims = Claim.objects.filter(ssn__name__contains=search_text).order_by('id')
        else:
            claims = Claim.objects.all().order_by('id')
        return render(
            request, 'publish/index.html', {'claims': claims}
        )
    else:
        return redirect('/login')          
    

def login_view(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        psw = request.POST["psw"]
        try:
            user = authenticate(username=uname, password=psw)
        except Exception as e:
            return render(
                request, 'publish/login.html', {'error_message': str(e)}
            )
        if user is None:
            return render(
                request, 'publish/login.html', {'error_message': "Can not found user."}
            )
        login(request, user)
        return redirect('index')
    else:
        return render(
                request, 'publish/login.html'
            )

def sign_up(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        psw = request.POST["psw"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(uname, email, psw)
            user.save()
        except Exception as e:
            return render(
                request, 'publish/sign_up.html', {'error_message': str(e)}
            )
        user = authenticate(username=uname, password=psw)
        login(request, user)
        return redirect("/")
    return render(
                request, 'publish/sign_up.html'
            )


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')