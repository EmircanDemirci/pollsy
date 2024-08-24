from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm,UpdateProfileForm,UpdateUserForm

from .models import Profile
from polls.models import Question

from mysite import settings
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("polls:index")
        else:
            #redirect invalid login page
            messages.success(request , ("There was an error to authenticate"))
            return redirect("login")
    else:
        return render(request , "login.html")
    

def logout_user(request):
    logout(request)
    messages.success(request , ("You were logged out!"))
    return redirect("user:login")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request,user)
            messages.success(request , ("Registration Successful"))
            return redirect("polls:index")
    else:
        form = RegisterUserForm()

    return render(request , 'register.html' , {'form':form})

@login_required
def profile(request):
    user = get_object_or_404(Profile,user_id=request.user)
    question = Question.objects.filter(published_user = request.user)
    return render(request , "profile.html" , {"ruser":user , "question":question})

@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form =UpdateProfileForm(request.POST,request.FILES , instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,"Your profile updated successfully")
            return redirect(to="user:profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request , "profile_edit.html" , {'user_form' : user_form , 'profile_form':profile_form})


@login_required
def profile_another(request , user_id):
    user = get_object_or_404(Profile , user_id = user_id)
    question = Question.objects.filter(published_user = user_id)
    return render(request, "profile.html" , {"ruser":user , "question" : question})
