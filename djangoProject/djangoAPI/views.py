from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Company

# Create your views here.
class CompanyListView(View):
    def get(self, request):
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
        list = Company.objects.get(pk=pk)
        #El segundo parámetro "False" indica que no se va a devolver un objeto JSON, sinó un Array de objetos JSON
        return JsonResponse(list)
    # def post(self, request):
    #     # post...
    # def put(self, request):
    #     # put...
    # def patch(self, request):
    #     # patch...
    # def delete(self, request):
    #     # delete...

