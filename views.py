from django.shortcuts import render, redirect
from.forms import EmployeeForm
from.models import Employee

# Create your views here.
def emp_form(request, id=0):
    if (request.method=="GET"):
        if (id == 0):       #insert operation
            form=EmployeeForm()
        else:                   #update operation
            employee = Employee.objects.get(pk=id)  # filtering based on primarykey
            form = EmployeeForm(instance=employee)
        return render(request,'emp_form.html',{'form':form})
    else:
        if (id == 0):  # insert operation
            form = EmployeeForm(request.POST)
        else:  # update
            employee = Employee.objects.get(pk=id)  # filtering based on primarykey
            form = EmployeeForm(request.POST, instance=employee)
        if(form.is_valid()):
            form.save()

        return redirect('/employee/list')

    return render(request,'emp_form.html', {'form':form})
def emp_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'emp_list.html', context)


def emp_delete(request,id):
    #deleting based on particular id
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')