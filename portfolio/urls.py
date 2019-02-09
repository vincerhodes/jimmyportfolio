from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import d3.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jimmy', jobs.views.home, name='home'),
    path('d3', d3.views.home, name='d3_home'),
    path('blog/', include('blog.urls')),
    path('d3/rounded_rect', d3.views.rounded_rect, name='rounded_rect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
