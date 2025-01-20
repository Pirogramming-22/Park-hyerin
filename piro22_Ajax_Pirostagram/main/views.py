from django.shortcuts import render, redirect
from .models import Post, Like, Comment
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts' : posts,
        }
    return render(request, 'main/post_list.html', ctx)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form' : form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form' : form,
        }
        return render(request, 'main/post_new.html', ctx)
    
def like_toggle(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()  # 이미 좋아요가 달렸으면 삭제
    return JsonResponse({'liked': created, 'like_count': post.likes.count()})

def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    content = request.POST.get('content')
    Comment.objects.create(post=post, user=request.user, content=content)
    return JsonResponse({'comment_count': post.comments.count()})
    