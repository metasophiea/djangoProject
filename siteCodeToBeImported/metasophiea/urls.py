import django
import continuousVerse
import continuousVerse.views

urlpatterns = [
    django.conf.urls.url(r'^admin/', django.contrib.admin.site.urls),
    django.conf.urls.url(r'^login/', continuousVerse.views.login, name='login'),
    django.conf.urls.url(r'^accounts/login/', django.views.generic.RedirectView.as_view(pattern_name='login', permanent=False)),
    django.conf.urls.url(r'^logout/', continuousVerse.views.logout),

    django.conf.urls.url(r'^processLogin\.exe', continuousVerse.views.processLogin),
    django.conf.urls.url(r'^processLogout\.exe/', continuousVerse.views.processLogout),

    django.conf.urls.url(r'^data/', continuousVerse.views.getData),
    django.conf.urls.url(r'^verses/', continuousVerse.views.getVerses),
    django.conf.urls.url(r'^$', continuousVerse.views.index)
]
