from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from student.models import Student

class StudentList(ListView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = ['first_name','last_name','email','mobile']
    success_url = reverse_lazy('student:student_list')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name','last_name','email','mobile']
    success_url = reverse_lazy('student:student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student_list')
