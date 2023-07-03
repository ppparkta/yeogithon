from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from user.models import Swuni
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): # 인덱스 페이지
    return render(request, 'index.html')
def post_list_view(request): # 전체 글 조회
    post_list = Post.objects.all().order_by('-regTime') # 전체 다 불러오기(최신 순)
    context = {
        'post_list': post_list,
    }
    return render(request, 'post/post_list.html', context) # settings.py의 templates 다음부터

def post_detail_view(request, id): # 세부 글 조회
    post = Post.objects.get(id=id)
    context = {
        'post' : post,
    }
    return render(request, 'post/post_detail.html', context)

@login_required
def post_create_view(request): # 글 생성
    if request.method == 'GET':
        return render(request, 'post/post_form.html')
    else:
        title = request.POST.get('title')
        body = request.POST.get('body')


        # 현재 로그인된 사용자의 Swuni 인스턴스 가져오기
        swuni = request.user
        #모델 생성
        Post.objects.create(
            title=title,
            body=body,
            swuniName=swuni,
        )
        return redirect('index')

def post_update_view(request, id): # 글 수정

    post = get_object_or_404(Post,id=id) # 존재하지 않는 글은 404 에러 뜨게

    if request.method == 'GET':
        context = { 'post' : post }
        return render(request, 'post/post_form.html', context)
    elif request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        # 데이터 변경(수정)
        post.title = title
        post.body = body
        post.save()

        return redirect('post:post-detail', post.id)

def post_delete_view(request, id): # 글 삭제
    post = get_object_or_404(Post, id=id)  # 존재하지 않는 글은 404 에러 뜨게
    if request.method == 'GET':
        context = {
            'post' : post
        }
        return render(request, 'post/post_confirm_delete.html', context)
    elif request.method == 'POST':
        # 삭제하면 삭제 후 index 페이지로
        post.delete()
        return redirect('index')
    # if request.method == 'POST':
    #     # 삭제하면 삭제 후 index 페이지로
    #     post.delete()
    #     return redirect('index')

def post_like(request, id): #찜
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        if post.like.filter(id=request.user.id).exists(): # 찜 이미 누른 상태일 때
            post.like.remove(request.user) # 찜 취소
            post.save()
        else: # 찜  누르지 않은 상태일 때
            post.like.add(request.user) # 찜 등록
            post.save()
        return redirect('post:post-list')
    else:
        post = get_object_or_404(Post, id=id)
        context = {
            'post': post
        }
        return render(request, 'post/post_detail.html', context)