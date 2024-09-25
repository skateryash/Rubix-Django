from course.models import Courses
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'
