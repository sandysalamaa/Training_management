from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .models import Course , Trainer
from django.urls import reverse_lazy

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html' # Ensure this matches the template path
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course-list')


