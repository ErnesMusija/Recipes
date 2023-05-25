from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('preporuka_recepta', views.preporuka_recepta, name="preporuka_recepta"),
    path('pretraga_recepata', views.pretraga_recepata, name="pretraga_recepata"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
