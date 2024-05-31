from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



# @login_required(login_url='login')
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user_done = User()
            user_done.username = username
            user_done.set_password(password1)
            user_done.save()
            user = authenticate(username=username,password=password1)
            login(request,user)

        return redirect('home')

    
    return render(request,'accounts/register.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')  
        else:
            return render(request,'accounts/login.html',{'Error':"Username or Password Incorrect"})


    return render(request,'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def new_meeting(request):
    
    return render(request,'videocall/streaming.html',{'username':request.user.username,})
@login_required(login_url='login')
def join_meeting(request):
    if request.method == "POST":
        roomID = request.POST['roomID']
        return redirect('/metting/?roomID='+roomID)
    return render(request,'videocall/joinroom.html')