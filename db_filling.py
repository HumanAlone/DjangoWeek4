from data import jobs, companies, specialties
from vacancies.models import Company, Specialty, Vacancy


def filling_db():
    for specialty in specialties:
        Specialty.objects.create(
            code=specialty['code'],
            title=specialty['title']
        )

    for company in companies:
        Company.objects.create(
            id=company['id'],
            name=company['title'],
            location=company['location'],
            logo=company['logo'],
            description=company['description'],
            employee_count=company['employee_count'],
        )

    for job in jobs:
        Vacancy.objects.create(
            id=job['id'],
            title=job['title'],
            specialty=Specialty.objects.get(code=job['specialty']),
            company=Company.objects.get(id=job['company']),
            skills=job['skills'],
            description=job['description'],
            salary_min=job['salary_from'],
            salary_max=job['salary_to'],
            published_at=job['posted'],
        )


if __name__ == '__main__':
    filling_db()
