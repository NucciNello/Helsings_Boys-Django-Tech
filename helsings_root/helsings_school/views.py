from django.shortcuts import render, redirect
from .models import Alumnus, Registered, User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def staff(request):
    return render(request, 'staff.html')

@login_required(login_url=("login"))
def alumni(request):
    if request.method == "POST":
        name = request.POST['Name']
        enrolled = request.POST['Year of enrollment']
        graduated = request.POST['Year of graduation']
        headmaster = request.POST['Headmaster at graduation']
        famous = request.POST['Famous Teacher at graduation']
        results = request.POST['Results']
        occupation = request.POST['Occupation']
        email = request.POST['Email']
        address = request.POST['Address']
        mobile = request.POST['Mobile']

        veteran = Alumnus.objects.create(
            name =  name,
            enrolled =  enrolled,
            graduated =  graduated,
            headmaster =  headmaster,
            famous =  famous,
            results =  results,
            occupation = occupation,
            email =  email,
            address = address,
            mobile = mobile
        )
        veteran.save()
    return render(request, 'alumni.html')

@login_required(login_url=("login"))
def table(request):
    veterans = Alumnus.objects.all
    return render(request, 'table.html', {'all':veterans})

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['sur_name']
        username = request.POST['user_name']
        password = request.POST['password']
        email = request.POST['email']
        second_name = request.POST['second_name']
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        facebook = request.POST['facebook']
        twitter = request.POST['twit']
        instagram = request.POST['instagram']
        cv = request.POST['cv']

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
        Registered.objects.create(
            user = user,
            # first_name = first_name,
            # last_name = last_name,
            # username = username,
            # password = password,
            # email = email,
            second_name = second_name,
            dob = dob,
            mobile = mobile,
            facebook = facebook,
            twitter = twitter,
            instagram = instagram,
            cv = cv
        )
        user.save()
        return render(request, 'home.html', {})
    else:
        return render(request, 'register.html', {})

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username =username, password = password )
        if user is not None:
            auth_login(request, user)
            return render(request, 'home.html')
        else:
            messages.success(request, ("There was an error! Try again"))
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect(home)








# def login(request):
#     if request.method == 'POST':
#         user_name = request.POST['username']
#         pass_word = request.POST['password']
       
#         nticasion = authenticate(request, user_name = user_name, password = pass_word )

#         if nticasion is not None:
#             auth_login(request, nticasion)
#             messages.success(request, ("Welcome {{ uname }}!"))
#             return redirect('home')
#         else:
#             messages.success(request, ("There was an error! Try again"))
#             return render(request, 'login.html', {})
#     else:
#         return render(request, 'login.html', {})
