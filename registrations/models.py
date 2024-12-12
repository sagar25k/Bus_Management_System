# registrations/models.py

from django.db import models
from students.models import Student
from buses.models import Buses
from routes.models import Route

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registrations')
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, related_name='registrations')
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='registrations')

    parent_name = models.CharField(max_length=100)
    student_mobileno = models.CharField(max_length=15)
    parent_mobileno = models.CharField(max_length=15)
    student_address = models.TextField()
    branch = models.CharField(max_length=100)
    boarding_location = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    confirmation = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])

    def __str__(self):
        return f"Registration for {self.student.first_name} {self.student.last_name} on Bus {self.bus.bus_no}"
