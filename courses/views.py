'''from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to athan enterprenuer page pa")
'''
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import User, Course, Enrollment
from .serializers import UserSerializer, CourseSerializer, EnrollmentSerializer

# Function-based view for the homepage
def home(request):
    return JsonResponse({"message": "Welcome to the Django API!"})

# ViewSets for API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
