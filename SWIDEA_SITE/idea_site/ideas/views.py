from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Idea, IdeaStar
from .forms import IdeaForm

# 메인페이지 - 아이디어 관리 리스트
def idea_list(request):
    sort_by = request.GET.get('sort_by', 'title')

    if sort_by == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort_by == 'likes':
        ideas = Idea.objects.filter(ideastar__isnull=False).order_by('ideastar__starred_at')
    elif sort_by == 'created_at':
        ideas = Idea.objects.all().order_by('created_at')
    else:
        ideas = Idea.objects.all().order_by('-created_at')

    paginator = Paginator(ideas, 4)
    page = request.GET.get('page')
    ideas = paginator.get_page(page)

    for idea in ideas:
        if request.user.is_authenticated:
            idea.is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
        else:
            star_key = f"starred_idea_{idea.id}"
            idea.is_starred = star_key in request.session

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'ideas/idea_list.html', {'ideas': ideas})  # 같은 템플릿으로 반환
    
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
    is_starred = False
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    else:
        star_key = f"starred_idea_{idea.id}"
        is_starred = star_key in request.session
    return render(request, 'ideas/idea_detail.html', {'idea': idea, 'is_starred': is_starred})


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

# 찜하기
def toggle_star(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    user = request.user if request.user.is_authenticated else None

    if user:
        starred = IdeaStar.objects.filter(user=user, idea=idea).exists()

        if starred:
            IdeaStar.objects.filter(user=user, idea=idea).delete()
            is_starred = False
            
        else:
            IdeaStar.objects.create(user=user, idea=idea)
            is_starred = True
    else:
        star_key = f"starred_idea_{idea.id}"

        if star_key in request.session:
            del request.session[star_key]
            is_starred = False
        else:
            request.session[star_key] = True
            is_starred = True

    return JsonResponse({'is_starred': is_starred})
