from django.shortcuts import render
from django.http import JsonResponse
from .models import Basket2

def basket2_list(request, firebase_uid):
    items = Basket2.objects.filter(firebase_uid=firebase_uid)
    data = list(items.values())  # QuerySet을 JSON 직렬화 가능한 형태로 변환
    return JsonResponse(data, safe=False)
