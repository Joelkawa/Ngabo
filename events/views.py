from django.shortcuts import render, redirect
from .models import FamilyEvents
from .forms import AddEventForm
from django .utils import timezone

# Create your views here.
def List_Events(request):
    events = FamilyEvents.objects.all().order_by('-happening_date')
    return render(request, 'events/events.html', context={'events':events})

def Add_Event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('events:list')
    else:
        form = AddEventForm()
    return render(request, 'events/add_event.html', {'form': form})

def Delete_Event(request, event_id):
    event = FamilyEvents.objects.get(id=event_id)
    event.delete()
    return redirect('events:list')



        