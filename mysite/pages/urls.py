from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('<page_url>', views.PageView.as_view(), name='<page_title>')
    ]
