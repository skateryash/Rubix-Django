from django.urls import path, include
from .views import course, course_api

# from myapp.views import UserViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'courses', CourseViewSet, basename='course')
# urlpatterns = router.urls

urlpatterns = [
    path('', course.list_courses, name='courses'),
    path('add/', course.add_course, name='add_course'),
    path('show/<int:course_id>/', course.show_course, name='course'),
    path('update/<int:course_id>/', course.update_course, name='update_course'),
    path('delete/<int:course_id>/', course.delete_course, name='delete_course'),

    path('api/index/', course_api.index),
    path('api/add/', course_api.add),
    path('api/edit/', course_api.edit),
    path('api/update/', course_api.update),
    path('api/delete/', course_api.delete),

    # path('register/', RegisterAPI.as_view()),
    # path('login/', LoginAPI.as_view()),
    # path('api/', CourseAPI.as_view()),

    # path('', include(router.urls)),
]
