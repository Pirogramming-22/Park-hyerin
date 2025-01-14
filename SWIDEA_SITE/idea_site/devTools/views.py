from django.shortcuts import render, get_object_or_404, redirect  
from .models import DevTool         
from .forms import DevToolForm
# Create your views here.

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devTools/devtool_list.html', {'devtools':devtools})

def devtool_add(request):
    if request. method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'devTools/devtool_form.html', {'form':form})