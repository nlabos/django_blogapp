# blogpost/admin.py

from django.contrib import admin
from .models import FirstModel, BlogModel

admin.site.register(FirstModel)
admin.site.register(BlogModel)