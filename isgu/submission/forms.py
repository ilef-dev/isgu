from django import forms
from .models import AccreditationApplication

class AccreditationForm(forms.ModelForm):
    class Meta:
        model = AccreditationApplication
        fields = [
            # Сведения о заявителе
            'applicant_category', 'full_name', 'ogrn', 'inn', 'phone_number', 'email',
            # Сведения об уполномоченном лице
            'representative_category', 'last_name', 'first_name', 'middle_name',
            'representative_phone_number', 'representative_email',
            # Документ, удостоверяющий личность
            'document_type', 'document_series', 'document_number', 'document_date',
            'issued_by', 'subdivision_code',
        ]
        widgets = {
            'document_date': forms.DateInput(attrs={'type': 'date'}),
        }
