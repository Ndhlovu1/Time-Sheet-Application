from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from TimeSheetsApp.models import TimesheetTable
from .serializers import TimeSheetSerializer

from rest_framework import generics


class ViewTimeSheets(generics.ListAPIView):
    queryset = TimesheetTable.objects.all()
    serializer_class = TimeSheetSerializer

#Edit/Delete APi View
class SingleTimeSheet(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimesheetTable.objects.all()
    serializer_class = TimeSheetSerializer


# ----------------------------------------------





