from rest_framework.routers import DefaultRouter
from .views import TestAPIViewset
from django.urls import path,include


router=DefaultRouter()

router.register('ProjectAPI',TestAPIViewset,basename='test1')
urlpatterns = [
    path('',include(router.urls)),
    

]



