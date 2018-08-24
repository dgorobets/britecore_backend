from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import RiskTypeViewSet

router = SimpleRouter()

router.register(r'api/risks', RiskTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
