from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import Page, PageContent


def PageView(request, page_id, page_url=Page.page_url):
    page = get_object_or_404(Page, pk=page_id)
    content = get_object_or_404(PageContent, pk=page_id)
    return render(request, 'pages/home.html', {'page': page,
                                                'content': content})
