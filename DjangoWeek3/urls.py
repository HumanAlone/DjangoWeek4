"""DjangoWeek3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies.views import main_view, vacancies_view, vacancy_view, company_view, specialty_vacancies_view
from vacancies.views import custom_handler_404, custom_handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="MainView"),
    path('vacancies/', vacancies_view, name="VacanciesView"),
    path('vacancies/cat/<str:cat>', specialty_vacancies_view, name="SpecialtyVacanciesView"),
    path('companies/<int:pk>/', company_view, name="CompanyView"),
    path('vacancies/<int:pk>/', vacancy_view, name="VacancyView"),
]

handler404 = custom_handler_404
handler500 = custom_handler_500
