from django.db import models

class AccreditationApplication(models.Model):
    STATUS_CHOICES = [
        ('not_reviewed', 'Не рассмотрено'),
        ('invalid_docs', 'Неправильные документы'),
        ('rejected', 'Отказано в аккредитации'),
        ('approved', 'Аккредитовано'),
    ]

    # Сведения о заявителе
    applicant_category = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    ogrn = models.CharField(max_length=13, unique=True)
    inn = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    # Сведения об уполномоченном лице
    representative_category = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    representative_phone_number = models.CharField(max_length=15)
    representative_email = models.EmailField(blank=True, null=True)

    # Документ, удостоверяющий личность
    document_type = models.CharField(max_length=255)
    document_series = models.CharField(max_length=10)
    document_number = models.CharField(max_length=15)
    document_date = models.DateField()
    issued_by = models.TextField()
    subdivision_code = models.CharField(max_length=10)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_reviewed'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.ogrn}) - {self.get_status_display()}"
