from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from vacancies.forms import RegisterForm, LoginForm, ApplicationForm
from vacancies.models import Specialty, Company, Vacancy, Application


def main_view(request):
    specialties = Specialty.objects.annotate(num_vacancies=Count('vacancies'))
    companies = Company.objects.annotate(num_vacancies=Count('vacancies'))
    context = {
        "specialties": specialties,
        "companies": companies,
    }
    return render(request, "vacancies/index.html", context=context)


def company_view(request, pk):
    company = get_object_or_404(Company, id=pk)
    vacancies = Vacancy.objects.filter(company_id=pk)
    context = {
        "company": company,
        "vacancies": vacancies,
    }
    return render(request, "vacancies/company.html", context=context)


def specialty_vacancies_view(request, cat):
    specialty_vacancies = Vacancy.objects.filter(specialty_id=get_object_or_404(Specialty, code=cat))
    context = {
        "specialty_vacancies": specialty_vacancies,
        "cat": cat,
    }
    return render(request, "vacancies/specialty-vacancies.html", context=context)


def vacancies_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, "vacancies/vacancies.html", {"vacancies": vacancies})


class VacancyView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        return render(request, "vacancies/vacancy.html", {"vacancy": vacancy, "form": ApplicationForm})

    def post(self, request, pk):
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            user = request.user.id
            written_username = application_form.cleaned_data.get('written_username')
            written_phone = application_form.cleaned_data.get('written_phone')
            written_cover_letter = application_form.cleaned_data.get('written_cover_letter')
            Application.objects.create(written_username=written_username, written_phone=written_phone,
                                       written_cover_letter=written_cover_letter, user_id=user,
                                       vacancy=Vacancy.objects.get(id=pk))
            return redirect('SendView', pk)
        return render(request, "vacancies/vacancy.html", {"form": ApplicationForm})


class LoginView(View):
    @staticmethod
    def get(request):
        return render(request, "vacancies/login.html", context={"form": LoginForm})

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data['login'], password=clean_data['login'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("MainView")
        else:
            form.add_error(None, 'Нет такого пользователя')
            return render(request, 'vacancies/login.html', {'form': form})
        return render(request, "vacancies/login.html", context={"form": form})


class RegisterView(View):
    @staticmethod
    def get(request):
        return render(request, "vacancies/register.html", context={"form": RegisterForm})

    @staticmethod
    def post(request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect("MainView")
        return render(request, "vacancies/register.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


def send_view(request, pk):
    context = {
        "pk": pk,
    }
    return render(request, "vacancies/sent.html", context=context)


def custom_handler_404(request, exception):
    return HttpResponseNotFound('<center><h1>Ничего не нашлось! Ошибка 404!</h1></center>')


def custom_handler_500(request):
    return HttpResponseNotFound('<center><h1>Вы сломали сервер! Ошибка 500!</h1></center>')
