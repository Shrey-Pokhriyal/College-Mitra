from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,superAdmin_views,admin_views,student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    
    #login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    
    #logout
    path('doLogout',views.doLogout,name='logout'),
    
    #profileUpdate
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profileUpdate'),
    
    #superAdmin path
    path('superAdmin/home',superAdmin_views.HOME,name='superAdminhome'),
    #student edits
    path('superAdmin/student/add',superAdmin_views.ADDSTUDENT,name='addStudent'),
    path('superAdmin/student/view',superAdmin_views.VIEWSTUDENT,name='viewstudent'),
    path('superAdmin/student/edit/<str:id>',superAdmin_views.EDITSTUDENT,name='editstudent'),
    path('superAdmin/student/update',superAdmin_views.UPDATESTUDENT,name='updatestudent'),
    path('superAdmin/student/delete/<str:id>',superAdmin_views.DELETESTUDENT,name='deletestudent'),
     #student edits
    path('superAdmin/staff/add',superAdmin_views.ADDSTAFF,name='addstaff'),
    path('superAdmin/staff/view',superAdmin_views.VIEWSTAFF,name='viewstaff'),
    path('superAdmin/staff/edit/<str:id>',superAdmin_views.EDITSTAFF,name='editstaff'),
    path('superAdmin/staff/update',superAdmin_views.UPDATESTAFF,name='updatestaff'),
    path('superAdmin/staff/delete/<str:id>',superAdmin_views.DELETESTAFF,name='deletestaff'),
    #courses
    path('superAdmin/course/add',superAdmin_views.ADDCOURSE,name='addcourse'),
    path('superAdmin/course/view',superAdmin_views.VIEWCOURSE,name='viewcourse'),
    path('superAdmin/course/edit/<str:id>',superAdmin_views.EDITCOURSE,name='editcourse'),
    path('superAdmin/course/update',superAdmin_views.UPDATECOURSE,name='updatecourse'),
    path('superAdmin/course/delete/<str:id>',superAdmin_views.DELETECOURSE,name='deletecourse'),
    
    #subject
    path('superAdmin/subject/add',superAdmin_views.ADDSUBJECT,name='addsubject'),
    path('superAdmin/subject/view',superAdmin_views.VIEWSUBJECT,name='viewsubject'),
    path('superAdmin/subject/edit/<str:id>',superAdmin_views.EDITSUBJECT,name='editsubject'),
    path('superAdmin/subject/update',superAdmin_views.UPDATESUBJECT,name='updatesubject'),
    path('superAdmin/subject/delete/<str:id>',superAdmin_views.DELETESUBJECT,name='deletesubject'),
    
    #subject
    path('superAdmin/session/add',superAdmin_views.ADDSESSION,name='addsession'),
    path('superAdmin/session/view',superAdmin_views.VIEWSESSION,name='viewsession'),
    path('superAdmin/session/edit/<str:id>',superAdmin_views.EDITSESSION,name='editsession'),
    path('superAdmin/session/update',superAdmin_views.UPDATESESSION,name='updatesession'),
    path('superAdmin/session/delete/<str:id>',superAdmin_views.DELETESESSION,name='deletesession'),
    
    #sendnotification
    path('superAdmin/admin/send_admin_notification',superAdmin_views.SEND_ADMIN_NOTIFICATION,name='send_admin_notification'),
    path('superAdmin/admin/save_admin_notification',superAdmin_views.SAVE_ADMIN_NOTIFICATION,name='save_admin_notification'),
    #sendnotificationtostudnet
    path('superAdmin/student/send_admin_notification',superAdmin_views.SEND_STUDENT_NOTIFICATION,name='send_student_notification'),
    path('superAdmin/student/save_admin_notification',superAdmin_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),
    #leave for staff
    path('superAdmin/staff_apply_leave',superAdmin_views.STAFF_VIEW_LEAVE,name='staff_view_leave'),
    path('superAdmin/staff_approve_leave/<str:id>',superAdmin_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('superAdmin/staff_disapprove_leave/<str:id>',superAdmin_views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),
    
    path('superAdmin/student_apply_leave',superAdmin_views.STUDENT_VIEW_LEAVE,name='student_view_leave'),
    path('superAdmin/student_approve_leave/<str:id>',superAdmin_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('superAdmin/student_disapprove_leave/<str:id>',superAdmin_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),
    
    #staff url
    path('Admin/home',admin_views.HOME,name='adminhome'),
    #notification
    path('Admin/notifications',admin_views.NOTIFICATIONS,name='adminNotifications'),
    path('Admin/status/<str:id>',admin_views.STATUS,name='adminStatus'),
    
    #leave
    path('Admin/staff_apply_leave',admin_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Admin/staff_add_leave',admin_views.STAFF_ADD_LEAVE,name='staff_add_leave'),
    
    #result
    path('Admin/add_result',admin_views.ADD_RESULT,name='add_result'),
    path('Admin/save_result',admin_views.SAVE_RESULT,name='save_result'),
    
    #student url
    path('student/home',student_views.HOME,name='studenthome'),
    #notification
    path('student/notifications',student_views.NOTIFICATIONS,name='studentNotifications'),
    path('student/status/<str:id>',student_views.STATUS,name='studentStatus'),
    
    #leave
    path('student/staff_apply_leave',student_views.STUDENT_APPLY_LEAVE,name='student_apply_leave'),
    path('student/staff_add_leave',student_views.STUDENT_ADD_LEAVE,name='student_add_leave'),
    
    #result
    path('student/result',student_views.RESULT,name='studentresult'),
    
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
