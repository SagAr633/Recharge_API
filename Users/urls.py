from Users import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('login', views.LoginViewSet, basename='login'),

urlpatterns = [
    # path('signup', views.UserRegistrationView.as_view(),name='signup'),
    #path('login', views.LoginViewSet.as_view(),name='login'),

] + router.urls
