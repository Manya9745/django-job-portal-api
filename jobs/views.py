# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Job
# from .serializers import JobSerializer

# class JobListAPI(APIView):
#     def get(self, request):
#         jobs = Job.objects.all()
#         serializer = JobSerializer(jobs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class JobCreateAPI(APIView):
#     def post(self, request):
#         serializer = JobSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserTestAPI(APIView):
#     def get(self, request):
#         return Response(
#             {"message": "API working successfully"},
#             status=status.HTTP_200_OK
#         )
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from django.http import HttpResponse

class JobListCreateAPI(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def home(request):
        return HttpResponse("Welcome to ATS System 🚀")
