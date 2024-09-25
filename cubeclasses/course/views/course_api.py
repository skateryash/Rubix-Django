from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from course.serializers import CourseSerializer
from course.models import Courses
from rest_framework import status, viewsets

# Method 1: View Set
class CourseViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Courses.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data})

# Method 2: API View
class CourseAPI(APIView):    
    def set_course(self, id):
        return Courses.objects.get(id=id)

    def get(self, request):
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        data = request.data
        course = self.set_course(data['id'])
        serializer = CourseSerializer(course, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        data = request.data
        course = self.set_course(data['id'])
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        course = self.set_course(request.data['id'])
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Method 3: api_view decorator
# @api_view(['GET'])
# def index(request):
#     courses = Courses.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add(request):
#     data = request.data
#     serializer = CourseSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PATCH'])
# def edit(request):
#     data = request.data
#     course = set_course(data['id'])
#     serializer = CourseSerializer(course, data=data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update(request):
#     data = request.data
#     course = set_course(data['id'])
#     serializer = CourseSerializer(course, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete(request):
#     course = set_course(request.data['id'])
#     course.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# def set_course(id):
#     return Courses.objects.get(id=id)
