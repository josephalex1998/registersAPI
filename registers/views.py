from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from registers.models import Registers
from registers.serializers import RegistersSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET','POST'])
def registers_list(request):
    if request.method == 'GET':
        registers=Registers.objects.all()

        name=request.GET.get('name',None)
        if name is not None:
            registers=registers.filter(name__icontains=name)

        registers_serializer= RegistersSerializer(registers, many=True)
        return JsonResponse(registers_serializer.data, safe=False)

    elif request.method == 'POST':
        registers_data=JSONParser().parse(request)
        registers_serializer=RegistersSerializer(data=registers_data)   
        if registers_serializer.is_valid():
            registers_serializer.save() 
            return JsonResponse(registers_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(registers_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def registers_detail(request,pk):

    try:
        registers= Registers.objects.get(pk=pk)
    
    except Registers.DoesNotExist:
        return JsonResponse({'message':'The user does not exist'},status=status.HTTP_404_NOT_FOUND)
        

    if request.method == 'GET':
        

        registers_serializer=RegistersSerializer(registers)
        return JsonResponse(registers_serializer.data)

    elif request.method == 'PUT':
        registers_data=JSONParser().parse(request)
        registers_serializer=RegistersSerializer(registers,data=registers_data)   
        if registers_serializer.is_valid():
            registers_serializer.save() 
            return JsonResponse(registers_serializer.data)
        return JsonResponse(registers_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        
        registers.delete()
        return JsonResponse({'message':'User deleted successfully'},status=status.HTTP_204_NO_CONTENT)
