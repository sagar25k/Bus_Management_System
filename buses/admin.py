from django.contrib import admin
from buses.models import Buses
from drivers.models import Driver
from incharges.models import Incharge
from students.models import Student
from routes.models import Route
from staff.models import Staff
from registrations.models import Registration

# Register all models
admin.site.register(Buses)
admin.site.register(Driver)
admin.site.register(Incharge)
admin.site.register(Route)
admin.site.register(Staff)
admin.site.register(Student)

# Custom admin for Registration model
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'student', 
        'bus', 
        'route', 
        'parent_name', 
        'student_mobileno', 
        'parent_mobileno', 
        'boarding_location', 
        'destination', 
        'confirmation'
    )
    search_fields = ('student__first_name', 'student__last_name', 'parent_name', 'boarding_location', 'destination')
    list_filter = ('confirmation', 'route', 'bus')
