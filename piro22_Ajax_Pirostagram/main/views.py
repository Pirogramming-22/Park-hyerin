from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

# 좋아요 상태 토글
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # 이미 좋아요가 눌렸으면 좋아요 취소
    like, created = Like.objects.get_or_create(post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked})

# 댓글 추가
@csrf_exempt
def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = get_object_or_404(Post, id=post_id)
        
        comment = Comment.objects.create(post=post, content=content)
        
        return JsonResponse({
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'created_at': comment.created_at
            }
        })
    
# 댓글 삭제
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'message': 'Comment deleted successfully'})