from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import IdeaForm

# Create your views here.
def idea_list(request): 
    ideas = Idea.objects.all()
    return render(request, 'ideas/idea_list.html', {'ideas':ideas})

def idea_add(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form':form})
