'''from django.urls import path
from .views import home  # Import the view

urlpatterns = [
    path('', home, name='home'),  # Set the homepage route
]
'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, EnrollmentViewSet, home  # Import home

# Router setup for API
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

# URL patterns
urlpatterns = [
    path('', home, name='home'),  # Home endpoint
    path('api/', include(router.urls)),  # API endpoints
]
