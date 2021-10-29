
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "Welcome Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('blog/', include('blog.urls'))
]
