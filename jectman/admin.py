from django.contrib import admin
from .models import Project, Backlog,Sprint,User,Epic, Sprintreport,Userproject
# Register your models here.

admin.site.register(Project)
admin.site.register(Backlog)
admin.site.register(Sprint)
admin.site.register(User)
admin.site.register(Epic)
admin.site.register(Sprintreport)
admin.site.register(Userproject)