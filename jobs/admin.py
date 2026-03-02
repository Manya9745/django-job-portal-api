# from django.contrib import admin

# from .models import User, Job, Application

# # admin.site.register(User)
# admin.site.register(Job)
# admin.site.register(Application)
# Register your models here.
# from django.contrib import admin
# from .models import Employer, Candidate, Job, Application

# admin.site.register(Employer)
# admin.site.register(Candidate)
# admin.site.register(Job)
# admin.site.register(Application)

from django.contrib import admin
from .models import Employer, Candidate, Job, Application


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'user')
    search_fields = ('company_name', 'location')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills')
    search_fields = ('user__username', 'skills')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'salary', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'candidate', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'candidate__user__username')