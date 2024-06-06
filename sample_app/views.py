from django.http import HttpResponse
from django.shortcuts import render  
from django.views import View  



  
class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'sample_app/top_page.html')
top_page = SampleView.as_view()


def process_view(request):
    if request.method == 'POST':
        combined_content = request.POST.get('combined_content', '')
        user_chat = request.POST.get('user_chat', '')
        # ここでcombined_contentやuser_chatを使って必要な処理を行う
        return HttpResponse(f"Received: {combined_content}")
    return render(request, 'sample_app/top_page.html')



# def aichat(request):
#     result = request.GET.get('result', 'No result found')
#     return render(request, 'sample_app/AIchat.html', {'result': result})