from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list),
    path('contacts/upload/', views.upload_contacts),
    path('contacts/save/', views.save_contacts),
    path('mailings/', views.create_mailing),
    path('mailings/<int:mailing_id>/upload/', views.upload_attachment),
    path('mailings/<int:mailing_id>/send/', views.send_mailing),
]
