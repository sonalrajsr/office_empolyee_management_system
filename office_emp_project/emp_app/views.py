from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index (request):
    return render(request, 'index.html')

def all_emp (request):
    emps = Employee.objects.all() # views all the list of employee
    contex = {
        'emps' : emps
    }
    return render(request, 'all_emp.html', contex)

def add_emp (request):
    if request.method == "POST":
        first_name = request.POST['first_name_form']
        last_name = request.POST['last_name_form']
        salary = int(request.POST['salary_form'])
        bonus = int(request.POST['bonus_form'])
        phone = int(request.POST['number_form'])
        dept = int(request.POST['dept_form'])
        role = int(request.POST['role_form'])
        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus = bonus, phone = phone, dept_id = dept, role_id = role)
        new_emp.save()
        return HttpResponse("Employee added successfully")
        # print("yes")
    elif request.method == 'GET': 
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('some error occured')
    
def remove_emp (request, emp_id = 0):
    if emp_id:
        try:
            employ_removed = Employee.objects.get(id = emp_id)
            employ_removed.delete()
            return HttpResponse(f'{employ_removed.first_name} {employ_removed.last_name} removed successfully')
        except:
            return HttpResponse("Please select correct details.")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp (request):
    if request.method  == 'POST' :
        name = request.POST['first_name_form']
        dept = request.POST['dept_form']
        role = request.POST['role_form']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Please enter correct Fields")
    # return render(request, 'filter_emp.html')

