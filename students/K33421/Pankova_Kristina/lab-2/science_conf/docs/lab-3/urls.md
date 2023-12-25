# Файл urls.py


```python
from django.urls import path

from .views import *


app_name = "beauty_marketplace_app"


urlpatterns = [
   path('salons/', SalonListAPIView.as_view()),
   path('salons/create/', SalonCreateAPIView.as_view()),
   
   path('owners/', SalonOwnerListAPIView.as_view()),
   path('owners/create/', SalonOwnerCreateAPIView.as_view()),

   path('services/', SalonServiceListAPIView.as_view()),
   path('services/create/', SalonServiceCreateAPIView.as_view()),

   path('customers/create/', CustomerCreateAPIView.as_view()),
   path('customers/create/', CustomerCreateAPIView.as_view()),

   path('appointments/', SalonAppointmentListAPIView.as_view()),
   path('appointments/create/', SalonAppointmentCreateAPIView.as_view()),

   path('salons/comments/', SalonCommentsListAPIView.as_view()),
   path('salons/comments/create', SalonCommentsCreateAPIView.as_view()),

   path('services/comments/', SalonServiceCommentsListAPIView.as_view()),
   path('services/comments/create/', SalonServiceCommentsCreateAPIView.as_view()),

]
```

