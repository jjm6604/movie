from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    # 댓글
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if movie.user == request.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if movie.user == request.user:
        movie.delete()
    else:
        return redirect('movies:detail', movie.pk) 
    return redirect('movies:index')


@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    # print(request.POST)
    # content = request.POST.get('content')
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment_form.save()
        # 저장한 comment 동적으로 detail.html에서 추가하기 넣어야함
        data = {
            'content': comment.content,
            'user': comment.user.username,
        }
        return JsonResponse(data)
    
    return JsonResponse({'fail': 'fail'})

@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)


@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    like_count = movie.like_users.all().count()
    context = {
        'is_liked': is_liked,
        'like_count': like_count,
    }
    return JsonResponse(context)