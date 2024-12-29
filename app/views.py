from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient



    
    

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class SignupPageView(TemplateView):
    template_name = 'app/signup.html'

class PatientListView(ListView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'app/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'app/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'address', 'primary_caregiver']
    template_name = 'app/patient_create.html'

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'address', 'primary_caregiver']
    template_name = 'app/patient_update.html'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'app/patient_delete.html'
    success_url = reverse_lazy('patient_list')

