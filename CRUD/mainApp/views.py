from django.shortcuts import render, redirect
from .models import Employee

def home(request):
    emp_data = Employee.objects.all()
    return render(request,"index.html",{"emp_data":emp_data})

def add_employee(request):
    if request.method == 'POST':
        empobj = Employee()
        empobj.Name = request.POST.get('name')
        empobj.Department = request.POST.get('department')
        empobj.Salary = request.POST.get('salary')
        empobj.save()
        return redirect("/")
        
    return render(request,"add_employee.html")

def edit_employee(request,emp_id):
    emp_data = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        emp_data.Name = request.POST.get('name')
        emp_data.Department = request.POST.get('department')
        emp_data.Salary = request.POST.get('salary')
        emp_data.save()
        return redirect("/")
    
    return render(request,"edit_employee.html",{"emp_data":emp_data})

def delete_employee(request,emp_id):
    emp_data = Employee.objects.get(emp_id=emp_id)
    if (emp_data):
        emp_data.delete()
        return redirect("/")