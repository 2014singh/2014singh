from django.shortcuts import render
from .models import EmpData
from .forms import Emp_insert_Form,Emp_delete_form,Emp_update_form
from django.http.response import HttpResponse

def home(request):
    return render(request,'home.html')



def emp_insert(request):
    if request.method=="POST":
        iform=Emp_insert_Form(request.POST)
        if iform.is_valid():
            emp_id=request.POST.get('emp_id','')
            emp_first_name=request.POST.get('emp_first_name','')
            emp_last_name=request.POST.get('emp_last_name','')
            emp_mobile_number=request.POST.get('emp_mobile_number','')
            emp_email_id=request.POST.get('emp_email_id','')
            emp_salary=request.POST.get('emp_salary','')
            emp_location=request.POST.get('emp_location','')
            emp_position=request.POST.get('emp_position','')

            data=EmpData(
                emp_id=emp_id,
                emp_first_name=emp_first_name,
                emp_last_name=emp_last_name,
                emp_mobile_number=emp_mobile_number,
                emp_email_id=emp_email_id,
                emp_salary=emp_salary,
                emp_location=emp_location,
                emp_position=emp_position,
            )
            data.save()
            iform=Emp_insert_Form()
            return render(request,'insert.html',{'iform':iform})
        else:
            return HttpResponse("Data Is Invalid")
    else:
        iform=Emp_insert_Form()
        return render(request,'insert.html',{'iform':iform})


def emp_retrive(request):
    rdata=EmpData.objects.all
    return render(request,'retrive.html',{'rdata':rdata})




def emp_update(request):
    if request.method=="POST":
        uform=Emp_update_form(request.POST)
        if uform.is_valid():
            emp_id=request.POST.get('emp_id')
            emp_location=request.POST.get('emp_location')
            udata=EmpData.objects.filter(emp_id=emp_id)
            if not udata:
                return HttpResponse("data is not avliable")
            else:
                udata.update(emp_location=emp_location)
                uform = Emp_update_form()
                return render(request, 'update.html', {'uform': uform})
        else:
            return HttpResponse("Invalid form")


    else:
        uform=Emp_update_form()
        return render(request,'update.html',{'uform':uform})


def emp_delete(request):
    if request.method=="POST":
        dform=Emp_delete_form(request.POST)
        if dform.is_valid():
            emp_id=request.POST.get('emp_id')
            ddata=EmpData.objects.filter(emp_id=emp_id)

            if not ddata:
                return HttpResponse("data not avliable")
            else:
                ddata.delete()
                dform = Emp_delete_form()
                return render(request, 'delete.html', {'dform': dform})

    else:
        dform=Emp_delete_form()
        return render(request,'delete.html',{'dform':dform})
