from django.contrib import admin
from .models import FaceRecognition
# Register your models here.

@admin.register(FaceRecognition)
class FaceRecognitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'record_date')