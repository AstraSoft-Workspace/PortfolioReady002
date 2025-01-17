from django.urls import path,include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('signin/', views.signin, name='signin'),
     path('auth/', include('social_django.urls', namespace='social')),
]