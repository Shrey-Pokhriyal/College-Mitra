from email import message
from multiprocessing import context
import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from collegeMitra_app.models import Course,SessionYear,Student,Staff,Subject,student_notification,student_leave,student_result
from collegeMitra_app.models import CustomUser
from django.contrib import messages


def HOME(req):
    return render(req,'student/home.html')

def NOTIFICATIONS(req):
    student = Student.objects.filter(admin= req.user.id)
    for i in student:
        student_id = i.id
    notification= student_notification.objects.filter(student_id=student_id)
    context={
            'notification':notification,
        }
    return render(req,'student/notification.html',context)

def STATUS(req,id):
    notification= student_notification.objects.get(id=id)
    notification.status=1
    notification.save()
    return redirect('studentNotifications')

def STUDENT_APPLY_LEAVE(req):
    student = Student.objects.filter(admin= req.user.id)
    for i in student:
        student_id = i.id
    leave= student_leave.objects.filter(student_id=student_id)
    context={
            'leave':leave,
        }
    return render(req,'student/apply_leave.html',context)

def STUDENT_ADD_LEAVE(req):
    student = Student.objects.get(admin= req.user.id)
    if req.method=='POST':
        leave_date=req.POST.get('date')
        reason=req.POST.get('reason')
        leave = student_leave(
            student_id=student,
            date=leave_date,
            message=reason,
        )
        leave.save()
        messages.success(req,'Application for Leave Submitted Successfully')
    
    return redirect('student_apply_leave')

def RESULT(req):

    student = Student.objects.get(admin=req.user.id)
    result = student_result.objects.filter(student_id=student)
    context= {
        'result':result,
    }
    return render(req,'student/view_result.html',context)