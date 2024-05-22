from django.shortcuts import render
from .models import Pictures


def my_page_view(request):
    pictures = Pictures.objects.all()
    return render(request, 'main/main_page.html', {'pictures': pictures})




