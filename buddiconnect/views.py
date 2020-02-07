
from django.shortcuts import render, redirect
from django.views import View
from django.template import loader
from .forms import SignUpForm, LogInForm
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


class Homepage(View):
    """ Class subview of View to Test homePage App"""
    def get(self, request):
        #  updateApp()  # Only use this function if you want to refresh the App with new Articles
        template = loader.get_template('home_Screen/home.html')  #  Templates folder needs to be within App is True
        return HttpResponse(template.render({}, request))


class Profilepage(View):
    """ This will display the profile model in Database"""
    def get(self, request):
        pass

    def post(self, request):
        pass


def signout(request):
    print("User", request.user)
    logout(request)
    return redirect('homePage')


def logIn(request):
    """ Will be used to Log In"""
    if request.method == 'GET':
        form = LogInForm()
        return render(request, 'loginPage/login_page.html', {'form': form})
    pass


def signup(request):
    """ This will prompt User Creation and with form"""
    if request.method == 'POST':
        print("Request is post")
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            """ If the form was created successfully"""
            print("Form was a success")
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is None:
                #  If user already exists
                pass
            else:
                #  If user is being created for the first time
                pass
            login(request, user)
            return redirect('homePage')
        else:
            print("Starting brand New")
            form = SignUpForm(request.POST)
    if request.method == 'GET':
        print("Landed on Signup Page")
        form = SignUpForm()
    return render(request, 'signupPage/signupPage.html', {'form': form})