from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from mtaa import tanzania
from rest_framework.response import Response
from .models import DenguaCase
from django_countries import countries
from .serializers import DenguaCaseSerializer
from Account.models import User
from Account.serializer import UserSerializer
from django.utils import timezone
from django.db.models import Count
# Create your views here.
class DenguaCaseManagementView(APIView):
    def post(self,request):
         try:
            data=request.data
            username = data["username"]
            del data["username"]
            print(f"Hello {username}")
            if username:
               try:
                # Retrieve the User object based on the username
                    user = User.objects.get(username=username)
                    denguaCase=DenguaCase.objects.create(created_by=user,**data)
                    serializer=DenguaCaseSerializer(denguaCase)
                    # serializer.is_valid(raise_exception=True)
                    return Response({"data":serializer.data, "status":status.HTTP_200_OK,"message":"Success"})
               except User.DoesNotExist:
                 return Response({"data":None, "status":status.HTTP_404_NOT_FOUND,"message":"User with this username does not exist."})

         except Exception as e:
             return Response({"data":f"{e}", "status":status.HTTP_404_NOT_FOUND,"message":None})
    def get(self,request):
        username=request.GET.get("username")
        case_id = request.GET.get('case_id')
        all = request.GET.get('all')
        just_all = request.GET.get('just_all')
        recents=request.GET.get("recents")
        num_reported_cases=request.GET.get("num_reported")
        this_week=request.GET.get("this_week")
        
        if case_id is not None:
            case=DenguaCase.objects.filter(id=case_id)
            if case.exists():
               serializer=DenguaCaseSerializer(case[0])
               data=serializer.data
               return Response({"message":"success","data":data,"status":status.HTTP_200_OK})
            return Response({"message":"success","data":None,"status":status.HTTP_200_OK})
        if recents is not None:
            cases=DenguaCase.objects.filter(created_by__username=username).order_by("-created_at")[:10]
            serializer=DenguaCaseSerializer(cases,many=True)
            data=serializer.data
            return Response({"message":"recents cases","data":data,"status":status.HTTP_200_OK})
        if all is not None:
            cases=DenguaCase.objects.filter(created_by__username=username)
            serializer=DenguaCaseSerializer(cases,many=True)
            data=serializer.data
            return Response({"message":"all cases","data":data,"status":status.HTTP_200_OK})
        if just_all is not None:
            cases=DenguaCase.objects.all()
            serializer=DenguaCaseSerializer(cases,many=True)
            data=serializer.data
            return Response({"message":"just all cases","data": data,"status":status.HTTP_200_OK})
        if num_reported_cases is not None:
            cases=DenguaCase.objects.count()
            return Response({"message":"Number of reported cases","data":cases,"status":status.HTTP_200_OK})
        if this_week is not None:
            now = timezone.now()
            start_of_week = now - timezone.timedelta(days=now.weekday())
            end_of_week = start_of_week + timezone.timedelta(days=7)

            cases_this_week = DenguaCase.objects.filter(
                created_at__gte=start_of_week,
                created_at__lt=end_of_week
            ).count()
            return Response({"message":"This week cases","data":cases_this_week,"status":status.HTTP_200_OK})
        else:
            return Response({"message":"success","data":None,"status":status.HTTP_200_OK})  
        
    def put(self,request):
        data=request.data
        case=DenguaCase.objects.get(id=data['case_id'])
        case.__dict__.update(**data)
        case.save()
        serializer=DenguaCaseSerializer(case)
        data=serializer.data
        return Response({"message":"success updated","data":data,"status":status.HTTP_200_OK})
    def delete(self,request):
        data=request.data
        dengua_case=DenguaCase.objects.get(id=data['case_id'])
        dengua_case.delete()
        return Response({"message":"success deleted","data":1,"status":status.HTTP_200_OK})
    
class AddressView(APIView):
    def get(self,request):
        country = request.query_params.get('country')
        region = request.query_params.get('region')
        district = request.query_params.get('district')
        ward = request.query_params.get('ward')

        data=[]
        if country and region and district and ward:
            data=tanzania.get(f'{region}').districts.get(f"{district}").wards.get(ward).streets
        elif country and region and district:
            data=tanzania.get(f'{region}').districts.get(f"{district}").wards
        elif region and country:
            data=tanzania.get(f'{region}').districts
        elif country:
             data=list(tanzania)
        else:
            for code, name in list(countries)[:]:
                country={"name":name,"code":code}
                data.append(country)
        return Response({"message":"success","data":data,"status":status.HTTP_200_OK})