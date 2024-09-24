from django.contrib import admin
from .models import Courses, CourseReview, Affiliates, Certificate

# Register your models here.
class CourseReviewInline(admin.TabularInline):
    model = CourseReview
    extra = 2

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'level')
    inlines = [CourseReviewInline]

class AffiliateAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('course',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('course', 'number')

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Affiliates, AffiliateAdmin)
admin.site.register(Certificate, CertificateAdmin)
