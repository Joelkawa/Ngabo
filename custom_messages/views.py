from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendMessageForm
from .models import Message

# Create your views here.

def Send_Message(request, reply_to_id=None):
    reply_to = None
    if reply_to_id:
        reply_to = get_object_or_404(Message, id= reply_to_id)
    
    if request.method == 'POST':
        form = SendMessageForm(request.POST,reply_to=reply_to)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            if reply_to:
                message.recipient = reply_to.sender
            message.save()
            return redirect('custom_messages:inbox')
    else:
        form = SendMessageForm(reply_to=reply_to)
    return render(request, 'custom_messages/send_message.html', {'form':form, 'reply_to':reply_to})


def Inbox(request):
    messages = Message.objects.filter(recipient=request.user, ).order_by('-timestamp')
    return render(request, 'custom_messages/inbox.html', {'messages':messages})
