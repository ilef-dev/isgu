from django.urls import path
from .views import submission_page
from . import views

urlpatterns = [
    path('', submission_page, name='submission_page'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/<int:application_id>/', views.application_detail, name='application_detail'),
]
