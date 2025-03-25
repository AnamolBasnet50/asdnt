from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("Homepage is working!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('courses/', include('courses.urls')),
    path('orders/', include('orders.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),  # Add this line for the homepage
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
