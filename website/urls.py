from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.about, name='about'),
    path('study/', views.study, name='study'),
    path('main_gallery/<int:study_id>/', views.main_gallery, name='main_gallery'),
    path('institute_news/<int:study_id>/', views.institute_news, name='institute_news'),
    path('study_complete/', views.study_complete, name='study_complete'),
    path('study_ongoing/', views.study_ongoing, name='study_ongoing'),
    path('gallery/<int:study_id>/', views.gallery, name='gallery'),
    path('video/<int:study_id>/', views.videos, name='video'),
    path('document/', views.document, name='document'),
    path('institute/<int:pk>/', views.institute, name='institute'),
    path('team/', views.team, name='team'),
    path('contact/', views.Contact, name='contact'),
    path('phasedes/<int:study_id>/', views.phasedes, name='phasedes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)