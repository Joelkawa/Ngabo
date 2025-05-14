from django.shortcuts import render, redirect
from .models import Origin
from .forms import Edit_Ancestry_Form

# Create your views here.

def ancestry(request):
    story = Origin.objects.all()
    return render(request, 'ancestry/ancestry.html', context={'story':story})


def edit_ancestry(request):
    hist = Origin.objects.get(id=1)

    if request.method == 'POST':
        form = Edit_Ancestry_Form(instance=hist, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ancestry:ancestry')
        
    else:
        form = Edit_Ancestry_Form(instance=hist)

    context = {'form':form, 'hist':hist}
    return render(request, 'ancestry/edit_ancestry.html', context)


    
