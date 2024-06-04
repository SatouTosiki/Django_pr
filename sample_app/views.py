from django.http import HttpResponse
from django.shortcuts import render  
from django.views import View  



  
class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'sample_app/top_page.html')
top_page = SampleView.as_view()



# def aichat(request):
#     result = request.GET.get('result', 'No result found')
#     return render(request, 'sample_app/AIchat.html', {'result': result})