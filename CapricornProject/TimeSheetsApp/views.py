from django.shortcuts import render
from .models import TimesheetTable
from datetime import datetime
from .forms import TimeSheetEntryForm
from django.http import JsonResponse


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
                days_taken_to_finish = cd['days_taken_to_finish'],
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

        





