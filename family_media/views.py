from django.shortcuts import render
from .models import  Media
from .forms import Upload_Media_Form
from django.shortcuts import redirect

# Create your views here.

def media(request):
    our_media = Media.objects.all().order_by('-date_added')
    return render(request, 'family_media/media.html', {'our_media':our_media})

def add_media(request):
    if request.method == 'POST':
        form = Upload_Media_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('family_media:family_media')
    else:
        form = Upload_Media_Form()
    return render(request, 'family_media/add_media.html', {'form': form})
