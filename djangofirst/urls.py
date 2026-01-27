from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import homepage, news_detail, category_detail, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', homepage, name='homepage'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('comment/delete/<int:id>/', delete_comment, name='delete_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
