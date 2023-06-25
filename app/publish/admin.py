from django.contrib import admin

from publish.models import Claim, Patient, Doctor


admin.site.register(Claim)
admin.site.register(Patient)
admin.site.register(Doctor)
