from rest_framework import serializers
from .models import TimesheetTable

class TimeSheetsSerializerTs(serializers.ModelSerializer):
    class Meta:
        model = TimesheetTable
        fields = ['id', 'project_Name', 'your_Name','your_employee_Id', 'start_date','end_date','hours_to_finish']



