# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Hey what's up!<h1>")

def album_details(request, album_id):
    return HttpResponse("<h2>This is album number %s<h2>"%str(album_id))

# Create your views here.
