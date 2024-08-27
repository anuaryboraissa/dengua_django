from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class TestView(APIView):
    def get(request,self):
        return Response({"message":"get method","status":status.HTTP_200_OK})
    def post(request,self):
        return Response({"message":"post method","status":status.HTTP_200_OK})
    def put(request,self):
        return Response({"message":"put method","status":status.HTTP_200_OK})
    def delete(request,self):
        return Response({"message":"delete method","status":status.HTTP_200_OK})
# Create your views here.

