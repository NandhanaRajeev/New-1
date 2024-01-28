from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# from .models import userDetails


login_required(login_url='login')
def index(request):
    return render(request, 'users/index.html')

def contact(request):
    return render(request, 'users/contacts.html')

def blog(request):
    return render(request, 'users/blog.html')

def user_login(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')

        user=authenticate(request, username=name, password=password)
        if user is not None:

            if user.is_superuser:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("trip")
            elif user.is_staff:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("trip")
            else:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("user")
        else:
            msg='invalid details'
            return render(request,'users/login.html',{'msg':msg})
    else:
        return render(request,'users/login.html')



    # return render(request, 'users/login.html')

def register(request):
    errors = {}
    if request.method == 'POST':

        name = request.POST['name'].strip()
        
        email = request.POST['email'].strip()
        
        password = request.POST['password'].strip()
        password = request.POST['password'].strip()

        new_user=User.objects.create_user(username=name,email=email)
        new_user.set_password('password')
        new_user.save()
        # userDetails.objects.create(user=new_user,)
        return redirect('login')
    else:
        return render(request, 'users/register.html')

def tnc(request):
    return render(request, 'users/tnc.html')
# def userData(request):
#     context={

#     }
#     return render(request, "users/UserData.html",context)
    # return render(request, 'users/register.html')

