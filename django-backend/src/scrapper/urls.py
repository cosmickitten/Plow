from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/scrapper_start/', views.ScrapperAPIView.as_view()),
    #path('api/v1/feed/', views.ScrapperViewSet.as_view({'get':'list'})),


]
