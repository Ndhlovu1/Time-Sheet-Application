from rest_framework import serializers
from .models import TimesheetTable

class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesheetTable
        fields = ['id', 'project_Name', 'your_Name','your_employee_Id', 'start_date','end_date','days_taken_to_finish']





