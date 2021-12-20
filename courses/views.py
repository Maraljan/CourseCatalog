import datetime

from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, FormView

from courses.models import Course
from courses.forms import SearchForm


class HomePageView(ListView, FormView):
    template_name = 'courses/homepage.html'
    form_class = SearchForm
    model = Course
    context_object_name = 'courses'

    def form_valid(self, form):
        query = form.cleaned_data['query']
        start_time = form.cleaned_data['start_time']
        if query and start_time:
            return HttpResponseRedirect(reverse('courses:both', kwargs={
                'query': query,
                'start_time': start_time,
            }))
        if query:
            return HttpResponseRedirect(reverse('courses:query', kwargs={
                'query': query,
            }))
        if start_time:
            return HttpResponseRedirect(reverse('courses:start_time', kwargs={
                'start_time': start_time,
            }))
        return HttpResponseRedirect(reverse('courses:homepage'))

    def get_queryset(self):
        queryset = Course.objects.all()
        if query := self.kwargs.get('query'):
            queryset = queryset.filter(Q(course_name__icontains=query) | Q(detail_info__icontains=query))
        if start_time := self.kwargs.get('start_time'):
            queryset = queryset.filter(start_time__gte=start_time)
        return queryset.order_by('-start_time')

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
