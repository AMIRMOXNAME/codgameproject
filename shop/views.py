from pprint import pp
from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout 
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    cp = Cp.objects.all()
    return render(request , 'html/index.html' , {'cp' : cp})
def detail(request , slug):
    cp = get_object_or_404(Cp , slug=slug)
    return render(request , 'html/detail.html' , {'cp':cp})

def dashboard(request):
    return render(request , 'html/dashboard.html')


# login , singup , logout
def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request , 'این نام کاربری قبلا استفاده شده است!')
            return redirect('post:signup')

        if len(username)<4 or len(username)>20:
            messages.error(request , 'نام کاربری حداقل باید شامل 4 کرکتر و حداکثر 20 کرکتر باشد!')
            return redirect('post:signup')       

        if len(fname or lname)<3 or len(fname or lname)>20:
            messages.error(request , 'نام و نام خانوادگی حداقل باید شامل 3 کرکتر و حداکثر 20 کرکتر باشد!')
            return redirect('post:signup')

        if User.objects.filter(email=email):
            messages.error(request , 'این ایمیل قبلا استفاده شده است!') 
            return redirect('post:signup')   

        if pass1 != pass2:
            messages.error(request , 'رمز عبور مطابقبت ندارد!')
            return redirect('post:signup')

        myuser = User.objects.create_user(username , email , pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request , 'اکانت شما با موفقیت ساخته شد')
        return redirect('post:login')

    return render(request , 'forms/signup.html')    


def user_login(request):
    if request.method == 'POST':
        form = loginforms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username = cd['username'] , password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request , user)
                    return redirect("post:index")
                else:
                    messages.error(request , 'اکانت شما مسدود شده است!')
            else:
                messages.error(request , "اطلاعات وارد شده صحیح نمیباشد!")
                return redirect('post:login')
    else:
        form = loginforms()
    return render(request , 'forms/login.html')

def user_logout(request):
    logout(request)
    return redirect("post:index")
#     
