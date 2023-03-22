from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/account/login/')),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('timesheet/', include('timesheets.urls')),
    path('subjects/', include('subjects.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
