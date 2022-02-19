from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Blockchain Backend Admin"
admin.site.site_title = "Blockchain Backend Admin Portal"
admin.site.index_title = "Welcome to Blockchain Backend admin portal"

urlpatterns = [
    # path('account/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('referral/', include('referral.urls'))
]

