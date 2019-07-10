# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,
# Create your views here.
def welcome(request):

    return render(request,'welcome.html')
def apartment(request):

    posts=Post.objects.all()
    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.name = current_user
            post.save()
        return redirect('apartment')
    else:
        form=NewPostForm()
    return render(request,'apartment.html',{"posts":posts,"form":form})