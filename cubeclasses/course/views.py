from django.shortcuts import redirect, render, get_object_or_404
from .models import Courses
from .forms import CourseForm

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    level_display = dict(Courses.LEVELS)[course.level]
    mode_display = dict(Courses.MODES)[course.mode]
    return render(request, 'course.html', {'course': course, 'level':level_display, 'mode':mode_display})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            new_course = form.save()
            return redirect('courses')
        else:
            return render(request, 'add_course.html', {'form': form})
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})
