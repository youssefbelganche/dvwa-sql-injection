from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .animals import animals_list
from .models import animal
from django.db import connection
from django.shortcuts import get_object_or_404
import json

from rest_framework.response import Response

from django.http import JsonResponse


@csrf_exempt
def home(request):
    return render(request, 'src/home.html')


@csrf_exempt
def query(request):
    query = request.POST.get('query')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM src_animal WHERE name = '"+ query +"'")
            row = cursor.fetchall()
    except Exception as E:
        print(E)        
        return JsonResponse({'error': str(E)}, status=400)
    return JsonResponse({'data': row}, status=200)


@csrf_exempt
def check_flag(request):
    print(request.POST.get('name'))
    print(request.POST.get('flag'))
    return HttpResponse(status=200)



def setup(request):
    for x in animals_list:
        tmp = animal(name=x.lower())
        tmp.save()
        print(f"saving {x}")
    return HttpResponse(status=200)