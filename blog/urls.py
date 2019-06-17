from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
     blog, post, search
)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog, name='post-list'),
    path('search/', search, name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
   
    path('post/<id>/', post, name='post-detail'),
   

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
