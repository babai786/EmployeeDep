from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee

from .serializers import EmployeeSerializer


class EmployeeCreate(APIView):

    def post(self,request):

        try:

            data = request.data
            name = data.get("name")
            phone = data.get("phone")
            address = data.get("address")


            qs = Employee(name=name,phone=phone,address=address)
            qs.save()
            return Response({"success":1,"message":"Record Created"})

        except Exception as e:
            return Response({"sucess":0,"message":str(e)})



class EmployeeFetch(APIView):

    def get(self,request):

        try:
            qs = Employee.objects.all()
            serializer = EmployeeSerializer(qs,many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({"sucess":0,"message":str(e)})







