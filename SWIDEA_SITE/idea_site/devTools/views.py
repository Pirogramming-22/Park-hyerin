from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import DevTool
from .forms import DevToolForm

# 개발툴 관리 리스트
def devtool_list(request):
    devtools = DevTool.objects.all().order_by('-id')
    paginator = Paginator(devtools, 4)
    page = request.GET.get('page')
    devtools = paginator.get_page(page)
    return render(request, 'devTools/devtool_list.html', {'devtools': devtools})

# 개발툴 등록
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect(devtool.get_absolute_url())
    else:
        form = DevToolForm()
    return render(request, 'devTools/devtool_form.html', {'form': form})

# 개발툴 상세 페이지
def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'devTools/devtool_detail.html', {'devtool': devtool})

# 개발툴 수정
def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect(devtool.get_absolute_url())
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'devTools/devtool_form.html', {'form': form})

# 개발툴 삭제
def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    devtool.delete()
    return redirect('devTools:list')