from django.shortcuts import render, redirect
from .forms import Family_Message_Form
from .models import Family_Messages
# Create your views here.

def Family(request):
    messages = Family_Messages.objects.all().order_by('-date_added')
    form = Family_Message_Form()
    return render(request, 'family_messages/messages_board.html', {'messages':messages,'form':form})
        

def SendMessage(request):
    if request.method == 'POST':
        form = Family_Message_Form(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('family_messages:family')
    else:
        form = Family_Message_Form()
    return render(request, 'family_messages/messages_board.html', {'form':form})
