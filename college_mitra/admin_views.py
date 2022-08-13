from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from collegeMitra_app.models import Course,SessionYear,Student,Staff,Subject,staff_notification,staff_leave,student_result
from collegeMitra_app.models import CustomUser
from django.contrib import messages

def HOME(req):
    return render(req,'Admin/home.html')

def NOTIFICATIONS(req):
    staff = Staff.objects.filter(admin= req.user.id)
    for i in staff:
        staff_id = i.id
    notification= staff_notification.objects.filter(admin_id=staff_id)
    context={
            'notification':notification,
        }
    return render(req,'Admin/notification.html',context)

def STATUS(req,id):
    notification= staff_notification.objects.get(id=id)
    notification.status=1
    notification.save()
    return redirect('adminNotifications')

def STAFF_APPLY_LEAVE(req):
    staff = Staff.objects.filter(admin= req.user.id)
    for i in staff:
        staff_id = i.id
    leave= staff_leave.objects.filter(staff_id=staff_id)
    context={
            'leave':leave,
        }
    return render(req,'Admin/apply_leave.html',context)

def STAFF_ADD_LEAVE(req):
    staff = Staff.objects.get(admin= req.user.id)
    if req.method=='POST':
        leave_date=req.POST.get('date')
        reason=req.POST.get('reason')
        leave = staff_leave(
            staff_id=staff,
            date=leave_date,
            message=reason,
        )
        leave.save()
        messages.success(req,'Application for Leave Submitted Successfully')
    
    return redirect('staff_apply_leave')

def ADD_RESULT(req):
    staff = Staff.objects.get(admin = req.user.id)

    subjects = Subject.objects.filter(staff = staff)
    print(subjects)
    session_year = SessionYear.objects.all()
    action = req.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if req.method == "POST":
           subject_id = req.POST.get('subject_id')
           session_year_id = req.POST.get('session_year_id')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = SessionYear.objects.get(id = session_year_id)

           subjects = Subject.objects.filter(id = subject_id)
           for i in subjects:
               student_id = i.course.id
               students = Student.objects.filter(course_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }

    return render(req,'Admin/add_result.html',context)

def SAVE_RESULT(request):
    if request.method == "POST":
        total= 0
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = student_result.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = student_result.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_marks = assignment_mark
            result.exam_marks = Exam_mark
            result.total= int(Exam_mark) + int(assignment_mark)
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('add_result')
        else:
            total = int(Exam_mark) + int(assignment_mark)
            result = student_result(student_id=get_student, subject_id=get_subject, exam_marks=Exam_mark,
                                   assignment_marks=assignment_mark,total = total)
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('add_result')
    