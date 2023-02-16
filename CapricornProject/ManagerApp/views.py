from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from TimeSheetsApp.models import TimesheetTable
from .serializers import TimeSheetSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

#Anyone Can View this page
@throttle_classes([AnonRateThrottle])
class ViewTimeSheets(generics.ListAPIView):
    queryset = TimesheetTable.objects.all()
    serializer_class = TimeSheetSerializer

#Edit/Delete APi View

@throttle_classes([UserRateThrottle])
@permission_classes([IsAdminUser])
class SingleTimeSheet(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimesheetTable.objects.all()
    serializer_class = TimeSheetSerializer

@throttle_classes([UserRateThrottle])
@permission_classes([IsAdminUser])
class AdminEditView(generics.ListCreateAPIView,generics.UpdateAPIView):
    queryset = TimesheetTable.objects.all()
    serializer_class = TimeSheetSerializer



# ----------------------------------------------





