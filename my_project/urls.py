
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # path('sample_app/', include('sample_app.urls')),
    path('', views.top),#URLが何も指定されなかったときに飛ぶページ
    path('sample_app/', include('sample_app.urls')),  # sample_appのURLパターンをインクルード
    path('admin/', admin.site.urls),
    # path('AIchat/', include('sample_app.urls'))   
]

