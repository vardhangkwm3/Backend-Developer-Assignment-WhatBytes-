from .forms import SignUP, LogIN
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .models import WatchOver
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def Signup(request):
    msg = []
    if request.method == "POST":
        form = SignUP(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Registered Successfully")
            useer = WatchOver(
                usr = user,
                Last_used = timezone.now()
            )
            useer.save()
            return redirect('login')
        else:
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{error}")
                    msg.append(f"{error}")
    else:
        form = SignUP()
    return render(request,'SignUP.html',{'form':form,'msg':msg}) 

def LOGIN(request):
    form = LogIN(request.POST or None)
    mssg = []
    if request.method == "POST":
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')

            user = authenticate(username=user_name,password=user_password)

            if user is None:
                try:
                    temp_user = User.objects.get(email = user_name)
                    print("using email for authentication")
                    user = authenticate(username=temp_user.username,password = user_password)
                except:
                    user = None
            
            if user is None:
                mssg.append("User Credentials Not Found")
                return render(request,"Login.html",{'form':form,'mssg':mssg})
            
            messages.success(request,"successfully Loggedin")
            login(request,user)
            return redirect('home')
    return render(request,"Login.html",{'form':form})

@login_required(login_url='login')
def ChangePassword(request):
    mssg = []
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            mssg.append("Password Changed Successfully")
            return render(request,"change.html",{'mssg':mssg,'form':form})
        else:
            for field,errList in form.errors.items():
                for err in errList:
                    mssg.append(f"{err}")
    else:
        form = PasswordChangeForm(request.user)
    cntxt = {"mssg":mssg,'form':form}
    return render(request, "change.html",cntxt)

@login_required(login_url='login')
def Home(request):
    return render(request,"home.html")

@login_required(login_url='login')
def Profile(request):
    user = WatchOver.objects.get(usr=request.user)
    return render(request,"Profile.html",{'req':user})

@login_required(login_url='login')
def LogOut(request):
    try:
        user = WatchOver.objects.get(usr=request.user)
        user.Last_used = timezone.now()
        user.save()
    except WatchOver.DoesNotExist:
        # Handle the case where WatchOver does not exist for the user
        pass
    logout(request)
    return redirect('login')
