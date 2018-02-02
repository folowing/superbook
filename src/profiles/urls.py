from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.SignInAndSignUp.as_view(), name="home", ),
)
