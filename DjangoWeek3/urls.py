from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

import vacancies.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vacancies.views.main_view, name="MainView"),
    path('vacancies/', vacancies.views.vacancies_view, name="VacanciesView"),
    path('vacancies/cat/<str:cat>', vacancies.views.specialty_vacancies_view, name="SpecialtyVacanciesView"),
    path('companies/<int:pk>/', vacancies.views.company_view, name="CompanyView"),
    path('vacancies/<int:pk>/', vacancies.views.VacancyView.as_view(), name="VacancyView"),
    path('login/', vacancies.views.LoginView.as_view(), name="LoginView"),
    path('logout/', vacancies.views.logout_view, name="LogoutView"),
    path('register/', vacancies.views.RegisterView.as_view(), name="RegisterView"),
    path('vacancies/<int:pk>/send/', vacancies.views.send_view, name="SendView"),
    path('mycompany/', login_required(accounts.views.MyCompany.as_view()), name="MyCompanyView"),

    path('mycompany/vacancies/', login_required(accounts.views.MyCompanyVacancies.as_view()),
         name="MyCompanyVacanciesView"),
    path('mycompany/vacancies/<int:vacancy_id>/', login_required(accounts.views.vacancy_edit_view),
         name="MyCompanyVacancyView"),
    path('myresume/', login_required(accounts.views.resume_create_view), name="MyResumeView"),
    path('myresume-edit/', login_required(accounts.views.resume_edit_view), name="MyResumeEditView"),
    path('vacancy-edit/', login_required(accounts.views.vacancy_edit_view), name="MyVacancyEditView"),
]

handler404 = vacancies.views.custom_handler_404
handler500 = vacancies.views.custom_handler_500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
