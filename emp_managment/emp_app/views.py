from datetime import datetime
from django.shortcuts import render, HttpResponse
from emp_app.models import Employee,Role,Department
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,"index.html",{})

def all_emp(request):
    emps=Employee.objects.all()
    return render(request,"view_all_emp.html",{"emps":emps})

def add_emp(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        salary=request.POST.get('salary')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        bonus=request.POST.get('bonus')
        phone=request.POST.get('phone')
        
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, dept_id=dept,role_id=role,bonus=bonus,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully! ")
    return render(request,"add_emp.html")


def filter_emp(request):
    if request.method == "POST":
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        
        return render(request,"view_all_emp.html",{"emps":emps})
    return render(request,"filter_emp.html")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            pass
    emps = Employee.objects.all()
    return render(request,"remove_emp.html",{"emps":emps})
