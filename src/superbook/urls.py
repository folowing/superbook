from django.conf.urls import include, url
from django.contrib import admin
from profiles.views import SignInAndSignUp, LogoutView, AboutView
from posts.views import MyFeedView

urlpatterns = (
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^myfeed/$', MyFeedView.as_view(),
        name='myfeed'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),

    url(r'^admin/', admin.site.urls),
)
