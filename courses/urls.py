from django.urls import path

from courses.views import CreateCourseView, HomePageView, DetailInfoView, DeleteCourseView, UpdateCourseView

app_name = 'courses'

urlpatterns = [
    path('create/', CreateCourseView.as_view(), name='create_course'),
    path('detail/<int:pk>', DetailInfoView.as_view(), name='detail_info'),
    path('delete/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),
    path('update/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('', HomePageView.as_view(), name='homepage'),
    path('both/<str:query>/<str:start_time>/', HomePageView.as_view(), name='both'),
    path('query/<str:query>/', HomePageView.as_view(), name='query'),
    path('start_time/<str:start_time>/', HomePageView.as_view(), name='start_time'),
]
