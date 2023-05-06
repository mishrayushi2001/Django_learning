from django.contrib import admin

from enroll.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','stuid','stuname','stuemail','stupass')

# admin.site.register(Student,StudentAdmin)
