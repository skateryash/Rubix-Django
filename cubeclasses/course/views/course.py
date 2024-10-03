from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from course.models import Courses
from course.forms import CourseForm

def list_courses(request):
    courses = Courses.objects.all()
    paginator = Paginator(courses, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses.html', {'page_obj': page_obj})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
        else:
            return render(request, 'add_course.html', {'form': form})
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def show_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    level_display = dict(Courses.LEVELS)[course.level]
    mode_display = dict(Courses.MODES)[course.mode]
    return render(request, 'course.html', {'course': course, 'level':level_display, 'mode':mode_display})

def update_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'update.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    return render(request, 'delete.html', {'course': course})
 