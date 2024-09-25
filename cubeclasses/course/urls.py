from django.urls import path, include
from .views import course, CourseAPI, CourseViewSet

# from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
urlpatterns = router.urls

urlpatterns = [
    path('', course.courses, name='courses'),
    path('<int:course_id>/', course.course, name='course'),
    path('add/', course.add_course, name='add_course'),

    # path('api/index/', course_api.index),
    # path('api/add/', course_api.add),
    # path('api/edit/', course_api.edit),
    # path('api/update/', course_api.update),
    # path('api/delete/', course_api.delete),

    path('api/', CourseAPI.as_view()),

    path('', include(router.urls)),
]
