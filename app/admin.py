from django.contrib import admin
from .models import RiskType


@admin.register(RiskType)
class RiskTypeAdmin(admin.ModelAdmin):
    pass
