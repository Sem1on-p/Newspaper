from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import models
from . import models


def blog(request):
    post_list = models.Post.objects.order_by('-id')
    return render(request, 'blog/blog.html', {'post_list': post_list})

def view_post(request, post_id):
    post = models.Post.objects.get(id=post_id)
    category = post.category_post.all()
    section = post.section_post.all()
    comments = models.Comment.objects.filter(post = post).order_by('-id')
    post_list = models.Post.objects.exclude(id=post_id).order_by('-id')[0:4]
    return render(request, 'blog/post.html',{'post':post,'post_list':post_list, 'category': category, 'section':section, 'comments': comments})

def add_new_comment(request, post_id):
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        a = models.Comment()
        a.post = models.Post.objects.get(id= post_id)
        a.author = author
        a.textComment = text
        if a.textComment!='':
            if a.author!='':
                a.save()
    return redirect ('view_post', post_id=post_id)

def editor(request):
    if request.user.is_authenticated:
        category_list = models.Category.objects.order_by('-id')
        section_list = models.Section.objects.order_by('-id')
        if request.method == 'GET':     
            return render(request, 'blog/editor.html', {'category_list': category_list, 'section_list': section_list})

        elif request.method == 'POST':
            category_list = models.Category.objects.order_by('-id')
            section_list = models.Section.objects.order_by('-id')
            title = request.POST['title']
            description = request.POST['description']
            text = request.POST['text']
            img = request.POST['img']
            a = models.Post()
            a.title = title
            a.description = description
            a.text = text
            a.img = img
            if a.text!='':
                if a.title!='':
                    a.save()
            return render(request, 'blog/editor.html', {'category_list': category_list, 'section_list': section_list})
    else:
        return redirect('auth')

def auth(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        if request.method == 'GET':
            return render(request, 'blog/auth.html')

        elif request.method == 'POST':
            username = request.POST['username'].lower()
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('editor')
    return render(request, 'registration/login.html')

