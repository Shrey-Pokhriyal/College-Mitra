from django.shortcuts import redirect,render,HttpResponse
from collegeMitra_app.emailBackend import emailBackend
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collegeMitra_app.models import CustomUser
from collegeMitra_app.models import CustomUser
def BASE(req):
    return render(req,'base.html')

def LOGIN(req):
    return render(req,'login.html')

def doLogin(req):
    if req.method == 'POST':
        user = emailBackend.authenticate(req,
                                         username=req.POST.get('email'),
                                         password=req.POST.get('password'),)
        if user!=None:
            login(req,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('superAdminhome')
            elif user_type == '2':
                return redirect('adminhome')
            elif user_type == '3':
                return redirect('studenthome')
            else:
                messages.error(req,'Email and Password Invalid')
                return redirect('login')
        else:
            messages.error(req,'Email and Password Invalid')
            return redirect('login')

def doLogout(req):
    logout(req)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(req):
    user = CustomUser.objects.get(id=req.user.id)
    context ={
        "user":user,
    }
    return render(req,'profile.html',context)

@login_required(login_url='/')
def PROFILE_UPDATE(req):
    if req.method == 'POST':
        profile_pic=req.FILES.get('profile_pic')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        password=req.POST.get('password')
        
        try:
            customuser=CustomUser.objects.get(id=req.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic=profile_pic
                
            if password != None and password != "":
                customuser.set_password(password)
            
            customuser.save()
            messages.success(req,'Profile Updated Successfully')
            redirect('profile')
        except:
            messages.failure(req,'Profile Updated Failed, Try again after sometime')
            pass
        
    return render(req,'profile.html')