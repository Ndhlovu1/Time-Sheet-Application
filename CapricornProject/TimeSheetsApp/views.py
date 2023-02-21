from django.shortcuts import render
from .models import TimesheetTable
from .forms import TimeSheetEntryForm
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from .serializers import TimeSheetsSerializerTs
from rest_framework.response import Response


#Create the html route view for the Book
def timeSheetView(request):
    form = TimeSheetEntryForm

    if request.method == 'POST':

        form = TimeSheetEntryForm(request.POST)

        if form.is_valid():
            #Ensure security of info entered
            cd = form.cleaned_data

            entry = TimesheetTable(
                project_Name = cd ['project_Name'],
                your_Name = cd['your_Name'],
                your_employee_Id=cd['your_employee_Id'],
                start_date = cd['start_date'],
                end_date = cd['end_date'],
                hours_to_finish = cd['hours_to_finish'],
            )
            entry.save()

            return JsonResponse({
                'Message': 'Thank you',
            })

        else:
            return JsonResponse({
                'Message': 'Something went wrong',
            })

    context = {'form':form}

    return render(request,'time.html',context)

        
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def Submissions(request):
    items = TimesheetTable.objects.all()
    serialized_item = TimeSheetsSerializerTs(items, many = True)

    return Response({'data': serialized_item.data}, template_name='submissions.html')






