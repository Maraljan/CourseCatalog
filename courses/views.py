from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from courses.forms import CourseForm


class MainPageView(FormView):
    template_name = 'main_page.html'
    form_class = CourseForm


