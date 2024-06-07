from django.http import HttpResponse
from django.shortcuts import render  
from django.views import View  
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyA518VtV-MwFxbrgT2r55oG0kndWq3OEls"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')


  
class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'sample_app/top_page.html')
top_page = SampleView.as_view()


def process_view(request):
    if request.method == 'POST':
        combined_content = request.POST.get('combined_content', '')
        user_chat = request.POST.get('user_chat', '')
        response_test = model.generate_content(
  [
    combined_content
  ],

)
        return render(request, 'sample_app/gemini.html', {
              "result_gemini": response_test.text,
		})
    
        #return HttpResponse(f"Received: {combined_content}")
    return render(request, 'sample_app/top_page.html')



# def aichat(request):
#     result = request.GET.get('result', 'No result found')
#     return render(request, 'sample_app/AIchat.html', {'result': result})