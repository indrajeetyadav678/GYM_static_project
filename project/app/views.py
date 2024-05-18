from django.shortcuts import render
from .models import*
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def classlt(request):
    return render(request, 'classlt.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def timetable(request):
    return render(request, 'timetable.html')

def calculate(request):
    return render(request, 'calculate.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def register(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')

# ==================== Registration Form ===================

def registerdata(request):
    print(request.method)
    name=request.POST.get('name')
    email=request.POST.get('email')
    print(email)
    number=request.POST.get('number')
    password=request.POST.get('password')
    con_password=request.POST.get('con_password')
    data=RegistrationModel.objects.filter(Email=email)
    if name=="" or email=="" or number=="" or password=="":
        msg="Please fill all data field"
        return render(request, 'registration.html', {'key':msg,'data1':name,'data2':email,'data3':number})     
    else:
        if data:
            msg="User aleary Exist"
            return render(request, 'registration.html', {'key':msg})
        else:
            if password==con_password:
                RegistrationModel.objects.create(
                    Name=name,
                    Email=email,
                    Number=number,
                    Password=password
                )
                msg="Registration Successfully Done"
                return render(request, 'login.html', {'key': msg})
            else:
                msg="Password and Confirm Password Not Match"
                return render(request, 'registration.html', {'key':msg,'data1':name,'data2':email,'data3':number})

# ====================== Login Form =====================  

def logindata(request):
    # print(request.POST)
    # userid=request.POST.get('userid')
    # username=RegistrationModel.objects.filter(Email=userid)
    # return render(request, 'register.html')

    userid=request.POST.get('userid')
    password=request.POST.get('password')
    username=RegistrationModel.objects.filter(Email=userid)
    if username:
        data=RegistrationModel.objects.get(Email=userid)
        Password= data.Password
        if Password==password:
            msg="Welcome To "+data.Name
            return render(request, 'index.html', {'key1': msg, 'user_name':data}) 
        else:
            msg="Enter Password is Wrong Please Enter Correct Password"
            return render(request, 'login.html', {'key1': msg})
    else:
        msg="Userid doesnot exist Please create Account"
        return render(request, 'registration.html', {'key1': msg})
    
# =============== profile Link ==============

def logout(request):
    return render(request, 'index.html')


def editpro(request):
    return render(request, 'editprofile.html')