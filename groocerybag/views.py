from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import items
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/log-in')
def home(request):
    user=request.user
    try:
        if request.method=='GET':
            date=request.GET['date']
            item=items.objects.filter(user=user,date=date)
        
            param={
                'item':item
                }
            return render(request,'index.html',param)
    except:
        item=items.objects.filter(user=user)
        param={
            'item':item
        }
        return render(request,'index.html',param)
@login_required(login_url='/log-in')
def add_item(request):
    if request.method=='POST':
        item_name=request.POST['item_name']
        item_qun=request.POST['item_qun']
        status=request.POST['status']
        date=request.POST['date']
        b = items(user=request.user,item_name=item_name,status=status, item_qun=item_qun,date=date)
        b.save()
        return redirect('/')
    return render(request,'add.html')
@login_required(login_url='/log-in')
def update_item(request,id):
    item=items.objects.filter(id=id)
    param={
        'item':item[0]
    }
    if request.method=='POST':
        item_name=request.POST['item_name']
        item_qun=request.POST['item_qun']
        status=request.POST['status']
        date=request.POST['date']
        item.update(user=request.user,item_name=item_name,status=status, item_qun=item_qun,date=date)
        return redirect('/')
    return render(request,'update.html',param)
@login_required(login_url='/log-in')
def delete_item(request,id):
    item=items.objects.filter(id=id)
    item.delete()
    return redirect('/')

def sign_up(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email)
        user1=User.objects.filter(username=username)
        if user.exists() or user1.exists():
            return HttpResponse('User already exixts')
        b=User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        b.save()
        login(request, b)
        return HttpResponse('Success')
    return render(request,'signup.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.filter(username=username)
        if user.exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('loggedin')
                return redirect('/')
            else:
                return HttpResponse('wrong password')
            
        else:
            return HttpResponse('No user exsts with this email')
    return render(request,'login.html')

@login_required(login_url='/log-in')
def log_out(request):
    logout(request)
    return HttpResponse('Logged Out')