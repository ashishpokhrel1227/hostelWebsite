from django.shortcuts import render

from hostel.models import Student
from hostel.forms import StudentForm


def index(request):
    return render(request, 'index.html', {})

def database(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            
            print('i am valid')
            form.save()
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'database.html', context=context)

def add(request):
    studentform = StudentForm()
    context = {
        'studentform': studentform
    }
    return render(request, 'addstudent.html', context=context)

