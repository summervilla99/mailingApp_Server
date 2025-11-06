# mailer/views.py
from django.http import JsonResponse

def contact_list(request):
    return JsonResponse({"message": "Contact list API working ✅"})

def upload_contacts(request):
    return JsonResponse({"message": "Upload contacts API working ✅"})

def save_contacts(request):
    return JsonResponse({"message": "Save contacts API working ✅"})

def create_mailing(request):
    return JsonResponse({"message": "Create mailing API working ✅"})

def upload_attachment(request, mailing_id):
    return JsonResponse({"message": f"Upload attachment for mailing {mailing_id} ✅"})

def send_mailing(request, mailing_id):
    return JsonResponse({"message": f"Send mailing {mailing_id} ✅"})
