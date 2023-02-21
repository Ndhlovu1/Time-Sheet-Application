from django import forms
from .models import TimesheetTable


#Add the Form Class for entering the details
class TimeSheetEntryForm(forms.ModelForm):
    class Meta:
        model = TimesheetTable
        fields = ['project_Name', 'your_Name','your_employee_Id','start_date', 'end_date','hours_to_finish']

        widgets = {
                    'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                    'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),       
        }        




