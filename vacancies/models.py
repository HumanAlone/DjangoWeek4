from django.contrib.auth.models import User
from django.db import models

from DjangoWeek3.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(verbose_name='Название компании', max_length=50, blank=True, null=True)
    location = models.CharField(verbose_name='География', max_length=50, blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to=MEDIA_COMPANY_IMAGE_DIR, default='logo_default.png',
                             blank=True, null=True)
    description = models.TextField(verbose_name='Информация о компании', blank=True, null=True)
    employee_count = models.IntegerField(verbose_name='Количество человек в компании', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies", blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=50, verbose_name='Вас зовут')
    written_phone = models.CharField(max_length=15, verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    def __str__(self):
        return self.written_username
