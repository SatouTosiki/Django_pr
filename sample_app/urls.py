from django.urls import path
from . import views

app_name = 'sample_app'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    path('aichat/', views.aichat, name='aichat'),



    
]


