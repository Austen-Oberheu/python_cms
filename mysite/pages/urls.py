from django.urls import path

from . import views
from .models import Page


urlpatterns = [
    path('<str:page_url>/<int:page_id>/', views.PageView, name='PageView')
    ]
