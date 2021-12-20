from django.urls import path

from courses.views import CreateCourseView, HomePageView, DetailInfoView, DeleteCourseView, UpdateCourseView

app_name = 'courses'

urlpatterns = [
    path('course/', HomePageView.as_view(), name='homepage'),
    path('course/<str:course_name>/', HomePageView.as_view(), name='homepage_filter'),
    path('create/', CreateCourseView.as_view(), name='create_course'),
    path('detail/<int:pk>', DetailInfoView.as_view(), name='detail_info'),
    path('delete/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),
    path('update/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
]