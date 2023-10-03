from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def allemp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,"allemp.html",context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        
        # Use the capitalized model name 'Employee' to create an instance
        data = Employee(
            
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date=datetime.now()
        )
        data.save()
        
        return HttpResponse("Done")
    
    return render(request, "add.html")


def remove(request,emps_id=0):
    if emps_id:
        try:
            delete=Employee.objects.get(id=emps_id)
            delete.delete()
            return render(request,"remove.html")
        except:
            pass
    emp=Employee.objects.all()
    data={
        'emp':emp
    }
    return render(request,"remove.html",data)
    
def search(request):
    if request.method == "POST":
        name = request.POST.get('name', '')  # Use get() to safely access form data
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, "allemp.html", context)
    elif request.method == "GET":
        return render(request, "search.html")
    return HttpResponse("ERROR occurred")
        
    