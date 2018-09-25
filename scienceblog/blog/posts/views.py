# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def post_home(request):
    return render(request,'index.html')


def post_create(request):
    return HttpResponse('create')


def post_update(request):
    return HttpResponse('update')


def post_delete(request):
    return HttpResponse('delete')


def post_detail(request, id):
    return HttpResponse('detail')
