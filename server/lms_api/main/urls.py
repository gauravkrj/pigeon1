from django.urls import path
from .import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login',views.teacher_login),

    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('student-login',views.student_login),

    path('parent/', views.ParentList.as_view()),
    path('parent/<int:pk>/', views.ParentDetail.as_view()),
    path('parent-login',views.parent_login),

    path('adminstaff/', views.AdminstaffList.as_view()),
    path('adminstaff/<int:pk>/', views.AdminstaffDetail.as_view()),
    path('adminstaff-login',views.adminstaff_login),

    path('classroom/', views.ClassroomList.as_view()),
    path('classroom/<int:pk>/', views.ClassroomDetail.as_view()),
   # path('useraccount/', view.UseraccountList.as_view()),
   # path('usermanager/', view.UsermanagerList.as_view()),
    #path('<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-retrieve-update-destroy'),
    # Other URL patterns for other views
]
