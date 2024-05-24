from django.shortcuts import render, redirect, reverse  
from django.views import View  
  
class top(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('sample_app:top_page'))
top = top.as_view()





