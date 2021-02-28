from django.forms import ModelForm, Textarea, TextInput, ClearableFileInput

from vacancies.models import Company


class VacancyForm:
    pass


class ResumeForm(ModelForm):
    pass


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'employee_count', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'}),
            'logo': ClearableFileInput(),
            'employee_count': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),

        }
