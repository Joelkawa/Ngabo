from django.shortcuts import render, redirect
from .models import OurHistory
from .forms import AddHistory

# Create your views here.
def history(request):
    histories = OurHistory.objects.all()
    context = {'histories':histories}
    return render(request,'about_us/history.html', context)
    
def add_history(request):
    if request.method == 'POST':
        form = AddHistory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_us:history')
    else:
        form = AddHistory()
    context = {'form':form}
    return render(request, 'about_us/add_history.html', context)   
    


