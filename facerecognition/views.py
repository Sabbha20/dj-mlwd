from django.shortcuts import render
from facerecognition.forms import FaceRecognitionForm

# Create your views here.
def index(req):
    form = FaceRecognitionForm
    
    if req.method == "POST":
        form = FaceRecognitionForm(req.POST or None, req.FILES or None)
        if form.is_valid():
            form.save(commit=True)
    context = {
        "form":form,
    }
    return render(req, 'index.html', context=context)