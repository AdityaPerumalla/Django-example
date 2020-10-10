from django.contrib import admin
from Second.models import Topic,WebPage,AccessRecord
# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
