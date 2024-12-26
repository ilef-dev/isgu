from django.shortcuts import get_object_or_404, render, redirect

from .models import AccreditationApplication
from .forms import AccreditationForm

def submission_page(request):
    if request.method == 'POST':
        form = AccreditationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = AccreditationForm()

    context = {
        'info': (
            "Для подачи заявки на государственную аккредитацию организаций в сфере "
            "информационных технологий заполните форму ниже. Убедитесь, что вы указали "
            "корректные данные, так как они будут проверены на соответствие требованиям."
        ),
        'form': form,
    }
    return render(request, 'submission_page.html', context)

# Список заявлений
def application_list(request):
    pending = AccreditationApplication.objects.filter(status='not_reviewed')  # Необработанные
    processed = AccreditationApplication.objects.exclude(status='not_reviewed')  # Обработанные
    return render(request, 'application_list.html', {'pending': pending, 'processed': processed})


def application_detail(request, application_id):
    application = get_object_or_404(AccreditationApplication, pk=application_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'documents_issue':
            application.status = 'invalid_docs'
        elif action == 'rejected':
            application.status = 'rejected'
        elif action == 'approved':
            application.status = 'approved'
        application.save()
        return redirect('application_list')
    return render(request, 'application_detail.html', {'application': application})

