from django.shortcuts import render
from rest_framework import viewsets
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from dummy import constants


# Create your views here.



class TestAPIViewset(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes     = [IsAuthenticated]
    parser_classes         = (MultiPartParser,)

    # test api's
    def someapi(self,request):
        try:
            return Response(
                        {'status': 1, 'responseData': {'key': "data", 'status_code': constants.STATUS_OK}},
                        status=constants.STATUS_OK)
                
        except:
            return Response(
                        {'status': 1, 'responseData': {'key': "data", 'status_code': constants.STATUS_OK}},
                        status=constants.STATUS_OK)
               
