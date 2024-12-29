from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from .views import HomePageView, AboutPageView, LoginPageView, SignupPageView
from .views import (
    PatientListView, 
    PatientDetailView, 
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView, 

)





urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),


    path('patient/', PatientListView.as_view(), name='patient'),    
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('patient/', PatientListView.as_view(), name='patient_list'),
   



    
    

   
]

