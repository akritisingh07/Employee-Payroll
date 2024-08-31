"""
URL configuration for EMPLOYEE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from payroll import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.IndexVw,name='index'),
    path('login',views.LoginXz,name='login'),
    path('logout',views.LogoutVw,name='logout'),
    path('attendance',views.AttendanceVw,name='attendance'),
    path('add_attendance',views.Add_attendanceVw,name='add_attendance'),
    path('attendance_dlt/<id>',views.Dlt_attendance_dataVw,name='attendance_dlt'),
    path('attendance_update/<id>',views.attend_list_updtVw,name='attendance_update'),
    path('payroll_list',views.PayrollListVw,name='payroll_list'),
    path('add_employee',views.AddEmployeeVw,name='add_employee'),
    path('registration',views.RegVw),
    path('employee_list',views.EmpVw,name='employee_list'),
    path('emp_list_dlt/<id>',views.Delete_emp_dataVw,name='emp_list_dlt'),
    path('emp_list_update/<id>',views.emp_list_updateVw,name='emp_list_update'),
    path('add_payroll',views.Add_PayVw,name='add_payroll'),
    path('payroll_list_dlt/<id>',views.Delete_payroll_dataVw,name='payroll_list_dlt'),
    path('payroll_list_updt/<id>',views.Payroll_List_UpdateVw,name='payroll_list_updt'),
    path('department',views.departmentVw,name='department'),
    path('department_list_del/<id>',views.Delete_depatVw,name='department_list_del')

    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)