from django.shortcuts import render, redirect
from .models import FamilyPost
from .forms import Add_post_form


# Create your views here.
def HomePage(request):
    return render(request, 'home/home.html')

def Posts(request):
    posts = FamilyPost.objects.all().order_by('-created_at')
    context = {'posts':posts}
    return render(request, 'home/home_post.html', context)




def AddPost(request):
    if request.method == 'POST':
        form = Add_post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home:posts')
    else:
        form=Add_post_form()
    return render(request, 'home/add_post.html', context={'form':form})

def family_tree(request):
    return render(request, 'home/family_tree.html')

