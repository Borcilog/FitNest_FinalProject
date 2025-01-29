from django.contrib import admin
from .models import (Post, Video, MembershipPlan,
                     Trainer, ClassCategory, Schedule)

admin.site.register(Post)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at') 
    search_fields = ('title',) 
    list_filter = ('created_at',)

admin.site.register(MembershipPlan)
class MembershipPlan(admin.ModelAdmin):
    list_display = ("name", "duration_months")

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'specialties')

admin.site.register(ClassCategory)
class ClassCategory(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'membership', 'class_category', 'trainer', 'session_time')
    list_filter = ('membership', 'class_category', 'trainer')
    search_fields = ('user_name', 'session_time')
