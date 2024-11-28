from django.contrib import admin

# Register your models here.
from .models import  *

admin.site.register(CustomCharityUser)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Donation)
admin.site.register(Profile)