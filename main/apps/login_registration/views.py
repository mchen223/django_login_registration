# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    if request.method == 'POST':
        if User.objects.process(request) == "registered":
            return redirect('/success')
        elif User.objects.process(request) == "unregistered":
            return redirect('/')

def login(request):
    if request.method == 'POST':
        if User.objects.login(request) == "logged in":
            return redirect('/success')
        else:
            return redirect('/')

def success(request):
    return render(request, 'login_registration/success.html')

def logout(request):
    status = ''
    return redirect('/')
