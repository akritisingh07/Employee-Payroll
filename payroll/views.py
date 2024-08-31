from django.shortcuts import render,redirect
from payroll.models import *
from django.http import HttpResponse 
from django.contrib import messages
# Create your views here.
#----------INDEX------------#
def IndexVw(request):
    if "email" in request.session:
        email = request.session['email']#get
        data = Registration_DB.objects.filter(email=email).first()
        return render(request,'index.html',{"data":data})
    else:
        return redirect('/login')


#----------LOGIN------------#
def LoginXz(request):
    if request.method == "POST":
        email = request.POST['email'] 
        password = request.POST['password']
        if Registration_DB.objects.filter(email=email,password=password).exists():
           data =Registration_DB.objects.get(email=email,password=password)
           request.session['email'] = data.email  #set
           return redirect('index')
        else:
            #return HttpResponse('Your Email / Password is invalid')
            messages.info(request,"Invalid email/password")
            return redirect('/login')
    return render(request,'login.html')

def authen(request):
    if('email' in request.session):
        return redirect('index')
    else:
        return redirect('login')
    

def LogoutVw(request):
    del request.session['email']
    messages.info(request,"Logout Successfully....")
    return redirect('/login')
    
#----------ATTENDANCE LIST------------#
def AttendanceVw(request):
    if "email" in request.session:
        email = request.session['email']#get
        data = Registration_DB.objects.filter(email=email).first()
        attend_data = Add_AttendanceDB.objects.filter(status=True)
        return render(request,'attendance.html',{"attend_data":attend_data,"data":data}) 
    else:
        return render('/login')



#---------Add Attendance List----------#
def Add_attendanceVw(request):
    if "email" in request.session:
        email = request.session['email']#get
        data = Registration_DB.objects.filter(email=email).first()
        if request.method == "POST":
            date = request.POST['date']
            emp_no = request.POST['emp_no']
            name = request.POST['name']
            time = request.POST['time']
        if Add_AttendanceDB.objects.filter(emp_no=emp_no,name=name).exists():
            return HttpResponse('Attendance data is already register')
        else:
            Add_AttendanceDB.objects.create(date=date,emp_no=emp_no,name=name,time=time)
        return render(request,'add_attendance.html')
    else:
        return redirect('/login')
#--------Attendance List Update---------#
def attend_list_updtVw(request,id):
    attend_data = Add_AttendanceDB.objects.filter(id=id)
    if request.method == "POST":
      date = request.POST['date']
      emp_no = request.POST['emp_no']
      name = request.POST['name']
      time = request.POST['time']
      data = Add_AttendanceDB.objects.get(id=id)
      data.date=date
      data.emp_no=emp_no
      data.name=name
      data.time=time
      data.save()
      return redirect('/attendance')
      
    return render(request,'attendance_update.html',{"attend_data":attend_data})

    

#----------Delete Attendance List------------#
def Dlt_attendance_dataVw(request,id):
    Add_AttendanceDB.objects.filter(id=id).update(status=False)
    return redirect('/attendance')

#----------PAYROLL LIST-------------#
def PayrollListVw(request):
    payr_data = Add_PayrollDB.objects.filter(status=True)
    return render(request,'payroll_list.html',{"payr_data":payr_data})

#---------DELETING PAYROLL LIST--------------#
def Delete_payroll_dataVw(request,id):
    Add_PayrollDB.objects.filter(id=id).update(status=False)
    return redirect('/payroll_list')

#---------Payroll List Update---------#
def Payroll_List_UpdateVw(request,id):
    payr_data = Add_PayrollDB.objects.filter(id=id)
    if "email" in request.session:
        email = request.session['email']#get
        data = Registration_DB.objects.filter(email=email).first()
    if request.method == "POST":
        refno = request.POST['refno']
        datefrom = request.POST['datefrom']
        dateto = request.POST['dateto']
        data = Add_PayrollDB.objects.get(id=id)
        data.refno=refno
        data.datefrom=datefrom
        data.dateto=dateto
        data.save()
        return redirect('/add_payroll')
    return render(request,'payroll_list.html',{"payr_data":payr_data})

#------------ADD EMPLOYEE LIST--------#
def AddEmployeeVw(request):
    if request.method == "POST":
        name = request.POST['emp_name']
        mobile = request.POST['numb']
        email = request.POST['email']
        addr = request.POST['addr']
        image = request.FILES['img']
        if Add_EmployeeDB.objects.filter(mobile=mobile,email=email).exists():
            return HttpResponse('employee data is already register')
        else:
            Add_EmployeeDB.objects.create(name=name,mobile=mobile,email=email,addr=addr,emp_img=image)
            return HttpResponse('data has been submitted successfully....')
    return render(request,'add_employee.html')


#---------employee list update -------------#
def emp_list_updateVw(request,id):
    #print('rdrdrdtffg',id)
    emp_data = Add_EmployeeDB.objects.filter(id=id)
    if request.method == "POST":
        name = request.POST['emp_name']
        mobile = request.POST['numb']
        email = request.POST['email']
        addr = request.POST['addr']
        image = request.FILES.get('img')
        data = Add_EmployeeDB.objects.get(id=id)
        if image.size == 0:
            data.name=name
            data.mobile=mobile
            data.email=email
            data.addr=addr
            data.save()
        else:
            data.name=name
            data.mobile=mobile
            data.email=email
            data.addr=addr
            data.emp_img=image
            data.save()
        return redirect('/employee_list')
    return render(request,'employee_update.html',{"emp_data":emp_data})


#------------REGISTRATION-------------#
def RegVw(request):
    if request.method == "POST":
        name = request.POST['name'] #Akriti
        email = request.POST['email'] #ak07@gmail.com
        password = request.POST['pass'] #12345
        if Registration_DB.objects.filter(name=name,email=email,password=password).exists():
           return HttpResponse('You are already Registered...')
        else:
            Registration_DB.objects.create(name=name,email=email,password=password)
            return HttpResponse('You are Succesfully Registered...')
   
    return render(request,'registration.html')

#----------EMPLOYEE LIST------------#
def EmpVw(request):
    emp_data = Add_EmployeeDB.objects.filter(status=True)
    return render(request,'employee_list.html',{"emp_data":emp_data})

#----------Deleting Employee list--------#
def Delete_emp_dataVw(request,id):
    Add_EmployeeDB.objects.filter(id=id).update(status=False)
    return redirect('/employee_list')

#----------ADD PAYROLL LIST------------#
def Add_PayVw(request):
    if request.method == "POST":
        refno = request.POST['refno']
        datefrom = request.POST['datefrom']
        dateto = request.POST['dateto']
        if Add_PayrollDB.objects.filter(refno=refno,datefrom=datefrom,dateto=dateto).exists():
            return HttpResponse('Payroll data is already register')
        else:
            Add_PayrollDB.objects.create(refno=refno,datefrom=datefrom,dateto=dateto)
            return HttpResponse('data has been submitted successfully....')
    return render(request,'add_payroll.html')


#-------------Department------------#
def departmentVw(request):
    depart_data = Add_DepartmentDB.objects.filter(status=True)
    if request.method == "POST":
        name = request.POST['name']
        if Add_DepartmentDB.objects.filter(name=name).exists():
            return HttpResponse('Department List is already Register')
        else:
            Add_DepartmentDB.objects.create(name=name)
            return HttpResponse('Data has been submitted successfully....')
    return render(request,'department.html',{"depart_data":depart_data})

 #-----------Department List Delete------------#
def Delete_depatVw(request,id):
    Add_DepartmentDB.objects.filter(id=id).update(status=False)
    return redirect('/department')