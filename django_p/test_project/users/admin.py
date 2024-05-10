from django.contrib import admin

# Register your models here.

from .models import laboratory
from .models import patients
from .models import employes
from .models import project
from .models import experiments
from .models import keywords
from .models import results
from .models import protocols

admin.site.register(laboratory)
admin.site.register(patients)
admin.site.register(employes)
admin.site.register(project)
admin.site.register(experiments)
admin.site.register(keywords)
admin.site.register(results)
admin.site.register(protocols)
