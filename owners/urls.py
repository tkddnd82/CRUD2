from django.urls import path
from owners.views import *

urlpatterns = [
     path('owners', OwnersView.as_view()),
     path('dogs', DogsView.as_view()),
     path('getdog', GetDogs.as_view()),
     path('getowner', GetOwners.as_view()),
     path('getdogowner', GetDogOwner.as_view()),
     
 ]
