from django.contrib import admin
from .models import Task


# This allows me to create Tasks from the admin page, still not working on display though
admin.site.register(Task)

