from django.contrib import admin
from test1.models import *

# Register your models here.
@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display=[
        'created',
        'status',
        'signup_date',
    ]