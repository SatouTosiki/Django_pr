
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('sample_app/', include('sample_app.urls')),
    path('', views.top),#URLが何も指定されなかったときに飛ぶページ
    path('admin/', admin.site.urls),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)