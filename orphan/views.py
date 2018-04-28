from django.shortcuts import render

from .forms import UploadProject


# Create your views here.


def home(request):
    return render(request, 'home.html')


def adopt(request):
    return render(request, 'adopt.html')


def upload(request):

    if request.method == "POST":

        form = UploadProject(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else:
        form = UploadProject()

        return render(request, "upload.html", {'form': form})
