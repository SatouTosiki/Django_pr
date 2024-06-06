from django.urls import path
from . import views
from .views import process_view

app_name = 'sample_app'


urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
     path('process/', process_view, name='process'),
    # path('result/', views.result.as_view(), name='result'),
    # path('AIchat/', views.aichat, name='aichat'),
]