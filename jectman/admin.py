from django.contrib import admin
from .models import Project, Backlog,Sprint
# Register your models here.

admin.site.register(Project)
admin.site.register(Backlog)
admin.site.register(Sprint)
