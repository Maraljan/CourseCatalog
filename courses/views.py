import datetime

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, FormView

from courses.forms import SearchForm
from courses.models import Course


class HomePageView(ListView, FormView):
    template_name = 'courses/homepage.html'
    form_class = SearchForm
    model = Course
    context_object_name = 'courses'

    def form_valid(self, form):
        course_name = form.cleaned_data['course_name']
        return HttpResponseRedirect(reverse('courses:homepage_filter', kwargs={
            'course_name': course_name,
        }))

    def get_queryset(self):
        queryset = Course.objects.all()
        if course := self.kwargs.get('course_name'):
            queryset = queryset.filter(course_name__icontains=course)
        return queryset

    def get_initial(self) -> dict:
        return {
            'course_name': self.kwargs.get('course_name')
        }


class DetailInfoView(DetailView):
    template_name = 'courses/detail_info.html'
    model = Course
    context_object_name = 'course'


class CreateCourseView(CreateView):
    template_name = 'courses/create_course.html'
    model = Course
    fields = ['course_name', 'price', 'detail_info', 'start_time', 'end_time', 'image']
    success_url = reverse_lazy('courses:homepage')

    def get_initial(self) -> dict:
        return {
            'start_time': datetime.date.today(),
            'end_time': datetime.date.today()

        }


class DeleteCourseView(DeleteView):
    template_name = 'courses/delete_course.html'
    model = Course
    success_url = reverse_lazy('courses:homepage')


class UpdateCourseView(UpdateView):
    template_name = 'courses/update_course.html'
    model = Course
    fields = ['course_name', 'price', 'detail_info', 'start_time', 'end_time', 'image']
    success_url = reverse_lazy('courses:homepage')
