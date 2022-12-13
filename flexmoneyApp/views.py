from tkinter.tix import Form
from django.shortcuts import render
from .serializer import FormSerializer
from .models import Yoga_Class_Data

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['Get']) #Read operation
def yoga_form_data(request):
    form_data=Yoga_Class_Data.objects.all()
    serializer = FormSerializer(form_data,many=True)

    return Response(serializer.data)


@api_view(['POST'])#creating
def create_user_admission(request):
    serializer = FormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Update_details(request,id):
    user_data=Yoga_Class_Data.objects.get(id=id)
    serializer = FormSerializer(instance=user_data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE']) #delete
def delete_details(request,id):
    user_data=Yoga_Class_Data.objects.get(id=id)
    user_data.delete()

    return Response("details deleted successfully...!")



@api_view(['GET'])
def view_details(request,id):
    user_data=Yoga_Class_Data.objects.get(id=id)
    serializer = FormSerializer(user_data)

    return Response(serializer.data)



