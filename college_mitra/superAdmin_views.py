from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from collegeMitra_app.models import Course,SessionYear,Student,Staff,Subject,staff_notification,staff_leave,student_leave,student_notification
from collegeMitra_app.models import CustomUser
from django.contrib import messages
@login_required(login_url='/')
def HOME(req):
    student_count=Student.objects.all().count()
    staff_count=Staff.objects.all().count()
    course_count=Course.objects.all().count()
    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
    }
    return render(req,'superAdmin/home.html',context)

@login_required(login_url='/')
def ADDSTUDENT(req):
    course=Course.objects.all()
    session_year=SessionYear.objects.all()
    context={
        'course':course,
        'session':session_year,
    }
    if req.method == 'POST':
        profile_pic=req.FILES.get('profile_pic')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        password=req.POST.get('password')
        address=req.POST.get('address')
        gender=req.POST.get('gender')
        course_id=req.POST.get('course_id')
        sessionyear_id=req.POST.get('sessionyear_id')
        email=req.POST.get('email')
        username=req.POST.get('user_name')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(req,'Student Email Already Exists')
            return redirect('addStudent')
        else:
            user= CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()
            course=Course.objects.get(id=course_id)
            session_year=SessionYear.objects.get(id=sessionyear_id)
            student= Student(
                admin=user,
                address=address,
                sessionyear_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(req,user.first_name +" "+user.last_name+ " successfully added")
            
    return render(req,'superAdmin/addstudent.html',context)

@login_required(login_url='/')
def VIEWSTUDENT(req):
    student = Student.objects.all()
    context={
        'student':student,
    }
    return render(req,'superAdmin/view_student.html',context)


@login_required(login_url='/')
def EDITSTUDENT(req,id):
    student = Student.objects.filter(id= id)
    course = Course.objects.all()
    session_year=SessionYear.objects.all()
    context = {
        'student':student,
        'course':course,
        'session':session_year,
    }
    return render(req,'superAdmin/editstudent.html',context)

@login_required(login_url='/')
def UPDATESTUDENT(req):
    if req.method == 'POST':
        profile_pic=req.FILES.get('profile_pic')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        password=req.POST.get('password')
        address=req.POST.get('address')
        gender=req.POST.get('gender')
        course_id=req.POST.get('course_id')
        sessionyear_id=req.POST.get('sessionyear_id')
        email=req.POST.get('email')
        username=req.POST.get('user_name')
        ID=req.POST.get('id')
        user = CustomUser.objects.get(id=ID)
        
        if profile_pic != None and profile_pic != "":
            user.profile_pic=profile_pic
        if first_name != None and first_name != "":
            user.first_name=first_name
        if last_name != None and last_name != "":
            user.last_name=last_name
        if password != None and password != "":
            user.set_password(password)
        if username != None and username != "":
            user.username=username
        if email != None and email != "":
            user.email=email

        user.save()
        student = Student.objects.get(admin = ID)
        student.address = address
        student.gender=gender
        
        course = Course.objects.get(id=course_id)
        year= SessionYear.objects.get(id=sessionyear_id)
        student.course_id=course
        student.sessionyear_id=year
        student.save()
        messages.success(req,'Record Updated Successfully')
        return redirect('viewstudent')
    return render(req,'superAdmin/editstudent.html')

def DELETESTUDENT(req,id):
    student = CustomUser.objects.get(id= id)
    student.delete()
    messages.success(req,'Records Deleted Successfully')
    return redirect('viewstudent')

def ADDCOURSE(req):
    if req.method=='POST':
        name=req.POST.get('course_name')
        course= Course(name=name)
        course.save()
        messages.success(req,'Course Added Successfully')
        return redirect('addcourse')
    return render(req,'superAdmin/addcourse.html')

@login_required(login_url='/')
def VIEWCOURSE(req):
    course = Course.objects.all()
    context={
        'course':course,
    }
    return render(req,'superAdmin/view_course.html',context)

@login_required(login_url='/')
def EDITCOURSE(req,id):
    course = Course.objects.filter(id=id)
    context = {
        'course':course,
    }
    return render(req,'superAdmin/editcourse.html',context)

@login_required(login_url='/')
def UPDATECOURSE(req):
    if req.method=='POST':
        name= req.POST.get('course_name')
        ID=req.POST.get('id')
        course=Course.objects.get(id=ID)
        course.name=name
        course.save()
        messages.success(req,'Updated Successfully')
        return redirect('viewcourse')
    return render(req,'superAdmin/editcourse.html',context)

@login_required(login_url='/')
def DELETECOURSE(req,id):
    course = Course.objects.filter(id=id)
    course.delete()
    messages.success(req,'Course Deleted Successfully')
    return redirect('viewcourse')

@login_required(login_url='/')
def ADDSTAFF(req):
    if req.method == 'POST':
        profile_pic=req.FILES.get('profile_pic')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        password=req.POST.get('password')
        address=req.POST.get('address')
        gender=req.POST.get('gender')
        email=req.POST.get('email')
        username=req.POST.get('user_name')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(req,'Staff Email Already Exists')
            return redirect('addstaff')
        else:
            user= CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()
            staff= Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(req,user.first_name +" "+user.last_name+ " successfully saved")
    return render(req,'superAdmin/addstaff.html')

@login_required(login_url='/')
def VIEWSTAFF(req):
    staff = Staff.objects.all()
    context={
        'staff':staff,
    }
    return render(req,'superAdmin/view_staff.html',context)

@login_required(login_url='/')
def EDITSTAFF(req,id):
    staff = Staff.objects.filter(id= id)
    context = {
        'staff':staff,
    }
    return render(req,'superAdmin/editstaff.html',context)

@login_required(login_url='/')
def UPDATESTAFF(req):
    if req.method == 'POST':
        profile_pic=req.FILES.get('profile_pic')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        password=req.POST.get('password')
        address=req.POST.get('address')
        gender=req.POST.get('gender')
        email=req.POST.get('email')
        username=req.POST.get('user_name')
        ID=req.POST.get('id')
        user = CustomUser.objects.get(id=ID)
        
        if profile_pic != None and profile_pic != "":
            user.profile_pic=profile_pic
        if first_name != None and first_name != "":
            user.first_name=first_name
        if last_name != None and last_name != "":
            user.last_name=last_name
        if password != None and password != "":
            user.set_password(password)
        if username != None and username != "":
            user.username=username
        if email != None and email != "":
            user.email=email

        user.save()
        staff = Staff.objects.get(admin = ID)
        staff.address = address
        staff.gender=gender
        staff.save()
        messages.success(req,'Record Updated Successfully')
        return redirect('viewstaff')
    return render(req,'superAdmin/editstaff.html')

def DELETESTAFF(req,id):
    staff = CustomUser.objects.get(id= id)
    staff.delete()
    messages.success(req,'Records Deleted Successfully')
    return redirect('viewstaff')

@login_required(login_url='/')
def ADDSUBJECT(req):
    course=Course.objects.all()
    staff=Staff.objects.all()
    context={
        'course':course,
        'staff':staff,
    }
    if req.method == 'POST':
        name=req.POST.get('name')
        staff_id=req.POST.get('staff_id')
        course_id=req.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        staff= Staff.objects.get(id=staff_id)
        if Subject.objects.filter(name= name).exists():
            messages.error(req,'Subject Already Exists')
            return redirect('addsubject')
        else:
            subject= Subject(
                name=name,
                course=course,
                staff=staff, 
            )
            subject.save()
            messages.success(req,name + " successfully Added")
    return render(req,'superAdmin/addsubject.html',context)

@login_required(login_url='/')
def VIEWSUBJECT(req):
    subject = Subject.objects.all()
    context={
        'subject':subject,
    }
    return render(req,'superAdmin/view_subject.html',context)

@login_required(login_url='/')
def EDITSUBJECT(req,id):
    subject = Subject.objects.filter(id= id)
    course = Course.objects.all()
    staff  = Staff.objects.all()
    context = {
        'subject':subject,
        'course':course,
        'staff':staff,
    }
    return render(req,'superAdmin/editsubject.html',context)

@login_required(login_url='/')
def UPDATESUBJECT(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        staff_id=req.POST.get('staff_id')
        course_id=req.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        staff= Staff.objects.get(id=staff_id)
        ID=req.POST.get('id')
        subject = Subject.objects.get(id=ID)
        subject.name=name
        subject.course=course
        subject.staff= staff
        subject.save()
        messages.success(req,'Subject Updated Successfully')
        return redirect('viewsubject')
    return render(req,'superAdmin/editsubject.html')

@login_required(login_url='/')
def DELETESUBJECT(req,id):
    subject = Subject.objects.get(id= id)
    subject.delete()
    messages.success(req,'Subject Deleted Successfully')
    return redirect('viewsubject')

@login_required(login_url='/')
def ADDSESSION(req):
    if req.method == 'POST':
        start= req.POST.get('start')
        end= req.POST.get('end')
        session = SessionYear(
            session_start=start,
            session_end=end,
        )
        session.save()
        messages.success(req,'Session Added Successfully')
        return redirect('addsession')
    return render(req,'superAdmin/addsession.html')

@login_required(login_url='/')
def VIEWSESSION(req):
    session = SessionYear.objects.all()
    context={
        'session':session,
    }
    return render(req,'superAdmin/view_session.html',context)

@login_required(login_url='/')
def EDITSESSION(req,id):
    session = SessionYear.objects.filter(id= id)
    context = {
        'session':session,
    }
    return render(req,'superAdmin/editsession.html',context)

@login_required(login_url='/')
def UPDATESESSION(req):
    if req.method == 'POST':
        start= req.POST.get('start')
        end= req.POST.get('end')
        ID= req.POST.get('id')
        session = SessionYear.objects.get(id=ID)
        session.session_start=start
        session.session_end=end
        session.save()
        messages.success(req,'Session Updated Successfully')
        return redirect('viewsession')

@login_required(login_url='/')
def DELETESESSION(req,id):
    session = SessionYear.objects.get(id= id)
    session.delete()
    messages.success(req,'Session Deleted Successfully')
    return redirect('viewsession')

@login_required(login_url='/')
def SEND_ADMIN_NOTIFICATION(req):
    staff = Staff.objects.all()
    see_notification = staff_notification.objects.all().order_by('-id')[0:5]
    
    context={
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(req,'superAdmin/staff_notification.html',context)

@login_required(login_url='/')
def SAVE_ADMIN_NOTIFICATION(req):
    if req.method== 'POST':
        staff_id=req.POST.get('admin_id')
        message=req.POST.get('message')
        
        staff = Staff.objects.get(admin=staff_id)
        notification= staff_notification(
            admin_id=staff,
            message=message
        )
        notification.save()
        messages.success(req,'Notification Sent')
        return redirect('send_admin_notification')
        
    return render(req,'superAdmin/staff_notification.html')

def STAFF_VIEW_LEAVE(req):
    leave=staff_leave.objects.all()
    context={
        'leave':leave,
    }
    return render(req,'superAdmin/staff_leave.html',context)

def STAFF_APPROVE_LEAVE(req,id):
    leave=staff_leave.objects.get(id=id)
    leave.status=1
    leave.save()
    return redirect('staff_view_leave')

def STAFF_DISAPPROVE_LEAVE(req,id):
    leave=staff_leave.objects.get(id=id)
    leave.status=2
    leave.save()
    return redirect('staff_view_leave')

@login_required(login_url='/')
def SEND_STUDENT_NOTIFICATION(req):
    student = Student.objects.all()
    see_notification = student_notification.objects.all().order_by('-id')[0:5]
    
    context={
        'staff':student,
        'see_notification':see_notification,
    }
    return render(req,'superAdmin/student_notification.html',context)

@login_required(login_url='/')
def SAVE_STUDENT_NOTIFICATION(req):
    if req.method== 'POST':
        student_id=req.POST.get('admin_id')
        message=req.POST.get('message')
        
        student = Student.objects.get(admin=student_id)
        notification= student_notification(
            student_id=student,
            message=message
        )
        notification.save()
        messages.success(req,'Notification Sent')
        return redirect('send_student_notification')
        
    return render(req,'superAdmin/staff_notification.html')

def STUDENT_VIEW_LEAVE(req):
    leave=student_leave.objects.all()
    context={
        'leave':leave,
    }
    return render(req,'superAdmin/student_leave.html',context)

def STUDENT_APPROVE_LEAVE(req,id):
    leave=student_leave.objects.get(id=id)
    leave.status=1
    leave.save()
    return redirect('student_view_leave')

def STUDENT_DISAPPROVE_LEAVE(req,id):
    leave=student_leave.objects.get(id=id)
    leave.status=2
    leave.save()
    return redirect('student_view_leave')