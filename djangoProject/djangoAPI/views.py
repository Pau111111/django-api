import json
import os
from django.http.response import FileResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Company
from django.forms.models import model_to_dict
from .src.MyClass import CustomClass
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.
class CompanyListView(APIView):
    permission_classes = [HasAPIKey] # Esta linea no es requerida creo

    def get(self, request):
        if('name' in request.GET):
            companyList = Company.objects.filter(name__contains=request.GET['name'])
        else:
            companyList = Company.objects.all()
    
        #El segundo parámetro "False" indica que no se va a devolver un objeto JSON, sinó un Array de objetos JSON
        return JsonResponse(list(companyList.values()), safe=False)
    # def post(self, request):
    #     # post...
    # def put(self, request):
    #     # put...
    # def patch(self, request):
    #     # patch...
    # def delete(self, request):
    #     # delete...

class CompanyDetailView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        myClass = CustomClass.myMethod()
        jsonVar = {"data": 100}
        print("Holaaaa" + str(jsonVar["data"]))

        # Enviar un fichero como respuesta
        # file = open('C:/Puchu/Personal_Projects/django-api/djangoProject/djangoAPI/src/files/test.txt', 'rb')
        file = open('C:/Puchu/Personal_Projects/django-api/djangoProject/djangoAPI/src/MyClass.py', 'rb')
        response = HttpResponse(FileResponse(file), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file.name)
        response['File-Name'] = os.path.basename(file.name)
        response['Access-Control-Expose-Headers'] = 'File-Name';
        # response["Access-Control-Allow-Origin"] = "*";
        # response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT";
        # response["Access-Control-Allow-Headers"] =  "Origin, X-Requested-With, Content-Type, Accept, Authorization, Content-Type";
        # response['Access-Control-Allow-Origin'] = "*"
        return response

        #El segundo parámetro "False" indica que no se va a devolver un objeto JSON, sinó un Array de objetos JSON
        return JsonResponse(jsonVar, safe=False)
        return JsonResponse(model_to_dict(company))
    # def post(self, request):
    #     # post...
    # def put(self, request):
    #     # put...
    # def patch(self, request):
    #     # patch...
    # def delete(self, request):
    #     # delete...

