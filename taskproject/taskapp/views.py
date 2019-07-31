from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from taskapp import forms
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from taskapp.forms import Usersignup

# Create your views here.



def logindetails(request):
    context={}
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('welcomee'))
        else:
            context['error']="provide correct information"
            return render(request, 'taskapp/home.html',context)


    else:
            print('error')
    return render(request, 'taskapp/login.html', context)


def welcomee(request):
    context={}
    context['user']=request.user
    return render(request, 'taskapp/welcome.html',context)

def user_logout(request):
    if request.method=='POST':
        logout(request)
    return HttpResponseRedirect(reverse('logindetails'))


def sign(request):
    if request.method == "POST":
        user_signup = Usersignup(request.POST)

        if user_signup.is_valid():
         user_signup.save()

        username = user_signup.cleaned_data.get('username')
        raw_password = user_signup.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)

        return redirect('logindetails')

    else:

        user_signup = Usersignup()

    return render(request, 'taskapp/signup.html',{'form':user_signup})




