from django.urls import path
from hostel import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_info/', views.database, name='student'),
    path('add_student/', views.add, name='addstudent')
]