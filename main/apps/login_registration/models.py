# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def process(self, request):
        data = request.POST
        status = "registered"
        if len(User.objects.filter(email=data['email'])) > 0:
            messages.error(request, 'Error: Email already registered!')
            status = "unregistered"
        elif not data['first_name'].isalpha() or not data['last_name'].isalpha():
            messages.error(request, 'Error: First and last name cannot be blank or contain numbers.')
            status = "unregistered"
        elif len(data['first_name']) < 2 or len(data['last_name']) < 2:
            messages.error(request, 'Error: First and last name needs to be at least two characters each.')
            status = "unregistered"
        elif len(data['password']) < 8:
            messages.error(request, 'Error: Passwords need to be at least 8 characters long.')
            status = "unregistered"
        elif not data['password']==data['confirm_password']:
            messages.error(request, 'Error: Password and password confirmation need to match.')
            status = "unregistered"
        elif status == "registered":
            self.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                )
            messages.success(request, "Welcome, " + User.objects.get(email=data['email']).first_name + '!')
            messages.success(request, 'Successfully ' + status + '!')
        return status

    def login(self, request):
        data = request.POST
        status = 'logged in'
        user = User.objects.filter(email=data['email'])
        if user:
            if data['password'] == User.objects.get(email=data['email']).password:
                messages.success(request, "Welcome back, " + User.objects.get(email=data['email']).first_name + '!')
                messages.success(request, 'Successfully ' + status + '!')
            else:
                messages.error(request, 'Password incorrect!')
                status = 'failure'
        else:
            messages.error(request, 'Username not found!')
            status = 'failure'
        return status

    def __str__(self):
        return str(self.email, self.password)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
