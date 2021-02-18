from django.db.models import Count
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

from vacancies.models import Specialty, Company, Vacancy


def main_view(request):
    specialties = Specialty.objects.annotate(num_vacancies=Count('vacancies'))
    companies = Company.objects.annotate(num_vacancies=Count('vacancies'))
    context = {
        "specialties": specialties,
        "companies": companies,
    }
    return render(request, "vacancies/index.html", context=context)


def company_view(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist:
        raise Http404
    vacancies = Vacancy.objects.filter(company_id=pk)
    context = {
        "company": company,
        "vacancies": vacancies,
    }
    return render(request, "vacancies/company.html", context=context)


def specialty_vacancies_view(request, cat):
    try:
        specialty_vacancies = Vacancy.objects.filter(specialty_id=Specialty.objects.get(code=cat))
    except Specialty.DoesNotExist:
        raise Http404
    context = {
        "specialty_vacancies": specialty_vacancies,
        "cat": cat,
    }
    return render(request, "vacancies/specialty-vacancies.html", context=context)


def vacancies_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, "vacancies/vacancies.html", {"vacancies": vacancies})


def vacancy_view(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist:
        raise Http404
    context = {
        "vacancy": vacancy,
    }
    return render(request, "vacancies/vacancy.html", context=context)


def custom_handler_404(request, exception):
    return HttpResponseNotFound('<center><h1>Ничего не нашлось! Ошибка 404!</h1></center>')


def custom_handler_500(request):
    return HttpResponseNotFound('<center><h1>Вы сломали сервер! Ошибка 500!</h1></center>')
