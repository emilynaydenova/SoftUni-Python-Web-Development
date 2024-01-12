from django.contrib import admin

from tasks.models import Task


# Register your models here.

# admin.site.register(Task)

# or -> can configure administration
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done',)
    list_filter = ('done',)
