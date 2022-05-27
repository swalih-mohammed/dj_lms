from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from courses.models import LiveClass, EnrolledCourse
from .models import Teacher

from .models import User, Student


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email',)


class inlineLiveClass(admin.StackedInline):
    model = LiveClass
    extra = 0


class TeacherAdmin(admin.ModelAdmin):
    inlines = [inlineLiveClass]
    list_display = [
        'user',
    ]
    search_fields = ['user']


class inlineEnrolledCourse(admin.StackedInline):
    model = EnrolledCourse
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    inlines = [inlineEnrolledCourse]
    list_display = [
        'user',
    ]
    search_fields = ['user']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
