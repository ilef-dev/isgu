from django.contrib import admin
from .models import AccreditationApplication

@admin.register(AccreditationApplication)
class AccreditationApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'ogrn', 'inn', 'created_at')
    search_fields = ('full_name', 'ogrn', 'inn')
    list_filter = ('applicant_category', 'representative_category')
