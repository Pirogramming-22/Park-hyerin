from django.shortcuts import render, get_object_or_404, redirect
from .models import MovieReview
from .forms import MovieReviewForm

# Create your views here.

# 리뷰 리스트 페이지
def post_list(request):
    reviews = MovieReview.objects.all()
    return render(request, 'reviews/post_list.html', {'reviews': reviews})

# 리뷰 디테일 페이지
def post_detail(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    return render(request, 'reviews/post_detail.html', {'review': review})

# 리뷰 작성 페이지
def post_new(request):
    if request.method == "POST":
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('post_detail', pk=review.pk)
    else:
        form = MovieReviewForm()
    return render(request, 'reviews/post_form.html', {'form': form})

# 리뷰 수정 페이지
def post_edit(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == "POST": # 새 리뷰 작성하거나 수정 후에 저장할 때
        form = MovieReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('post_detail', pk=review.pk)
    else:
        form = MovieReviewForm(instance=review)
    return render(request, 'reviews/post_form.html', {'form': form})

# 리뷰 삭제
def post_delete(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    review.delete()
    return redirect('post_list')