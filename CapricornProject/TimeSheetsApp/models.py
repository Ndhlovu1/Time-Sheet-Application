from django.db import models

# Create your models here.

class TimesheetTable(models.Model):
    project_Name = models.CharField(max_length=255)
    your_Name = models.CharField(max_length=255)
    your_employee_Id = models.SmallIntegerField(default=10)
    start_date = models.DateField()
    end_date = models.DateField()
    hours_to_finish = models.IntegerField(null=False)


    def __str__(self) -> str:
        return self.your_Name +'-'+self.project_Name




