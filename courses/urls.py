from django.urls import path

from courses.views import MainPageView

app_name = 'courses'

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]