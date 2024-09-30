from django import forms
from facerecognition.models import FaceRecognition


class FaceRecognitionForm(forms.ModelForm):
    class Meta:
        model = FaceRecognition
        fields = ['image']
