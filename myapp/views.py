from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Employee
from .forms import EmployeeDetails


def homepage(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")


def signuppage(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        re_password = request.POST.get("re_pass")
        print(username, email, password, re_password)
        if password == re_password:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect("/login")

        else:
            return HttpResponse("please enter both password same")
    return render(request, "signup.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        # if user enter correct credentials then let them pass
        user = authenticate(username=username, password=password)
        print(authenticate)
        if user is not None:
            # print(username, password)
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials, please try again")
            return render(request, "login.html")
    return render(request, "login.html")


def logoutpage(request):
    logout(request)
    return redirect("/login")


# this function will add the add and show in page
def add_show(request):
    if request.method == "POST":
        fm = EmployeeDetails(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            salary = fm.cleaned_data["salary"]
            phone = fm.cleaned_data["phone"]
            reg = Employee(name=name, email=email, salary=salary, phone=phone)
            reg.save()
            fm = EmployeeDetails()
    else:
        fm = EmployeeDetails()
    stud = Employee.objects.all()
    return render(request, "addandshow.html", {"form": fm, "stu": stud})


def delete_data(request, id):
    if request.method == "POST":
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


# this function will update the data and return that updated data to main page
def update_data(request, id):
    if request.method == "POST":
        pi = Employee.objects.get(pk=id)
        fm = EmployeeDetails(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeDetails(instance=pi)
    return render(request, "updatedata.html", {"form": fm})


# Create your views here.
