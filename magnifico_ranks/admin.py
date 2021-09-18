from django.contrib import admin
from .models import Image, Project, Profile, Like

# Register your models here.
admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Like)
