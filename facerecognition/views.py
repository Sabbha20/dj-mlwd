from django.shortcuts import render
from facerecognition.forms import FaceRecognitionForm
from facerecognition.ml_pipeline import pipeline_model

from django.conf import settings
from facerecognition.models import FaceRecognition

import os

# Create your views here.
def index(req):
    form = FaceRecognitionForm
    
    if req.method == "POST":
        form = FaceRecognitionForm(req.POST or None, req.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)
            
            # extract image from db
            primary_key = save.pk
            imgobj = FaceRecognition.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT, fileroot)
            results = pipeline_model(filepath)
            
            print(results)
            context = {
                "form":form,
                "upload": True,
                "results": results[1], 
            }
            return render(req, 'index.html', context=context)
            
            
    context = {
        "form":form,
        "upload": False,
    }
    return render(req, 'index.html', context=context)