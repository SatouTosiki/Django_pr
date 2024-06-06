
from django.shortcuts import render, redirect, reverse  
from django.views import View  

  
class top(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('sample_app:top_page'))
top = top.as_view()


def home(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        # 何か処理を行う（ここでは単純に入力を大文字に変換）
        processed_data = input_data.upper()
        # 処理結果をリダイレクト先のURLに渡す
        return redirect('result', processed_data=processed_data)
    return render(request, 'home.html')

def result(request, processed_data):
    return render(request, 'test.html', {'processed_data': processed_data})



