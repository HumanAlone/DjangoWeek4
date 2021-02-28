from django.shortcuts import render
from django.views import View

from accounts.forms import CompanyForm
from vacancies.models import Company, Vacancy


class MyCompany(View):
    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            location = data.get('location')
            logo = data.get('logo')
            employee_count = data.get('employee_count')
            description = data.get('description')
            Company.objects.filter(owner_id=request.user.pk).update(name=name, location=location, logo=logo,
                                                                    employee_count=employee_count,
                                                                    description=description)
            return render(request, "accounts/company-edit.html", {'form': form})
        return render(request, "accounts/company-edit.html", {'form': CompanyForm})

    def get(self, request):
        pk = request.user.pk
        if pk:
            company = Company.objects.filter(owner_id=pk).first()
            if company:
                form = CompanyForm(instance=company)
                return render(request, "accounts/company-edit.html", {'form': form})
        Company.objects.create(owner_id=pk)
        return render(request, "accounts/company-create.html")


class MyCompanyVacancies(View):
    def get(self, request):
        pk = request.user.pk
        vacancies = Vacancy.objects.filter(company__owner=pk)
        if not vacancies:
            Vacancy.objects.create(company_id=Company.objects.get(owner_id=pk).id, salary_min=0, salary_max=0,
                                   published_at='2020-01-01', specialty_id=26, title='Черновик')
            return render(request, "accounts/vacancy-create.html")
        return render(request, "accounts/vacancy-list.html", {"vacancies": vacancies})


def vacancy_edit_view(request, vacancy_id):
    return render(request, "accounts/vacancy-edit.html", {"vacancy_id": vacancy_id})


def resume_create_view(request):
    return render(request, "accounts/resume-create.html")


def resume_edit_view(request):
    return render(request, "accounts/resume-edit.html")
