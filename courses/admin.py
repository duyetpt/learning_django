from django.contrib import admin
from courses.models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'educator')
    search_fields = ('name',)

admin.site.register(Course, CourseAdmin)
