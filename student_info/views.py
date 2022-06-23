
from django.http.response import HttpResponse, HttpResponseGone
from django.shortcuts import render
from  django.http  import HttpResponse
from .models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response


@csrf_exempt
def stdList(request):
    if request.method == "GET":
        allStd = student.objects.all()
        serializer = StudentReg(allStd.order_by('-id'), many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudentReg(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status =400)


@csrf_exempt
def login(request):
    try:
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password']
    except:
        return HttpResponse(status = 404)
    if request.method == 'POST':
        try:
            loginStd = student.objects.filter(email = email, password = password)
            serializer = StudentReg(loginStd[0])
            return JsonResponse(serializer.data)
        except:
            return HttpResponse("Unauthorized user")


@csrf_exempt
def stdUpdate(request, id):
    try:
        updateData = student.objects.get(id = id)
    except:
        return HttpResponse(status = 404)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentReg(updateData, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)



@csrf_exempt
def stdDel(request, id):
    try:
        data = student.objects.get(id = id)
    except:
        return HttpResponse(status = 404)
    if request.method == 'DELETE':
        data.delete()
        return HttpResponse(status = 200)
