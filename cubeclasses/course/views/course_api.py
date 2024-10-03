from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from course.serializers import CourseSerializer, RegisterSerializer, LoginSerializer
from course.models import Courses
from rest_framework import status, viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.data['username'],
                            password=serializer.data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status': True, 
                         'message': 'user logged in successfully',
                         'token': str(token)}, status.HTTP_201_CREATED)

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status': True, 'message': 'user created successfully'}, status.HTTP_201_CREATED)

# # Method 1: View Set
# class CourseViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         queryset = Courses.objects.all()
#         serializer = CourseSerializer(queryset, many=True)
#         return Response({'status': 200, 'data': serializer.data})

# Method 2: API View
# class CourseAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def set_course(self, id):
#         return Courses.objects.get(id=id)

#     def get(self, request):
#         try:    
#             courses = Courses.objects.all()
#             page = request.GET.get('page', 1)
#             page_size = 3
#             paginator = Paginator(courses, page_size)
#             serializer = CourseSerializer(paginator.page(page), many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response({
#                 'status': False,
#                 'message': 'Invalid page'
#             })
    
#     def post(self, request):
#         data = request.data
#         serializer = CourseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request):
#         data = request.data
#         course = self.set_course(data['id'])
#         serializer = CourseSerializer(course, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request):
#         data = request.data
#         course = self.set_course(data['id'])
#         serializer = CourseSerializer(course, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         course = self.set_course(request.data['id'])
    
#     def delete(self, request):
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Method 3: api_view decorator
@api_view(['GET'])
def index(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    data = request.data
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit(request):
    data = request.data
    course = set_course(data['id'])
    serializer = CourseSerializer(course, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request):
    data = request.data
    course = set_course(data['id'])
    serializer = CourseSerializer(course, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request):
    course = set_course(request.data['id'])
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def set_course(id):
    return Courses.objects.get(id=id)
