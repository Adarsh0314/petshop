from django.shortcuts import render
from .models import pet_tbl
from .serializers import petform
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def Readdata(req):
    obj=pet_tbl.objects.all()
    form =petform(obj,many=True)
    return Response(form.data)

@api_view(['GET'])
def Readone(req,pk):
    obj=pet_tbl.objects.get(id=pk)
    form=petform(obj,many=False)
    return Response(form.data)

@api_view(['Post'])
def PostData(req):
    form =petform(data=req.data)
    if form.is_valid():
        form.save()
    return Response(form.data)    


@api_view(['Put'])
def UpdateData(req,pk):
    obj = pet_tbl.objects.get(id=pk)
    form=petform(instance=obj,data=req.data)
    if form.is_valid():
        form.save()
    return Response(form.data)    