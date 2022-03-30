from .views import send_image, send_txt, Homepage
from django.urls import path


app_name = 'wbot'
urlpatterns = [
    path('', Homepage.as_view(), name='hp' ),
    path('img/', send_image, name='img'),
    path('txt/', send_txt, name='txt'),
    
]

