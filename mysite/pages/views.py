from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from . models import Page, PageContent




class PageView(generic.TemplateView):
    model = Page
    template_name = 'pages/home.html'
    