from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Idea, IdeaStar
from .forms import IdeaForm

# 메인페이지 - 아이디어 관리 리스트
def idea_list(request):
    ideas = Idea.objects.all().order_by('-id')
    paginator = Paginator(ideas, 4)
    page = request.GET.get('page')
    ideas = paginator.get_page(page)
    return render(request, 'ideas/idea_list.html', {'ideas': ideas})

# 아이디어 등록
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect(idea.get_absolute_url())
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form': form})

# 아이디어 상세 페이지
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

# 아이디어 수정
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect(idea.get_absolute_url())
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_form.html', {'form': form})

# 아이디어 삭제
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('ideas:list')

# 관심도 증가/감소 (AJAX)
def idea_interest(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    action = request.POST.get('action')
    if action == 'increase':
        idea.interest += 1
    elif action == 'decrease' and idea.interest > 0:
        idea.interest -= 1
    idea.save()
    return JsonResponse({'interest': idea.interest})